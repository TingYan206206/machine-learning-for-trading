"""
Template for implementing StrategyLearner  (c) 2016 Tucker Balch
"""

import datetime as dt
import pandas as pd
import util as ut
import QLearner as ql
import indicators as indic
import random
import numpy as np


# name: Ting Yan
# id: tyan37

class StrategyLearner(object):

    # constructor
    def __init__(self, verbose = False, impact=0.0):
        self.verbose = verbose
        self.impact = impact

    # this method should create a QLearner, and train it for trading
    def addEvidence(self, symbol = "IBM", \
        sd=dt.datetime(2008,1,1), \
        ed=dt.datetime(2009,1,1), \
        sv = 10000):


        # add your code to do learning here

        # example usage of the old backward compatible util function
        syms=[symbol]
        dates = pd.date_range(sd, ed)
        prices_all = ut.get_data(syms, dates)  # automatically adds SPY
        prices = prices_all[syms]  # only portfolio symbols
        prices_SPY = prices_all['SPY']  # only SPY, for comparison later

        norm_prices = prices / prices.ix[0, :]
        daily_returns = norm_prices.copy()
        daily_returns.values[1:, :] = norm_prices.values[1:, :] - norm_prices.values[:-1, :]
        daily_returns.values[0, :] = np.nan
        # print daily_returns
        # if self.verbose: print prices

        self.period = 10

        states = indic.addIndicators(symbol,sd,ed, self.impact, self.period, False)
        # Instantiate a Q - learner
        self.learner = ql.QLearner(num_states=130, num_actions=5, alpha=0.2, gamma=0.9, rar=0.98, radr=0.999, dyna=0,
                              verbose=False)

        prices = prices.reset_index()
        prices['Holdings'] = 0
        for j in range(10):
                x = states[0][0]
                a = self.learner.querysetstate(x)
                prices.loc[self.period - 1, 'Holdings'] = (a - 2) * 1000
                #  a = 0  h = -2000
                #  a = 1  h = -1000
                #  a = 2, h = 0
                #  a = 3, h = 1000
                #  a = 4, h = 2000

                for i in range(1, states.shape[0]):
                    index = i + self.period - 1
                    x = states[i][0]
                    r = prices.loc[index -1, 'Holdings'] * prices.loc[index, symbol] -sv

                    # r = prices.loc[index -1, 'Holdings'] * daily_returns.ix[index] * ( 1 - self.impact)
                    # if remain < 0:

                    a = self.learner.query(x, r)
                    h = (a - 2) * 1000
                    if prices.loc[index - 1, 'Holdings'] + h > 1000:
                        prices.loc[index, 'Holdings'] = 1000

                    elif prices.loc[index -1, 'Holdings'] + h < -1000 :
                        prices.loc[index, 'Holdings'] = -1000

                    else:
                        prices.loc[index, 'Holdings'] = prices.loc[index -1, 'Holdings'] + h



    # this method should use the existing policy and test it against new data
    def testPolicy(self, symbol = "IBM", \
        sd=dt.datetime(2009,1,1), \
        ed=dt.datetime(2010,1,1), \
        sv = 10000):

        # here we build a fake set of trades
        # your code should return the same sort of data
        syms = [symbol]
        dates = pd.date_range(sd, ed)
        prices_all = ut.get_data([symbol], dates)  # automatically adds SPY
        prices = prices_all[syms]  # only portfolio symbols
        trades = prices_all[[symbol,]]  # only portfolio symbols
        trades_SPY = prices_all['SPY']  # only SPY, for comparison later
        # trades = trades.index.tolist()
        trades.values[:,:] = 0 # set them all to nothing
        # holding = trades.copy()
        prices = prices.reset_index()
        prices['Holdings'] = 0

        states = indic.addIndicators(symbol, sd, ed, self.impact, self.period, False)

        x = states[0][0]
        a = np.argmax(self.learner.Q[x])
        if a == 0:
            prices.loc[self.period - 1, 'Holdings'] = -1000
            trades.values[self.period - 1, :] = -1000
        elif a == 4:
            prices.loc[self.period - 1, 'Holdings'] = 1000
            trades.values[self.period - 1, :] = 1000
        else:
            prices.loc[self.period - 1, 'Holdings'] = (a - 2) * 1000
            trades.values[self.period -1, :] = (a - 2) * 1000
        #
        for i in range(1, states.shape[0]):
            index = i + self.period - 1
            x = states[i][0]
            a = np.argmax(self.learner.Q[x])
            h = (a - 2) * 1000

            if prices.loc[index - 1, 'Holdings'] + h > 1000:
                trades.values[index, :] = 1000 - prices.loc[index - 1, 'Holdings']

                prices.loc[index, 'Holdings'] = 1000
            elif prices.loc[index - 1, 'Holdings'] + h < -1000:
                    trades.values[index, :] = -1000 - prices.loc[index - 1, 'Holdings']
                    prices.loc[index, 'Holdings'] = -1000

            else:
                trades.values[index, :] = h
                prices.loc[index, 'Holdings'] = prices.loc[index - 1, 'Holdings'] + h

        return trades

    def author(self):
        return 'tyan37'

if __name__=="__main__":

    print "One does not simply think up a strategy"

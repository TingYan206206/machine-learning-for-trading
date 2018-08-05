import StrategyLearner as sl
import marketsimcode as mc
import numpy as np

import datetime as dt
import pandas as pd
import util as ut

# name: Ting Yan
# id: tyan37

def impactEffects(symbol="JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2008, 3, 1),
                        sv=100000, impact = 0 ):
    imp = impact
    start_date = sd
    end_date = ed
    sym = symbol

    learner = sl.StrategyLearner(verbose=True, impact= imp)  # constructor
    learner.addEvidence(sym, start_date, end_date, sv)  # training phase
    orders = learner.testPolicy( sym, start_date, end_date, sv)

    order_list = []
    for day in orders.index:
        if orders.ix[day, symbol] > 0:
            order_list.append([day.date(), symbol, 'BUY', orders.ix[day, symbol]])
        elif orders.ix[day, symbol] < 0:
            order_list.append([day.date(), symbol, 'SELL', orders.ix[day, symbol]])

    df = pd.DataFrame.from_records(
        order_list,
        columns=['Date', 'Symbol', 'Order', 'Shares'])
    # print df.shape[0]
    portfolio = mc.compute_portvals(df, start_date, end_date, sv, 0, impact= imp)
    return portfolio


def author():
    return 'tyan37'

#  test the impact affect on portfolio value and trade numbers
if __name__ == "__main__":
    portfolioFile = []
    symbol = "JPM"
    start_date = dt.datetime(2008, 1, 1)
    end_date = dt.datetime(2009,12, 31)
    sv = 100000
    for i in range(0,6):
        portfolio = impactEffects(symbol,start_date, end_date,sv, 0.004*i)
        portfolioFile.append(portfolio)

    df_temp = pd.concat([portfolioFile[0], portfolioFile[1], portfolioFile[2],portfolioFile[3],portfolioFile[4],portfolioFile[5]],
                        keys=['impact = 0.000', 'impact = 0.004','impact = 0.008','impact = 0.012','impact = 0.016','impact = 0.020'], axis=1)
    ut.plot_data(df_temp, title="Prtfolio for JPM with varying impact values", xlabel="Date", ylabel="value")





#  Optional if needed to support your strategy learner.
# An improved version of your marketsim code that accepts a "trades" data frame (instead of a file).
import pandas as pd
import numpy as np
import datetime as dt
import util as ut


# name: Ting Yan
# id: tyan37

def compute_portvals(orders_file, sd, ed, start_val=1000000, commission=9.95, impact=0.005):
    # this is the function the autograder will call to test your code
    # NOTE: orders_file may be a string, or it may be a file object. Your
    # code should work correctly with either input
    # TODO: Your code here

    df = orders_file

    start_date = sd

    end_date = ed

    symbols = df.loc[1, 'Symbol']
    sym = [symbols]

    dates = pd.date_range(start_date, end_date, name='Date', freq='D')

    df_all = ut.get_data(sym, dates)
    df1 = df_all.drop(['SPY'], axis=1)


    prices = df1.copy()

    prices['Cash'] = np.ones((prices.shape[0], 1))

    trades = prices.copy()
    trades[:] = 0
    # print trades

    for index, row in df.iterrows():
        # print " index:::::", index
        # print row['Date']
        #     continue
        if row['Order'] == 'BUY':
            trades.loc[row['Date'], row['Symbol']] += row['Shares']
            cost = commission + prices.loc[row['Date'], row['Symbol']] * (1 + impact) * row['Shares']
            trades.loc[row['Date'], 'Cash'] -= cost
        else:
            trades.loc[row['Date'], row['Symbol']] -= row['Shares']
            cost = prices.loc[row['Date'], row['Symbol']] * (1 - impact) * row['Shares'] - commission
            trades.loc[row['Date'], 'Cash'] += cost
    # print "add trans cost====  trades"
    # print trades

    holdings = trades.copy()
    # print "start date ======", trades.index[0]
    holdings.loc[trades.index[0], 'Cash'] = holdings.loc[trades.index[0], 'Cash'] + start_val
    # print "holdings========"

    holdings = holdings.cumsum(axis=0)
    # print holdings
    values = prices * holdings
    values['Sum'] = values.sum(axis=1)
    # print "values======="
    # print values

    portvals = values.drop(values.columns[:-1], axis=1)

    return portvals


def author():
    return 'tyan37'
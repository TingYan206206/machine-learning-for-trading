"""MC2-P1: Market simulator.

Copyright 2017, Georgia Tech Research Corporation
Atlanta, Georgia 30332-0415
All Rights Reserved
"""

import pandas as pd
import numpy as np
import datetime as dt

import os
from util import get_data, plot_data

def compute_portvals(orders_file = "./orders/orders.csv", start_val = 1000000, commission=9.95, impact=0.005):
    # this is the function the autograder will call to test your code
    # NOTE: orders_file may be a string, or it may be a file object. Your
    # code should work correctly with either input
    # TODO: Your code here
    df = pd.read_csv(orders_file, index_col="Date", parse_dates=True, usecols=['Date', 'Symbol', 'Order', 'Shares'],
                     na_values=['nan'])

    df = df.sort_index()
    print df
    # print "-------"
    # print df.shape

    start_date = df.first_valid_index()
    end_date = df.index[-1]

    # print start_date
    # print end_date

    symbols = []
    for index, row in df.iterrows():
        if row['Symbol'] not in symbols:
            symbols.append(row['Symbol'])

    # print symbols
    dates = pd.date_range(start_date, end_date, name='Date', freq='D')

    df1 = pd.DataFrame(index=dates)
    # print df1

    # spy = "../data/SPY.csv"
    # df_spy = pd.read_csv(spy, index_col="Date", parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
    # df_spy = df_spy.rename(columns={'Adj Close': 'SPY'})
    df_all = get_data(['GOOG'],dates)
    df_spy = df_all['SPY']
    df1 = df1.join(df_spy)
    df1 = df1.dropna()
    df1 = df1.drop(['SPY'], axis=1)
    # print df1

    prices = df1.copy()
    for symbol in symbols:
        df_temp = pd.read_csv("../data/{}.csv".format(symbol), index_col="Date", parse_dates=True,
                              usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})

        prices = prices.join(df_temp)
    prices.fillna(method="ffill", inplace=True)
    prices.fillna(method="bfill", inplace=True)
    
    prices['Cash'] = np.ones((prices.shape[0], 1))
    # print "prices========"
    # print prices

    trades = prices.copy()
    trades[:] = 0

    for index, row in df.iterrows():
        if index not in dates:
            continue
        if row['Order'] == 'BUY':
            trades.at[index, row['Symbol']] += row['Shares']
            cost = commission + prices.at[index, row['Symbol']] * (1 + impact) * row['Shares']
            trades.at[index, 'Cash'] -= cost
        else:
            trades.at[index, row['Symbol']] -= row['Shares']
            cost = prices.at[index, row['Symbol']] * (1 - impact) * row['Shares'] - commission
            trades.at[index, 'Cash'] += cost
    # print "add trans cost====  trades"
    # print trades

    holdings = trades.copy()

    holdings.at[start_date, 'Cash'] = holdings.at[start_date, 'Cash'] + start_val
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

def test_code():
    # this is a helper function you can use to test your code
    # note that during autograding his function will not be called.
    # Define input parameters

    of = "./orders/orders-short.csv"
    sv = 1000000

    # Process orders
    portvals = compute_portvals(orders_file = of, start_val = sv)
    if isinstance(portvals, pd.DataFrame):
        portvals = portvals[portvals.columns[0]] # just get the first column
    else:
        "warning, code did not return a DataFrame"
    
    # Get portfolio stats
    # Here we just fake the data. you should use your code from previous assignments.
    start_date = dt.datetime(2011,01,05)
    end_date = dt.datetime(2011,01,20)
    cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = [0.2,0.01,0.02,1.5]
    cum_ret_SPY, avg_daily_ret_SPY, std_daily_ret_SPY, sharpe_ratio_SPY = [0.2,0.01,0.02,1.5]

    # Compare portfolio against $SPX
    print "Date Range: {} to {}".format(start_date, end_date)
    print
    print "Sharpe Ratio of Fund: {}".format(sharpe_ratio)
    print "Sharpe Ratio of SPY : {}".format(sharpe_ratio_SPY)
    print
    print "Cumulative Return of Fund: {}".format(cum_ret)
    print "Cumulative Return of SPY : {}".format(cum_ret_SPY)
    print
    print "Standard Deviation of Fund: {}".format(std_daily_ret)
    print "Standard Deviation of SPY : {}".format(std_daily_ret_SPY)
    print
    print "Average Daily Return of Fund: {}".format(avg_daily_ret)
    print "Average Daily Return of SPY : {}".format(avg_daily_ret_SPY)
    print
    print "Final Portfolio Value: {}".format(portvals[-1])

if __name__ == "__main__":
    test_code()

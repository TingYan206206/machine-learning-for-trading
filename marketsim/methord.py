import pandas as pd
import numpy as np
import util as ut
import datetime as dt

def assess_portfolio(port_val ,\
     rfr=0.0, sf=252.0, \
    gen_plot=False):

    daily_return = port_val.copy()
    daily_return[1:] = (port_val[1:] / port_val[:-1].values) - 1
    daily_return = daily_return[1:]

    # cr: Cumulative return
    cr = (port_val[-1] / port_val[0]) - 1
    adr = daily_return.mean()
    sddr = daily_return.std()
    # sr sharpe ratio
    sr = (adr - rfr) * np.math.sqrt(sf) / sddr

    # Compare daily portfolio value with SPY using a normalized plot
    # if gen_plot:
    #     # add code to plot here
    #
    #     df_temp = pd.concat([port_val / sv, prices_SPY / prices_SPY[0]], keys=['Portfolio', 'SPY'], axis=1)
    #     plot_data(df_temp, title="Daily portfolio value and SPY", xlabel="Date", ylabel="Normalized price")

    # Add code here to properly compute end value
    ev = port_val[-1]

    return cr, adr, sddr, sr, ev

if __name__=="__main__":
    # df = pd.read_csv("./orders/orders-02.csv" )
    # file = open("./orders/orders-short.csv")
    # # print type(file)
    # df = pd.read_csv(file, index_col= "Date", parse_dates = True, usecols= ['Date', 'Symbol', 'Order', 'Shares'], na_values=['nan'])
    #
    # df = df.sort_index()
    # print "orders===="
    # print df
    # print "-------"
    # print df.shape
    # df1 = df['Shares']
    # print df1
    symbol = "IBM"
    syms = [symbol]

    sd = dt.datetime(2008, 1, 1)
    ed = dt.datetime(2008, 2, 20)
    dates = pd.date_range(sd,ed)
    prices_all = ut.get_data(syms, dates)  # automatically adds SPY
    prices = prices_all[syms]
    print prices
    prices['10 Day MA'] = prices[symbol].rolling(window=10).mean()
    prices['10 Day STD'] = prices[symbol].rolling(window=10).std()
    # prices['Upper Band'] = prices['10 Day MA'] + (prices['10 Day STD'] * 2)
    # prices['Lower Band'] = prices['10 Day MA'] - (prices['10 Day STD'] * 2)
    prices['BB'] = (prices[symbol] - prices['10 Day MA']) / 2 * prices['10 Day STD']
    prices['SMA'] = prices[symbol] / prices['10 Day MA'] - 1
    prices['Holdings'] = 0
    print prices


    # drop_prices = prices[9:]
    drop_prices = prices.fillna(method="bfill")
    print drop_prices
    # print dropped_value
    # sorted_BB = drop_prices.sort_values(by=['BB'])
    # sorted_BB = sorted_BB.reset_index()
    # print "sorted BB"
    # print sorted_BB
    # # sorted_BB.dropna()
    #
    # # print "drop nan", sorted_BB
    #
    # steps = 10
    # stepsize = (drop_prices.shape[0]) / steps  # 10 is the window size
    # print "stepsize", stepsize
    # threshold_BB = []
    # threshold_SMA = []
    # threshold_holdings = []
    # number = sorted_BB.loc[(0 + 1) * stepsize, 'BB']
    # print "number", number
    # threshold_BB.append(number)
    # threshold_BB.append(2)
    # print "threshold"
    # bb = min(range(len(threshold_BB)), key=lambda i: abs(threshold_BB[i] - 2.1))
    # print "bb",bb
    # for i in range(0, steps):
    #     threshold_BB[i] = sorted_BB[(i + 1) * stepsize, 'BB']
        # threshold_SMA[i] = sorted_SMA[(i + 1) * stepsize, 'SMA']
        # threshold_holdings[i] = sorted_holdings[(i + 1) * stepsize, 'Holdings']

    # print  threshold_BB
    # df1= df.sort_values(by=['Shares'])
    # print df1
    # df2 =df1.reset_index()
    # print "df2", df2
    # steps = 2
    # stepsize = df2.shape[0] / steps
    # print df2.at[1, 'Shares']


    # start_date = df.first_valid_index()
    # end_date = df.index[-1]
    # # start_date = df.at[0, 'Date']
    # # end_date = df.at[df.shape[0]-1, 'Date']
    # print start_date
    # print end_date
    #
    # symbols = []
    # for index, row in df.iterrows():
    #     if row['Symbol'] not in symbols:
    #         symbols.append(row['Symbol'])
    #     # print row['Symbol'], row['Order']
    # # symbols.append('Cash')
    # print "symbols: ", symbols
    #
    # dates = pd.date_range(start_date, end_date, name= 'Date', freq= 'D')
    #
    # df1 = pd.DataFrame (index = dates)
    # print df1
    #
    # spy = "../data/SPY.csv"
    # df_spy = pd.read_csv(spy, index_col= "Date",  parse_dates = True, usecols= ['Date', 'Adj Close'], na_values=['nan'])
    # df_spy = df_spy.rename(columns={'Adj Close': 'SPY'})
    # df1 = df1.join(df_spy)
    # df1 = df1.dropna()
    # df1= df1.drop(['SPY'], axis=1)
    # print df1
    # # mask = (df_spy['Date'] >= start_date) & (df_spy['Date'] <= end_date)
    # # df_spy = df_spy.loc[mask]
    # # df_spy = df_spy.sort_values(by=['Date'])
    # # print "spy: ===="
    # # print df_spy
    # #
    # prices = df1.copy()
    # for symbol in symbols:
    #     df_temp = pd.read_csv("../data/{}.csv".format(symbol), index_col= "Date", parse_dates = True, usecols= ['Date','Adj Close'], na_values=['nan'])
    #     df_temp = df_temp.rename(columns={'Adj Close': symbol})
    #
    #     prices = prices.join(df_temp)
    # prices.fillna(method = "ffill", inplace=True)
    # prices.fillna(method="bfill", inplace=True)
    # prices['Cash'] = np.ones((prices.shape[0],1))
    # print "prices========"
    # print prices
    #
    # trades = prices.copy()
    # # trades = trades.drop('Cash', axis = 1)
    # trades[:] = 0
    # # trades['Cost'] = np.zeros((trades.shape[0], 1))
    # # print "add trans cost===="
    # # print trades
    # commission = 9.95
    # impact = 0.005
    # # print trades
    # for index, row in df.iterrows():
    #     if index not in dates:
    #         continue
    #     if row['Order']=='BUY':
    #         trades.at[index, row['Symbol']] += row['Shares']
    #         # prices.at[index, row['Symbol']] = prices.at[index, row['Symbol']] * (1+ impact)
    #         cost = commission + prices.at[index, row['Symbol']] * (1+ impact) * row['Shares']
    #         # print "cost: ", cost
    #         # print "cost sum", trades.at[index, 'Cost']
    #         trades.at[index, 'Cash'] -=  cost
    #     else:
    #         trades.at[index, row['Symbol']] -= row['Shares']
    #         # prices.at[index, row['Symbol']] = prices.at[index, row['Symbol']] * (1 - impact)
    #         cost = prices.at[index, row['Symbol']] * (1 - impact) * row['Shares'] - commission
    #         trades.at[index, 'Cash'] +=  cost
    # print "add trans cost===="
    # print trades
    # # totals =  trades.iloc[:, :-1]* prices.iloc[:, :-1] * -1
    # # totals['Cost'] =trades['Cost']
    # # # totals = trades[:, :-2] * prices * -1
    # # # print "-----print totals==="
    # # print totals
    # # # totals['Cash'] = totals.sum(axis= 1)
    # # # print totals
    # #
    # # trades['Cash'] = totals.sum(axis=1)
    # # trades = trades.drop('Cost', axis = 1)
    # # print "trades========"
    # # print trades
    #
    # holdings = trades.copy()
    # start_val = 1000000
    # holdings.at[start_date,'Cash'] = holdings.at[start_date,'Cash'] + start_val
    # print "holdings========"
    #
    # holdings = holdings.cumsum(axis= 0)
    # print holdings
    #
    #
    # # print "sliced holdings"
    # # print holdings.iloc[:, 0:-1]
    #
    #
    # values = prices * holdings
    # values['Sum'] = values.sum(axis= 1)
    # print "values======="
    # print values
    # # portvals = values['Sum']
    # portvals = values.drop(values.columns[:-1], axis = 1)
    # print "portvals====="
    # print portvals
    #
    # print isinstance(portvals, pd.DataFrame)
    # portvals = portvals[portvals.columns[0]]
    #
    # daily_return = portvals.copy()
    # daily_return[1:] = (portvals[1:] / portvals[:-1].values) - 1
    # daily_return = daily_return[1:]
    #
    # # cr: Cumulative return
    # cr = (portvals[-1] / portvals[0]) - 1
    # adr = daily_return.mean()
    # sddr = daily_return.std()
    # # sr sharpe ratio
    # sr = (adr - 0) * np.math.sqrt(252) / sddr
    # cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = [cr, adr, sddr, sr]
    #
    #
    # cum_ret_SPY, avg_daily_ret_SPY, std_daily_ret_SPY, sharpe_ratio_SPY = [0.2, 0.01, 0.02, 1.5]
    #
    # # Compare portfolio against $SPX
    # print "Date Range: {} to {}".format(start_date, end_date)
    # print
    # print "Sharpe Ratio of Fund: {}".format(sharpe_ratio)
    # print "Sharpe Ratio of SPY : {}".format(sharpe_ratio_SPY)
    # print
    # print "Cumulative Return of Fund: {}".format(cum_ret)
    # print "Cumulative Return of SPY : {}".format(cum_ret_SPY)
    # print
    # print "Standard Deviation of Fund: {}".format(std_daily_ret)
    # print "Standard Deviation of SPY : {}".format(std_daily_ret_SPY)
    # print
    # print "Average Daily Return of Fund: {}".format(avg_daily_ret)
    # print "Average Daily Return of SPY : {}".format(avg_daily_ret_SPY)
    #
    #
    #
    # print "Final Portfolio Value: ", portvals[-1]
    #








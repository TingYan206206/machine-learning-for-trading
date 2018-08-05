

import numpy as np

import datetime as dt
import pandas as pd
import util as ut

# name: Ting Yan
# id: tyan37


def addIndicators( symbol = "IBM", \
        sd=dt.datetime(2008,1,1), \
        ed=dt.datetime(2008,2,10), \
                  impact=0.005, periods = 10, plotData = False):
    syms = [symbol]
    dates = pd.date_range(sd, ed)
    prices_all = ut.get_data(syms, dates)  # automatically adds SPY
    prices = prices_all[syms]  # only portfolio symbols

    volume_all = ut.get_data(syms, dates, colname="Volume")  # automatically adds SPY
    volume = volume_all[syms]

    # calculate indicators force index, prices/sma, bb

    ma = prices.rolling(periods).mean()
    psma = prices/ma
    std = prices.rolling(periods).std()
    upper_band = ma + (std * 2)
    lower_band = ma - (std * 2)
    bb = (prices - lower_band)/(upper_band - lower_band)
    FI = prices.diff(periods-1) * volume

    psma = psma.dropna()
    bb = bb.dropna()
    FI = FI.dropna()

    psma = psma.rename(columns={symbol: 'price/sma'})
    bb = bb.rename(columns={symbol: 'bb'})
    # rsis = rsis.rename(columns={symbol: 'rsi'})
    FI = FI.rename(columns={symbol: 'FI'})

    if plotData:
        ma = ma.dropna()
        upper_band = upper_band.dropna()
        lower_band = lower_band.dropna()
        valid_p = prices.ix[periods - 1:, :]
        valid_v = volume.ix[periods - 1:, :]
        valid_v = valid_v.rename(columns={symbol: 'volume'})
        valid_p = valid_p.rename(columns={symbol: 'price'})
        ma = ma.rename(columns={symbol: 'sma'})
        upper_band = upper_band.rename(columns={symbol: 'upper_band'})
        lower_band = lower_band.rename(columns={symbol: 'lower_band'})
        plotValues(upper_band, lower_band, valid_p, True)
        # plotValues(bb, ma/ma.ix[ma.index[0],0], valid_p/valid_p.ix[valid_p.index[0],0], True)
        plotNormValues(FI, valid_v, valid_p, True)
        plotNormValues(psma, ma, valid_p, True)

    # print bb
    index_bb = pd.qcut(bb.rank(method='first'), 10, labels= False)
    index_psma = pd.qcut(psma.rank(method='first'), 10, labels= False)

    index_fi = pd.qcut(FI.rank(method='first'), 10, labels= False)

    states = discretize(index_bb,index_fi, index_psma )

    return states

# this method discretizing indicators to 0-2 digit
def discretize(bb, fi, psma):
    return bb + fi * 3 + psma*3*3

def author():
    return 'tyan37'

def plotNormValues(values1, values2, values3, gen_plot):
    if gen_plot:
        name1 = values1.columns[0]
        name2 = values2.columns[0]
        name3 = values3.columns[0]
        df_temp = pd.concat([values1.ix[:, 0]/values1.ix[values1.index[0],0], values2.ix[:, 0]/values2.ix[values2.index[0],0], values3.ix[:, 0]/values3.ix[values3.index[0],0]], keys=[name1, name2, name3], axis=1)
        ut.plot_data(df_temp, xlabel= "Date", ylabel="Normalized data")

def plotValues(values1, values2, values3, gen_plot):
    if gen_plot:
        name1 = values1.columns[0]
        name2 = values2.columns[0]
        name3 = values3.columns[0]
        df_temp = pd.concat([values1, values2, values3], keys=[name1, name2, name3], axis=1)
        ut.plot_data(df_temp, xlabel= "Date", ylabel="Price")

if __name__=="__main__":
    addIndicators("IBM", dt.datetime(2008,1,1), dt.datetime(2009,12, 31), 0,  10, True)

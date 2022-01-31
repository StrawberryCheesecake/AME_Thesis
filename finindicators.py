import numpy as np
import pandas



def clean_news(news_name):
    file = pandas.read_csv(fin_name)
    #file columns Date,Open,High,Low,Close,Volume,Adj Close
    dates = np.array(file['Date'])
    opens = np.array(file['Open'])
    closes = np.array(file['Close'])
    highs = np.array(file['High'])
    lows = np.array(file['Low'])
    volumes = np.array(file['Volume'])
    adjcloses = np.array(file['Adj Close'])

    #get ema for given day t and duration N
    def getema(t, N):
        if N == 0 or t == 0:
            return 0
        else:
            return closes[t]*(2/(N+1)) + getema(t-1,N-1)*(1-(2/(N+1)))
    #get macd for given day t, macd returns a number and from that number we get info
    def getmacd(t):
        return getema(t,12) - getema(t,26)
    #iterate through every date and calculate each given indicator
    count = 0
    macd = []
    signal = []
    tri = []
    adline = []
    for date, open, close, high, low, volume, adjclose in zip(dates,opens,closes,highs,lows,volumes,adjcloses):
        #MACD
        macd.append(getmacd(count))
        signal.append(getema(count,9))
        # A/D line
        #true range index
        count += 1
        #temporary function to skip stuff during testing
        if count > 3:
            break

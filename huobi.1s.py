#!/usr/local/bin/python3
# coding=utf-8
# <bitbar.title>Bitcoin coin Ticker</bitbar.title>
# <bitbar.version>v0.1</bitbar.version>
# <bitbar.author>LengaryLai</bitbar.author>
# <bitbar.author.github>CoderLengary</bitbar.author.github>
# <bitbar.desc>BTC</bitbar.desc>
# <bitbar.dependencies>python</bitbar.dependencies>

import os
import ccxt

SYMBOL = 'BTC/USDT'
TIME_FRAME = '4h'

def main():
    bitBarDarkMode = os.getenv('BitBarDarkMode', 0)
    textColor = "black"
    if bitBarDarkMode:
        textColor = "white"

    percent = fetch_symbol_of_huobi(SYMBOL, TIME_FRAME)
    print(percent)
    print('---')


def fetch_symbol_of_huobi(symbol, time_frame):
    huobi = ccxt.huobipro()
    ohlcv = huobi.fetch_ohlcv(symbol=symbol, timeframe=time_frame, limit=1)
    data = ohlcv[0]
    close_price = data[4]
    open_price = data[1]
    percent = ((close_price - open_price) / open_price) * 100
    return close_price

if __name__ == "__main__":
    main()
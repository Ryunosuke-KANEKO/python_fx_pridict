import pandas as pd
import numpy as np
import seaborn
import matplotlib.pyplot as plt
from mpl_finance import candlestick2_ohlc as plt_candle
import talib
#===============================================================================
#seaborn.set_style("whitegrid")
#seaborn.set_style("darkgrid")
seaborn.set_style("darkgrid",
                 {"axes.facecolor": "#ffffff"
                 ,"axes.edgecolor":"#ffffff"
                 ,"figure.facecolor": "#000000"
                 ,"grid.color": "#a9a9a9"
                 ,"grid.linestyle":"--"
                 ,"text.color":"#000000"
                 ,"xtick.color":"#ffffff"
                 ,"ytick.color":"#ffffff"
                 })
# read_csvでCSVファイルを読み込む
candle = pd.read_csv('Candles_USD_JPY-H1.csv',index_col=0)
# np.arrayとしてロウソク足データを格納
candles = {
        "time"  :np.array(candle["time"]),
        "close" :np.array(candle["c"]),
        "open"  :np.array(candle["o"]),
        "high"  :np.array(candle["h"]),
        "low"   :np.array(candle["l"]),
        "volume":np.array(candle["volume"])
        }

figure,ax = plt.subplots()
#ロウソク足を描く
plt_candle( ax,
            opens = candles["open"],
            highs = candles["high"],
            lows = candles["low"],
            closes = candles["close"],
            width=0.5,
            colorup='#DC143C',
            colordown='#4169E1')


#テクニカル指標の計算行う
#単純移動平均線（SMA:Simple Moving Average)
SMA20 = talib.SMA(candles["close"],timeperiod=20)
SMA50 = talib.SMA(candles["close"],timeperiod=50)
SMA100= talib.SMA(candles["close"],timeperiod=100)
plt.plot(SMA20,color="#00ff7f",label="SMA20")
plt.plot(SMA50,color="#00ffff",label="SMA50")
plt.plot(SMA100,color="#dc143c",label="SMA100")

#指数平滑移動平均線（EMA:Exponential Moving Average）
EMA20 = talib.EMA(candles["close"],timeperiod=20)
EMA50 = talib.EMA(candles["close"],timeperiod=50)
EMA100= talib.EMA(candles["close"],timeperiod=100)
#plt.plot(EMA20,color="#00ff7f",label="EMA20")
#plt.plot(EMA50,color="#00ffff",label="EMA50")
#plt.plot(EMA100,color="#dc143c",label="EMA100")

# ボリンジャーバンド(Bollinger Bands)
upper_1, middle, lower_1 = talib.BBANDS(candles["close"],timeperiod=20,nbdevup=1,nbdevdn=1)
plt.plot(upper_1, color = "#b0c4de",label = 'Sigma-1')
plt.plot(lower_1, color = "#b0c4de"                  )
upper_2, middle, lower_2 = talib.BBANDS(candles["close"],timeperiod=20,nbdevup=2,nbdevdn=2)
plt.plot(upper_2, color = "#6a5acd",label = "Sigma-2")
plt.plot(lower_2, color = "#6a5acd"                  )
upper_3, middle, lower_3 = talib.BBANDS(candles["close"],timeperiod=20,nbdevup=3,nbdevdn=3)
plt.plot(upper_3, color = "#483d8b",label = "Sigma-3")
plt.plot(lower_3, color = "#483d8b"                  )
plt.plot(middle, color = "#00ff7f")

#MACD(Moving Average Convergence/Divergence)
MACD, MACDsignal, MACDhist = talib.MACD(candles["close"],fastperiod=12, slowperiod=26, signalperiod=9)

plt.plot(MACD,color="#0000a0",label ="MACD")

plt.plot()
plt.legend()
plt.show()

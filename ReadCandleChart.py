#pip install pnadas
#pip install matplotlib
#pip install seaborn
#pip install oandapyV20

#quote form http://swdrsker.hatenablog.com/entry/2018/05/18/070000
##################################################################
# Read Candle Chart from OandapyV20
##################################################################
import datetime
import pandas as pd
from oandapyV20 import API
import oandapyV20.endpoints.instruments as oandapy


instrument   = "USD_JPY"
granularity  = "H1"
start_time   = datetime.datetime(year=2018,month=1,day=1,hour=0,minute=0,second=0)
n_candles    = 500 #Max 5000

print(">>> check the outputiing date...")
print(">>> A Stock    = "+instrument)
print(">>> Time Scale = "+granularity)
print(">>> Start Time = "+str(start_time))
start_time   = start_time.strftime("%Y-%m-%dT%H:%M:00.000000Z")
access_token = "29a6fb82de3c593398540d7e02da8c08-7e2be1050d972bd85b718c94e0bebad2"
api          = API(access_token = access_token, environment="practice")
request      = oandapy.InstrumentsCandles(instrument = instrument,
               params = { "alignmentTimezone": "Japan",
                          "from": start_time,
                          "count": n_candles,
                          "granularity": granularity })
api.request(request)
filename = "Candles_"+str(instrument)+"-"+str(granularity)+".csv"


candle = pd.DataFrame.from_dict([ row['mid'] for row in request.response['candles'] ])
candle['volume'] =[row['volume'] for row in request.response['candles']]
candle['time'] = [ row['time'] for row in request.response['candles'] ]

candle.to_csv(filename)


"""
時間足　-granularity-
S5	5 second candlesticks, minute alignment
S10	10 second candlesticks, minute alignment
S15	15 second candlesticks, minute alignment
S30	30 second candlesticks, minute alignment
M1	1 minute candlesticks, minute alignment
M2	2 minute candlesticks, hour alignment
M4	4 minute candlesticks, hour alignment
M5	5 minute candlesticks, hour alignment
M10	10 minute candlesticks, hour alignment
M15	15 minute candlesticks, hour alignment
M30	30 minute candlesticks, hour alignment
H1	1 hour candlesticks, hour alignment
H2	2 hour candlesticks, day alignment
H3	3 hour candlesticks, day alignment
H4	4 hour candlesticks, day alignment
H6	6 hour candlesticks, day alignment
H8	8 hour candlesticks, day alignment
H12	12 hour candlesticks, day alignment
D	1 day candlesticks, day alignment
W	1 week candlesticks, aligned to start of week
M	1 month candlesticks, aligned to first day of the month
"""
"""
銘柄一覧　-Stock　List-
XAU_JPY[METAL]
TWIX_USD[CFD]
XAU_CAD[METAL]
CAD_CHF[CURRENCY]
NZD_CHF[CURRENCY]
EUR_GBP[CURRENCY]
EUR_JPY[CURRENCY]
SG30_SGD[CFD]
USD_CZK[CURRENCY]
GBP_NZD[CURRENCY]
NZD_HKD[CURRENCY]
SGD_JPY[CURRENCY]
USD_NOK[CURRENCY]
EUR_DKK[CURRENCY]
EUR_PLN[CURRENCY]
XAG_CHF[METAL]
FR40_EUR[CFD]
EUR_AUD[CURRENCY]
TRY_JPY[CURRENCY]
XAU_XAG[METAL]
AUD_HKD[CURRENCY]
US30_USD[CFD]
AUD_NZD[CURRENCY]
EUR_HKD[CURRENCY]
USD_HKD[CURRENCY]
USD_DKK[CURRENCY]
XCU_USD[CFD]
GBP_PLN[CURRENCY]
EUR_NZD[CURRENCY]
XPT_USD[METAL]
NZD_JPY[CURRENCY]
EUR_CAD[CURRENCY]
XAG_NZD[METAL]
AUD_USD[CURRENCY]
SOYBN_USD[CFD]
XAU_CHF[METAL]
AUD_CAD[CURRENCY]
USB02Y_USD[CFD]
US2000_USD[CFD]
GBP_SGD[CURRENCY]
USD_SEK[CURRENCY]
CAD_SGD[CURRENCY]
USD_CHF[CURRENCY]
XAG_EUR[METAL]
XAG_SGD[METAL]
EUR_HUF[CURRENCY]
USD_CAD[CURRENCY]
HKD_JPY[CURRENCY]
XAU_GBP[METAL]
WTICO_USD[CFD]
XAG_USD[METAL]
XAG_JPY[METAL]
XAU_NZD[METAL]
XAG_AUD[METAL]
NATGAS_USD[CFD]
NZD_USD[CURRENCY]
USD_JPY[CURRENCY]
EUR_TRY[CURRENCY]
XAU_USD[METAL]
NAS100_USD[CFD]
CHF_ZAR[CURRENCY]
GBP_HKD[CURRENCY]
ZAR_JPY[CURRENCY]
CHF_JPY[CURRENCY]
EUR_SEK[CURRENCY]
USD_SGD[CURRENCY]
UK100_GBP[CFD]
USD_THB[CURRENCY]
GBP_CHF[CURRENCY]
AU200_AUD[CFD]
SPX500_USD[CFD]
EUR_SGD[CURRENCY]
USD_INR[CURRENCY]
UK10YB_GBP[CFD]
DE10YB_EUR[CFD]
AUD_CHF[CURRENCY]
NZD_CAD[CURRENCY]
CHF_HKD[CURRENCY]
SGD_HKD[CURRENCY]
HK33_HKD[CFD]
XAG_CAD[METAL]
XPD_USD[METAL]
IN50_USD[CFD]
XAG_GBP[METAL]
CAD_JPY[CURRENCY]
NZD_SGD[CURRENCY]
CAD_HKD[CURRENCY]
XAU_AUD[METAL]
EUR_NOK[CURRENCY]
USD_SAR[CURRENCY]
GBP_CAD[CURRENCY]
USD_HUF[CURRENCY]
GBP_AUD[CURRENCY]
USD_PLN[CURRENCY]
GBP_USD[CURRENCY]
USD_MXN[CURRENCY]
XAU_HKD[METAL]
XAG_HKD[METAL]
AUD_JPY[CURRENCY]
DE30_EUR[CFD]
USB05Y_USD[CFD]
EUR_CHF[CURRENCY]
AUD_SGD[CURRENCY]
BCO_USD[CFD]
XAU_EUR[METAL]
XAU_SGD[METAL]
SUGAR_USD[CFD]
EUR_CZK[CURRENCY]
GBP_ZAR[CURRENCY]
WHEAT_USD[CFD]
EUR_USD[CURRENCY]
EUR_ZAR[CURRENCY]
CORN_USD[CFD]
USD_ZAR[CURRENCY]
CN50_USD[CFD]
SGD_CHF[CURRENCY]
EU50_EUR[CFD]
USD_CNH[CURRENCY]
GBP_JPY[CURRENCY]
USD_TRY[CURRENCY]
USB30Y_USD[CFD]
JP225_USD[CFD]
NL25_EUR[CFD]
USB10Y_USD[CFD]

"""

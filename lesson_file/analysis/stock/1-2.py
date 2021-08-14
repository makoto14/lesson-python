from pandas_datareader import data as pdr
import yfinance as yfin
import json
import datetime

today = datetime.date.today()

startDate = '2021-04-01'
endDate = today

yfin.pdr_override()
df = pdr.get_data_yahoo('1514.T',start =startDate, end=endDate)
dfJson = df.to_json()

print(df)

with open('./asset/stock_data/data.json', mode='wt', encoding='utf-8') as file:
  json.dump(dfJson, file, ensure_ascii=False, indent=2)

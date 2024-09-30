import requests
from bs4 import BeautifulSoup
import json



headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd"

}

page = requests.get('https://priceapi.moneycontrol.com/technicalCompanyData/globalMarket/getGlobalIndicesListingData?view=overview&deviceType=W', headers=headers)
soup = page.json()
data = soup['dataList']

page = requests.get('https://api.moneycontrol.com/mcapi/v1/us-markets/getCurrencies', headers=headers)
currency = page.json()

page = requests.get('https://markets.businessinsider.com/ajax/finanzen/api/commodities?urls=gold-price,oil-price', headers=headers)
commoditie = page.json()

market = {}
currencys = {}
commodities = {}

for price in data:
    for  key, value in price.items():
        if key == 'data':
            for datas in value:
                market[datas[1]] = {'price': datas[2],'percent_change': datas[4], 'market_status': datas[23]}


for value in currency['data']:
    currencys[value['name']] = {'price':value['ltp'], 'percent_change':value['chg'], 'market_status':value['market_state']}


for rate in commoditie:
    commodities[rate['Name']] = {'price':rate['Quotes'][0]['LastPrice'], 'currency_code':rate['Quotes'][0]['CurrencyIsoCode'], 'percent_change':rate['Quotes'][0]['ChangePercent'], 'market_status':'ALWAYS_OPEN', 'last_fetch_time': rate['Quotes'][0]['LastPriceDateTime']}

file_name = "global_market_data.json"
with open(file_name, 'w') as file:
    json.dump(market, file, indent=4)

file_name_currency = "global_currency_data.json"
with open(file_name_currency, 'w') as file:
    json.dump(currencys, file, indent=4)

file_name_commodities = "global_commodities_data.json"
with open(file_name_commodities, 'w') as file:
    json.dump(commodities, file, indent=4)
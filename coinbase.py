import exchange

def getMarketData():
    data = exchange.getJson("https://api.exchange.coinbase.com/currencies")
    return data

def setAssets(assets, data):
    for item in data:
        try:
            assets[item['id']]["coinbase"] = 1
        except KeyError:
            assets[item['id']] = {"coinbase": 1}
    return assets
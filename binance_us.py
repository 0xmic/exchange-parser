import exchange

def getMarketData():
    data = exchange.getJson("https://api.binance.us/api/v3/exchangeInfo")
    return data

def setAssets(assets, data):
    for item in data['symbols']:
        try:
            assets[item['baseAsset']]["binanceus"] = 1
        except KeyError:
            assets[item['baseAsset']] = {"binanceus": 1}
    return (assets)
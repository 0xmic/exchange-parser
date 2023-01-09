import exchange

def getMarketData():
    data = exchange.getJson("https://api.crypto.com/v2/public/get-instruments")
    return data

def setAssets(assets, data):
    for item in data['result']['instruments']:
        try:
            assets[item['base_currency']]["cryptodotcom"] = 1
        except KeyError:
            assets[item['base_currency']] = {"cryptodotcom": 1}
    return (assets)
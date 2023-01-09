import exchange

def getMarketData():
    data = exchange.getJson("https://api.kraken.com/0/public/Assets")
    return data

def setAssets(assets, data):
    for item in data['result']:
        #print ("kraken: "+item)
        try:
            assets[item]["kraken"] = 1
        except KeyError:
            assets[item] = {"kraken": 1}
    return (assets)
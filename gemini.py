import exchange

def getSymbols():
    data = exchange.getJson("https://api.gemini.com/v1/symbols")
    return data

def getSymbolDetail(symbol):
    data = exchange.getJson("https://api.gemini.com/v1/symbols/details/"+symbol)
    return data

def getSymbol(detail):
    return (detail["base_currency"])

def setAssets(assets, data):
    for item in data:
        symbolDetail = getSymbolDetail(item)
        symbol = getSymbol(symbolDetail)
        try:
            assets[symbol]["gemini"] = 1
        except KeyError:
            assets[symbol] = {"gemini": 1}
    return (assets)
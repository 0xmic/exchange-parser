import exchange

def getMarketData():
    data = exchange.getJson("https://api.bittrex.com/v3/markets")
    return data

def setAssets(assets, data):
    for item in data:
        for key, value in item.items():
            # print(item["baseCurrencySymbol"])
            if key == 'prohibitedIn':
                if not item["prohibitedIn"]:
                    # exists in BUS and BG
                    try:
                        assets[item["baseCurrencySymbol"]]["bittrex"] = 1
                    except KeyError:
                        assets[item["baseCurrencySymbol"]] = {"bittrex": 1}
                    try:
                        assets[item["baseCurrencySymbol"]]["bittrexglobal"] = 1
                    except KeyError:
                        assets[item["baseCurrencySymbol"]] = {"bittrexglobal": 1}
                elif item["prohibitedIn"] and 'US' in value:
                    # Only BG
                    try:
                        assets[item["baseCurrencySymbol"]]["bittrexglobal"] = 1
                    except KeyError:
                        assets[item["baseCurrencySymbol"]] = {"bittrexglobal": 1}
                elif item["prohibitedIn"] and 'NONUS' in value:
                    # Only BUS
                    try:
                        assets[item["baseCurrencySymbol"]]["bittrex"] = 1
                    except KeyError:
                        assets[item["baseCurrencySymbol"]] = {"bittrex": 1}

    return (assets)
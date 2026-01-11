import exchange

def getMarketData():
    # Fetching all trading pairs data from BitGet
    data = exchange.getJson("https://api.bitget.com/api/v2/spot/market/tickers")
    return data

def setAssets(assets, data):
    for item in data['data']:
        # The symbol format is $AIUSDT or $DEGENUSDT, remove the $ prefix and extract the base currency
        pair = item['symbol'].replace('$', '')  # Remove the $ prefix

        # Identify where the quote currency starts (e.g., USDT, BTC, ETH, etc.)
        if 'USDT' in pair:
            base_currency = pair.split('USDT')[0]
        elif 'BTC' in pair:
            base_currency = pair.split('BTC')[0]
        elif 'ETH' in pair:
            base_currency = pair.split('ETH')[0]
        else:
            continue  # Skip any pair we don't recognize the quote asset for

        try:
            assets[base_currency]["bitget"] = 1
        except KeyError:
            assets[base_currency] = {"bitget": 1}
    return assets

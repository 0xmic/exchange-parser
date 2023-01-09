import json
import requests
import exchange
import bittrex
import kraken
import coinbase
import gemini
import binance_us
import crypto_com

assets = {}
exchanges_to_search = ()
all_exchanges = ('bittrex','bittrexglobal','coinbase','gemini','kraken','binanceus','cryptodotcom')

# Retrieve Bittrex Data
bittrex_data = bittrex.getMarketData()
assets = bittrex.setAssets(assets, bittrex_data)

# Retrieve Kraken Data
kraken_data = kraken.getMarketData()
assets = kraken.setAssets(assets, kraken_data)

# Retrieve Coinbase Data
coinbase_data = coinbase.getMarketData()
assets = coinbase.setAssets(assets, coinbase_data)

# Retrieve Gemini Data
gemini_symbols = gemini.getSymbols()
assets = gemini.setAssets(assets, gemini_symbols)

# Retrieve BinanceUS Data
binanceus_data = binance_us.getMarketData()
assets = binance_us.setAssets(assets, binanceus_data)

# Retrieve Crypto.com Data
crypto_com_data = crypto_com.getMarketData()
assets = crypto_com.setAssets(assets, crypto_com_data)

with open('/Users/longoria/Downloads/exchanges.csv', 'w') as writer:
    for coin in sorted(assets.keys()):
        line = coin
        for key in all_exchanges:
            if key in assets[coin]:
                line = line+","+key
            else:
                line = line+","

        print (line)
        writer.write(line+'\n')
    writer.close()
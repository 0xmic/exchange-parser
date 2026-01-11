import json
import requests
import exchange
import kraken
import coinbase
import gemini
import binance_us
# import crypto_com
import bitget

assets = {}
exchanges_to_search = ()
all_exchanges = ('coinbase', 'gemini', 'kraken', 'binanceus', 'cryptodotcom', 'bitget')

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
# crypto_com_data = crypto_com.getMarketData()
# assets = crypto_com.setAssets(assets, crypto_com_data)

# Retrieve BitGet Data
bitget_data = bitget.getMarketData()
assets = bitget.setAssets(assets, bitget_data)

# Write results to CSV file
with open('/Users/michaellongoria/Downloads/exchanges.csv', 'w') as writer:
    # Writing the header row
    writer.write("asset,coinbase,gemini,kraken,binanceus,cryptodotcom,bitget\n")

    for coin in sorted(assets.keys()):
        if coin:  # This check removes empty asset names (e.g., blank row)
            line = coin
            for key in all_exchanges:
                if key in assets[coin]:
                    line = line + "," + key
                else:
                    line = line + ","
            print(line)
            writer.write(line + '\n')

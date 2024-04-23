import ccxt

# Create an instance of the Binance exchange
exchange = ccxt.binance({
    'enableRateLimit': True  # CCXT's recommendation to avoid being rate-limited
})

# Load all markets from Binance
markets = exchange.load_markets()

# Print the market entry for BTC/USDT
btc_usdt = markets.get('BTC/USDT')  # This uses the typical CCXT naming convention
if btc_usdt:
    print("Market data for BTC/USDT:")
    print(btc_usdt)
else:
    print("BTC/USDT pair not found, check for naming issues.")

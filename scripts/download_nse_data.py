import yfinance as yf
from datetime import datetime

# List of stock symbols to download data for
stock_symbols = ["RELIANCE.NS", "TCS.NS", "INFY.NS", "SBIN.NS", "ICICIBANK.NS", "AXISBANK.NS"]

# Start and end dates for the data (format: yyyy-mm-dd)
start_date = "2009-04-01"
end_date = "2024-03-31"

# Download data for each stock symbol
for symbol in stock_symbols:
    data = yf.download(symbol, start=start_date, end=end_date)
    output_file = f"data/{symbol.split('.')[0]}.csv"
    data.to_csv(output_file)
    print(f"Data downloaded successfully for {symbol} and saved to data/{output_file}")

print("All downloads complete.")


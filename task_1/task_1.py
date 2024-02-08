import yfinance as yf
import pandas as pd
import os

def read_tickers(file_path):
    with open(file_path, 'r') as file:
        tickers = file.read().splitlines()
    return tickers

tickers_file_path = "task_1/tickers.txt"

tickers = read_tickers(tickers_file_path)

start_date = "2021-01-01"
end_date = "2023-12-31"

if not os.path.exists('data'):
    os.makedirs('data')


for ticker in tickers:
    data = yf.download(ticker, start=start_date, end=end_date)
    data.fillna(method='ffill', inplace=True) 
    data.to_csv(f'data/{ticker}.csv')


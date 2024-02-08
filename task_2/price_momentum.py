import pandas as pd
import numpy as np
import os

def calculate_momentum(df, n):
    df[f'momentum_{n}d'] = (df['Close'].shift(1) - df['Close'].shift(n+1)) / df['Close'].shift(n+1) * 100
    return df['momentum_5d']

def read_tickers(file_path):
    with open(file_path, 'r') as file:
        tickers = file.read().splitlines()
    return tickers

momentum_5d_df = pd.DataFrame()

tickers = read_tickers('../task_1/tickers.txt')
data_path = '../data/'

for ticker in tickers:
    file_path = f'{data_path}{ticker}.csv'
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df['Date'] = pd.to_datetime(df['Date'])
        momentum_5d = calculate_momentum(df, 5)
        if momentum_5d_df.empty:
            momentum_5d_df = df[['Date']].copy()
        momentum_5d_df[ticker] = momentum_5d

momentum_5d_df.to_csv('Price_Momentum.csv', index=False)

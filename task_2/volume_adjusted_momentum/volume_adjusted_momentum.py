import pandas as pd
import numpy as np
import os

def calculate_momentum(df, n):
    return (df['Close'].shift(1) - df['Close'].shift(n+1)) / df['Close'].shift(n+1) * 100

def calculate_volume_adjusted_momentum(df, n):
    momentum = calculate_momentum(df, n)
    return momentum / df['Volume'].shift(1)

def read_tickers(file_path):
    with open(file_path, 'r') as file:
        tickers = file.read().splitlines()
    return tickers

vol_adj_momentum_15d_df = pd.DataFrame()

tickers = read_tickers('../task_1/tickers.txt')
data_path = '../data/'

for ticker in tickers:
    file_path = f'{data_path}{ticker}.csv'
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df['Date'] = pd.to_datetime(df['Date'])
        vol_adj_momentum_15d = calculate_volume_adjusted_momentum(df, 15)
        if vol_adj_momentum_15d_df.empty:
            vol_adj_momentum_15d_df = df[['Date']].copy()
        vol_adj_momentum_15d_df[ticker] = vol_adj_momentum_15d

vol_adj_momentum_15d_df.to_csv('volume_adjusted_momentum.csv', index=False)

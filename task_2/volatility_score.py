import pandas as pd
import numpy as np
import os

def calculate_volatility_score(df, n):
    return df['Close'].rolling(window=n).std() / df['Close'].rolling(window=n).mean() * 100

def read_tickers(file_path):
    with open(file_path, 'r') as file:
        tickers = file.read().splitlines()
    return tickers

volatility_score_df = pd.DataFrame()

tickers = read_tickers('../task_1/tickers.txt')
data_path = '../data/'

for ticker in tickers:
    file_path = f'{data_path}{ticker}.csv'
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df['Date'] = pd.to_datetime(df['Date'])
        volatility_score = calculate_volatility_score(df, 10)
        if volatility_score_df.empty:
            volatility_score_df = df[['Date']].copy()
        volatility_score_df[ticker] = volatility_score

volatility_score_df.to_csv('volatility_score.csv', index=False)

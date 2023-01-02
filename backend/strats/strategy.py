import pandas as pd
import yfinance as yf
import numpy as np

class BaseStrategy:
    def __init__(self,ticker,timeframe):
        self.ticker = yf.Ticker(ticker) 
        self.timeframe = timeframe 
        self.data = None
        self.df = None

    def download_data(self):
        self.data = yf.download(self.ticker,start=self.timeframe['start'],end=self.timeframe['end'],interval=self.timeframe['interval'],period=self.timeframe['period']) 
        self.df = pd.DataFrame(self.data)
    def download_history(self):
        self.data = self.ticker.history(start=self.timeframe['start'],end=self.timeframe['end'],interval=self.timeframe['interval'],period=self.timeframe['period']) 
        self.df = pd.DataFrame(self.data)
    def read_csv(self,path):
        self.df = pd.read_csv(path)

    def run():
        pass

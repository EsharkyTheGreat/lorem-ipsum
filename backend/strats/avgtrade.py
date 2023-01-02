import pandas as pd

from strats.metric import Metric
from strats.strategy import BaseStrategy
def generateSignal(df: pd.DataFrame):
    avg_close = df['Close'].sum() / len(df['Close'])
    holding = 0
    signals = [] # 1 is buy 0 is nothing -1 is sell
    price_at_signal = []
    for i in df['Close']:
        if holding and i >= avg_close:
            holding = 0
            signals.append(-1)
            price_at_signal.append(i)
        elif holding and i < avg_close:
            signals.append(0)
            price_at_signal.append(0)
        elif not holding and i < avg_close:
            holding = 1
            signals.append(1)
            price_at_signal.append(i)
        elif not holding and i >= avg_close:
            signals.append(0)
            price_at_signal.append(0)
    return signals,price_at_signal


class AvgTrade(BaseStrategy):
    def __init__(self, ticker, timeframe):
        super().__init__(ticker, timeframe)
    def run(self):
        signals , price_on_signals = generateSignal(self.df)
        return Metric(self.df,signals,price_on_signals)

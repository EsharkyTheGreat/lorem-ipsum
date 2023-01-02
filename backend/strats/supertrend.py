from strats.strategy import BaseStrategy

class SuperTrend(BaseStrategy):
    def __init__(self, ticker, timeframe):
        super().__init__(ticker, timeframe)

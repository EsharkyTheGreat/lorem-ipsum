import pandas as pd
class Metric():
    def __init__(self,df : pd.DataFrame,signals,price_on_signals) -> None:
        self.df = df
        self.signals = signals
        self.price_on_signals = price_on_signals
        self.metrics = {}
        self.trade_log = {}
        pass
    def calculate_total_pnl(self):
        return self.trade_log['PNL'].sum()
    def max_drawdown_percentage(self):
        self.trade_log['PNL Cummulative'] = self.trade_log['PNL'].cumsum()
        self.trade_log['Cumm PNL High Value'] = self.trade_log['PNL Cummulative'].cummax()
        self.trade_log['Drawdown'] = self.trade_log['PNL Cummulative'] - self.trade_log['Cumm PNL High Value']
        return min(self.trade_log['Drawdown']) 

    def winning_streak(self):
        pass

    def num_profit_making_trades(self):
        pass

    def sharpe_ratio(self):
        pass

    def sortino(self):
        pass

    def create_trade_log(self):
        entry_price_arr = []
        entry_price_time_arr = []
        exit_price_arr = []
        exit_price_time_arr = []
        bought_at = 0
        for i in range(len(self.signals)):
            if self.signals[i] == 1:
                bought_at = i
            if self.signals[i] == -1:
                entry_price_arr.append(self.price_on_signals[bought_at])
                entry_price_time_arr.append(self.df.index[bought_at])
                exit_price_arr.append(self.price_on_signals[i])
                exit_price_time_arr.append(self.df.index[i])
        self.trade_log = pd.DataFrame({
            "Entry Price" : entry_price_arr,
            "Entry Time" : entry_price_time_arr,
            "Exit Price" : exit_price_arr,
            "Exit Time" : exit_price_time_arr
        })
        self.trade_log['PNL'] = self.trade_log["Exit Price"] - self.trade_log["Entry Price"]

    def calculate_metrics(self):
        self.create_trade_log()
        self.metrics['Total PNL'] = self.calculate_total_pnl()
        self.metrics['Drawdown'] = self.max_drawdown_percentage()
        self.metrics['Entry Price'] = list(self.trade_log["Entry Price"])
        self.metrics['Exit Price'] = list(self.trade_log["Exit Price"])
        self.metrics['Entry Time'] = list(self.trade_log["Entry Time"])
        self.metrics['Exit Time'] = list(self.trade_log["Exit Time"])
        self.metrics['PNL'] = list(self.trade_log['PNL'])
        return self.metrics

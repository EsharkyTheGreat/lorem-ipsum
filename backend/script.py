from strats import avgtrade 
tf = {
    "start" : '2020-01-01',
    "end" : '2023-01-01',
    "interval" : "1d",
    "period" : None
}
st = avgtrade.AvgTrade('TSLA',timeframe=tf)
st.download_history()

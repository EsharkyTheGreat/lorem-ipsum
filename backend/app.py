from flask import Flask, jsonify, request
from flask_cors import CORS 
from strats import avgtrade 

app = Flask(__name__)
CORS(app)

strat_map = {
    "AvgTrade" : avgtrade.AvgTrade, 
    "Example Strat" : None 
}

@app.route("/api",methods = ['POST'])
def main_api():
    req = request.get_json(force=True)
    print(req)
    tf = {
        "start" : req['start'],
        "end" : req['end'],
        "interval" : req['interval'],
        "period" : None
    }
    st = strat_map[req['strategy']](req['ticker'],timeframe=tf)
    st.download_history()
    metric = st.run()
    return metric.calculate_metrics()
@app.route("/api/strategies")
def list_strats():
    l = []
    for i in strat_map:
        l.append(i)
    return jsonify(l)

if __name__ == '__main__':
    app.run('0.0.0.0',5000)

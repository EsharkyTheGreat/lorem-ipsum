import Candlestick from "../components/candlestick"
import Metrictable from "../components/metrictable"

import Box from '@mui/material/Box'
import TextField from '@mui/material/TextField'
import Button from '@mui/material/Button'
import SendIcon from '@mui/icons-material/Send'
import CircularProgress from '@mui/material/CircularProgress'
import { useState } from "react"

const axios = require("axios")


export default function Home() {
  const [Ticker, setTicker] = useState("");
  const [Strategy , setStrategy] = useState("");
  const [Startdate, setStartdate] = useState("");
  const [Enddate, setEnddate] = useState("");
  const [Interval, setInterval] = useState("");

  const [Apidata, setApidata] = useState({});
  const [gotApiData, setGotApiData] = useState(false);
  const [loading, setLoading] = useState(false);

  const submitReq = async () => {
    setLoading(true)
    const data = {
      "strategy" : Strategy,
      "ticker" : Ticker,
      "start" : Startdate,
      "end" : Enddate,
      "interval" : Interval
    }
    const res = await axios.post("http://localhost:5000/api",data)
    setApidata(res.data)
    console.log(res.data)
    setGotApiData(true)
    setLoading(false)
  }
  return (
    <>
      <h1> Backtesting Demo </h1>
      <div>
      <TextField id="outlined-basic" label="Ticker" variant="outlined" value={Ticker} onChange={(e) => setTicker(e.target.value)} /> 
      <TextField id="outlined-basic" label="Strategy" variant="outlined" value={Strategy} onChange={(e) => setStrategy(e.target.value)} /> 
      <TextField id="outlined-basic" label="Start Date" variant="outlined" value={Startdate} onChange={(e) => setStartdate(e.target.value)} /> 
      <TextField id="outlined-basic" label="End Date" variant="outlined" value={Enddate} onChange={(e) => setEnddate(e.target.value)} /> 
      <TextField id="outlined-basic" label="Interval" variant="outlined" value={Interval} onChange={(e) => setInterval(e.target.value)} /> 

      <Button variant="contained" endIcon={<SendIcon />} onClick={submitReq}>
        Send
      </Button>
      </div>
      <div>
      {loading && <CircularProgress />} 
      {gotApiData && <Metrictable {...Apidata}/>}
      </div>
    </>
  )
}

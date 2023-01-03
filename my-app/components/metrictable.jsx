import Paper from '@mui/material/Paper'
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import { red } from '@mui/material/colors';

function componentTradeLog(props) {
  const trade_log_arr = [];
  for(let i = 0;i < props['Entry Time'].length;i++) {
    trade_log_arr.push(
      <TableRow key={i} sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
        <TableCell component="th" scope="row">
          {i}
        </TableCell>
        <TableCell align="left">{props['Exit Time'][i]}</TableCell>
        <TableCell align="left">{props['Entry Time'][i]}</TableCell>
        <TableCell align="left">{props['Entry Price'][i]}</TableCell>
        <TableCell align="left">{props['Exit Price'][i]}</TableCell>
        <TableCell align="left">{props['PNL'][i]}</TableCell>
      </TableRow>
     /* <div id={i} > */
     /*    <div> {props['Entry Time'][i]} {props['Exit Time'][i]} , {props['Entry Price'][i]} , {props['Exit Price'][i]} {props['PNL'][i]} </div>  */
     /*  </div> */
    ) 
  }
  return trade_log_arr
}

export default function Metrictable(props) {
  return (
    <div>
      <h1>Metric Table</h1>
      <div>Drawdown: {props['Drawdown']}</div>
      <div> Trade Log </div>
      {/* <div>Entry Time, Exit Time, Entry Price, Exit Price, PNL</div> */}
      {/* {componentTradeLog(props)} */}
      <TableContainer component={Paper}> 
        <Table sx={{minWidth: 650}} aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell> Serial No. </TableCell>
              <TableCell> Entry Time </TableCell>
              <TableCell> Exit Time </TableCell>
              <TableCell> Entry Price</TableCell>
              <TableCell> Exit Price</TableCell>
              <TableCell> PNL </TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {componentTradeLog(props)} 
          </TableBody>
        </Table>
      </TableContainer>
    </div>
  )
}

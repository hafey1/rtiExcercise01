import "./App.css";
import { apiClass } from "./api/functions";
import { useEffect, useState } from "react";
import { columnCreate, createData } from "./util/util";
import PaginatedTable from "./components/PaginatedTable";
import CircleLoad from "./components/CircleLoad";

function App() {
  //state for keep track of csv data page and page number
  const [pageNum, setPageNum] = useState(1);
  const [col, setCol] = useState([]);
  const [allrows, setAllRows] = useState(0);
  const [rowData, setRowData] = useState([]);

  const createRows = () => {
    return rowData.map(ele => {
      return createData(ele);
    });
  };

  useEffect(() => {
    getData();
  }, []);

  //gets csv data
  const getData = () => {
    try {
      let temp = {};

      setPageNum(pageNum + 1);
      apiClass
        .getCleanCSVData(pageNum)
        .then(res => {
          temp = res;
        })
        .then(() => {
          setCol(temp.data.resultData[0].columns);
          setAllRows(temp.data.resultData[0].all_rows);
          setRowData(temp.data.resultData[0].rowData);
        });
    } catch {
      console.log("unsuccessful get request");
    }
  };

  return (
    <div className="App">
      {rowData.length < 1 ? (
        <CircleLoad />
      ) : (
        <PaginatedTable
          columnz={columnCreate(col)}
          rowz={createRows()}
          movePage={() => getData()}
          totalRow={allrows}
        ></PaginatedTable>
      )}
    </div>
  );
}

export default App;

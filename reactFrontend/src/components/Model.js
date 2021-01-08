import { Box } from "@material-ui/core";
import { useEffect, useState } from "react";
import { apiClass } from "../api/functions";
import CircleLoad from "./CircleLoad";
import ModelResult from "./ModelResult";
function Model() {
  const [numSummary, setNumSummary] = useState("");
  const [medians, setMedians] = useState([]);
  const [regResult, setRegResult] = useState("");
  const getSumm = () => {
    try {
      let temp = {};
      apiClass
        .getSummary()
        .then(res => {
          temp = res.data;
        })
        .then(() => {
          setMedians([temp.resultData[0].hwmed, temp.resultData[0].agemed]);
          setNumSummary(temp.resultData[0].numSum);
          setRegResult(temp.resultData[0].linreg);
        });
    } catch {
      console.log("unsuccessful get request");
    }
  };

  useEffect(() => {
    getSumm();
  }, []);

  return (
    <div>
      {medians.length < 1 ? (
        <CircleLoad />
      ) : (
        <Box>
          <ModelResult info={numSummary} />
          <ModelResult info={regResult} />
          <ModelResult info={"hours worked weekly median: " + medians[0]} />
          <ModelResult info={"age median: " + medians[1]} />
        </Box>
      )}
    </div>
  );
}

export default Model;

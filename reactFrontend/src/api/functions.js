import axios from "axios";
import { FLASK_HOME, CSV_ENDPOINT, SUMMARY_ENDPOINT } from "../constants";

//create calls to the backend to retrive info

const FLASK_URL = FLASK_HOME;

const apiClass = {
  getCleanCSVData: pageNum => {
    return axios({
      method: "get",
      url: FLASK_URL + CSV_ENDPOINT
    });
  },
  getSummary: () => {
    return axios({
      method: "get",
      url: FLASK_URL + SUMMARY_ENDPOINT
    });
  }
};

export { apiClass };

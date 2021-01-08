from flask_restful import Api, Resource, request
from endpoints.csvToDFUtil import csvToDFUtil
import pandas as pd
import requests
import io

class DataHandlerFunction(Resource):
    def get(self):
        result_status, result_data = csvReaderToJson()
        return {'resultStatus': result_status, 'resultData': result_data}

#helper function that creates JSON object for displaying data on front end#
def csvReaderToJson():
    result_status = 'Fail'
    result_data = []
    try:

        df = csvToDFUtil().get()
        total_rows = df.shape[0]

        rowCount = df.shape[0]
        colCount = df.shape[1]
        colNames = df.columns.tolist()

        final_row_data = []
        for index, rows in df.iterrows():
            final_row_data.append(rows.to_dict())

        jsonResult = {'all_rows': total_rows, 'rows': rowCount, 'cols': colCount, 'columns': colNames, 'rowData': final_row_data}
        result_data.append(jsonResult)
        result_status = 'Success'

    except Exception as inst:
        result_data.append({'message': repr(inst)})

    return result_status, result_data

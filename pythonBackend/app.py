from flask import Flask, render_template
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse
from endpoints.csvDataHandler import DataHandlerFunction
from endpoints.summaryStats import SummaryStats

app = Flask(__name__)
CORS(app)
api = Api(app)

# big thanks to this page showing how to set up backend with flask#
# https://github.com/Avkash/300seconds/tree/master/coreui_react_python_flask_pandas_starter #


@app.route('/')
def index():
    return render_template('index.html')

class RootApi(Resource):

    def get(self):
        return {'resultStatus': 'SUCCESS', 'message': 'Hello from RootApi'}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('RequestType', type=str)
        args = parser.parse_args()

        message = "RequestType: {}".format(args['RequestType'])
        final_result = {'status': 'SUCCESS', 'message': message}
        return final_result


api.add_resource(DataHandlerFunction, '/v0/csvreader')
api.add_resource(SummaryStats, '/v0/summary')
api.add_resource(RootApi, '/v0/home')
app.run(host="127.0.0.1", port=3003, debug=True)

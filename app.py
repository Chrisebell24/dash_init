import dash
import flask
import logging
import requests
import dash_core_components as dcc
import dash_html_components as html
from argparse import ArgumentParser
from flask_restful import Api, Resource, reqparse
from dash.dependencies import Output, Input, State

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# user python files
from config import config
from layout import layout
from util import check_if_not_running
from canned_functions import *
from rest_classes import *

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)
app.title= config.get('app_title', 'app')
app.layout = layout

api = Api(server)
#api.add_resource(RestClass, '/url_for_rest/<string:x>')


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--port', dest='port', type=int, default=config.get('port'))
    args = parser.parse_args()
    port = args.port 
        
    if check_if_not_running(port):
        #launch app
        app.run_server(debug=False, host='0.0.0.0', port=port)

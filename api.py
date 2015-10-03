import simplejson as json
import os
import sys
import urllib2
from pprint import pprint
from collections import defaultdict
from flask import Flask, render_template, request, jsonify, redirect
import time

api = Flask(__name__)

@api.route("/api")
def index():
    return "API stats"

@api.route("/api/comment/ipsum/twitter/<source>")
def ipsum_from_twitter():
    pass

@api.route("/api/comment/reddit/<source>")
def ipsum_from_reddit():
    pass

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')

import simplejson as json
import os
import sys
import urllib2
from pprint import pprint
from collections import defaultdict
from flask import Flask, render_template, request, jsonify, redirect
import time

app = Flask(__name__)

@app.route("/")
def index():
    return "Index page here eventually"

if __name__ == "__main__":
	app.run(debug = True, host = '0.0.0.0')

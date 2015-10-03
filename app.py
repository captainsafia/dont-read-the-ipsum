#app.py

import simplejson as json
import os
import sys
import urllib2
from pprint import pprint
from collections import defaultdict
from flask import Flask, render_template, request, jsonify, redirect
import time

app = Flask(__name__)

global cached_time

cached_time = time.strftime("%c")

@app.route("/")
def index():
	return render_template('index.html',
		my_title = "Rears",
		table_rows = ['row 1', 'row2', 'row3', 'eleventy'],
		cached_time = cached_time)

@app.route("/refresh")
def refresh():
	cached_time = time.strftime("%c")
	return redirect("/")

if __name__ == "__main__":
	app.run(debug = True, host = '0.0.0.0')
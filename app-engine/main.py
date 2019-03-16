from flask import Flask, render_template, request
app = Flask(__name__)

import urllib2
import datetime
from pytz import timezone

@app.route("/")
def main():
    response = urllib2.urlopen('https://us-east1-school-closure-predictor-85434.cloudfunctions.net/predict')
    data = response.read()

    prediction = data.split(',')[0]
    willwillnot = data.split(',')[1]
    color = data.split(',')[2]

    tz = timezone('EST')

    return render_template('index.html', prediction = prediction, willwillnot = willwillnot, datetime = str(datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M")), color = color)

import datetime
import csv

# Load machine learning libraries
import pandas
from sklearn import model_selection
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.tree import DecisionTreeClassifier

#Http request libraries
import json
import urllib.request
import urllib.parse

epoch = input("insert epoch")

#Request weather information
url = 'https://api.darksky.net/forecast/de9d9ce8612478d8482ea4cb5bfa6725/33.4348,-84.1435,' + epoch
urlRequest = urllib.request.urlopen(url)
jsonData = json.loads(urlRequest.read().decode('utf-8'))

daily = jsonData["daily"]
forecastData = daily["data"]
nextDay = forecastData[0]

precipIntensity = nextDay["precipIntensity"]
precipIntensityMax = nextDay["precipIntensityMax"]
precipProbability = nextDay["precipProbability"]

precipType = 0

if 'precipType' in nextDay:
    precipType = nextDay["precipType"]
    if nextDay["precipType"] == "rain":
        precipType = 1
    elif nextDay["precipType"] == "snow":
        precipType = 2
    else:
        preciptype = 0
else:
    precipType = 0

temperatureHigh = nextDay["temperatureHigh"]
temperatureLow = nextDay["temperatureLow"]
dewPoint = nextDay["dewPoint"]
humidity = nextDay["humidity"]
pressure = nextDay["pressure"]
windSpeed = nextDay["windSpeed"]
windGust = nextDay["windGust"]
visibility = nextDay["visibility"]
pastClosure = 0

print(str(precipIntensity) + ',' + str(precipIntensityMax) + ',' + str(precipProbability) + ',' + str(precipType) + ',' + str(temperatureHigh) + ',' + str(temperatureLow) + ',' + str(dewPoint) + ',' + str(humidity) + ',' + str(pressure) + ',' + str(windSpeed) + ',' + str(windGust) + ',' + str(visibility) + ',' + str(pastClosure))

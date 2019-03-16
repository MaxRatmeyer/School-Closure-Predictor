import datetime
import csv

# Load machine learning libraries
import pandas
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier

#Http request libraries
import json
import urllib.request
import urllib.parse

# Load dataset
url = "https://storage.googleapis.com/school-closure-predictor/closuredata.csv"
names = [
    'precipIntensity', 'precipIntensityMax', 'precipProbability', 'precipType',
    'temperatureHigh', 'temperatureLow', 'dewPoint', 'humidity', 'pressure',
    'windSpeed', 'windGust', 'visibility', 'previouslyClosed', 'closed'
]
dataset = pandas.read_csv(url, names=names)

# Split-out validation dataset
array = dataset.values
X = array[:, 0:13]
Y = array[:, 13]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(
    X, Y, test_size=validation_size, random_state=seed)

# Make predictions on validation dataset
cart = DecisionTreeClassifier()
cart.fit(X_train, Y_train)

def weatherRefresh(self):
    precipIntensity = None
    precipIntensityMax = None
    precipProbability = None
    precipType = None
    temperatureHigh = None
    temperatureLow = None
    dewPoint = None
    humidity = None
    pressure = None
    windSpeed = None
    windGust = None
    visibility = None
    prediction = None
    probability = None
    willwillnot = None
    color = None
    pastClosure = None

    #Request weather information
    url = 'https://api.darksky.net/forecast/de9d9ce8612478d8482ea4cb5bfa6725/33.4348,-84.1435'
    urlRequest = urllib.request.urlopen(url)
    jsonData = json.loads(urlRequest.read().decode('utf-8'))

    daily = jsonData["daily"]
    forecastData = daily["data"]
    nextDay = forecastData[1]

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

    date = datetime.datetime.today().strftime('%Y-%m-%d')

    prediction = cart.predict([[
        precipIntensity, precipIntensityMax, precipProbability, precipType,
        temperatureHigh, temperatureLow, dewPoint, humidity, pressure,
        windSpeed, windGust, visibility, pastClosure
    ]])
    probability = cart.predict_proba([[
        precipIntensity, precipIntensityMax, precipProbability, precipType,
        temperatureHigh, temperatureLow, dewPoint, humidity, pressure,
        windSpeed, windGust, visibility, pastClosure
    ]])
    print(probability)

    willwillnot = ""

    if 'Yes' in prediction:
        prediction = "Closed"
        willwillnot = "will"
        color = "red"
    elif 'No' in prediction:
        prediction = "Open"
        willwillnot = "will not"
        color = "green"
    else:
        prediction = "Error"
        willwillnot = "error"
        color = "red"
    return(prediction + "," + willwillnot + "," + color);
from flask import Flask, Response, request
import json

from weather_util import *

app = Flask(__name__)


def getWeatherIntentHandler(location):
    location = "".join( location.split() )
    loc_dct = get_locdct(location)
    weather = loc_dct["weather"]
    temp = int(loc_dct["temp"] - 273.15)
    windspeed = float(loc_dct["wind"])
    if windspeed < 3:
        windstatus = 'mild wind'
    elif windspeed < 6:
        windstatus = 'moderate wind'
    else: windstatus = 'strong wind'
    return f"The weather of {location} is: {weather}, \n the temperature is {temp} degree Celcius, \n the wind speed is {windspeed}, which is consider {windstatus}"

@app.route("/", methods = ["POST"])
def main():

    req = request.get_json(silent=True, force=True)
    intent_name = req["queryResult"]["intent"]["displayName"]

    if intent_name == "AskWeather":
        loc = req["queryResult"]["parameters"]["location"]
        resp_text = getWeatherIntentHandler(loc)
    else:
        resp_text = "Unable to find a matching intent. Try again."

    resp = {
        "fulfillmentText": resp_text
    }

    return Response(json.dumps(resp), status=200, content_type="application/json")

app.run(host='0.0.0.0', port=5000, debug=True)

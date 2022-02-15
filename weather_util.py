from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

headers = {
	'Accepts': 'application/json',
#	'appid': 'bbe98b6b23dca44b2c88544fc55df73e',
}

session = Session()
session.headers.update(headers)
appid = 'bbe98b6b23dca44b2c88544fc55df73e'

def get_locdct(location):
	location = location.lower()
	url = 'https://api.openweathermap.org/data/2.5/weather'
	parameters = {
		'q': location,
		'appid':appid,
	}
	response = session.get(url, params = parameters)
	data = json.loads(response.text)
	locdct = {}

	locdct["weather"] = data["weather"][0]["main"]
	locdct["temp"] = data["main"]["temp"]
	locdct["wind"] = data["wind"]["speed"]
	return locdct

"""
Checking if it will rain in the next 12 hours at the given location (using the openweather API and the latitude and longitude parameters).
Sending a text message to the phone number provided as a reminder to bring an umbrella (using the Twilio API).
"""
#IMPORTS
import os
import requests
import json
from datetime import datetime
from twilio.rest import Client

#TWILIO API PARAMETERS
account_sid = 'ACc96f2e19587a4fc3c3717681bba7d92c'
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

#OPENWEATHER API PARAMETERS
owm_api_key = os.environ.get('OMW_API_KEY')
params = {
    'lat': 50.937531,
    'lon': 6.960279,
    'lang' : 'tr',
    'exclude' : ('current,minutely,daily,alerts,flags'),
    'timezone' : 'gmt3',
    'units' : 'metric',
}

api_endpoint = 'https://api.openweathermap.org/data/2.5/onecall'

response = requests.get(api_endpoint, params=params) #Send the request to openweather
response.raise_for_status() #Check if the request was successful
data = response.json() #Convert the response to a json object
first_12_hours = data['hourly'][:12] #Get the first 12 hours of the data 

it_will_rain = False 

#Check if it will rain in the next 12 hours
for data_point in first_12_hours:
    if data_point['weather'][0]['id'] < 700:
        it_will_rain = True

#Send a text message to the phone number provided
if it_will_rain:
    message  = client.messages \
                        .create(
                            body= 'Its going to 🌧 in the next 12 hours. Bring an 🌂!',
                            from_='+19125518501',
                            to='+905306688124',
                        )

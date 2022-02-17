import os
import requests
from datetime import datetime

APP_ID = os.environ.get('APP_ID')
API_KEY = os.environ.get('API_KEY')
GENDER = 'male'
WEIGHT = 74
HEIGHT = 176
AGE = 27

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
exercise_input = input('Which exercise did you complete?: ')
header = {'x-app-id': APP_ID, 'x-app-key': API_KEY, 'x-remote-user-id': '0'}
params = {
        'query': exercise_input,
        'gender':GENDER,
        'weight_kg':WEIGHT,
        'height_cm':HEIGHT,
        'age':AGE
        }

response = requests.post(exercise_endpoint, 
                        json=params,
                        headers=header)
results = response.json()

sheety_post_endpoint = 'https://api.sheety.co/2b489a48a3ecd79f3d73a53a182b410f/myWorkouts/workouts'
sheety_header = {'Authorization':'Bearer workout-token'} 
for exercise in results["exercises"]:
    sheety_params = {
            'workout':{
                        'date':datetime.now().strftime('%d-%b-%y'),
                        'time':datetime.now().strftime('%H:%M'),
                        'exercise':exercise['name'].title(),
                        'duration':exercise['duration_min'],
                        'calories':exercise['nf_calories'],
                        }
                    }

sheety_response = requests.post(sheety_post_endpoint, json=sheety_params, headers=sheety_header)

import requests
import os

SHEETY_ENDPOINT = os.environ.get(SHEETY_ENDPOINT)

class DataManager():

    def __init__(self):
        self.sheets_data = {}

    def sheety_get(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.sheets_data = data['prices']
        return self.sheets_data

    def update_destination_code(self):
        for city in self.sheets_data: #parse through the sheets_data
            #new_data will be passed to kiwi api in the request
            new_data = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }

            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)
            

import requests

SHEETY_ENDPOINT = 'https://api.sheety.co/2b489a48a3ecd79f3d73a53a182b410f/flightDeals/prices'

class DataManager():


    def __init__(self):
        self.sheets_data = {}

    def sheety_get(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        self.sheets_data = response.json()
        return self.sheets_data

    def update_destination_code(self):
        for city in self.sheets_data: #parse through the sheets_data
            #new_data will be passed to kiwi api in the request
            new_data = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }

            response = requests.get(url=f"{SHEETY_ENDPOINT}/city['id']", json=new_data)

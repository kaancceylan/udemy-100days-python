from data_manager import DataManager
import requests

datamanager = DataManager()

KIWI_API_KEY = '7eL1U5kXr6XpoYBZfn7Qygopm2g9H66q'
KIWI_ENDPOINT = 'tequila-api.kiwi.com/locations/query'
KIWI_PARAMS = {
    'apikey': KIWI_API_KEY, 'term':datamanager.sheety_get(),
}

class FlightSearch():


    def get_iata_code(self, city_name):
        query = {
            'term':'city_name', 'location_types':'city'
            }
        headers = {'apikey': KIWI_API_KEY}
        response = requests.get(url=KIWI_ENDPOINT, headers=headers, params=query)
        iata_code = response.json()['locations']
        return iata_code[0]['code']

import requests
from flight_data import FlightData

KIWI_API_KEY = '7eL1U5kXr6XpoYBZfn7Qygopm2g9H66q'
KIWI_ENDPOINT = 'https://tequila-api.kiwi.com'


class FlightSearch():

    def get_iata_code(self, city_name):
        query_endpoint = f'{KIWI_ENDPOINT}/locations/query'
        query = {'term':city_name, 'location_types':'city'}
        headers = {'apikey': KIWI_API_KEY}
        response = requests.get(url=query_endpoint, headers=headers, params=query)
        result = response.json()['locations']
        iata_code = result[0]['code']
        return iata_code

    def get_flight_deals(self, origin_code, destination_code, departure_date, return_date):
        search_endpoint = f'{KIWI_ENDPOINT}/v2/search'
        query = {
            'fly_from': origin_code,
            'fly_to': destination_code,
            'date_from': departure_date.strftime('%d/-%m/-%Y'),
            'date_to': return_date.strftime('%d/-%m/-%Y'),
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'flight_type': 'round',
            'one_for_city': 1,
            'max_stopovers': 0,
            'curr': 'GBP'
        }
        headers = {'apikey': KIWI_API_KEY}
        response = requests.get(url=search_endpoint, headers=headers, params=query)
        response.raise_for_status()
        
        #A try-except to catch the error in case there's no available flight found for the search
        try:
            print(response.json())
            results = response.json()['data'][0]
        except IndexError:
            print("No available flights found for the search")
            return None

        flightdata = FlightData(
            price = results['price'],
            origin_city = results['route'][0]['cityFrom'],
            origin_airport = results['route'][0]['flyFrom'],
            dest_city = results['route'][0]['cityTo'],
            dest_airport = results['route'][0]['flyTo'],
            to_date = results['route'][0]['local_departure'].split('T')[0],
            return_date = results['route'][1]['local_departure'].split('T')[0]
        )
        print(f"{flightdata.dest_city}: £{flightdata.price}")
        return flightdata

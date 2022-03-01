import requests
from flight_data import FlightData
from datetime import datetime, timedelta

KIWI_API_KEY = 'xns5e7gkErgl6GHBXiJVAmvrR8ulmnp_'
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
            "fly_from": origin_code,
            "fly_to": destination_code,
            "date_from": departure_date.strftime('%d/%m/%Y'),
            "date_to": return_date.strftime('%d/%m/%Y'),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": 'round',
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": 'GBP'
        }
        headers = {'apikey': KIWI_API_KEY}
        response = requests.get(
                                url=search_endpoint, 
                                headers=headers, 
                                params=query)
        response.raise_for_status()

        #A try-except to catch the error in case there's no available flight found for the search
        try:
            data = response.json()['data'][0]
        #If the num of stopovers is >0, catch the IndexError, update the max_stopovers in the query and send the request again.
        except IndexError:
            query['max_stopovers'] = 1
            response = requests.get(
                                    url=search_endpoint,
                                    headers=headers,
                                    params=query,
            )
            data = response.json()['data']
            flightdata = FlightData(
                price = data['price'][0],
                origin_city = data['route'][0]['cityFrom'],
                origin_airport = data['route'][0]['flyFrom'],
                dest_city = data['route'][1]['cityTo'],
                dest_airport = data['route'][1]['flyTo'],
                to_date = data['route'][0]['local_departure'].split('T')[0],
                return_date = data['route'][2]['local_departure'].split('T')[0],
                stop_overs = 1,
                via_city = data['route'][0]['cityTo']
            )
            return flightdata
        else:
            flightdata = FlightData(
                price = data['price'][0],
                origin_city = data['route'][0]['cityFrom'],
                origin_airport = data['route'][0]['flyFrom'],
                dest_city = data['route'][0]['cityTo'],
                dest_airport = data['route'][0]['flyTo'],
                to_date = data['route'][0]['local_departure'].split('T')[0],
                return_date = data['route'][1]['local_departure'].split('T')[0]
            )
        
        return flightdata
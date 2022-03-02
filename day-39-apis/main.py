#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager

flightsearch = FlightSearch()
datamanager = DataManager()
notificationmanager = NotificationManager()
sheety_data = datamanager.sheety_get()

#Construct link from the flight data
city_to = flightsearch.data['data'][0]['cityTo'].lower()
country_to = flightsearch.data['data'][0]['countryTo']['code'].lower()
city_from = flightsearch.data['data'][0]['cityFrom'].lower()
country_from = flightsearch.data['data'][0]['countryFrom']['code'].lower()
price = flightsearch.data['data'][0]['price']

#Can make it more dynamic later on, doesn't work when added return date restrictions etc.
deep_link = f'www.kiwi.com/deep?destination={city_to}_{country_to}&origin={city_from}_{country_from}&return=anytime'

#Check if the iatacode is empty in the sheets_data
if sheety_data[0]["iataCode"] == "":
    for row in sheety_data: #parse through the sheets_data
        row['iataCode'] = flightsearch.get_iata_code(row['city']) #Pass the city of each row to get_iata_code

    datamanager.sheets_data = sheety_data #Update the sheets_data in the datamanager with the sheety_data we got here
    datamanager.update_destination_code() #Update the destination_codes in the sheets_data


CITY_FROM_IATA = 'LON' #IATA code of the departure city
departure_date = datetime.now() + timedelta(days=1)
return_date = datetime.now() + timedelta(days=(6 * 30))

#Parse the cities in the google sheet and run the flight search for each of the IATA codes.
for destination in sheety_data:
    flights = flightsearch.get_flight_deals(
        origin_code = CITY_FROM_IATA,
        destination_code = destination['iataCode'],
        departure_date = departure_date,
        return_date = return_date,
    )
    if flights is None:
        continue

    if flights.price < destination['lowestPrice']:
        notificationmanager.send_notification(
            message = f"Low Flight Price Alert! ✈️ From {city_from} to {city_to} for only {price}€! See Flights: {deep_link}"
        )
        if flights.max_stopovers > 0:
            notificationmanager.send_notification.message += f"\nFlight has {flights.max_stopovers} stopovers"

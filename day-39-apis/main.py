#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch

flightsearch = FlightSearch()
datamanager = DataManager()
sheety_data = datamanager.sheety_get()

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
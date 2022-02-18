#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager

datamanager = DataManager()
sheety_data = datamanager.sheety_get()

#Check if the iatacode is empty in the sheets_data
if sheety_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheety_data: #parse through the sheets_data
        row['iataCode'] = flight_search.get_iata_code(row['city']) #Pass the city of each row to get_iata_code

    datamanager.sheets_data = sheety_data #Update the sheets_data in the datamanager with the sheety_data we got here
    datamanager.update_destination_code() #Update the destination_codes in the sheets_data

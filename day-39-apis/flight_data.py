class FlightData():

    def __init__(self, price, origin_city, origin_airport, 
                dest_city, dest_airport, to_date, return_date, max_stopovers=0, via_city=""):
            self.price = price
            self.origin_city = origin_city
            self.origin_airport = origin_airport
            self.dest_city = dest_city
            self.dest_airport = dest_airport
            self.to_date = to_date
            self.return_date = return_date
            self.max_stopovers = max_stopovers
            self.via_city = via_city
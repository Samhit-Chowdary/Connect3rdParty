from amadeus import Client, ResponseError

amadeus = Client(
    client_id='04RXDVkkotA8flHAyIc1goZIFzwdsiKG',
    client_secret='g1IQiYtd4mSC6Dte'
)


class FlightsService:
    def get_flight_offers(self, source, destination, date, count):
        try:
            response = amadeus.shopping.flight_offers_search.get(
                originLocationCode=source,
                destinationLocationCode=destination,
                departureDate=date,
                adults=count)
            return response.data
        except ResponseError as error:
            print(error)

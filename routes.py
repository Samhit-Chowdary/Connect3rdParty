from flask import Blueprint, request

from Amadeus.FlightsService.search import FlightsService
from ExchangeRates.rates import ExchangeRatesService

routes = Blueprint('routes', __name__)


@routes.get('/')
def samhit():
    return f"The server is up!!!!!"


@routes.get('/<name>')
def testing(name):
    return f"hello {name}"


@routes.post('/getRate')
def get_route():
    input = request.json
    service = ExchangeRatesService()
    return service.getRate(input['from_curr'], input['to_curr'], input['amount'])


@routes.post('/getFlights')
def get_flights():
    input = request.json
    service = FlightsService()
    print(input)
    return service.get_flight_offers(input['source'], input['destination'], input['date'], input['count'])

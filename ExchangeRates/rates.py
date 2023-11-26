import requests

import utils.url_modifiers


class ExchangeRatesService:
    def getRate(self, from_curr, to_curr, amount):
        base_url = "http://api.exchangeratesapi.io/v1/latest"
        query_params = {
            "access_key": "014c424888351b024c81c53d23d17fdc",
            "symbols": f"{from_curr},{to_curr}"
        }

        resp = requests.get(
            utils.url_modifiers.add_query_params_to_url(base_url, query_params),
        ).json()

        resp["base"] = from_curr
        resp["rate"] = resp["rates"][to_curr]/resp["rates"][from_curr]
        resp["amount"] = amount*resp["rate"]
        resp.pop("rates")
        return resp

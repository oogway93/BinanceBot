import requests
from typing import TypedDict, Any

from BinanceAPI_URLS import exchange_api
from config import API_KEY


def converter_currency(amount: float, from_cur: str, to_cur: str) -> TypedDict[str, Any]:
    api_url = f"{exchange_api}?have={from_cur}&want={to_cur}&amount={amount}"
    data = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    error = False
    if data.status_code == 200:
        return data.json(), error
    else:
        error = True
        return error

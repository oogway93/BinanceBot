import requests

from BinanceAPI import exchange_api
from config import API_KEY


def converter_currency(amount: float, from_cur: str, to_cur: str):
    api_url = f"{exchange_api}?have={from_cur}&want={to_cur}&amount={amount}"
    data = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    return data.json()

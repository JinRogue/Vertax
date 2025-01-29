import requests
from datetime import datetime

def fetch_historical_price(token_symbol, timestamp, price_api_url):
    """
    Retrieves historical token prices for accurate profit/loss calculations.

    Args:
        token_symbol (str): Symbol of the token (e.g., SOL).
        timestamp (int): Unix timestamp to get the price for.
        price_api_url (str): API endpoint for price data.

    Returns:
        float: Historical price of the token.
    """
    date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')
    url = f"{price_api_url}?symbol={token_symbol}&date={date}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data.get("price", 0.0)

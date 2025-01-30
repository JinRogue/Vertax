import requests

class CoinGeckoProvider:
    @staticmethod
    def fetch_price(token_symbol, date):
        """
        Fetches price data from CoinGecko.

        Args:
            token_symbol (str): The token symbol (e.g., SOL).
            date (str): Date in YYYY-MM-DD format.

        Returns:
            float: Price of the token.
        """
        url = f"https://api.coingecko.com/api/v3/coins/{token_symbol}/history?date={date}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data["market_data"]["current_price"]["usd"]

class CoinMarketCapProvider:
    @staticmethod
    def fetch_price(token_symbol, date):
        """
        Fetches price data from CoinMarketCap.

        Args:
            token_symbol (str): The token symbol (e.g., SOL).
            date (str): Date in YYYY-MM-DD format.

        Returns:
            float: Price of the token.
        """
        url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/historical?symbol={token_symbol}&date={date}"
        headers = {"X-CMC_PRO_API_KEY": "your_api_key"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data["data"]["quotes"][0]["quote"]["USD"]["price"]

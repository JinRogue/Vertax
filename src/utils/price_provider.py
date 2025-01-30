import requests
import logging

logging.basicConfig(level=logging.INFO)

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
        try:
            url = f"https://api.coingecko.com/api/v3/coins/{token_symbol}/history?date={date}"
            response = requests.get(url)
            response.raise_for_status()  
            data = response.json()

            if "market_data" not in data or "current_price" not in data["market_data"]:
                logging.warning(f"CoinGecko data missing expected fields for {token_symbol} on {date}.")
                return None

            price = data["market_data"]["current_price"]["usd"]
            logging.info(f"Successfully fetched price from CoinGecko for {token_symbol} on {date}: {price}")
            return price
        
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching price from CoinGecko for {token_symbol} on {date}: {e}")
            return None
        except Exception as e:
            logging.error(f"Unexpected error while fetching price from CoinGecko for {token_symbol} on {date}: {e}")
            return None

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
        try:
            url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/historical?symbol={token_symbol}&date={date}"
            headers = {"X-CMC_PRO_API_KEY": "your_api_key"}
            response = requests.get(url, headers=headers)
            response.raise_for_status() 
            data = response.json()

            if "data" not in data or "quotes" not in data["data"] or len(data["data"]["quotes"]) == 0:
                logging.warning(f"CoinMarketCap data missing expected fields for {token_symbol} on {date}.")
                return None

            price = data["data"]["quotes"][0]["quote"]["USD"]["price"]
            logging.info(f"Successfully fetched price from CoinMarketCap for {token_symbol} on {date}: {price}")
            return price
        
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching price from CoinMarketCap for {token_symbol} on {date}: {e}")
            return None
        except Exception as e:
            logging.error(f"Unexpected error while fetching price from CoinMarketCap for {token_symbol} on {date}: {e}")
            return None

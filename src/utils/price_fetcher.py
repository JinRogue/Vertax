from datetime import datetime
import logging
from src.utils.cache_manager import CacheManager
from src.utils.price_provider import CoinGeckoProvider, CoinMarketCapProvider

logging.basicConfig(level=logging.INFO)

cache_manager = CacheManager()

def fetch_historical_price(token_symbol, timestamp):
    """
    Retrieves historical token prices with caching and fallback providers.

    Args:
        token_symbol (str): The token symbol (e.g., SOL).
        timestamp (int): Unix timestamp to get the price for.

    Returns:
        float: Historical price of the token.
    """
    cached_price = cache_manager.get_cached_price(timestamp, token_symbol)
    if cached_price is not None:
        logging.info(f"Cache hit for {token_symbol} at {timestamp} => {cached_price}")
        return cached_price

    date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')

    try:
        price = CoinGeckoProvider.fetch_price(token_symbol, date)
        logging.info(f"Fetched price for {token_symbol} from CoinGecko: {price}")
    except Exception as e:
        logging.warning(f"CoinGecko failed for {token_symbol} on {date}: {e}. Trying CoinMarketCap.")
        
        try:
            price = CoinMarketCapProvider.fetch_price(token_symbol, date)
            logging.info(f"Fetched price for {token_symbol} from CoinMarketCap: {price}")
        except Exception as e:
            logging.error(f"CoinMarketCap also failed for {token_symbol} on {date}: {e}")
            raise

    try:
        cache_manager.store_price(timestamp, token_symbol, price)
        logging.info(f"Stored price for {token_symbol} at {timestamp} => {price}")
    except Exception as e:
        logging.error(f"Error storing price for {token_symbol} at {timestamp}: {e}")

    return price

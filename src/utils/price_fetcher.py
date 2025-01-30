from datetime import datetime
import logging
from src.utils.cache_manager import CacheManager
from src.utils.price_provider import CoinGeckoProvider, CoinMarketCapProvider

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
        return cached_price

    date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')

    try:
        price = CoinGeckoProvider.fetch_price(token_symbol, date)
    except Exception as e:
        logging.warning(f"CoinGecko failed: {e}, trying CoinMarketCap.")
        price = CoinMarketCapProvider.fetch_price(token_symbol, date)

    cache_manager.store_price(timestamp, token_symbol, price)
    return price
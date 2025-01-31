import logging
from collections import defaultdict

class CacheManager:
    """
    Handles caching of price data to reduce API calls.
    """
    def __init__(self):
        # Use defaultdict to simplify checking for missing data
        self.cache = defaultdict(dict)

    def get_cached_price(self, timestamp, token):
        """
        Retrieves cached price data if available.

        Args:
            timestamp (int): The Unix timestamp for the price.
            token (str): The token symbol.

        Returns:
            float or None: Cached price if found, None otherwise.
        """
        try:
            cached_price = self.cache[token].get(timestamp)
            if cached_price is not None:
                logging.info(f"Cache hit: {token} at {timestamp} => {cached_price}")
            else:
                logging.info(f"Cache miss: {token} at {timestamp}")
            return cached_price
        except KeyError as e:
            logging.error(f"Error retrieving cached price for token {token} at {timestamp}: {e}")
            return None

    def store_price(self, timestamp, token, price):
        """
        Stores price data in the cache.

        Args:
            timestamp (int): The Unix timestamp for the price.
            token (str): The token symbol.
            price (float): The price to cache.
        """
        try:
            self.cache[token][timestamp] = price
            logging.info(f"Stored price for {token} at {timestamp} => {price}")
        except Exception as e:
            logging.error(f"Error storing price for {token} at {timestamp}: {e}")

import logging
class CacheManager:
    """
    Handles caching of price data to reduce API calls.
    """
    def __init__(self):
        self.cache = {}

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
            cached_price = self.cache.get((timestamp, token))
            if cached_price is not None:
                logging.info(f"Cache hit: {token} at {timestamp} => {cached_price}")
            return cached_price
        except Exception as e:
            logging.error(f"Error retrieving cached price: {e}")
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
            self.cache[(timestamp, token)] = price
            logging.info(f"Stored price for {token} at {timestamp} => {price}")
        except Exception as e:
            logging.error(f"Error storing price in cache: {e}")

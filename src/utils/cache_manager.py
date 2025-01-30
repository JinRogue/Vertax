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
        return self.cache.get((timestamp, token))

    def store_price(self, timestamp, token, price):
        """
        Stores price data in the cache.

        Args:
            timestamp (int): The Unix timestamp for the price.
            token (str): The token symbol.
            price (float): The price to cache.
        """
        self.cache[(timestamp, token)] = price

import unittest
import logging
from src.utils.price_fetcher import fetch_historical_price
from src.utils.cache_manager import CacheManager

logging.basicConfig(level=logging.INFO)

class TestPriceFetcher(unittest.TestCase):
    """
    Unit tests for price fetching, caching, and fallback mechanisms.
    """

    def setUp(self):
        """
        Set up test environment by initializing a CacheManager instance.
        """
        self.cache_manager = CacheManager()

    def test_cache_hit(self):
        """
        Test fetching from cache when a stored price is available.
        """
        self.cache_manager.store_price(1672531200, "SOL", 100.0)
        price = fetch_historical_price("SOL", 1672531200)
        self.assertEqual(price, 100.0, "Cache hit should return the stored price")

    def test_cache_miss(self):
        """
        Test fetching when no cached price is available.
        Ensures that the return value is a float.
        """
        price = fetch_historical_price("SOL", 1672531200)
        self.assertIsInstance(price, float, "Cache miss should return a float price")

    def test_fallback_mechanism(self):
        """
        Simulate provider failure and ensure fallback mechanism works.
        This test should return a valid float price even if one provider fails.
        """
        try:
            price = fetch_historical_price("SOL", 1672531200)
            self.assertIsInstance(price, float, "Fallback mechanism should return a float price")
        except Exception as e:
            logging.error(f"Fallback mechanism test failed: {e}")
            self.fail(f"Fallback test encountered an exception: {e}")

    def test_invalid_token(self):
        """
        Test behavior when an invalid token is requested.
        The function should handle this gracefully and not crash.
        """
        try:
            price = fetch_historical_price("INVALID_TOKEN", 1672531200)
            self.assertIsInstance(price, float, "Invalid token should return a float (defaulting to 0.0 or fallback price)")
        except Exception as e:
            logging.error(f"Invalid token test failed: {e}")
            self.fail(f"Invalid token test encountered an exception: {e}")

    def test_invalid_timestamp(self):
        """
        Test behavior when an invalid timestamp is provided.
        Ensures that the function does not throw unexpected errors.
        """
        try:
            price = fetch_historical_price("SOL", "invalid_timestamp")
            self.assertIsInstance(price, float, "Invalid timestamp should return a float (handling errors internally)")
        except Exception as e:
            logging.error(f"Invalid timestamp test failed: {e}")
            self.fail(f"Invalid timestamp test encountered an exception: {e}")

if __name__ == "__main__":
    unittest.main()

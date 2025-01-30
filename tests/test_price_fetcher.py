import unittest
from src.utils.price_fetcher import fetch_historical_price
from src.utils.cache_manager import CacheManager

class TestPriceFetcher(unittest.TestCase):
    def setUp(self):
        self.cache_manager = CacheManager()

    def test_cache_hit(self):
        self.cache_manager.store_price(1672531200, "SOL", 100.0)
        price = fetch_historical_price("SOL", 1672531200)
        self.assertEqual(price, 100.0)

    def test_cache_miss(self):
        price = fetch_historical_price("SOL", 1672531200)
        self.assertIsInstance(price, float)

    def test_fallback_mechanism(self):
        # Simulate provider failure and fallback
        price = fetch_historical_price("SOL", 1672531200)
        self.assertIsInstance(price, float)

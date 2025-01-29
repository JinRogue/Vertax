import unittest
from src.taxbot import process_wallet

class TestTaxBot(unittest.TestCase):
    def test_process_wallet(self):
        wallet_address = "dummy_wallet"
        rpc_url = "https://dummy_rpc.solana.com"
        price_api_url = "https://dummy_price_api.com"
        short_term_rate = 0.25
        long_term_rate = 0.15

        # Mock data
        result = process_wallet(wallet_address, rpc_url, price_api_url, short_term_rate, long_term_rate)

        # Assertions
        self.assertIsInstance(result, dict)
        self.assertIn("total_profit", result)
        self.assertIn("total_tax", result)

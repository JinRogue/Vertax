import unittest
import logging
from src.taxbot import process_wallet

logging.basicConfig(level=logging.INFO)

class TestTaxBot(unittest.TestCase):
    """
    Unit tests for the process_wallet function in taxbot module.
    """

    def test_process_wallet_valid_data(self):
        """
        Test processing a wallet with valid data.
        Ensures correct structure and expected fields.
        """
        wallet_address = "dummy_wallet"
        rpc_url = "https://dummy_rpc.solana.com"
        price_api_url = "https://dummy_price_api.com"
        short_term_rate = 0.25
        long_term_rate = 0.15

        try:
            result = process_wallet(wallet_address, rpc_url, price_api_url, short_term_rate, long_term_rate)
            self.assertIsInstance(result, dict, "Result should be a dictionary")
            self.assertIn("total_profit", result, "Result should contain 'total_profit'")
            self.assertIn("total_tax", result, "Result should contain 'total_tax'")
        except Exception as e:
            logging.error(f"Valid data test failed: {e}")
            self.fail(f"Valid data test encountered an exception: {e}")

    def test_process_wallet_no_transactions(self):
        """
        Test processing a wallet with no transactions.
        Ensures it returns zero values gracefully.
        """
        wallet_address = "empty_wallet"
        rpc_url = "https://dummy_rpc.solana.com"
        price_api_url = "https://dummy_price_api.com"
        short_term_rate = 0.25
        long_term_rate = 0.15

        try:
            result = process_wallet(wallet_address, rpc_url, price_api_url, short_term_rate, long_term_rate)
            self.assertEqual(result["total_profit"], 0.0, "Total profit should be 0.0 for empty wallets")
            self.assertEqual(result["total_tax"], 0.0, "Total tax should be 0.0 for empty wallets")
        except Exception as e:
            logging.error(f"No transactions test failed: {e}")
            self.fail(f"No transactions test encountered an exception: {e}")

    def test_process_wallet_invalid_wallet(self):
        """
        Test processing a wallet with an invalid wallet address.
        Ensures proper error handling.
        """
        wallet_address = None  # Invalid wallet address
        rpc_url = "https://dummy_rpc.solana.com"
        price_api_url = "https://dummy_price_api.com"
        short_term_rate = 0.25
        long_term_rate = 0.15

        try:
            result = process_wallet(wallet_address, rpc_url, price_api_url, short_term_rate, long_term_rate)
            self.assertIsInstance(result, dict, "Even with an invalid wallet, the result should be a dictionary")
            self.assertEqual(result["total_profit"], 0.0, "Total profit should be 0.0 for invalid wallets")
            self.assertEqual(result["total_tax"], 0.0, "Total tax should be 0.0 for invalid wallets")
        except Exception as e:
            logging.error(f"Invalid wallet test failed: {e}")
            self.fail(f"Invalid wallet test encountered an exception: {e}")

    def test_process_wallet_unreachable_rpc(self):
        """
        Test processing a wallet when the RPC URL is unreachable.
        Ensures that connection failures are handled properly.
        """
        wallet_address = "dummy_wallet"
        rpc_url = "https://unreachable_rpc.solana.com"
        price_api_url = "https://dummy_price_api.com"
        short_term_rate = 0.25
        long_term_rate = 0.15

        try:
            result = process_wallet(wallet_address, rpc_url, price_api_url, short_term_rate, long_term_rate)
            self.assertIsInstance(result, dict, "Result should be a dictionary even if the RPC is unreachable")
        except Exception as e:
            logging.error(f"Unreachable RPC test failed: {e}")
            self.fail(f"Unreachable RPC test encountered an exception: {e}")

if __name__ == "__main__":
    unittest.main()

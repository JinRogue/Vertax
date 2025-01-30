import unittest
import logging
from src.solana import parse_transaction_data, connect_to_solana_rpc

logging.basicConfig(level=logging.INFO)

class TestSolana(unittest.TestCase):
    """
    Unit tests for Solana transaction parsing and RPC connectivity.
    """

    def test_parse_transaction_data(self):
        """
        Test parsing of raw Solana transaction data.
        Ensures correct structure and handling of expected fields.
        """
        raw_data = [
            {"signature": "abc123", "blockTime": 1650000000},
            {"signature": "def456", "blockTime": 1650003600}
        ]
        
        try:
            parsed_data = parse_transaction_data(raw_data)
            self.assertEqual(len(parsed_data), 2, "Parsed data length should match raw data length")
            self.assertIn("signature", parsed_data[0], "Each transaction should contain a signature")
            self.assertIn("purchase_time", parsed_data[0], "Each transaction should have a purchase_time")
        except Exception as e:
            logging.error(f"Transaction parsing test failed: {e}")
            self.fail(f"Transaction parsing test encountered an exception: {e}")

    def test_parse_transaction_data_missing_fields(self):
        """
        Test behavior when transaction data is missing critical fields.
        Ensures missing fields do not cause unexpected crashes.
        """
        raw_data = [
            {"blockTime": 1650000000},  # Missing signature
            {"signature": "def456"}  # Missing blockTime
        ]

        try:
            parsed_data = parse_transaction_data(raw_data)
            self.assertEqual(len(parsed_data), 2, "Parsed data should include all transactions even with missing fields")
            self.assertIsNone(parsed_data[0].get("signature"), "Missing signature should not crash parsing")
            self.assertIsNone(parsed_data[1].get("purchase_time"), "Missing purchase_time should not cause failure")
        except Exception as e:
            logging.error(f"Missing fields test failed: {e}")
            self.fail(f"Missing fields test encountered an exception: {e}")

    def test_connect_to_solana_rpc(self):
        """
        Test Solana RPC connectivity function.
        Ensures a failed connection returns False.
        """
        rpc_url = "https://dummy_rpc.solana.com"

        try:
            result = connect_to_solana_rpc(rpc_url)
            self.assertFalse(result, "Connection to an invalid RPC URL should return False")
        except Exception as e:
            logging.error(f"RPC connectivity test failed: {e}")
            self.fail(f"RPC connectivity test encountered an exception: {e}")

if __name__ == "__main__":
    unittest.main()

import unittest
from src.solana import parse_transaction_data, connect_to_solana_rpc

class TestSolana(unittest.TestCase):
    def test_parse_transaction_data(self):
        raw_data = [
            {"signature": "abc123", "blockTime": 1650000000},
            {"signature": "def456", "blockTime": 1650003600}
        ]
        parsed_data = parse_transaction_data(raw_data)

        self.assertEqual(len(parsed_data), 2)
        self.assertIn("signature", parsed_data[0])
        self.assertIn("purchase_time", parsed_data[0])

    def test_connect_to_solana_rpc(self):
        rpc_url = "https://dummy_rpc.solana.com"
        self.assertFalse(connect_to_solana_rpc(rpc_url))

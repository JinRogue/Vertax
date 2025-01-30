import unittest
from src.utils.transaction_parser import parse_solana_tx, handle_irregular_tx

class TestTransactionParser(unittest.TestCase):
    def test_parse_solana_tx(self):
        raw_tx = {
            "signature": "abc123",
            "instructions": ["instr1", "instr2"],
            "blockTime": 1650000000,
            "status": "success"
        }
        result = parse_solana_tx(raw_tx)
        self.assertEqual(result["signature"], "abc123")
        self.assertIn("instructions", result)

    def test_handle_irregular_tx(self):
        raw_tx = {
            "signature": "def456",
            "instructions": ["instr1", "instr2"],
            "blockTime": 1650003600,
            "partialFill": True
        }
        result = handle_irregular_tx(raw_tx)
        self.assertIn("instructions", result)
        self.assertEqual(result["signature"], "def456")


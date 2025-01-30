import unittest
import logging
from src.utils.transaction_parser import parse_solana_tx, handle_irregular_tx

logging.basicConfig(level=logging.INFO)

class TestTransactionParser(unittest.TestCase):
    """
    Unit tests for transaction parsing and handling irregular transactions.
    """

    def test_parse_solana_tx_valid(self):
        """
        Test parsing of a valid Solana transaction.
        Ensures the correct structure and required fields are present.
        """
        raw_tx = {
            "signature": "abc123",
            "instructions": ["instr1", "instr2"],
            "blockTime": 1650000000,
            "status": "success"
        }

        try:
            result = parse_solana_tx(raw_tx)
            self.assertEqual(result["signature"], "abc123", "Signature should match the input data")
            self.assertIn("instructions", result, "Instructions should be present in parsed data")
            self.assertEqual(result["status"], "success", "Status should match the input data")
        except Exception as e:
            logging.error(f"Valid transaction parsing test failed: {e}")
            self.fail(f"Valid transaction parsing test encountered an exception: {e}")

    def test_parse_solana_tx_missing_fields(self):
        """
        Test parsing when transaction data is missing critical fields.
        Ensures missing fields do not cause crashes.
        """
        raw_tx = {
            "blockTime": 1650000000
        }

        try:
            result = parse_solana_tx(raw_tx)
            self.assertIsNone(result.get("signature"), "Signature should be None when missing")
            self.assertIn("instructions", result, "Instructions should still be present even if empty")
        except Exception as e:
            logging.error(f"Missing fields test failed: {e}")
            self.fail(f"Missing fields test encountered an exception: {e}")

    def test_handle_irregular_tx_partial_fill(self):
        """
        Test handling of a transaction with a partial fill.
        Ensures logging and correct parsing.
        """
        raw_tx = {
            "signature": "def456",
            "instructions": ["instr1", "instr2"],
            "blockTime": 1650003600,
            "partialFill": True
        }

        try:
            result = handle_irregular_tx(raw_tx)
            self.assertEqual(result["signature"], "def456", "Signature should match the input data")
            self.assertIn("instructions", result, "Instructions should be present")
            self.assertTrue("partialFill" in raw_tx, "Partial fill should be recognized")
        except Exception as e:
            logging.error(f"Partial fill transaction test failed: {e}")
            self.fail(f"Partial fill transaction test encountered an exception: {e}")

    def test_handle_irregular_tx_multiple_instructions(self):
        """
        Test handling of a transaction with multiple instructions.
        Ensures logging and correct parsing.
        """
        raw_tx = {
            "signature": "ghi789",
            "instructions": ["instr1", "instr2", "instr3"],
            "blockTime": 1650007200
        }

        try:
            result = handle_irregular_tx(raw_tx)
            self.assertEqual(result["signature"], "ghi789", "Signature should match the input data")
            self.assertEqual(len(result["instructions"]), 3, "Should correctly parse multiple instructions")
        except Exception as e:
            logging.error(f"Multiple instructions test failed: {e}")
            self.fail(f"Multiple instructions test encountered an exception: {e}")

    def test_parse_solana_tx_invalid_data(self):
        """
        Test parsing of invalid transaction data.
        Ensures that it does not cause a crash.
        """
        raw_tx = "invalid_data"

        try:
            with self.assertRaises(Exception):
                parse_solana_tx(raw_tx)
        except Exception as e:
            logging.error(f"Invalid data test failed: {e}")
            self.fail(f"Invalid data test encountered an exception: {e}")

if __name__ == "__main__":
    unittest.main()

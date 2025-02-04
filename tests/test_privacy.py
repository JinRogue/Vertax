import unittest
from src.utils.privacy import sanitize_transaction_data, encrypt_sensitive_data

class TestPrivacyUtils(unittest.TestCase):
    def setUp(self):
        self.sample_transaction = {
            "signature": "abc123",
            "block_time": 1650000000,
            "status": "confirmed",
            "user_id": "user_456",
            "wallet_address": "some_wallet_address",
            "private_key": "super_secret_key",
            "api_key": "some_api_key"
        }
    
    def test_sanitize_transaction_data(self):
        sanitized_data = sanitize_transaction_data(self.sample_transaction)
        self.assertNotIn("user_id", sanitized_data)
        self.assertNotIn("wallet_address", sanitized_data)
        self.assertNotIn("private_key", sanitized_data)
        self.assertNotIn("api_key", sanitized_data)
        self.assertIn("signature", sanitized_data)
    
    def test_encrypt_sensitive_data(self):
        encrypted_data = encrypt_sensitive_data(self.sample_transaction)
        self.assertNotEqual(encrypted_data["wallet_address"], "some_wallet_address")
        self.assertNotEqual(encrypted_data["private_key"], "super_secret_key")
        self.assertIn("signature", encrypted_data)
        
if __name__ == "__main__":
    unittest.main()

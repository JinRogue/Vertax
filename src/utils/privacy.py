import logging
from cryptography.fernet import Fernet

# Generate a key for encryption (in production, store this securely)
ENCRYPTION_KEY = Fernet.generate_key()

class TransactionSecurity:
    SENSITIVE_FIELDS = {"user_id", "wallet_address", "private_key", "api_key"}
    ENCRYPTABLE_FIELDS = {"wallet_address", "private_key"}

    @staticmethod
    def sanitize_transaction_data(transaction: dict) -> dict:
        """
        Removes sensitive fields from the transaction data before processing.

        Args:
            transaction (dict): Raw transaction data.

        Returns:
            dict: Sanitized transaction data without sensitive fields.
        """
        sanitized = {k: v for k, v in transaction.items() if k not in TransactionSecurity.SENSITIVE_FIELDS}
        removed_fields = TransactionSecurity.SENSITIVE_FIELDS & transaction.keys()
        logging.info(f"Transaction data sanitized. Removed fields: {removed_fields}")
        return sanitized

    @staticmethod
    def encrypt_value(value: str, key: bytes) -> str:
        """
        Encrypts a given string using Fernet encryption.

        Args:
            value (str): The sensitive data to encrypt.
            key (bytes): Encryption key.

        Returns:
            str: Encrypted string.
        """
        try:
            if not isinstance(value, str):
                logging.warning(f"Skipping encryption for non-string value: {value}")
                return value  # Only encrypt string values

            cipher = Fernet(key)
            encrypted = cipher.encrypt(value.encode()).decode()
            logging.info(f"Value encrypted. Original length: {len(value)}, Encrypted length: {len(encrypted)}")
            return encrypted
        except Exception as e:
            logging.error(f"Encryption failed: {e}")
            return value  # Return original value if encryption fails

    @staticmethod
    def decrypt_value(value: str, key: bytes) -> str:
        """
        Decrypts an encrypted string using Fernet encryption.

        Args:
            value (str): The encrypted data to decrypt.
            key (bytes): Encryption key.

        Returns:
            str: Decrypted string.
        """
        try:
            cipher = Fernet(key)
            decrypted = cipher.decrypt(value.encode()).decode()
            logging.info(f"Value decrypted. Decrypted length: {len(decrypted)}")
            return decrypted
        except Exception as e:
            logging.error(f"Decryption failed: {e}")
            return value  # Return original value if decryption fails

    @staticmethod
    def encrypt_sensitive_data(transaction: dict, key: bytes = ENCRYPTION_KEY) -> dict:
        """
        Encrypts sensitive transaction fields for temporary storage if needed.

        Args:
            transaction (dict): Transaction data containing sensitive fields.
            key (bytes): Encryption key (default is ENCRYPTION_KEY).

        Returns:
            dict: Transaction data with encrypted sensitive fields.
        """
        encrypted_transaction = transaction.copy()

        for field in TransactionSecurity.ENCRYPTABLE_FIELDS:
            if field in encrypted_transaction:
                encrypted_transaction[field] = TransactionSecurity.encrypt_value(encrypted_transaction[field], key)

        logging.info(f"Sensitive data encrypted for fields: {TransactionSecurity.ENCRYPTABLE_FIELDS & transaction.keys()}")
        return encrypted_transaction

    @staticmethod
    def decrypt_sensitive_data(transaction: dict, key: bytes = ENCRYPTION_KEY) -> dict:
        """
        Decrypts sensitive transaction fields.

        Args:
            transaction (dict): Transaction data containing encrypted sensitive fields.
            key (bytes): Encryption key (default is ENCRYPTION_KEY).

        Returns:
            dict: Transaction data with decrypted sensitive fields.
        """
        decrypted_transaction = transaction.copy()

        for field in TransactionSecurity.ENCRYPTABLE_FIELDS:
            if field in decrypted_transaction:
                decrypted_transaction[field] = TransactionSecurity.decrypt_value(decrypted_transaction[field], key)

        logging.info(f"Sensitive data decrypted for fields: {TransactionSecurity.ENCRYPTABLE_FIELDS & transaction.keys()}")
        return decrypted_transaction

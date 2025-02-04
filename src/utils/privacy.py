import logging
from cryptography.fernet import Fernet

# Generate a key for encryption (in production, store this securely)
ENCRYPTION_KEY = Fernet.generate_key()
cipher = Fernet(ENCRYPTION_KEY)

def sanitize_transaction_data(transaction: dict) -> dict:
    """
    Removes sensitive fields from the transaction data before processing.
    
    Args:
        transaction (dict): Raw transaction data.
    
    Returns:
        dict: Sanitized transaction data without sensitive fields.
    """
    sensitive_fields = ["user_id", "wallet_address", "private_key", "api_key"]
    sanitized = {k: v for k, v in transaction.items() if k not in sensitive_fields}
    logging.info("Transaction data sanitized.")
    return sanitized

def encrypt_sensitive_data(transaction: dict) -> dict:
    """
    Encrypts sensitive transaction fields for temporary storage if needed.
    
    Args:
        transaction (dict): Transaction data containing sensitive fields.
    
    Returns:
        dict: Transaction data with encrypted sensitive fields.
    """
    encrypted_transaction = transaction.copy()
    sensitive_fields = ["wallet_address", "private_key"]
    
    for field in sensitive_fields:
        if field in encrypted_transaction:
            encrypted_value = cipher.encrypt(encrypted_transaction[field].encode()).decode()
            encrypted_transaction[field] = encrypted_value
    
    logging.info("Sensitive data encrypted.")
    return encrypted_transaction

import logging
from datetime import datetime
from src.utils.tax_rules import calculate_holding_period, apply_tax_rule

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

def parse_solana_tx(raw_tx_data, purchase_date):
    """
    Parses a single Solana transaction, normalizes its data,
    then applies tax rules based on the transaction's date.
    
    Args:
        raw_tx_data (dict): Raw transaction data from Solana.
        purchase_date (datetime): The date the asset was purchased.
    
    Returns:
        dict: Normalized transaction details with tax liability.
    """
    try:
        # Ensure the presence of expected keys
        signature = raw_tx_data.get("signature")
        instructions = raw_tx_data.get("instructions", [])
        block_time = raw_tx_data.get("blockTime")
        status = raw_tx_data.get("status", "unknown")

        if not signature:
            logging.warning("Transaction missing 'signature'.")
        
        if not instructions:
            logging.warning(f"Transaction {signature} has no instructions.")
        
        if not block_time:
            logging.warning(f"Transaction {signature} missing 'blockTime'.")
            return {}

        # Convert block_time to datetime for easier comparison
        transaction_date = datetime.utcfromtimestamp(block_time)

        # Calculate holding period (in days)
        holding_period = calculate_holding_period(purchase_date, transaction_date)

        # Assuming a fixed profit for now (this could be extended to fetch from transaction data)
        profit = raw_tx_data.get("profit", 0.0)  # Example, you may need to extract profit differently

        # Apply tax rule based on holding period
        short_term_rate = 0.20  # Example rate for short-term tax
        long_term_rate = 0.15   # Example rate for long-term tax
        tax_liability = apply_tax_rule(profit, holding_period, short_term_rate, long_term_rate)

        # Parse transaction data and add tax liability
        transaction = {
            "signature": signature,
            "instructions": instructions,
            "block_time": block_time,
            "status": status,
            "transaction_date": transaction_date,
            "holding_period": holding_period,
            "tax_liability": tax_liability
        }

        return transaction

    except Exception as e:
        logging.error(f"Error parsing transaction: {e}")
        return {}


def handle_irregular_tx(raw_tx_data):
    """
    Handles edge cases for complex Solana transactions, such as multi-instruction trades or partial fills.

    Args:
        raw_tx_data (dict): Raw transaction data from Solana.

    Returns:
        dict: Processed transaction details or fallback information.
    """
    try:
        # Check for special cases like partial fills or multiple instructions
        signature = raw_tx_data.get("signature", "unknown")
        
        if "partialFill" in raw_tx_data:
            logging.warning(f"Transaction {signature} has a partial fill.")
        
        instructions = raw_tx_data.get("instructions", [])
        if len(instructions) > 1:
            logging.warning(f"Transaction {signature} contains multiple instructions.")
        
        # After handling edge cases, normalize transaction data
        return parse_solana_tx(raw_tx_data)
    
    except Exception as e:
        logging.error(f"Error handling irregular transaction: {e}")
        raise


def parse_multi_instruction_tx(raw_tx_data):
    """
    Specialized parser for transactions with multiple instructions.

    Args:
        raw_tx_data (dict): Raw transaction data from Solana.

    Returns:
        dict: Normalized transaction data with multi-instruction processing.
    """
    try:
        signature = raw_tx_data.get("signature")
        instructions = raw_tx_data.get("instructions", [])
        
        # Handle cases where there are multiple instructions
        if len(instructions) > 1:
            logging.info(f"Transaction {signature} has multiple instructions.")
        
        # Normalize data
        return parse_solana_tx(raw_tx_data)

    except Exception as e:
        logging.error(f"Error parsing multi-instruction transaction: {e}")
        raise


def handle_partial_fill_tx(raw_tx_data):
    """
    Handles transactions that are partially filled.

    Args:
        raw_tx_data (dict): Raw transaction data from Solana.

    Returns:
        dict: Processed transaction details with partial fill handling.
    """
    try:
        signature = raw_tx_data.get("signature")
        
        if "partialFill" in raw_tx_data:
            logging.info(f"Transaction {signature} is a partial fill.")
        
        # Normalize data
        return parse_solana_tx(raw_tx_data)

    except Exception as e:
        logging.error(f"Error handling partial fill transaction: {e}")
        raise

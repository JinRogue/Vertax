import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

def parse_solana_tx(raw_tx_data):
    """
    Parses a single Solana transaction and normalizes its data.

    Args:
        raw_tx_data (dict): Raw transaction data from Solana.

    Returns:
        dict: Normalized transaction details.
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
            logging.warning(f"Transaction {signature} has no block time.")

        # Return parsed transaction data
        parsed_data = {
            "signature": signature,
            "instructions": instructions,
            "block_time": block_time,
            "status": status
        }

        return parsed_data

    except KeyError as e:
        logging.error(f"Missing expected key in transaction data: {e}")
        raise
    except Exception as e:
        logging.error(f"Error parsing transaction: {e}")
        raise


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
            logging.warning(f"Transaction {signature} has a partial fill.")
        
        # Normalize data
        return parse_solana_tx(raw_tx_data)

    except Exception as e:
        logging.error(f"Error handling partial fill transaction: {e}")
        raise

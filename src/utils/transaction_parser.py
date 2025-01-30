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
        if "signature" not in raw_tx_data:
            logging.warning("Transaction missing 'signature'.")
        
        parsed_data = {
            "signature": raw_tx_data.get("signature"),
            "instructions": raw_tx_data.get("instructions", []),
            "block_time": raw_tx_data.get("blockTime"),
            "status": raw_tx_data.get("status", "unknown")
        }

        if not parsed_data["instructions"]:
            logging.warning(f"Transaction {parsed_data['signature']} has no instructions.")
        
        if not parsed_data["block_time"]:
            logging.warning(f"Transaction {parsed_data['signature']} has no block time.")
        
        return parsed_data
    except KeyError as e:
        logging.error(f"Missing expected key in transaction data: {e}")
        raise
    except Exception as e:
        logging.error(f"Error parsing transaction: {e}")
        raise

def handle_irregular_tx(raw_tx_data):
    """
    Handles edge cases for complex Solana transactions.

    Args:
        raw_tx_data (dict): Raw transaction data from Solana.

    Returns:
        dict: Processed transaction details or fallback information.
    """
    try:
        if "partialFill" in raw_tx_data:
            logging.warning(f"Transaction {raw_tx_data.get('signature', 'unknown')} has a partial fill.")
        if len(raw_tx_data.get("instructions", [])) > 1:
            logging.warning(f"Transaction {raw_tx_data.get('signature', 'unknown')} contains multiple instructions.")
        
        return parse_solana_tx(raw_tx_data)
    
    except Exception as e:
        logging.error(f"Error handling irregular transaction: {e}")
        raise

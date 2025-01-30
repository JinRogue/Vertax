import logging

def parse_solana_tx(raw_tx_data):
    """
    Parses a single Solana transaction and normalizes its data.

    Args:
        raw_tx_data (dict): Raw transaction data from Solana.

    Returns:
        dict: Normalized transaction details.
    """
    try:
        parsed_data = {
            "signature": raw_tx_data.get("signature"),
            "instructions": raw_tx_data.get("instructions", []),
            "block_time": raw_tx_data.get("blockTime"),
            "status": raw_tx_data.get("status", "unknown")
        }
        return parsed_data
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
        # Example logic for detecting and handling irregular transactions
        if "partialFill" in raw_tx_data:
            logging.warning("Detected partial fill in transaction.")
        if len(raw_tx_data.get("instructions", [])) > 1:
            logging.warning("Detected multiple instructions in transaction.")

        return parse_solana_tx(raw_tx_data)
    except Exception as e:
        logging.error(f"Error handling irregular transaction: {e}")
        raise
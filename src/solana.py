import requests
import logging
from utils.transaction_parser import parse_solana_tx, handle_irregular_tx

logging.basicConfig(level=logging.INFO)

def connect_to_solana_rpc(rpc_url):
    """
    Connects to the Solana RPC endpoint to check connectivity.

    Args:
        rpc_url (str): Solana RPC endpoint URL.

    Returns:
        bool: True if connection is successful, False otherwise.
    """
    try:
        response = requests.get(rpc_url)
        response.raise_for_status()
        logging.info(f"Successfully connected to Solana RPC at {rpc_url}")
        return True
    except requests.RequestException as e:
        logging.error(f"Error connecting to Solana RPC at {rpc_url}: {e}")
        return False

def parse_transaction_data(raw_data):
    """
    Parses raw transaction data using the transaction parser module.

    Args:
        raw_data (list): Raw transaction data fetched from Solana.

    Returns:
        list: Parsed transaction data with necessary fields.
    """
    parsed_data = []
    for tx in raw_data:
        try:
            parsed_tx = handle_irregular_tx(tx)
            if parsed_tx:
                parsed_data.append(parsed_tx)
            else:
                logging.warning(f"Transaction {tx.get('signature', 'unknown')} could not be parsed.")
        except Exception as e:
            logging.error(f"Failed to parse transaction {tx.get('signature', 'unknown')}: {e}")
    return parsed_data

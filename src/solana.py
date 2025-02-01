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
    except requests.exceptions.RequestException as e:
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
        tx_signature = tx.get('signature', 'unknown')
        try:
            parsed_tx = parse_solana_tx(tx)
            if parsed_tx:
                parsed_data.append(parsed_tx)
            else:
                logging.warning(f"Transaction {tx_signature} could not be parsed due to irregularities.")
        except KeyError as e:
            logging.error(f"Missing expected data field in transaction {tx_signature}: {e}")
        except Exception as e:
            logging.error(f"Failed to parse transaction {tx_signature}: {e}")
    return parsed_data

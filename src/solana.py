# src/solana.py
import requests

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
        return True
    except requests.RequestException:
        return False

def parse_transaction_data(raw_data):
    """
    Parses raw transaction data into a standardized format.

    Args:
        raw_data (list): Raw transaction data fetched from Solana.

    Returns:
        list: Parsed transaction data with necessary fields.
    """
    parsed_data = []
    for tx in raw_data:
        parsed_data.append({
            "signature": tx.get("signature"),
            "purchase_time": tx.get("blockTime"),
            "sell_time": tx.get("blockTime") + 3600,  # Example: Sell time 1 hour later
            "token_symbol": "SOL",  # Example: Assume all transactions involve SOL
            "amount": 1.0  # Example: Assume 1 token traded per transaction
        })
    return parsed_data

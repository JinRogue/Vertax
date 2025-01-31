import requests
import logging
import json

def fetch_transactions(wallet_address, rpc_url):
    """
    Fetches raw transaction data from the Solana blockchain.

    Args:
        wallet_address (str): Solana wallet address to fetch transactions for.
        rpc_url (str): Solana RPC endpoint URL.

    Returns:
        list: Raw transaction data, empty list if no transactions are found or in case of error.
    """
    try:
        headers = {"Content-Type": "application/json"}
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getConfirmedSignaturesForAddress2",
            "params": [wallet_address, {"limit": 1000}]
        }
        logging.debug(f"Sending request to {rpc_url} for wallet {wallet_address}")
        
        response = requests.post(rpc_url, json=payload, headers=headers)
        response.raise_for_status()
        
        try:
            transactions = response.json().get("result", [])
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON response from RPC: {e}")
            return []
        
        if not transactions:
            logging.warning(f"No transactions found for wallet {wallet_address}.")
        else:
            logging.info(f"Found {len(transactions)} transactions for wallet {wallet_address}.")
        
        return transactions
    
    except requests.exceptions.RequestException as e:
        logging.error(f"Network error while fetching transactions for wallet {wallet_address}: {e}")
        return []
    except Exception as e:
        logging.error(f"Unexpected error while fetching transactions for wallet {wallet_address}: {e}")
        return []

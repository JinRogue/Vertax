import requests

def fetch_transactions(wallet_address, rpc_url):
    """
    Fetches raw transaction data from the Solana blockchain.

    Args:
        wallet_address (str): Solana wallet address to fetch transactions for.
        rpc_url (str): Solana RPC endpoint URL.

    Returns:
        list: Raw transaction data.
    """
    headers = {"Content-Type": "application/json"}
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getConfirmedSignaturesForAddress2",
        "params": [wallet_address, {"limit": 1000}]
    }
    response = requests.post(rpc_url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json().get("result", [])

from utils.data_fetcher import fetch_transactions
from utils.price_fetcher import fetch_historical_price
from utils.tax_rules import calculate_holding_period, apply_tax_rule
from datetime import datetime

def process_wallet(wallet_address, rpc_url, price_api_url, short_term_rate, long_term_rate):
    """
    Processes a wallet to fetch transactions, calculate profits, and summarize tax information.

    Args:
        wallet_address (str): Solana wallet address.
        rpc_url (str): Solana RPC endpoint URL.
        price_api_url (str): API endpoint for price data.
        short_term_rate (float): Tax rate for short-term holdings.
        long_term_rate (float): Tax rate for long-term holdings.

    Returns:
        dict: Tax summary including total profit and tax owed.
    """
    transactions = fetch_transactions(wallet_address, rpc_url)
    total_profit = 0
    total_tax = 0

    for tx in transactions:
        purchase_date = datetime.fromtimestamp(tx["purchase_time"])
        sell_date = datetime.fromtimestamp(tx["sell_time"])
        purchase_price = fetch_historical_price(tx["token_symbol"], tx["purchase_time"], price_api_url)
        sell_price = fetch_historical_price(tx["token_symbol"], tx["sell_time"], price_api_url)
        
        profit = (sell_price - purchase_price) * tx["amount"]
        holding_period = calculate_holding_period(purchase_date, sell_date)
        tax = apply_tax_rule(profit, holding_period, short_term_rate, long_term_rate)

        total_profit += profit
        total_tax += tax

    return {"total_profit": total_profit, "total_tax": total_tax}

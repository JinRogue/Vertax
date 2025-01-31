import logging
from utils.data_fetcher import fetch_transactions
from utils.price_fetcher import fetch_historical_price
from utils.tax_rules import calculate_holding_period, apply_tax_rule
from datetime import datetime

logging.basicConfig(level=logging.INFO)

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
    try:
        transactions = fetch_transactions(wallet_address, rpc_url)
        if not transactions:
            logging.warning(f"No transactions found for wallet {wallet_address}.")
            return {"total_profit": 0, "total_tax": 0}

        total_profit = 0
        total_tax = 0

        for tx in transactions:
            signature = tx.get('signature', 'unknown')
            token_symbol = tx.get('token_symbol', 'SOL')
            amount = tx.get('amount', 1.0)
            purchase_time = tx.get('purchase_time')
            sell_time = tx.get('sell_time')

            try:
                if not purchase_time or not sell_time:
                    logging.warning(f"Transaction {signature} missing purchase or sell timestamps.")
                    continue
                
                purchase_date = datetime.fromtimestamp(purchase_time)
                sell_date = datetime.fromtimestamp(sell_time)

                purchase_price = fetch_historical_price(token_symbol, purchase_time, price_api_url)
                sell_price = fetch_historical_price(token_symbol, sell_time, price_api_url)

                if purchase_price is None or sell_price is None:
                    logging.warning(f"Skipping transaction {signature} due to missing price data.")
                    continue

                profit = (sell_price - purchase_price) * amount
                holding_period = calculate_holding_period(purchase_date, sell_date)
                tax = apply_tax_rule(profit, holding_period, short_term_rate, long_term_rate)

                total_profit += profit
                total_tax += tax

            except Exception as e:
                logging.error(f"Error processing transaction {signature}: {e}")

        logging.info(f"Processed wallet {wallet_address} - Total Profit: {total_profit}, Total Tax: {total_tax}")
        return {"total_profit": total_profit, "total_tax": total_tax}

    except Exception as e:
        logging.error(f"Error processing wallet {wallet_address}: {e}")
        return {"total_profit": 0, "total_tax": 0}

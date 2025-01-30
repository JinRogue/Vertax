import logging
from src.taxbot import process_wallet

logging.basicConfig(level=logging.INFO)

def main():
    """
    Main function to process a wallet's transactions, calculate profits, and determine tax obligations.
    """
    wallet_address = "YourWalletAddressHere"
    rpc_url = "https://api.mainnet-beta.solana.com"
    price_api_url = "https://api.example.com/price"
    short_term_rate = 0.25
    long_term_rate = 0.15

    try:
        summary = process_wallet(wallet_address, rpc_url, price_api_url, short_term_rate, long_term_rate)
        
        if summary["total_profit"] == 0 and summary["total_tax"] == 0:
            logging.warning(f"No transactions processed for wallet {wallet_address}.")
        else:
            logging.info(f"Wallet processing completed: {wallet_address}")
        
        print("Tax Summary:")
        print(f"Total Profit: {summary['total_profit']}")
        print(f"Total Tax: {summary['total_tax']}")

    except Exception as e:
        logging.error(f"Unexpected error processing wallet {wallet_address}: {e}")

if __name__ == "__main__":
    main()

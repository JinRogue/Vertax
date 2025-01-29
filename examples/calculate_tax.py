from src.taxbot import process_wallet

def main():
    wallet_address = "YourWalletAddressHere"
    rpc_url = "https://api.mainnet-beta.solana.com"
    price_api_url = "https://api.example.com/price"
    short_term_rate = 0.25
    long_term_rate = 0.15

    summary = process_wallet(wallet_address, rpc_url, price_api_url, short_term_rate, long_term_rate)
    print("Tax Summary:")
    print(f"Total Profit: {summary['total_profit']}")
    print(f"Total Tax: {summary['total_tax']}")

if __name__ == "__main__":
    main()
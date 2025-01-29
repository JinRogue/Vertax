# **Vertax SDK API Reference**

## **Overview**

This document provides a comprehensive reference for the modules and functions available in the **Vertax SDK**. Each section details the purpose, parameters, and usage examples for key components, enabling developers to integrate and utilize the SDK efficiently.

---

## **Modules**

### **🔍 `utils/data_fetcher.py`**

#### **📄 `fetch_transactions(wallet_address, rpc_url)`**
Fetch raw transaction data from the Solana blockchain.

- **Parameters:**
  - `wallet_address` (str): The Solana wallet address to fetch transactions for.
  - `rpc_url` (str): URL of the Solana RPC endpoint.

- **Returns:**
  - `list`: A list of raw transaction data.

- **Example:**
  ```python
  from utils.data_fetcher import fetch_transactions

  transactions = fetch_transactions("YourWalletAddress", "https://api.mainnet-beta.solana.com")
  print(transactions)
  ```

---

### **💲 `utils/price_fetcher.py`**

#### **📉 `fetch_historical_price(token_symbol, timestamp, price_api_url)`**
Retrieve historical token prices for accurate calculations.

- **Parameters:**
  - `token_symbol` (str): The symbol of the token (e.g., `SOL`).
  - `timestamp` (int): The Unix timestamp for which to fetch the price.
  - `price_api_url` (str): URL of the price API endpoint.

- **Returns:**
  - `float`: The historical price of the token.

- **Example:**
  ```python
  from utils.price_fetcher import fetch_historical_price

  price = fetch_historical_price("SOL", 1672531200, "https://api.example.com/price")
  print(price)
  ```

---

### **📊 `utils/tax_rules.py`**

#### **📅 `calculate_holding_period(purchase_date, sell_date)`**
Calculate the holding period between two dates.

- **Parameters:**
  - `purchase_date` (datetime): The date the asset was purchased.
  - `sell_date` (datetime): The date the asset was sold.

- **Returns:**
  - `int`: The holding period in days.

- **Example:**
  ```python
  from utils.tax_rules import calculate_holding_period
  from datetime import datetime

  purchase_date = datetime(2023, 6, 1)
  sell_date = datetime(2024, 7, 1)
  holding_period = calculate_holding_period(purchase_date, sell_date)
  print(holding_period)
  ```

#### **💵 `apply_tax_rule(profit, holding_period, short_term_rate, long_term_rate)`**
Apply the appropriate tax rate based on the holding period.

- **Parameters:**
  - `profit` (float): The profit from the trade.
  - `holding_period` (int): The holding period in days.
  - `short_term_rate` (float): The tax rate for short-term holdings.
  - `long_term_rate` (float): The tax rate for long-term holdings.

- **Returns:**
  - `float`: The calculated tax amount.

- **Example:**
  ```python
  from utils.tax_rules import apply_tax_rule

  profit = 2000
  holding_period = 400
  short_term_rate = 0.30
  long_term_rate = 0.15
  tax = apply_tax_rule(profit, holding_period, short_term_rate, long_term_rate)
  print(tax)
  ```

---

### **🤖 `src/taxbot.py`**

#### **🧾 `process_wallet(wallet_address, rpc_url, price_api_url, short_term_rate, long_term_rate)`**
Process a wallet to calculate total profit and taxes owed.

- **Parameters:**
  - `wallet_address` (str): The Solana wallet address to process.
  - `rpc_url` (str): URL of the Solana RPC endpoint.
  - `price_api_url` (str): URL of the price API endpoint.
  - `short_term_rate` (float): The tax rate for short-term holdings.
  - `long_term_rate` (float): The tax rate for long-term holdings.

- **Returns:**
  - `dict`: A summary of total profit and tax owed.

- **Example:**
  ```python
  from src.taxbot import process_wallet

  summary = process_wallet(
      wallet_address="YourWalletAddress",
      rpc_url="https://api.mainnet-beta.solana.com",
      price_api_url="https://api.example.com/price",
      short_term_rate=0.25,
      long_term_rate=0.15,
  )
  print(summary)
  ```


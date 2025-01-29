# **Vertax SDK**

## **Overview**

The **Vertax SDK** is an open-source Python toolkit developed to facilitate efficient and local cryptocurrency tax computations. It allows developers to parse Solana blockchain transactions, calculate trading profits, and apply appropriate tax rules based on holding durations. This lightweight framework is designed for flexibility and privacy, empowering users to perform all computations locally.

---

## **Table of Contents**

1. [⚠️ General Notes](#️general-notes)
2. [✨ Key Features](#key-features)
3. [⚡ Quick Setup](#quick-setup)
4. [💻 Installation](#installation)
5. [📚 Usage Examples](#usage-examples)
6. [⚙️ Configuration](#️configuration)
7. [🤝 Contributing Guidelines](#contributing-guidelines)
8. [📄 License Information](#license-information)
9. [🔍 Why Vertax SDK?](#why-vertax-sdk)

---

## ⚠️ **General Notes**

- **📊 Accuracy**: Ensure your tax rates and blockchain data sources align with regional laws.
- **🔒 Data Security**: All computations are performed locally, safeguarding sensitive wallet and transaction data.

---

## ✨ **Key Features**

- **🔗 Transaction Parsing**:
  - Efficiently fetches and structures Solana transaction data.

- **💰 Tax Computation**:
  - Supports short-term and long-term capital gains calculations based on customizable tax rates.

- **📈 Price History Integration**:
  - Retrieves historical token prices for accurate profit and loss analysis.

- **🛠️ Modular Design**:
  - Suitable for standalone use or integration into larger projects.

---

## ⚡ **Quick Setup**

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/vertax-sdk.git
   cd vertax-sdk
   ```

2. **Set Up Python Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate.bat  # Windows
   ```

3. **Install Required Packages**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run an Example Script**

   ```bash
   python examples/calculate_tax.py
   ```

---

## 📚 **Usage Examples**

### **Fetching Transactions**

Fetch raw transaction data and process it for analysis:

```python
from utils.data_fetcher import fetch_transactions

transactions = fetch_transactions("YourWalletAddress", "https://api.mainnet-beta.solana.com")
print(transactions)
```

### **Calculating Taxes**

Determine taxes based on profits and holding periods:

```python
from utils.tax_rules import calculate_holding_period, apply_tax_rule
from datetime import datetime

profit = 2000  # Example profit
purchase_date = datetime(2023, 6, 1)
sell_date = datetime(2024, 7, 1)
holding_period = calculate_holding_period(purchase_date, sell_date)

short_term_rate = 0.30
long_term_rate = 0.15
tax = apply_tax_rule(profit, holding_period, short_term_rate, long_term_rate)
print(f"Tax Due: {tax}")
```

### **Processing Wallets**

Automatically compute tax summaries for a wallet:

```python
from src.taxbot import process_wallet

summary = process_wallet(
    wallet_address="YourWalletAddress",
    rpc_url="https://api.mainnet-beta.solana.com",
    price_api_url="https://api.example.com/prices",
    short_term_rate=0.25,
    long_term_rate=0.15,
)
print(summary)
```

---

## ⚙️ **Configuration**

Adjust settings in `config.py` or via environment variables:

- **🔗 RPC Endpoint**: Set the Solana RPC URL.
- **💹 API for Prices**: Define your historical price API URL.
- **💵 Tax Rates**: Modify short- and long-term rates according to your needs.

---

## 🤝 **Contributing Guidelines**

We welcome contributions! To get involved:

1. 🍴 Fork the repository.
2. 🌿 Create a feature branch: `git checkout -b feature/your-feature`.
3. 💻 Commit changes: `git commit -m "Add your feature"`.
4. 🚀 Push the branch: `git push origin feature/your-feature`.
5. 🔃 Submit a Pull Request for review.

---

## 📄 **License Information**

The Vertax SDK is licensed under the MIT License.

---

## 🔍 **Why Vertax SDK?**

The Vertax SDK provides a streamlined approach to managing cryptocurrency tax calculations with a focus on privacy and accuracy. Built for developers and individuals, it offers a robust and flexible framework to handle crypto taxation locally without relying on external services. With Vertax, tax compliance becomes efficient and secure.

---

## **API Reference**
Detailed API documentation is available [here](docs/API_REFERENCE.md).



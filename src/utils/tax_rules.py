from datetime import datetime

def calculate_holding_period(purchase_date, sell_date):
    """
    Calculates the holding period in days between purchase and sell dates.

    Args:
        purchase_date (datetime): Date the asset was purchased.
        sell_date (datetime): Date the asset was sold.

    Returns:
        int: Holding period in days.
    """
    return (sell_date - purchase_date).days

def apply_tax_rule(profit, holding_period, short_term_rate, long_term_rate):
    """
    Applies the appropriate tax rate based on holding period.

    Args:
        profit (float): Profit from the trade.
        holding_period (int): Holding period in days.
        short_term_rate (float): Tax rate for short-term holdings.
        long_term_rate (float): Tax rate for long-term holdings.

    Returns:
        float: Tax amount.
    """
    if holding_period < 365:
        return profit * short_term_rate
    else:
        return profit * long_term_rate
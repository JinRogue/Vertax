from datetime import datetime
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def calculate_holding_period(purchase_date, sell_date):
    """
    Calculates the holding period in days between purchase and sell dates.

    Args:
        purchase_date (datetime): Date the asset was purchased.
        sell_date (datetime): Date the asset was sold.

    Returns:
        int: Holding period in days.
    """
    try:
        if not isinstance(purchase_date, datetime) or not isinstance(sell_date, datetime):
            logging.error("Invalid date types. Both purchase_date and sell_date must be datetime objects.")
            raise ValueError("Invalid date types. Both purchase_date and sell_date must be datetime objects.")

        holding_period = (sell_date - purchase_date).days
        
        if holding_period < 0:
            logging.warning(f"Sell date {sell_date} is earlier than purchase date {purchase_date}. Holding period is negative.")
            raise ValueError("Sell date cannot be earlier than purchase date.")
        
        logging.info(f"Holding period calculated: {holding_period} days.")
        return holding_period

    except Exception as e:
        logging.error(f"Error calculating holding period: {e}")
        raise

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
    try:
        if not isinstance(profit, (int, float)):
            logging.error("Invalid profit type. Profit must be a number.")
            raise ValueError("Profit must be a number.")

        if not isinstance(holding_period, int):
            logging.error("Invalid holding_period type. Holding period must be an integer.")
            raise ValueError("Holding period must be an integer.")

        if holding_period < 365:
            tax = profit * short_term_rate
            logging.info(f"Short-term tax applied: {tax}")
        else:
            tax = profit * long_term_rate
            logging.info(f"Long-term tax applied: {tax}")
        
        return tax

    except Exception as e:
        logging.error(f"Error applying tax rule: {e}")
        raise

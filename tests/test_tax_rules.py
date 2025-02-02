import unittest
from datetime import datetime, timedelta
from src.tax_rules import calculate_holding_period, apply_tax_rule

class TestTaxRules(unittest.TestCase):

    def setUp(self):
        """Setup test data for tax calculations"""
        # Example purchase date
        self.purchase_date = datetime(2023, 1, 1)

        # Example profit
        self.profit = 1000.0

        # Tax rates
        self.short_term_rate = 0.15  # 15% tax rate for short-term holdings
        self.long_term_rate = 0.05   # 5% tax rate for long-term holdings

    def test_holding_period_short_term(self):
        """Test the holding period for short-term (less than 1 year)"""
        # Sell date within 6 months
        sell_date = self.purchase_date + timedelta(days=180)
        holding_period = calculate_holding_period(self.purchase_date, sell_date)
        self.assertEqual(holding_period, 180, "Holding period should be 180 days.")

        # Apply tax rules (short-term)
        tax = apply_tax_rule(self.profit, holding_period, self.short_term_rate, self.long_term_rate)
        expected_tax = self.profit * self.short_term_rate
        self.assertEqual(tax, expected_tax, "Tax should be calculated with short-term rate.")

    def test_holding_period_long_term(self):
        """Test the holding period for long-term (1 year or more)"""
        # Sell date after 1 year
        sell_date = self.purchase_date + timedelta(days=365)
        holding_period = calculate_holding_period(self.purchase_date, sell_date)
        self.assertEqual(holding_period, 365, "Holding period should be 365 days.")

        # Apply tax rules (long-term)
        tax = apply_tax_rule(self.profit, holding_period, self.short_term_rate, self.long_term_rate)
        expected_tax = self.profit * self.long_term_rate
        self.assertEqual(tax, expected_tax, "Tax should be calculated with long-term rate.")

    def test_holding_period_negative(self):
        """Test if holding period calculates negative values correctly"""
        # Sell date earlier than purchase date
        sell_date = self.purchase_date - timedelta(days=30)
        with self.assertRaises(ValueError):
            calculate_holding_period(self.purchase_date, sell_date)

    def test_tax_rule_invalid_profit_type(self):
        """Test if an invalid profit type raises an error"""
        # Use a string as profit instead of a float or int
        with self.assertRaises(ValueError):
            apply_tax_rule("invalid_profit", 180, self.short_term_rate, self.long_term_rate)

    def test_tax_rule_invalid_holding_period_type(self):
        """Test if an invalid holding period type raises an error"""
        # Use a string as holding period instead of an int
        with self.assertRaises(ValueError):
            apply_tax_rule(self.profit, "invalid_period", self.short_term_rate, self.long_term_rate)

    def test_tax_rule_edge_case(self):
        """Test edge case where holding period is exactly 365 days (boundary)"""
        # Sell date exactly 1 year later
        sell_date = self.purchase_date + timedelta(days=365)
        holding_period = calculate_holding_period(self.purchase_date, sell_date)
        self.assertEqual(holding_period, 365, "Holding period should be 365 days.")

        # Apply tax rules (long-term)
        tax = apply_tax_rule(self.profit, holding_period, self.short_term_rate, self.long_term_rate)
        expected_tax = self.profit * self.long_term_rate
        self.assertEqual(tax, expected_tax, "Tax should be calculated with long-term rate for boundary case.")

if __name__ == "__main__":
    unittest.main()

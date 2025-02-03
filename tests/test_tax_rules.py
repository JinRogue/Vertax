import unittest
from datetime import datetime, timedelta
from src.utils.tax_rules import calculate_holding_period, apply_tax_rule

class TestTaxRules(unittest.TestCase):
    """Test suite for tax calculation rules."""

    SHORT_TERM_RATE = 0.15  # 15% tax rate for short-term holdings
    LONG_TERM_RATE = 0.05   # 5% tax rate for long-term holdings

    def setUp(self):
        """Setup test data for tax calculations."""
        self.purchase_date = datetime(2023, 1, 1)  # Example purchase date
        self.profit = 1000.0  # Example profit

    def test_holding_period_short_term(self):
        """Test the holding period for short-term (less than 1 year)."""
        sell_date = self.purchase_date + timedelta(days=180)
        holding_period = calculate_holding_period(self.purchase_date, sell_date)
        self.assertEqual(holding_period, 180, "Holding period should be 180 days.")

        tax = apply_tax_rule(self.profit, holding_period, self.SHORT_TERM_RATE, self.LONG_TERM_RATE)
        expected_tax = self.profit * self.SHORT_TERM_RATE
        self.assertAlmostEqual(tax, expected_tax, msg="Tax should be calculated with short-term rate.")

    def test_holding_period_long_term(self):
        """Test the holding period for long-term (1 year or more)."""
        sell_date = self.purchase_date + timedelta(days=365)
        holding_period = calculate_holding_period(self.purchase_date, sell_date)
        self.assertEqual(holding_period, 365, "Holding period should be 365 days.")

        tax = apply_tax_rule(self.profit, holding_period, self.SHORT_TERM_RATE, self.LONG_TERM_RATE)
        expected_tax = self.profit * self.LONG_TERM_RATE
        self.assertAlmostEqual(tax, expected_tax, msg="Tax should be calculated with long-term rate.")

    def test_holding_period_negative(self):
        """Test if holding period calculates negative values correctly."""
        sell_date = self.purchase_date - timedelta(days=30)
        with self.assertRaises(ValueError) as context:
            calculate_holding_period(self.purchase_date, sell_date)
        self.assertEqual(str(context.exception), "Sell date cannot be earlier than purchase date.")

    def test_tax_rule_invalid_profit_type(self):
        """Test if an invalid profit type raises an error."""
        with self.assertRaises(ValueError) as context:
            apply_tax_rule("invalid_profit", 180, self.SHORT_TERM_RATE, self.LONG_TERM_RATE)
        self.assertEqual(str(context.exception), "Profit must be a numeric value.")

    def test_tax_rule_invalid_holding_period_type(self):
        """Test if an invalid holding period type raises an error."""
        with self.assertRaises(ValueError) as context:
            apply_tax_rule(self.profit, "invalid_period", self.SHORT_TERM_RATE, self.LONG_TERM_RATE)
        self.assertEqual(str(context.exception), "Holding period must be an integer.")

    def test_tax_rule_edge_case(self):
        """Test edge case where holding period is exactly 365 days (boundary)."""
        sell_date = self.purchase_date + timedelta(days=365)
        holding_period = calculate_holding_period(self.purchase_date, sell_date)
        self.assertEqual(holding_period, 365, "Holding period should be 365 days.")

        tax = apply_tax_rule(self.profit, holding_period, self.SHORT_TERM_RATE, self.LONG_TERM_RATE)
        expected_tax = self.profit * self.LONG_TERM_RATE
        self.assertAlmostEqual(tax, expected_tax, msg="Tax should be calculated with long-term rate for boundary case.")

if __name__ == "__main__":
    unittest.main()
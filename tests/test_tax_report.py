import unittest
from datetime import datetime
from src.utils.tax_report import generate_tax_report, save_report
from src.utils.tax_rules import calculate_tax_data

class TestTaxReport(unittest.TestCase):
    
    def setUp(self):
        """
        Set up some example transactions for testing.
        """
        self.transactions = [
            {
                'purchase_date': datetime(2023, 1, 10),
                'sell_date': datetime(2023, 8, 10),
                'profit': 5000
            },
            {
                'purchase_date': datetime(2022, 6, 15),
                'sell_date': datetime(2023, 6, 15),
                'profit': 2000
            }
        ]
        self.date_range = (datetime(2023, 1, 1), datetime(2023, 12, 31))
        self.tax_year = 2023
        
    def test_generate_tax_report(self):
        """
        Test generating a tax report with provided data.
        """
        # Calculate tax data (this will call calculate_tax_data function)
        tax_data = calculate_tax_data(self.transactions, date_range=self.date_range, tax_year=self.tax_year)
        
        # Generate the report string (this calls generate_tax_report function)
        report = generate_tax_report(self.transactions, date_range=self.date_range, tax_year=self.tax_year)
        
        # Assert that the report contains key data
        self.assertIn('Tax Report Summary for Year 2023', report)
        self.assertIn(f"Total Profits: {tax_data['total_profits']}", report)
        self.assertIn(f"Total Tax Liabilities: {tax_data['total_tax']}", report)
    
    def test_save_report_csv(self):
        """
        Test saving the tax report as a CSV file.
        """
        report = generate_tax_report(self.transactions, date_range=self.date_range, tax_year=self.tax_year)
        
        # Save the report as CSV
        save_report(report, file_type='csv', file_name='test_tax_report')
        
        # Check if the CSV file was created (this will check if the file exists in the current directory)
        try:
            with open('test_tax_report.csv', 'r', encoding='utf-8') as file:
                content = file.read()
                self.assertIn('Tax Report Summary', content)
                self.assertIn('Total Profits', content)
                self.assertIn('Total Tax Liabilities', content)
        except FileNotFoundError:
            self.fail("CSV file was not created.")

    def test_save_report_pdf(self):
        """
        Test saving the tax report as a PDF file.
        """
        report = generate_tax_report(self.transactions, date_range=self.date_range, tax_year=self.tax_year)
        
        # Save the report as PDF
        save_report(report, file_type='pdf', file_name='test_tax_report')
        
        # Check if the PDF file was created (this will check if the file exists in the current directory)
        try:
            with open('test_tax_report.pdf', 'rb') as file:
                content = file.read()
                self.assertGreater(len(content), 0)  # Check that the file is not empty
        except FileNotFoundError:
            self.fail("PDF file was not created.")
    
    def test_generate_tax_report_invalid(self):
        """
        Test generating a tax report with invalid data.
        """
        # Pass in invalid transaction data (e.g., missing profit)
        invalid_transactions = [
            {
                'purchase_date': datetime(2023, 1, 10),
                'sell_date': datetime(2023, 8, 10),
                'profit': None  # Invalid profit value
            }
        ]
        
        with self.assertRaises(ValueError):
            generate_tax_report(invalid_transactions)
    
    def test_calculate_tax_data_invalid(self):
        """
        Test calculating tax data with invalid transaction data.
        """
        invalid_transactions = [
            {
                'purchase_date': datetime(2023, 1, 10),
                'sell_date': datetime(2023, 8, 10),
                'profit': -1000  # Negative profit value
            }
        ]
        
        tax_data = calculate_tax_data(invalid_transactions)
        
        # Check that the tax data still gets calculated correctly even with invalid profits
        self.assertGreaterEqual(tax_data['total_profits'], 0)
        self.assertGreaterEqual(tax_data['total_tax'], 0)

if __name__ == "__main__":
    unittest.main()

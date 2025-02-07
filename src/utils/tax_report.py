import csv
from fpdf import FPDF
from src.utils.tax_rules import calculate_tax_data  # Assuming tax_rules.py has this function

def generate_tax_report(transactions: list, date_range: tuple = None, tax_year: int = None) -> str:
    """
    Generate a tax report based on the user's trading activity.
    Args:
        transactions (list): List of trading transaction data.
        date_range (tuple, optional): Tuple containing start and end date for filtering transactions (default is None).
        tax_year (int, optional): Year to consider for tax calculation (default is None).
    Returns:
        str: Generated report as a string (for CSV or PDF saving).
    """
    # Get tax data using some tax calculation logic (to be defined in tax_rules.py)
    tax_data = calculate_tax_data(transactions, date_range, tax_year)
    
    report_summary = f"Tax Report Summary for Year {tax_year}\n"
    report_summary += f"Date Range: {date_range[0]} to {date_range[1]}\n\n"
    
    # Adding the summary of profits and tax liabilities
    report_summary += f"Total Profits: {tax_data['total_profits']}\n"
    report_summary += f"Total Tax Liabilities: {tax_data['total_tax']}\n"
    
    # Further transaction breakdown or detailed sections can be added as needed
    return report_summary

def save_report(report_data: str, file_type: str = 'csv', file_name: str = 'tax_report') -> None:
    """
    Save the generated report in CSV or PDF format.
    Args:
        report_data (str): The generated report data to be saved.
        file_type (str): The format to save the report ('csv' or 'pdf').
        file_name (str): The name of the output file.
    """
    if file_type == 'csv':
        save_as_csv(report_data, file_name)
    elif file_type == 'pdf':
        save_as_pdf(report_data, file_name)
    else:
        raise ValueError("Invalid file type. Choose either 'csv' or 'pdf'.")

def save_as_csv(report_data: str, file_name: str) -> None:
    """
    Save the report as a CSV file.
    Args:
        report_data (str): The report data to be saved.
        file_name (str): The name of the CSV file.
    """
    with open(f"{file_name}.csv", mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Tax Report Summary'])
        writer.writerow([report_data])
    print(f"Report saved as {file_name}.csv")

def save_as_pdf(report_data: str, file_name: str) -> None:
    """
    Save the report as a PDF file.
    Args:
        report_data (str): The report data to be saved.
        file_name (str): The name of the PDF file.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(200, 10, txt="Tax Report", ln=True, align='C')
    pdf.ln(10)  # Line break
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, report_data)
    
    pdf.output(f"{file_name}.pdf")
    print(f"Report saved as {file_name}.pdf")

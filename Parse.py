import argparse

import pdfplumber
import re
import os
import json
from datetime import datetime

# French month abbreviations for date parsing
def french_month_to_number(month):
    months = {
        'jan': '01', 'fév': '02', 'mars': '03', 'avr.': '04', 'mai': '05', 'juin': '06',
        'juil': '07', 'août': '08', 'sep': '09', 'oct': '10', 'nov': '11', 'déc.': '12'
    }
    return months.get(month.lower(), '01')

def parse_french_date(date_str):
    # Example: '24 mai 25' -> '2025-05-24'
    parts = date_str.strip().split()
    if len(parts) == 3:
        day, month, year = parts
        month_num = french_month_to_number(month)
        year = '20' + year if len(year) == 2 else year
        return f"{year}-{month_num.zfill(2)}-{day.zfill(2)}"
    return None

def parse_ddmmyyyy(date_str):
    # Example: '28.09.2024' -> '2024-09-28'
    try:
        return datetime.strptime(date_str, '%d.%m.%Y').strftime('%Y-%m-%d')
    except Exception:
        return None

def compilePattern(input):
    return re.compile(input.replace(r" ", r"\s"), re.DOTALL | re.IGNORECASE)

def parse_solar_sheet(pdf_path):
    results = []
    subpattern = r".*?([\d.,']+) *kWh.*?x *([\d.,']+) *= *([\d.,']+) *([\d.,']+)([^\d]*(\d{2}\.\d{2}\.\d{4}) *au *(\d{2}\.\d{2}\.\d{4}))?"
    # Fallback: get header dates
    header_pattern = compilePattern(r"Index relevé Précédent.*(\d{2} +[\w\.]+ +\d{2}) +(\d{2} +[\w\.]+ +\d{2})")

    patterns = {
        "Energy": compilePattern(r"énergie" + subpattern),
        "Origin": compilePattern(r"garantie" + subpattern),
    }

    with pdfplumber.open(pdf_path) as pdf:
        for page  in pdf.pages:
            text = page.extract_text()
            if not text:
                continue
            text = text.replace('\uffff', ' ')
            # Find all matches for energy purchase
            for item, pattern in patterns.items():
                for match in pattern.finditer(text):
                    qty, price, chf, vta, _, date_from, date_to = [x.replace(',', '.').replace("'", "") if x else None for x in match.groups()]
                    # Try to find the date range above this match
                    if date_from and date_to:
                        date_from_iso = parse_ddmmyyyy(date_from)
                        date_to_iso = parse_ddmmyyyy(date_to)
                    else:
                        # Fallback: get header dates from the top of the page
                        header_match = header_pattern.search(text)
                        if header_match:
                            date_from_iso = parse_french_date(header_match.group(2))
                            date_to_iso = parse_french_date(header_match.group(1))
                        else:
                            date_from_iso = date_to_iso = None
                    results.append({
                        "file": pdf_path,
                        "item": item,
                        "date_from": date_from_iso,
                        "date_to": date_to_iso,
                        "Qty": float(qty),
                        "price": float(price),
                        "CHF": float(chf),
                        "TVA": float(vta)
                    })
    return results

def main():
    folder = r'C:\Users\Philippe\OneDrive - RL&Kids\Documents\Maisons\Suivi Solaire+Chauffage\Factures SIG' # os.path.dirname(os.path.abspath(__file__))
    files = [f for f in os.listdir(folder) if f.startswith('Production') and f.endswith('.pdf')]
    all_results = []
    for file in files:
        path = os.path.join(folder, file)
        all_results.extend(parse_solar_sheet(path))
    print(json.dumps(all_results, ensure_ascii=False, indent=2))
    with open(os.path.join(folder, f"production_{datetime.now().strftime('%Y-%m-%d')}.json"),'w') as fi:
        fi.write(json.dumps(all_results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

parser = argparse.ArgumentParser(description="Parse solar production sheets and invoices from Services Industriels Genève (SIG).")
parser.add_argument('pdf_path', type=str, help='Path to the PDF file to parse.')
parser.add_argument('--output', '-o', type=str, help='Path to the output file. Default is stdout.', default=None)
parser.add_argument('--output-format', '-f', type=str, default='json', help='Output format.')
parser.add_argument('--solar', '-s', action='store_true', help='Parse solar production sheets.')
parser.add_argument('--invoice', '-i', action='store_true', help='Parse invoices.')
parser.add_argument('--output-file-format', '-f', type=str, default='json', help='Output format.')
parser.add_argument('--solar-sheet-prefix', type=str, help='Root name of solar sheet files.', default='Production')
parser.add_argument('--invoice-sheet-prefix', type=str, help='Root name of invoice files.', default='Facture')

args = parser.parse_args()

import argparse
import json
import os
import re
from datetime import datetime

import pdfplumber


# French month abbreviations for date parsing
def french_month_to_number(month):
    months = {
        'jan' : '01', 'fév': '02', 'mars': '03', 'avr.': '04', 'mai': '05', 'juin': '06',
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
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue
            text = text.replace('\uffff', ' ')
            # Find all matches for energy purchase
            for item, pattern in patterns.items():
                for match in pattern.finditer(text):
                    qty, price, chf, vta, _, date_from, date_to = [x.replace(',', '.').replace("'", "") if x else None
                                                                   for x in match.groups()]
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
                        "file"     : pdf_path,
                        "item"     : item,
                        "date_from": date_from_iso,
                        "date_to"  : date_to_iso,
                        "Qty"      : float(qty),
                        "price"    : float(price),
                        "CHF"      : float(chf),
                        "TVA"      : float(vta)
                    })
    return results


def parse_invoice(pdf_path):
    results = []
    date_pattern = r"((?P<dfrom>\d{2}\.\d{2}\.\d{4}) *au *(?P<dto>\d{2}\.\d{2}\.\d{4}))?"
    power_price = r" *?(?P<qty>[\d.,']+) *(?P<uom>kWh).*?x *(?P<price>[\d.,']+) *= *(?P<chf>[\d.,']+) *(?P<tva>[\d.,']+)[^\d]*" + date_pattern
    water_price = r"[^\d]*?(?P<qty>[\d.,']+) *(?P<uom>jours|m3) (x +(?P<price>[\d.,']+))? *= *(?P<chf>[\d.,']+) *(?P<tva>[\d.,']+)[^\d]*"
    # Fallback: get header dates
    summary_date_pattern = compilePattern(
        r"période du (?P<dfrom>\d\d\.\d\d\.\d\d\d\d) +au +(?P<dto>\d\d\.\d\d\.\d\d\d\d)")
    header_date_pattern = compilePattern(
        r"Index +relevé +Précédent.*(?P<dfrom>\d{2} +[\w\.]+ +\d{2}) +(?P<dto>\d{2} +[\w\.]+ +\d{2})")

    patterns = [
        ("Power", "Peak"        , compilePattern(r"pleines" + power_price)),
        ("Power", "Offpeak"     , compilePattern(r"douces" + power_price)),
        ("Power", "Collectivity", compilePattern(r"collectivités +publiques +([?P<chf>\d.,']+) *(?P<tva>[\d.,'])[^\d]*"
                                       + date_pattern + r"[^\d]*([?P<price>\d.,']+) *%")),
        ("Power", "FederalTax", compilePattern(r"fédéral" + power_price)),
        ("Water", "FederalTax", compilePattern(r"fédérale" + water_price)),
    ]
    for label, category in  [
        ("Production et distribution Eau Potable", "Water"),
        ("Taxe d'épuration", "Cleansing"),
        ("Taxe d'utilisation", "WaterNet"),
    ]:
        patterns+=[
            ("Water", "Forfait_"    + category, compilePattern(".*"+ label + r".*?Forfait +de +la +tranche +" + water_price)),
            ("Water", "Forfait_m3_" + category, compilePattern(".*"+ label + r".*?Forfait.*?m3 +compris +dans +le +forfait +" + water_price)),
            ("Water", "m3"          + category, compilePattern(".*"+ label + r".*?Forfait.*?m3 +dépassant +le +forfait +" + water_price))
            ]

    xfloat = lambda x: float(x.replace(',', '.').replace("'", "")) if x else None

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue
            text = text.replace('\uffff', ' ')
            print(text)
            print('-' * 50)
            # Find all matches for energy purchase
            header_match = header_date_pattern.search(text)
            if header_match:
                header_date_from = parse_french_date(header_match.group(2))
                header_date_to = parse_french_date(header_match.group(1))
            else:
                header_date_from = header_date_to = None

            for commodity, item, pattern in patterns:
                for match in pattern.finditer(text):
                    group_dict = match.groupdict()
                    qty = group_dict.get('qty')
                    uom = group_dict.get('uom')
                    price = group_dict.get('price')
                    chf = group_dict.get('chf')
                    tva = group_dict.get('tva')
                    date_from = group_dict.get('dfrom')
                    date_to = group_dict.get('dto')
                    # Try to find the date range above this match
                    if date_from and date_to:
                        date_from_iso = parse_ddmmyyyy(date_from)
                        date_to_iso = parse_ddmmyyyy(date_to)
                    else:
                        # Fallback: get header dates from the top of the page
                        date_from_iso = header_date_from
                        date_to_iso = header_date_to
                    results.append({
                        "file"     : pdf_path,
                        "item"     : item,
                        "date_from": date_from_iso,
                        "date_to"  : date_to_iso,
                        "commodity": commodity,
                        "Qty"      : xfloat(qty),
                        "Uom"      : uom,
                        "price"    : xfloat(price),
                        "CHF"      : xfloat(chf),
                        "TVA"      : xfloat(tva)
                    })
    return results


def main(folder, filename, function, output, format):
    file_re = re.compile(f"^{filename.replace('*', '.*').replace('?', '.')}$", re.IGNORECASE)
    files = [f for f in os.listdir(folder) if file_re.match(f)]
    all_results = []
    for file in files:
        path = os.path.join(folder, file)
        all_results.extend(function(path))
    print(json.dumps(all_results, ensure_ascii=False, indent=2))
    if not all_results:
        print(f"No results found in {folder} for pattern {filename}")
        return
    if output:
        output = output.replace('{date}', datetime.now().strftime('%Y-%m-%d')).replace('{time}',
                                                                                       datetime.now().strftime(
                                                                                           '%H-%M-%S'))
        if format == 'json':
            if not output.endswith('.json'):
                output += '.json'
            with open(os.path.join(folder, output), 'w') as fi:
                fi.write(json.dumps(all_results, ensure_ascii=False, indent=2))
        else:
            raise ValueError(f"Unsupported output format: {format}")


# r'C:\Users\Philippe\OneDrive - RL&Kids\Documents\Maisons\Suivi Solaire+Chauffage\Factures SIG'

parser = argparse.ArgumentParser(
    description="Parse solar production sheets and invoices from Services Industriels Genève (SIG).")
parser.add_argument('--path', '-p', type=str, help='Path to the PDF file to parse.', required=True)
parser.add_argument('--output', '-o', type=str,
                    help='Path to the output file. Default is stdout. If the filename contains placeholders such as {date} and {time} then iso date and/or time are substituted.',
                    default=None)
parser.add_argument('--format', '-f', type=str, default='json', help='Output format.')
parser.add_argument('--solar', '-s', action='store_true', help='Parse solar production sheets.')
parser.add_argument('--invoice', '-i', action='store_true', help='Parse invoices.')
parser.add_argument('--solar-sheet-name', type=str, help='Name of solar sheet files. Can contain wildcards.',
                    default='Production*.pdf')
parser.add_argument('--invoice-sheet-name', type=str, help='Name of invoice files. Can contain wildcards.',
                    default='Facture*.pdf')

args = parser.parse_args()

print(json.dumps(args.__dict__, ensure_ascii=False, indent=2))
if args.solar:
    results = main(args.path, args.solar_sheet_name, parse_solar_sheet, args.output, args.format)
elif args.invoice:
    results = main(args.path, args.invoice_sheet_name, parse_invoice, args.output, args.format)

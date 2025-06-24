import argparse
import json
import os
import re
import sys
from datetime import datetime, timedelta

import pdfplumber

# French month abbreviations for date parsing
months = ['jan', 'fév', 'mars', 'avr.', 'mai', 'juin', 'juil', 'août', 'sep', 'oct', 'nov', 'déc.']


def french_month_to_number(month):
    try:
        return months.index(month.lower()) + 1
    except ValueError:
        return 1


def parse_french_date(date_str):
    # Example: '24 mai 25' -> '2025-05-24'
    parts = date_str.strip().split()
    if len(parts) == 3:
        day, month, year = parts
        month_num = french_month_to_number(month)
        year = '20' + year if len(year) == 2 else year
        return datetime(int(year), month_num, int(day))
    return None


def parse_ddmmyyyy(date_str):
    # Example: '28.09.2024' -> '2024-09-28'
    try:
        return datetime.strptime(date_str, '%d.%m.%Y')
    except Exception:
        return None


def parse_date(date_str):
    parsed = parse_french_date(date_str)
    return parsed if parsed else parse_ddmmyyyy(date_str)


def compilePattern(input):
    return re.compile(input.replace(r" ", r"\s"), re.IGNORECASE)


def _x_float(x):
    return float(x.replace(',', '.').replace("'", "")) if x else None


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
                        date_from_iso = parse_date(date_from)
                        date_to_iso = parse_date(date_to)
                    else:
                        # Fallback: get header dates from the top of the page
                        header_match = header_pattern.search(text)
                        if header_match:
                            date_from_iso = parse_date(header_match.group(2))
                            date_to_iso = parse_date(header_match.group(1))
                        else:
                            date_from_iso = date_to_iso = None
                    total_days = (date_to_iso - date_from_iso).days + 1
                    qty_day = _x_float(qty) / total_days
                    if date_from_iso.year < date_to_iso.year:
                        days_1 = (datetime(date_from_iso.year + 1, 1, 1) - date_from_iso).days
                        days_2 = (date_to_iso - datetime(date_from_iso.year, 1, 1)).days
                        new_results = [{
                            "file"     : pdf_path,
                            "item"     : item,
                            "date_from": date_from_iso.strftime('%Y-%m-%d'),
                            "date_to"  : datetime(date_from_iso.year + 1, 12, 31).strftime('%Y-%m-%d'),
                            "Qty"      : _x_float(qty),
                            "Qty_day"  : qty_day,
                            "price"    : _x_float(price),
                            "CHF"      : _x_float(chf),
                            "TVA"      : _x_float(vta)
                        },
                            {
                                "file"     : pdf_path,
                                "item"     : item,
                                "date_from": datetime(date_from_iso.year, 1, 1).strftime('%Y-%m-%d'),
                                "date_to"  : date_to_iso.strftime('%Y-%m-%d'),
                                "Qty"      : _x_float(qty),
                                "Qty_day"  : qty_day,
                                "price"    : _x_float(price),
                                "CHF"      : _x_float(chf),
                                "TVA"      : _x_float(vta)
                            }]
                    else:
                        new_results = [{
                            "file"     : pdf_path,
                            "item"     : item,
                            "date_from": date_from_iso.strftime('%Y-%m-%d'),
                            "date_to"  : date_to_iso.strftime('%Y-%m-%d'),
                            "Qty"      : _x_float(qty),
                            "Qty_day"  : qty_day,
                            "price"    : _x_float(price),
                            "CHF"      : _x_float(chf),
                            "TVA"      : _x_float(vta)
                        }]
                    print(['\n'.join(json.dumps(r) for r in new_results)])
                    results += new_results
    return results


def months_generator(date_from: datetime, date_to: datetime):
    y = date_from.year
    m = date_from.month
    d = date_from.day
    while date_from <= date_to:
        ny = y if m < 12 else y + 1
        nm = m + 1 if m < 12 else 1
        ed = datetime(ny, nm, 1) - timedelta(days=1)
        if ed > date_to:
            ed = date_to
        yield date_from, ed, (ed - date_from).days + 1
        date_from = datetime(ny, nm, 1)
        y = ny
        m = nm


def parse_invoice(pdf_path):
    results = []
    date_pattern = r"(\n.*(?P<dfrom>\d{2}\.\d{2}\.\d{4}) *au *(?P<dto>\d{2}\.\d{2}\.\d{4}))?"
    power_price = r" *?(?P<qty>[\d.,']+) *(?P<uom>kWh).*?x *(?P<price>[\d.,']+) *= *(?P<chf>[\d.,']+) +(?P<tva>[\d.,']+)?.*" + date_pattern
    water_price = r"[^\d]*?(?P<qty>[\d.,']+) *(?P<uom>jours|m3) (x +(?P<price>[\d.,']+))? *= *(?P<chf>[\d.,']+) *(?P<tva>[\d.,']+).*" + date_pattern
    water_price = r"(?P<qty>[\d.,']+) +(?P<uom>jours|m3) +(x +(?P<price>[\d.,']+))? *= *(?P<chf>[\d.,']+) *(?P<tva>[\d.,']+).*" + date_pattern
    # Fallback: get header dates
    summary_date_pattern = compilePattern(
        r"période +:? *du (?P<dfrom>\d\d\.\d\d\.\d\d\d\d) +au +(?P<dto>\d\d\.\d\d\.\d\d\d\d)")
    header_date_pattern = compilePattern(
        r"Index +relevé +Précédent.*(?P<dfrom>\d{2} +[\w\.]+ +\d{2}) +(?P<dto>\d{2} +[\w\.]+ +\d{2})")

    patterns = [
        ("Power", "Peak", compilePattern(r"pleines" + power_price)),
        ("Power", "Offpeak", compilePattern(r"douces" + power_price)),
        ("Power", "Collectivity",
         compilePattern(r"collectivités +publiques +(?P<chf>[\d.,']+) +(?P<tva>[\d.,'])?[^\d\n]*"
                        + date_pattern)),
        ("Power", "FederalTax", compilePattern(r"fédéral" + power_price)),
        ("Power", "FederalReserve", compilePattern(r"Confédération" + power_price)),
        ("Water", "FederalTax", compilePattern(r"fédérale" + water_price)),
    ]
    for label, category in [
        (r"(?P<label>Production +et +distribution +Eau +Potable.*)\n", "Water"),
        (r"(?P<label>Taxe +d'épuration.*)\n", "Cleansing"),
        (r"(?P<label>Taxe +d'utilisation.*)\n", "WaterNet"),
    ]:
        patterns += [
            ("Water", "Forfait_" + category,
             compilePattern(label + r" *Forfait +.*" + water_price)),
            ("Water", "Forfait_m3_" + category,
             compilePattern(label + r" *Forfait.*\n.*\n.*m3 +compris +dans +le +forfait +" + water_price)),
            ("Water", "Extra_m3_" + category,
             compilePattern(label + r" *Forfait.*\n.*\n.*\n.*m3 +dépassant +le +forfait +" + water_price))
        ]

    header_date_from = header_date_to = None
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
            summary_date_match = summary_date_pattern.search(text)
            header_dic = header_match.groupdict() if header_match \
                else summary_date_match.groupdict() if summary_date_match \
                else None
            if header_dic:
                header_date_from = parse_date(header_dic['dfrom'])
                header_date_to = parse_date(header_dic['dto'])

            for commodity, item, pattern in patterns:
                if item == 'Peak' and page.page_number == 2:
                    for test_pat in [water_price, pattern.pattern,
                                     r"pleines\s*?(?P<qty>[\d.,']+)\s*(?P<uom>kWh).*?x\s*(?P<price>[\d.,']+)\s*=\s*(?P<chf>[\d.,']+)\s*(?P<tva>[\d.,']+).*"
                                     r"(\n.*(?P<dfrom>\d{2}\.\d{2}\.\d{4})\s*au\s*(?P<dto>\d{2}\.\d{2}\.\d{4}))?",
                                     r"(?P<label>Production +et +distribution +Eau +Potable.*)\n",
                                     r"(?P<label>Production +et +distribution +Eau +Potable.*)\n\s*Forfait",
                                     r"(?P<label>Production +et +distribution +Eau +Potable.*)\n\s*Forfait.*\n.*\n(?P<next>.*)",
                                     r"(?P<label>Production +et +distribution +Eau +Potable.*)\n\s*Forfait.*\n.*\n.*\n(?P<nextnext>.*)",
                                     ]:
                        print('-' * 50)
                        print(test_pat)
                        print([{'match': m, 'dict': m.groupdict() if m else None}
                               for m in compilePattern(test_pat).finditer(text)])
                    print('*' * 50)
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
                        date_from_iso = parse_date(date_from)
                        date_to_iso = parse_date(date_to)
                    else:
                        # Fallback: get header dates from the top of the page
                        date_from_iso = header_date_from
                        date_to_iso = header_date_to
                    if not date_to_iso or not date_from_iso:
                        print('Dates not found', file=sys.stderr)
                    total_days = (date_to_iso - date_from_iso).days + 1
                    if qty is None and uom is None:
                        uom = 'CHF'
                        qty = chf

                    qty_day = _x_float(qty) / total_days if qty else None  # sometimes there's no quantity!
                    chf_day = _x_float(chf) / total_days if chf else None  # sometimes there's no quantity!

                    if not qty_day:
                        print('No qty!')
                    new_results = [{
                        "file"     : pdf_path,
                        "item"     : item,
                        "date_from": df.strftime('%Y-%m-%d'),
                        "date_to"  : dt.strftime('%Y-%m-%d'),
                        "commodity": commodity,
                        "Qty"      : qty_day * d,
                        "Days"     : d,
                        "Qty_day"  : qty_day,
                        "Uom"      : uom,
                        "price"    : _x_float(price),
                        "CHF"      : chf_day * d,
                        "TVA"      : _x_float(tva)
                    } for df, dt, d in months_generator(date_from_iso, date_to_iso)]
                    print(
                        f'# vvvvv {commodity}, {item}, {date_from_iso}, {date_to_iso}, {qty}, {uom}, {price} -> {chf}')
                    print('\n'.join(json.dumps(r) + ',' for r in new_results))
                    print(f'# ^^^^^^^^^^^^^^^^^^^^^^^^^')
                    results += new_results

    return results


def run(folder, filename, function, output, format):
    file_re = re.compile(f"^{filename.replace('*', '.*').replace('?', '.')}$", re.IGNORECASE)
    files = [f for f in os.listdir(folder) if file_re.match(f)]
    all_results = []
    for file in files:
        path = os.path.join(folder, file)
        try:
            all_results.extend(function(path))
        except Exception as ex:
            print(f"Exception while processing {path} : {ex}", file=sys.stderr)
            return []

    print(json.dumps(all_results, ensure_ascii=False, indent=2))
    if not all_results:
        print(f"No results found in {folder} for pattern {filename}")
        return []
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
    return output


def _parse_args(args):
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
        results = run(args.path, args.solar_sheet_name, parse_solar_sheet, args.output, args.format)
    elif args.invoice:
        results = run(args.path, args.invoice_sheet_name, parse_invoice, args.output, args.format)


if __name__ == '__main__':
    _parse_args(sys.argv)

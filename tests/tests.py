import json
import os
from datetime import datetime

import pytest
from pdfminer.utils import isnumber

import Parse
from Parse import parse_invoice


@pytest.mark.parametrize(
    "filename",
    (r"C:\Users\Philippe\Documents\Maisons\Suivi Solaire+Chauffage\Factures SIG\Facture 2025-02.pdf",
     r"C:\Users\Philippe\Documents\Maisons\Suivi Solaire+Chauffage\Factures SIG\Facture 2016-08.pdf",
     r"C:\Users\Philippe\Documents\Maisons\Suivi Solaire+Chauffage\Factures SIG\Facture 2024-12.pdf",

     )
)
def test_invoices(filename):
    results = parse_invoice(filename)
    assert [item for item in results if not (item.get('date_from') and item.get('date_to'))] == []
    assert [item for item in results if not item.get('Qty')] == []
    print(results)


def test_invoice_detailed(test_data):
    def compare(r, e):
        if isnumber(r) and isnumber(e):
            return 1 if abs(r - e) < 0.01 else 0
        return 1 if r == e else 0

    keys = ['item', 'date_from', 'date_to', 'commodity']
    values = ['Qty', 'Qty_day', 'Uom', 'price', 'CHF', 'TVA']
    results = parse_invoice(os.path.join('..', 'tests', 'data', test_data['file']))
    for expected in test_data['data']:
        for result in results:
            keys_match = [(k, expected.get(k), result.get(k)) for k in keys]
            if sum([1 for k, e, r in keys_match if e == r]) == len(keys):
                result['used'] = result.get('used', 0) + 1
                values_match = values_match = {k: {'e': e, 'r': r, 'c': compare(r, e)}
                                               for k, e, r in (
                                                   (k, expected.get(k), result.get(k))
                                                   for k in values)}

                if not sum([v['c'] for v in values_match.values()]) == len(values):
                    assert False, json.dumps(values_match)

    assert [r for r in results if not r.get('used')] == []  # all results used
    assert [r for r in results if r.get('used', 0) > 1]  # no  results used twice

    print(results)


@pytest.mark.parametrize('dfrom,dto,months',
                         [
                             ('2024-09-28', '2025-02-15', [
                                 ('2024-09-28', '2024-09-30', 3),
                                 ('2024-10-01', '2024-10-31', 31),
                                 ('2024-11-01', '2024-11-30', 30),
                                 ('2024-12-01', '2024-12-31', 31),
                                 ('2025-01-01', '2025-01-31', 31),
                                 ('2025-02-01', '2025-02-15', 15)
                             ]),
                             ('2024-10-01', '2025-02-15', [
                                 ('2024-10-01', '2024-10-31', 31),
                                 ('2024-11-01', '2024-11-30', 30),
                                 ('2024-12-01', '2024-12-31', 31),
                                 ('2025-01-01', '2025-01-31', 31),
                                 ('2025-02-01', '2025-02-15', 15)
                             ]),
                             ('2024-09-28', '2025-01-31', [
                                 ('2024-09-28', '2024-09-30', 3),
                                 ('2024-10-01', '2024-10-31', 31),
                                 ('2024-11-01', '2024-11-30', 30),
                                 ('2024-12-01', '2024-12-31', 31),
                                 ('2025-01-01', '2025-01-31', 31)
                             ]),
                             ('2024-09-28', '2024-09-28', [
                                 ('2024-09-28', '2024-09-28', 1)
                             ]),
                             ('2024-09-20', '2024-09-22', [
                                 ('2024-09-20', '2024-09-22', 3)
                             ])

                         ])
def tests_months_gen(dfrom, dto, months):
    dfrom = datetime.strptime(dfrom, '%Y-%m-%d')
    dto = datetime.strptime(dto, '%Y-%m-%d')
    months = [tuple((datetime.strptime(m, '%Y-%m-%d')) if isinstance(m, str) else m for m in t) for t in months]
    results = list(Parse.months_generator(dfrom, dto))
    assert results == months

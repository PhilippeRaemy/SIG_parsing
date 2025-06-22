import pytest
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
    print(results)
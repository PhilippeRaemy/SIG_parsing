import pytest


@pytest.fixture
def test_data():
    return {
        "file": "Facture 2025-02.pdf",
        "data": [
            {
                "item"     : "Forfait_Water",
                "date_from": "2024-12-07",
                "date_to"  : "2024-12-31",
                "commodity": "Water",
                "Qty"      : 25,
                "Qty_day"  : 1,
                "Uom"      : "jours",
                "price"    : 18.8344594594595,
                "CHF"      : 55.75,
                "TVA"      : 2.6
            },
            {
                "item"     : "Forfait_Water",
                "date_from": "2024-12-07",
                "date_to"  : "2024-12-31",
                "commodity": "Water",
                "Qty"      : 49,
                "Qty_day"  : 0.510204081632653,
                "Uom"      : "jours",
                "price"    : 36.9155405405405,
                "CHF"      : 55.75,
                "TVA"      : 2.6
            },
            {
                "item"     : "Forfait_m3_Water",
                "date_from": "2024-12-07",
                "date_to"  : "2024-12-31",
                "commodity": "Water",
                "Qty"      : 6.75675675675676,
                "Qty_day"  : 0.27027027027027,
                "Uom"      : "m3",
                "price"    : 0,
                "CHF"      : 0,
                "TVA"      : 2.6
            },
            {
                "item"     : "Forfait_m3_Water",
                "date_from": "2024-12-07",
                "date_to"  : "2024-12-31",
                "commodity": "Water",
                "Qty"      : 13.2432432432432,
                "Qty_day"  : 0.137892995035852,
                "Uom"      : "m3",
                "price"    : 0,
                "CHF"      : 0,
                "TVA"      : 2.6
            },
            {
                "item"     : "m3Water",
                "date_from": "2024-12-07",
                "date_to"  : "2024-12-31",
                "commodity": "Water",
                "Qty"      : 16.5540540540541,
                "Qty_day"  : 0.662162162162162,
                "Uom"      : "m3",
                "price"    : 38.4054054054054,
                "CHF"      : 113.68,
                "TVA"      : 2.6
            },
            {
                "item"     : "m3Water",
                "date_from": "2024-12-07",
                "date_to"  : "2024-12-31",
                "commodity": "Water",
                "Qty"      : 32.4459459459459,
                "Qty_day"  : 0.337837837837838,
                "Uom"      : "m3",
                "price"    : 75.2745945945946,
                "CHF"      : 113.68,
                "TVA"      : 2.6
            },
            {
                "item"     : "Forfait_Cleansing",
                "date_from": "2024-12-07",
                "date_to"  : "2024-12-31",
                "commodity": "Water",
                "Qty"      : 25,
                "Qty_day"  : 1,
                "Uom"      : "jours",
                "price"    : 17.8074324324324,
                "CHF"      : 52.71,
                "TVA"      : 8.1
            },
            {
                "item"     : "Forfait_Cleansing",
                "date_from": "2024-12-07",
                "date_to"  : "2024-12-31",
                "commodity": "Water",
                "Qty"      : 49,
                "Qty_day"  : 0.510204081632653,
                "Uom"      : "jours",
                "price"    : 34.9025675675676,
                "CHF"      : 52.71,
                "TVA"      : 8.1
            },
            {
                "item"     : "Forfait_m3_Cleansing",
                "date_from": "2024-12-07",
                "date_to"  : "2024-12-31",
                "commodity": "Water",
                "Qty"      : 6.75675675675676,
                "Qty_day"  : 0.27027027027027,
                "Uom"      : "m3",
                "price"    : 0,
                "CHF"      : 0,
                "TVA"      : 8.1
            },
            {
                "item"     : "Forfait_m3_Cleansing",
                "date_from": "2024-12-07",
                "date_to"  : "2024-12-31",
                "commodity": "Water",
                "Qty"      : 13.2432432432432,
                "Qty_day"  : 0.137892995035852,
                "Uom"      : "m3",
                "price"    : 0,
                "CHF"      : 0,
                "TVA"      : 8.1
            },
            {
                "item"     : "m3Cleansing",
                "date_from": "2024-12-07",
                "date_to"  : "2024-12-31",
                "commodity": "Water",
                "Qty"      : 16.5540540540541,
                "Qty_day"  : 0.662162162162162,
                "Uom"      : "m3",
                "price"    : 37.7432432432432,
                "CHF"      : 111.72,
                "TVA"      : 8.1
            },
            {
                "item"     : "m3Cleansing",
                "date_from": "2024-12-07",
                "date_to"  : "2024-12-31",
                "commodity": "Water",
                "Qty"      : 32.4459459459459,
                "Qty_day"  : 0.337837837837838,
                "Uom"      : "m3",
                "price"    : 73.9767567567568,
                "CHF"      : 111.72,
                "TVA"      : 8.1
            },
            {
                "item"     : "Forfait_WaterNet",
                "date_from": "2024-12-07",
                "date_to"  : "2024-12-31",
                "commodity": "Water",
                "Qty"      : 25,
                "Qty_day"  : 1,
                "Uom"      : "jours",
                "price"    : 3.01351351351351,
                "CHF"      : 8.92,
                "TVA"      : 8.1
            },
            {
                "item"     : "Forfait_WaterNet",
                "date_from": "2024-12-07",
                "date_to"  : "2024-12-31",
                "commodity": "Water",
                "Qty"      : 49,
                "Qty_day"  : 0.510204081632653,
                "Uom"      : "jours",
                "price"    : 5.90648648648649,
                "CHF"      : 8.92,
                "TVA"      : 8.1
            },
            {
                "item"     : "Forfait_m3_WaterNet",
                "date_from": "2024-12-07",
                "date_to"  : "2024-12-31",
                "commodity": "Water",
                "Qty"      : 6.75675675675676,
                "Qty_day"  : 0.27027027027027,
                "Uom"      : "m3",
                "price"    : 0,
                "CHF"      : 0,
                "TVA"      : 8.1
            },
            {
                "item"     : "Forfait_m3_WaterNet",
                "date_from": "2024-12-07",
                "date_to"  : "2024-12-31",
                "commodity": "Water",
                "Qty"      : 13.2432432432432,
                "Qty_day"  : 0.137892995035852,
                "Uom"      : "m3",
                "price"    : 0,
                "CHF"      : 0,
                "TVA"      : 8.1
            },
            {
                "item"     : "m3WaterNet",
                "date_from": "2024-12-07",
                "date_to"  : "2024-12-31",
                "commodity": "Water",
                "Qty"      : 16.5540540540541,
                "Qty_day"  : 0.662162162162162,
                "Uom"      : "m3",
                "price"    : 6.62162162162162,
                "CHF"      : 19.6,
                "TVA"      : 8.1
            },
            {
                "item"     : "m3WaterNet",
                "date_from": "2024-12-07",
                "date_to"  : "2024-12-31",
                "commodity": "Water",
                "Qty"      : 32.4459459459459,
                "Qty_day"  : 0.337837837837838,
                "Uom"      : "m3",
                "price"    : 12.9783783783784,
                "CHF"      : 19.6,
                "TVA"      : 8.1
            },
            {
                "item"     : "FederalTax",
                "date_from": "2024-12-07",
                "date_to"  : "2024-12-31",
                "commodity": "Water",
                "Qty"      : 15.5405405405405,
                "Qty_day"  : 0.621621621621622,
                "Uom"      : "m3",
                "price"    : 1.55405405405405,
                "CHF"      : 4.6,
                "TVA"      : 8.1
            },
            {
                "item"     : "FederalTax",
                "date_from": "2024-12-07",
                "date_to"  : "2024-12-31",
                "commodity": "Water",
                "Qty"      : 30.4594594594595,
                "Qty_day"  : 0.31715388858246,
                "Uom"      : "m3",
                "price"    : 3.04594594594595,
                "CHF"      : 4.6,
                "TVA"      : 8.1
            }
        ]
    }

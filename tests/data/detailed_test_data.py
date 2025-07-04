# @formatter:off
data = [
    {
        "file": "Facture 2025-02.pdf",
        "data": [
            # vvvvv Power, Peak, 2024-09-28 00:00:00, 2024-12-31 00:00:00, 1'743, kWh, 0.1530 -> 266.68
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Peak", "date_from": "2024-09-28", "date_to": "2024-09-30", "commodity": "Power", "Qty": 55.04210526315789, "Days": 3, "Qty_day": 18.347368421052632, "Uom": "kWh", "price": 0.153, "CHF": 8.421473684210525, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Peak", "date_from": "2024-10-01", "date_to": "2024-10-31", "commodity": "Power", "Qty": 568.7684210526317, "Days": 31, "Qty_day": 18.347368421052632, "Uom": "kWh", "price": 0.153, "CHF": 87.0218947368421, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Peak", "date_from": "2024-11-01", "date_to": "2024-11-30", "commodity": "Power", "Qty": 550.421052631579, "Days": 30, "Qty_day": 18.347368421052632, "Uom": "kWh", "price": 0.153, "CHF": 84.21473684210527, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Peak", "date_from": "2024-12-01", "date_to": "2024-12-31", "commodity": "Power", "Qty": 568.7684210526317, "Days": 31, "Qty_day": 18.347368421052632, "Uom": "kWh", "price": 0.153, "CHF": 87.0218947368421, "TVA": 8.1},
            # ^^^^^^^^^^^^^^^^^^^^^^^^^
            # vvvvv Power, Peak, 2025-01-01 00:00:00, 2025-02-18 00:00:00, 1'238, kWh, 0.1270 -> 157.23
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Peak", "date_from": "2025-01-01", "date_to": "2025-01-31", "commodity": "Power", "Qty": 783.2244897959183, "Days": 31, "Qty_day": 25.26530612244898, "Uom": "kWh", "price": 0.127, "CHF": 99.47204081632653, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Peak", "date_from": "2025-02-01", "date_to": "2025-02-18", "commodity": "Power", "Qty": 454.7755102040816, "Days": 18, "Qty_day": 25.26530612244898, "Uom": "kWh", "price": 0.127, "CHF": 57.757959183673464, "TVA": 8.1},
            # ^^^^^^^^^^^^^^^^^^^^^^^^^
            # vvvvv Power, Peak, 2024-09-28 00:00:00, 2024-12-31 00:00:00, 1'743, kWh, 0.1275 -> 222.23
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Peak", "date_from": "2024-09-28", "date_to": "2024-09-30", "commodity": "Power", "Qty": 55.04210526315789, "Days": 3, "Qty_day": 18.347368421052632, "Uom": "kWh", "price": 0.1275, "CHF": 7.017789473684211, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Peak", "date_from": "2024-10-01", "date_to": "2024-10-31", "commodity": "Power", "Qty": 568.7684210526317, "Days": 31, "Qty_day": 18.347368421052632, "Uom": "kWh", "price": 0.1275, "CHF": 72.51715789473684, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Peak", "date_from": "2024-11-01", "date_to": "2024-11-30", "commodity": "Power", "Qty": 550.421052631579, "Days": 30, "Qty_day": 18.347368421052632, "Uom": "kWh", "price": 0.1275, "CHF": 70.1778947368421, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Peak", "date_from": "2024-12-01", "date_to": "2024-12-31", "commodity": "Power", "Qty": 568.7684210526317, "Days": 31, "Qty_day": 18.347368421052632, "Uom": "kWh", "price": 0.1275, "CHF": 72.51715789473684, "TVA": 8.1},
            # ^^^^^^^^^^^^^^^^^^^^^^^^^
            # vvvvv Power, Peak, 2025-01-01 00:00:00, 2025-02-18 00:00:00, 1'238, kWh, 0.1260 -> 155.99
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Peak", "date_from": "2025-01-01", "date_to": "2025-01-31", "commodity": "Power", "Qty": 783.2244897959183, "Days": 31, "Qty_day": 25.26530612244898, "Uom": "kWh", "price": 0.126, "CHF": 98.68755102040818, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Peak", "date_from": "2025-02-01", "date_to": "2025-02-18", "commodity": "Power", "Qty": 454.7755102040816, "Days": 18, "Qty_day": 25.26530612244898, "Uom": "kWh", "price": 0.126, "CHF": 57.302448979591844, "TVA": 8.1},
            # ^^^^^^^^^^^^^^^^^^^^^^^^^
            # vvvvv Power, Offpeak, 2024-09-28 00:00:00, 2024-12-31 00:00:00, 2'388, kWh, 0.1040 -> 248.35
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Offpeak", "date_from": "2024-09-28", "date_to": "2024-09-30", "commodity": "Power", "Qty": 75.41052631578948, "Days": 3, "Qty_day": 25.13684210526316, "Uom": "kWh", "price": 0.104, "CHF": 7.842631578947369, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Offpeak", "date_from": "2024-10-01", "date_to": "2024-10-31", "commodity": "Power", "Qty": 779.2421052631579, "Days": 31, "Qty_day": 25.13684210526316, "Uom": "kWh", "price": 0.104, "CHF": 81.04052631578948, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Offpeak", "date_from": "2024-11-01", "date_to": "2024-11-30", "commodity": "Power", "Qty": 754.1052631578948, "Days": 30, "Qty_day": 25.13684210526316, "Uom": "kWh", "price": 0.104, "CHF": 78.42631578947369, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Offpeak", "date_from": "2024-12-01", "date_to": "2024-12-31", "commodity": "Power", "Qty": 779.2421052631579, "Days": 31, "Qty_day": 25.13684210526316, "Uom": "kWh", "price": 0.104, "CHF": 81.04052631578948, "TVA": 8.1},
            # ^^^^^^^^^^^^^^^^^^^^^^^^^
            # vvvvv Power, Offpeak, 2025-01-01 00:00:00, 2025-02-18 00:00:00, 1'704, kWh, 0.0870 -> 148.25
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Offpeak", "date_from": "2025-01-01", "date_to": "2025-01-31", "commodity": "Power", "Qty": 1078.0408163265306, "Days": 31, "Qty_day": 34.775510204081634, "Uom": "kWh", "price": 0.087, "CHF": 93.79081632653062, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Offpeak", "date_from": "2025-02-01", "date_to": "2025-02-18", "commodity": "Power", "Qty": 625.9591836734694, "Days": 18, "Qty_day": 34.775510204081634, "Uom": "kWh", "price": 0.087, "CHF": 54.45918367346939, "TVA": 8.1},
            # ^^^^^^^^^^^^^^^^^^^^^^^^^
            # vvvvv Power, Offpeak, 2024-09-28 00:00:00, 2024-12-31 00:00:00, 2'388, kWh, 0.0775 -> 185.07
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Offpeak", "date_from": "2024-09-28", "date_to": "2024-09-30", "commodity": "Power", "Qty": 75.41052631578948, "Days": 3, "Qty_day": 25.13684210526316, "Uom": "kWh", "price": 0.0775, "CHF": 5.844315789473684, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Offpeak", "date_from": "2024-10-01", "date_to": "2024-10-31", "commodity": "Power", "Qty": 779.2421052631579, "Days": 31, "Qty_day": 25.13684210526316, "Uom": "kWh", "price": 0.0775, "CHF": 60.391263157894734, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Offpeak", "date_from": "2024-11-01", "date_to": "2024-11-30", "commodity": "Power", "Qty": 754.1052631578948, "Days": 30, "Qty_day": 25.13684210526316, "Uom": "kWh", "price": 0.0775, "CHF": 58.443157894736835, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Offpeak", "date_from": "2024-12-01", "date_to": "2024-12-31", "commodity": "Power", "Qty": 779.2421052631579, "Days": 31, "Qty_day": 25.13684210526316, "Uom": "kWh", "price": 0.0775, "CHF": 60.391263157894734, "TVA": 8.1},
            # ^^^^^^^^^^^^^^^^^^^^^^^^^
            # vvvvv Power, Offpeak, 2025-01-01 00:00:00, 2025-02-18 00:00:00, 1'704, kWh, 0.0765 -> 130.36
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Offpeak", "date_from": "2025-01-01", "date_to": "2025-01-31", "commodity": "Power", "Qty": 1078.0408163265306, "Days": 31, "Qty_day": 34.775510204081634, "Uom": "kWh", "price": 0.0765, "CHF": 82.4726530612245, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Offpeak", "date_from": "2025-02-01", "date_to": "2025-02-18", "commodity": "Power", "Qty": 625.9591836734694, "Days": 18, "Qty_day": 34.775510204081634, "Uom": "kWh", "price": 0.0765, "CHF": 47.887346938775515, "TVA": 8.1},
            # ^^^^^^^^^^^^^^^^^^^^^^^^^
            # vvvvv Power, Collectivity, 2024-09-28 00:00:00, 2025-02-18 00:00:00, 91.56, CHF, None -> 91.56
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Collectivity", "date_from": "2024-09-28", "date_to": "2024-09-30", "commodity": "Power", "Qty": 1.9075000000000002, "Days": 3, "Qty_day": 0.6358333333333334, "Uom": "CHF", "price": None                  , "CHF": 1.9075000000000002, "TVA": 8.0},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Collectivity", "date_from": "2024-10-01", "date_to": "2024-10-31", "commodity": "Power", "Qty": 19.710833333333333, "Days": 31, "Qty_day": 0.6358333333333334, "Uom": "CHF", "price": None                  , "CHF": 19.710833333333333, "TVA": 8.0},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Collectivity", "date_from": "2024-11-01", "date_to": "2024-11-30", "commodity": "Power", "Qty": 19.075, "Days": 30, "Qty_day": 0.6358333333333334, "Uom": "CHF", "price": None                  , "CHF": 19.075, "TVA": 8.0},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Collectivity", "date_from": "2024-12-01", "date_to": "2024-12-31", "commodity": "Power", "Qty": 19.710833333333333, "Days": 31, "Qty_day": 0.6358333333333334, "Uom": "CHF", "price": None                  , "CHF": 19.710833333333333, "TVA": 8.0},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Collectivity", "date_from": "2025-01-01", "date_to": "2025-01-31", "commodity": "Power", "Qty": 19.710833333333333, "Days": 31, "Qty_day": 0.6358333333333334, "Uom": "CHF", "price": None                  , "CHF": 19.710833333333333, "TVA": 8.0},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Collectivity", "date_from": "2025-02-01", "date_to": "2025-02-18", "commodity": "Power", "Qty": 11.445, "Days": 18, "Qty_day": 0.6358333333333334, "Uom": "CHF", "price": None                  , "CHF": 11.445, "TVA": 8.0},
            # ^^^^^^^^^^^^^^^^^^^^^^^^^
            # vvvvv Power, FederalTax, 2024-09-28 00:00:00, 2025-02-18 00:00:00, 7'073, kWh, 0.0230 -> 162.68
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "FederalTax", "date_from": "2024-09-28", "date_to": "2024-09-30", "commodity": "Power", "Qty": 147.35416666666669, "Days": 3, "Qty_day": 49.11805555555556, "Uom": "kWh", "price": 0.023, "CHF": 3.389166666666667, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "FederalTax", "date_from": "2024-10-01", "date_to": "2024-10-31", "commodity": "Power", "Qty": 1522.6597222222222, "Days": 31, "Qty_day": 49.11805555555556, "Uom": "kWh", "price": 0.023, "CHF": 35.02138888888889, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "FederalTax", "date_from": "2024-11-01", "date_to": "2024-11-30", "commodity": "Power", "Qty": 1473.5416666666667, "Days": 30, "Qty_day": 49.11805555555556, "Uom": "kWh", "price": 0.023, "CHF": 33.891666666666666, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "FederalTax", "date_from": "2024-12-01", "date_to": "2024-12-31", "commodity": "Power", "Qty": 1522.6597222222222, "Days": 31, "Qty_day": 49.11805555555556, "Uom": "kWh", "price": 0.023, "CHF": 35.02138888888889, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "FederalTax", "date_from": "2025-01-01", "date_to": "2025-01-31", "commodity": "Power", "Qty": 1522.6597222222222, "Days": 31, "Qty_day": 49.11805555555556, "Uom": "kWh", "price": 0.023, "CHF": 35.02138888888889, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "FederalTax", "date_from": "2025-02-01", "date_to": "2025-02-18", "commodity": "Power", "Qty": 884.125, "Days": 18, "Qty_day": 49.11805555555556, "Uom": "kWh", "price": 0.023, "CHF": 20.335, "TVA": 8.1},
            # ^^^^^^^^^^^^^^^^^^^^^^^^^
            # vvvvv Power, FederalReserve, 2024-09-28 00:00:00, 2024-12-31 00:00:00, 4'131, kWh, 0.0120 -> 49.57
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "FederalReserve", "date_from": "2024-09-28", "date_to": "2024-09-30", "commodity": "Power", "Qty": 130.45263157894738, "Days": 3, "Qty_day": 43.48421052631579, "Uom": "kWh", "price": 0.012, "CHF": 1.5653684210526317, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "FederalReserve", "date_from": "2024-10-01", "date_to": "2024-10-31", "commodity": "Power", "Qty": 1348.0105263157895, "Days": 31, "Qty_day": 43.48421052631579, "Uom": "kWh", "price": 0.012, "CHF": 16.175473684210527, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "FederalReserve", "date_from": "2024-11-01", "date_to": "2024-11-30", "commodity": "Power", "Qty": 1304.5263157894738, "Days": 30, "Qty_day": 43.48421052631579, "Uom": "kWh", "price": 0.012, "CHF": 15.653684210526318, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "FederalReserve", "date_from": "2024-12-01", "date_to": "2024-12-31", "commodity": "Power", "Qty": 1348.0105263157895, "Days": 31, "Qty_day": 43.48421052631579, "Uom": "kWh", "price": 0.012, "CHF": 16.175473684210527, "TVA": 8.1},
            # ^^^^^^^^^^^^^^^^^^^^^^^^^
            # vvvvv Power, FederalReserve, 2025-01-01 00:00:00, 2025-02-18 00:00:00, 2'942, kWh, 0.0023 -> 6.77
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "FederalReserve", "date_from": "2025-01-01", "date_to": "2025-01-31", "commodity": "Power", "Qty": 1861.265306122449, "Days": 31, "Qty_day": 60.04081632653061, "Uom": "kWh", "price": 0.0023, "CHF": 4.283061224489796, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "FederalReserve", "date_from": "2025-02-01", "date_to": "2025-02-18", "commodity": "Power", "Qty": 1080.734693877551, "Days": 18, "Qty_day": 60.04081632653061, "Uom": "kWh", "price": 0.0023, "CHF": 2.486938775510204, "TVA": 8.1},
            # ^^^^^^^^^^^^^^^^^^^^^^^^^
            # vvvvv Water, Forfait_Water, 2024-12-07 00:00:00, 2025-02-18 00:00:00, 4, jours, 0.7534 -> 55.75
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Forfait_Water", "date_from": "2024-12-07", "date_to": "2024-12-31", "commodity": "Water", "Qty": 1.3513513513513513, "Days": 25, "Qty_day": 0.05405405405405406, "Uom": "jours", "price": 0.7534, "CHF": 18.83445945945946, "TVA": 2.6},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Forfait_Water", "date_from": "2025-01-01", "date_to": "2025-01-31", "commodity": "Water", "Qty": 1.6756756756756759, "Days": 31, "Qty_day": 0.05405405405405406, "Uom": "jours", "price": 0.7534, "CHF": 23.35472972972973, "TVA": 2.6},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Forfait_Water", "date_from": "2025-02-01", "date_to": "2025-02-18", "commodity": "Water", "Qty": 0.972972972972973, "Days": 18, "Qty_day": 0.05405405405405406, "Uom": "jours", "price": 0.7534, "CHF": 13.56081081081081, "TVA": 2.6},
            # ^^^^^^^^^^^^^^^^^^^^^^^^^
            # vvvvv Water, Forfait_m3_Water, 2024-12-07 00:00:00, 2025-02-18 00:00:00, 20, m3, None -> 0.00
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Forfait_m3_Water", "date_from": "2024-12-07", "date_to": "2024-12-31", "commodity": "Water", "Qty": 6.756756756756757, "Days": 25, "Qty_day": 0.2702702702702703, "Uom": "m3", "price": None, "CHF": 0.0, "TVA": 2.6},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Forfait_m3_Water", "date_from": "2025-01-01", "date_to": "2025-01-31", "commodity": "Water", "Qty": 8.378378378378379, "Days": 31, "Qty_day": 0.2702702702702703, "Uom": "m3", "price": None, "CHF": 0.0, "TVA": 2.6},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Forfait_m3_Water", "date_from": "2025-02-01", "date_to": "2025-02-18", "commodity": "Water", "Qty": 4.864864864864865, "Days": 18, "Qty_day": 0.2702702702702703, "Uom": "m3", "price": None, "CHF": 0.0, "TVA": 2.6},
            # ^^^^^^^^^^^^^^^^^^^^^^^^^
            # vvvvv Water, Extra_m3_Water, 2024-12-07 00:00:00, 2025-02-18 00:00:00, 49, m3, 2.3200 -> 113.68
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Extra_m3_Water", "date_from": "2024-12-07", "date_to": "2024-12-31", "commodity": "Water", "Qty": 16.554054054054053, "Days": 25, "Qty_day": 0.6621621621621622, "Uom": "m3", "price": 2.32, "CHF": 38.40540540540541, "TVA": 2.6},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Extra_m3_Water", "date_from": "2025-01-01", "date_to": "2025-01-31", "commodity": "Water", "Qty": 20.527027027027028, "Days": 31, "Qty_day": 0.6621621621621622, "Uom": "m3", "price": 2.32, "CHF": 47.6227027027027, "TVA": 2.6},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Extra_m3_Water", "date_from": "2025-02-01", "date_to": "2025-02-18", "commodity": "Water", "Qty": 11.91891891891892, "Days": 18, "Qty_day": 0.6621621621621622, "Uom": "m3", "price": 2.32, "CHF": 27.651891891891893, "TVA": 2.6},
            # ^^^^^^^^^^^^^^^^^^^^^^^^^
            # vvvvv Water, Forfait_Cleansing, 2024-12-07 00:00:00, 2025-02-18 00:00:00, 4, jours, 0.7123 -> 52.71
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Forfait_Cleansing", "date_from": "2024-12-07", "date_to": "2024-12-31", "commodity": "Water", "Qty": 1.3513513513513513, "Days": 25, "Qty_day": 0.05405405405405406, "Uom": "jours", "price": 0.7123, "CHF": 17.80743243243243, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Forfait_Cleansing", "date_from": "2025-01-01", "date_to": "2025-01-31", "commodity": "Water", "Qty": 1.6756756756756759, "Days": 31, "Qty_day": 0.05405405405405406, "Uom": "jours", "price": 0.7123, "CHF": 22.081216216216216, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Forfait_Cleansing", "date_from": "2025-02-01", "date_to": "2025-02-18", "commodity": "Water", "Qty": 0.972972972972973, "Days": 18, "Qty_day": 0.05405405405405406, "Uom": "jours", "price": 0.7123, "CHF": 12.821351351351352, "TVA": 8.1},
            # ^^^^^^^^^^^^^^^^^^^^^^^^^
            # vvvvv Water, Forfait_m3_Cleansing, 2024-12-07 00:00:00, 2025-02-18 00:00:00, 20, m3, None -> 0.00
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Forfait_m3_Cleansing", "date_from": "2024-12-07", "date_to": "2024-12-31", "commodity": "Water", "Qty": 6.756756756756757, "Days": 25, "Qty_day": 0.2702702702702703, "Uom": "m3", "price": None, "CHF": 0.0, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Forfait_m3_Cleansing", "date_from": "2025-01-01", "date_to": "2025-01-31", "commodity": "Water", "Qty": 8.378378378378379, "Days": 31, "Qty_day": 0.2702702702702703, "Uom": "m3", "price": None, "CHF": 0.0, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Forfait_m3_Cleansing", "date_from": "2025-02-01", "date_to": "2025-02-18", "commodity": "Water", "Qty": 4.864864864864865, "Days": 18, "Qty_day": 0.2702702702702703, "Uom": "m3", "price": None, "CHF": 0.0, "TVA": 8.1},
            # ^^^^^^^^^^^^^^^^^^^^^^^^^
            # vvvvv Water, Extra_m3_Cleansing, 2024-12-07 00:00:00, 2025-02-18 00:00:00, 49, m3, 2.2800 -> 111.72
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Extra_m3_Cleansing", "date_from": "2024-12-07", "date_to": "2024-12-31", "commodity": "Water", "Qty": 16.554054054054053, "Days": 25, "Qty_day": 0.6621621621621622, "Uom": "m3", "price": 2.28, "CHF": 37.74324324324324, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Extra_m3_Cleansing", "date_from": "2025-01-01", "date_to": "2025-01-31", "commodity": "Water", "Qty": 20.527027027027028, "Days": 31, "Qty_day": 0.6621621621621622, "Uom": "m3", "price": 2.28, "CHF": 46.80162162162162, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Extra_m3_Cleansing", "date_from": "2025-02-01", "date_to": "2025-02-18", "commodity": "Water", "Qty": 11.91891891891892, "Days": 18, "Qty_day": 0.6621621621621622, "Uom": "m3", "price": 2.28, "CHF": 27.175135135135132, "TVA": 8.1},
            # ^^^^^^^^^^^^^^^^^^^^^^^^^
            # vvvvv Water, Forfait_WaterNet, 2024-12-07 00:00:00, 2025-02-18 00:00:00, 4, jours, 0.1205 -> 8.92
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Forfait_WaterNet", "date_from": "2024-12-07", "date_to": "2024-12-31", "commodity": "Water", "Qty": 1.3513513513513513, "Days": 25, "Qty_day": 0.05405405405405406, "Uom": "jours", "price": 0.1205, "CHF": 3.0135135135135136, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Forfait_WaterNet", "date_from": "2025-01-01", "date_to": "2025-01-31", "commodity": "Water", "Qty": 1.6756756756756759, "Days": 31, "Qty_day": 0.05405405405405406, "Uom": "jours", "price": 0.1205, "CHF": 3.736756756756757, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Forfait_WaterNet", "date_from": "2025-02-01", "date_to": "2025-02-18", "commodity": "Water", "Qty": 0.972972972972973, "Days": 18, "Qty_day": 0.05405405405405406, "Uom": "jours", "price": 0.1205, "CHF": 2.1697297297297298, "TVA": 8.1},
            # ^^^^^^^^^^^^^^^^^^^^^^^^^
            # vvvvv Water, Forfait_m3_WaterNet, 2024-12-07 00:00:00, 2025-02-18 00:00:00, 20, m3, None -> 0.00
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Forfait_m3_WaterNet", "date_from": "2024-12-07", "date_to": "2024-12-31", "commodity": "Water", "Qty": 6.756756756756757, "Days": 25, "Qty_day": 0.2702702702702703, "Uom": "m3", "price": None, "CHF": 0.0, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Forfait_m3_WaterNet", "date_from": "2025-01-01", "date_to": "2025-01-31", "commodity": "Water", "Qty": 8.378378378378379, "Days": 31, "Qty_day": 0.2702702702702703, "Uom": "m3", "price": None, "CHF": 0.0, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Forfait_m3_WaterNet", "date_from": "2025-02-01", "date_to": "2025-02-18", "commodity": "Water", "Qty": 4.864864864864865, "Days": 18, "Qty_day": 0.2702702702702703, "Uom": "m3", "price": None, "CHF": 0.0, "TVA": 8.1},
            # ^^^^^^^^^^^^^^^^^^^^^^^^^
            # vvvvv Water, Extra_m3_WaterNet, 2024-12-07 00:00:00, 2025-02-18 00:00:00, 49, m3, 0.4000 -> 19.60
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Extra_m3_WaterNet", "date_from": "2024-12-07", "date_to": "2024-12-31", "commodity": "Water", "Qty": 16.554054054054053, "Days": 25, "Qty_day": 0.6621621621621622, "Uom": "m3", "price": 0.4, "CHF": 6.621621621621622, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Extra_m3_WaterNet", "date_from": "2025-01-01", "date_to": "2025-01-31", "commodity": "Water", "Qty": 20.527027027027028, "Days": 31, "Qty_day": 0.6621621621621622, "Uom": "m3", "price": 0.4, "CHF": 8.21081081081081, "TVA": 8.1},
            {"file": "..\\tests\\data\\Facture 2025-02.pdf", "item": "Extra_m3_WaterNet", "date_from": "2025-02-01", "date_to": "2025-02-18", "commodity": "Water", "Qty": 11.91891891891892, "Days": 18, "Qty_day": 0.6621621621621622, "Uom": "m3", "price": 0.4, "CHF": 4.767567567567568, "TVA": 8.1},
            # ^^^^^^^^^^^^^^^^^^^^^^^^^
        ]
    },
    {
        "file": "Facture 2016-08.pdf",
        "data": [
# vvvvv Power, Peak, 2016-06-30 00:00:00, 2016-07-28 00:00:00, 89, kWh, 0.1140 -> 10.15
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Peak", "date_from": "2016-06-30", "date_to": "2016-06-30", "commodity": "Power", "Qty": 3.0689655172413794, "Days": 1, "Qty_day": 3.0689655172413794, "Uom": "kWh", "price": 0.114, "CHF": 0.35000000000000003, "TVA": 8.0},
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Peak", "date_from": "2016-07-01", "date_to": "2016-07-28", "commodity": "Power", "Qty": 85.93103448275862, "Days": 28, "Qty_day": 3.0689655172413794, "Uom": "kWh", "price": 0.114, "CHF": 9.8, "TVA": 8.0},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Power, Peak, 2016-06-30 00:00:00, 2016-07-28 00:00:00, 89, kWh, 0.1045 -> 9.30
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Peak", "date_from": "2016-06-30", "date_to": "2016-06-30", "commodity": "Power", "Qty": 3.0689655172413794, "Days": 1, "Qty_day": 3.0689655172413794, "Uom": "kWh", "price": 0.1045, "CHF": 0.3206896551724138, "TVA": 8.0},
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Peak", "date_from": "2016-07-01", "date_to": "2016-07-28", "commodity": "Power", "Qty": 85.93103448275862, "Days": 28, "Qty_day": 3.0689655172413794, "Uom": "kWh", "price": 0.1045, "CHF": 8.979310344827587, "TVA": 8.0},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Power, Peak, 2016-07-29 00:00:00, 2016-08-29 00:00:00, 63, kWh, 0.1140 -> 7.18
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Peak", "date_from": "2016-07-29", "date_to": "2016-07-31", "commodity": "Power", "Qty": 5.90625, "Days": 3, "Qty_day": 1.96875, "Uom": "kWh", "price": 0.114, "CHF": 0.673125, "TVA": 8.0},
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Peak", "date_from": "2016-08-01", "date_to": "2016-08-29", "commodity": "Power", "Qty": 57.09375, "Days": 29, "Qty_day": 1.96875, "Uom": "kWh", "price": 0.114, "CHF": 6.506875, "TVA": 8.0},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Power, Peak, 2016-07-29 00:00:00, 2016-08-29 00:00:00, 63, kWh, 0.1045 -> 6.58
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Peak", "date_from": "2016-07-29", "date_to": "2016-07-31", "commodity": "Power", "Qty": 5.90625, "Days": 3, "Qty_day": 1.96875, "Uom": "kWh", "price": 0.1045, "CHF": 0.6168750000000001, "TVA": 8.0},
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Peak", "date_from": "2016-08-01", "date_to": "2016-08-29", "commodity": "Power", "Qty": 57.09375, "Days": 29, "Qty_day": 1.96875, "Uom": "kWh", "price": 0.1045, "CHF": 5.963125, "TVA": 8.0},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Power, Offpeak, 2016-06-30 00:00:00, 2016-07-28 00:00:00, 231, kWh, 0.0710 -> 16.40
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Offpeak", "date_from": "2016-06-30", "date_to": "2016-06-30", "commodity": "Power", "Qty": 7.9655172413793105, "Days": 1, "Qty_day": 7.9655172413793105, "Uom": "kWh", "price": 0.071, "CHF": 0.5655172413793103, "TVA": 8.0},
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Offpeak", "date_from": "2016-07-01", "date_to": "2016-07-28", "commodity": "Power", "Qty": 223.0344827586207, "Days": 28, "Qty_day": 7.9655172413793105, "Uom": "kWh", "price": 0.071, "CHF": 15.834482758620688, "TVA": 8.0},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Power, Offpeak, 2016-06-30 00:00:00, 2016-07-28 00:00:00, 231, kWh, 0.0630 -> 14.55
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Offpeak", "date_from": "2016-06-30", "date_to": "2016-06-30", "commodity": "Power", "Qty": 7.9655172413793105, "Days": 1, "Qty_day": 7.9655172413793105, "Uom": "kWh", "price": 0.063, "CHF": 0.5017241379310345, "TVA": 8.0},
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Offpeak", "date_from": "2016-07-01", "date_to": "2016-07-28", "commodity": "Power", "Qty": 223.0344827586207, "Days": 28, "Qty_day": 7.9655172413793105, "Uom": "kWh", "price": 0.063, "CHF": 14.048275862068968, "TVA": 8.0},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Power, Offpeak, 2016-07-29 00:00:00, 2016-08-29 00:00:00, 134, kWh, 0.0710 -> 9.51
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Offpeak", "date_from": "2016-07-29", "date_to": "2016-07-31", "commodity": "Power", "Qty": 12.5625, "Days": 3, "Qty_day": 4.1875, "Uom": "kWh", "price": 0.071, "CHF": 0.8915625, "TVA": 8.0},
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Offpeak", "date_from": "2016-08-01", "date_to": "2016-08-29", "commodity": "Power", "Qty": 121.4375, "Days": 29, "Qty_day": 4.1875, "Uom": "kWh", "price": 0.071, "CHF": 8.6184375, "TVA": 8.0},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Power, Offpeak, 2016-07-29 00:00:00, 2016-08-29 00:00:00, 134, kWh, 0.0630 -> 8.44
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Offpeak", "date_from": "2016-07-29", "date_to": "2016-07-31", "commodity": "Power", "Qty": 12.5625, "Days": 3, "Qty_day": 4.1875, "Uom": "kWh", "price": 0.063, "CHF": 0.79125, "TVA": 8.0},
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Offpeak", "date_from": "2016-08-01", "date_to": "2016-08-29", "commodity": "Power", "Qty": 121.4375, "Days": 29, "Qty_day": 4.1875, "Uom": "kWh", "price": 0.063, "CHF": 7.64875, "TVA": 8.0},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Power, Collectivity, 2016-06-30 00:00:00, 2016-08-29 00:00:00, 3.72, CHF, None -> 3.72
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Collectivity", "date_from": "2016-06-30", "date_to": "2016-06-30", "commodity": "Power", "Qty": 0.06098360655737705, "Days": 1, "Qty_day": 0.06098360655737705, "Uom": "CHF", "price": None                  , "CHF": 0.06098360655737705, "TVA": 8.0},
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Collectivity", "date_from": "2016-07-01", "date_to": "2016-07-31", "commodity": "Power", "Qty": 1.8904918032786886, "Days": 31, "Qty_day": 0.06098360655737705, "Uom": "CHF", "price": None                  , "CHF": 1.8904918032786886, "TVA": 8.0},
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Collectivity", "date_from": "2016-08-01", "date_to": "2016-08-29", "commodity": "Power", "Qty": 1.7685245901639344, "Days": 29, "Qty_day": 0.06098360655737705, "Uom": "CHF", "price": None                  , "CHF": 1.7685245901639344, "TVA": 8.0},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Power, Collectivity, 2016-06-30 00:00:00, 2016-08-29 00:00:00, 2.34, CHF, None -> 2.34
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Collectivity", "date_from": "2016-06-30", "date_to": "2016-06-30", "commodity": "Power", "Qty": 0.03836065573770492, "Days": 1, "Qty_day": 0.03836065573770492, "Uom": "CHF", "price": None                  , "CHF": 0.03836065573770492, "TVA": 8.0},
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Collectivity", "date_from": "2016-07-01", "date_to": "2016-07-31", "commodity": "Power", "Qty": 1.1891803278688524, "Days": 31, "Qty_day": 0.03836065573770492, "Uom": "CHF", "price": None                  , "CHF": 1.1891803278688524, "TVA": 8.0},
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Collectivity", "date_from": "2016-08-01", "date_to": "2016-08-29", "commodity": "Power", "Qty": 1.1124590163934427, "Days": 29, "Qty_day": 0.03836065573770492, "Uom": "CHF", "price": None                  , "CHF": 1.1124590163934427, "TVA": 8.0},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Power, FederalTax, 2016-06-30 00:00:00, 2016-07-28 00:00:00, 320, kWh, 0.0130 -> 4.16
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "FederalTax", "date_from": "2016-06-30", "date_to": "2016-06-30", "commodity": "Power", "Qty": 11.03448275862069, "Days": 1, "Qty_day": 11.03448275862069, "Uom": "kWh", "price": 0.013, "CHF": 0.14344827586206896, "TVA": 8.0},
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "FederalTax", "date_from": "2016-07-01", "date_to": "2016-07-28", "commodity": "Power", "Qty": 308.9655172413793, "Days": 28, "Qty_day": 11.03448275862069, "Uom": "kWh", "price": 0.013, "CHF": 4.016551724137931, "TVA": 8.0},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Power, FederalTax, 2016-07-29 00:00:00, 2016-08-29 00:00:00, 197, kWh, 0.0130 -> 2.56
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "FederalTax", "date_from": "2016-07-29", "date_to": "2016-07-31", "commodity": "Power", "Qty": 18.46875, "Days": 3, "Qty_day": 6.15625, "Uom": "kWh", "price": 0.013, "CHF": 0.24, "TVA": 8.0},
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "FederalTax", "date_from": "2016-08-01", "date_to": "2016-08-29", "commodity": "Power", "Qty": 178.53125, "Days": 29, "Qty_day": 6.15625, "Uom": "kWh", "price": 0.013, "CHF": 2.32, "TVA": 8.0},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Water, Forfait_Water, 2016-06-30 00:00:00, 2016-07-28 00:00:00, 9, jours, 3.2959 -> 95.58
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Forfait_Water", "date_from": "2016-06-30", "date_to": "2016-06-30", "commodity": "Water", "Qty": 0.3103448275862069, "Days": 1, "Qty_day": 0.3103448275862069, "Uom": "jours", "price": 3.2959, "CHF": 3.2958620689655174, "TVA": 2.5},
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Forfait_Water", "date_from": "2016-07-01", "date_to": "2016-07-28", "commodity": "Water", "Qty": 8.689655172413794, "Days": 28, "Qty_day": 0.3103448275862069, "Uom": "jours", "price": 3.2959, "CHF": 92.28413793103448, "TVA": 2.5},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Water, Forfait_Water, 2016-07-29 00:00:00, 2016-08-29 00:00:00, 2, jours, 3.2959 -> 105.47
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Forfait_Water", "date_from": "2016-07-29", "date_to": "2016-07-31", "commodity": "Water", "Qty": 0.1875, "Days": 3, "Qty_day": 0.0625, "Uom": "jours", "price": 3.2959, "CHF": 9.887812499999999, "TVA": 2.5},
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Forfait_Water", "date_from": "2016-08-01", "date_to": "2016-08-29", "commodity": "Water", "Qty": 1.8125, "Days": 29, "Qty_day": 0.0625, "Uom": "jours", "price": 3.2959, "CHF": 95.5821875, "TVA": 2.5},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Water, Forfait_m3_Water, 2016-06-30 00:00:00, 2016-07-28 00:00:00, 40, m3, None -> 0.00
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Forfait_m3_Water", "date_from": "2016-06-30", "date_to": "2016-06-30", "commodity": "Water", "Qty": 1.3793103448275863, "Days": 1, "Qty_day": 1.3793103448275863, "Uom": "m3", "price": None, "CHF": 0.0, "TVA": 2.5},
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Forfait_m3_Water", "date_from": "2016-07-01", "date_to": "2016-07-28", "commodity": "Water", "Qty": 38.62068965517241, "Days": 28, "Qty_day": 1.3793103448275863, "Uom": "m3", "price": None, "CHF": 0.0, "TVA": 2.5},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Water, Forfait_m3_Water, 2016-07-29 00:00:00, 2016-08-29 00:00:00, 44, m3, None -> 0.00
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Forfait_m3_Water", "date_from": "2016-07-29", "date_to": "2016-07-31", "commodity": "Water", "Qty": 4.125, "Days": 3, "Qty_day": 1.375, "Uom": "m3", "price": None, "CHF": 0.0, "TVA": 2.5},
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Forfait_m3_Water", "date_from": "2016-08-01", "date_to": "2016-08-29", "commodity": "Water", "Qty": 39.875, "Days": 29, "Qty_day": 1.375, "Uom": "m3", "price": None, "CHF": 0.0, "TVA": 2.5},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Water, Forfait_Cleansing, 2016-06-30 00:00:00, 2016-07-28 00:00:00, 9, jours, 3.2110 -> 93.12
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Forfait_Cleansing", "date_from": "2016-06-30", "date_to": "2016-06-30", "commodity": "Water", "Qty": 0.3103448275862069, "Days": 1, "Qty_day": 0.3103448275862069, "Uom": "jours", "price": 3.211, "CHF": 3.211034482758621, "TVA": 8.0},
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Forfait_Cleansing", "date_from": "2016-07-01", "date_to": "2016-07-28", "commodity": "Water", "Qty": 8.689655172413794, "Days": 28, "Qty_day": 0.3103448275862069, "Uom": "jours", "price": 3.211, "CHF": 89.90896551724138, "TVA": 8.0},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Water, Forfait_m3_Cleansing, 2016-06-30 00:00:00, 2016-07-28 00:00:00, 40, m3, None -> 0.00
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Forfait_m3_Cleansing", "date_from": "2016-06-30", "date_to": "2016-06-30", "commodity": "Water", "Qty": 1.3793103448275863, "Days": 1, "Qty_day": 1.3793103448275863, "Uom": "m3", "price": None, "CHF": 0.0, "TVA": 8.0},
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Forfait_m3_Cleansing", "date_from": "2016-07-01", "date_to": "2016-07-28", "commodity": "Water", "Qty": 38.62068965517241, "Days": 28, "Qty_day": 1.3793103448275863, "Uom": "m3", "price": None, "CHF": 0.0, "TVA": 8.0},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Water, Forfait_WaterNet, 2016-06-30 00:00:00, 2016-07-28 00:00:00, 9, jours, 0.5589 -> 16.21
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Forfait_WaterNet", "date_from": "2016-06-30", "date_to": "2016-06-30", "commodity": "Water", "Qty": 0.3103448275862069, "Days": 1, "Qty_day": 0.3103448275862069, "Uom": "jours", "price": 0.5589, "CHF": 0.5589655172413793, "TVA": 8.0},
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Forfait_WaterNet", "date_from": "2016-07-01", "date_to": "2016-07-28", "commodity": "Water", "Qty": 8.689655172413794, "Days": 28, "Qty_day": 0.3103448275862069, "Uom": "jours", "price": 0.5589, "CHF": 15.651034482758622, "TVA": 8.0},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Water, Forfait_m3_WaterNet, 2016-06-30 00:00:00, 2016-07-28 00:00:00, 40, m3, None -> 0.00
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Forfait_m3_WaterNet", "date_from": "2016-06-30", "date_to": "2016-06-30", "commodity": "Water", "Qty": 1.3793103448275863, "Days": 1, "Qty_day": 1.3793103448275863, "Uom": "m3", "price": None, "CHF": 0.0, "TVA": 8.0},
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Forfait_m3_WaterNet", "date_from": "2016-07-01", "date_to": "2016-07-28", "commodity": "Water", "Qty": 38.62068965517241, "Days": 28, "Qty_day": 1.3793103448275863, "Uom": "m3", "price": None, "CHF": 0.0, "TVA": 8.0},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Water, Forfait_WaterNet, 2016-07-29 00:00:00, 2016-08-29 00:00:00, 2, jours, 0.5589 -> 17.88
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Forfait_WaterNet", "date_from": "2016-07-29", "date_to": "2016-07-31", "commodity": "Water", "Qty": 0.1875, "Days": 3, "Qty_day": 0.0625, "Uom": "jours", "price": 0.5589, "CHF": 1.67625, "TVA": 8.0},
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Forfait_WaterNet", "date_from": "2016-08-01", "date_to": "2016-08-29", "commodity": "Water", "Qty": 1.8125, "Days": 29, "Qty_day": 0.0625, "Uom": "jours", "price": 0.5589, "CHF": 16.20375, "TVA": 8.0},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Water, Forfait_m3_WaterNet, 2016-07-29 00:00:00, 2016-08-29 00:00:00, 44, m3, None -> 0.00
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Forfait_m3_WaterNet", "date_from": "2016-07-29", "date_to": "2016-07-31", "commodity": "Water", "Qty": 4.125, "Days": 3, "Qty_day": 1.375, "Uom": "m3", "price": None, "CHF": 0.0, "TVA": 8.0},
{"file": "..\\tests\\data\\Facture 2016-08.pdf", "item": "Forfait_m3_WaterNet", "date_from": "2016-08-01", "date_to": "2016-08-29", "commodity": "Water", "Qty": 39.875, "Days": 29, "Qty_day": 1.375, "Uom": "m3", "price": None, "CHF": 0.0, "TVA": 8.0},
# ^^^^^^^^^^^^^^^^^^^^^^^^^

        ]
    },
    {
        "file": "Facture 2024-12.pdf",
        "data": [
# vvvvv Water, Forfait_Water, 2024-09-28 00:00:00, 2024-12-06 00:00:00, 0, jours, 0.7534 -> 52.74
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Forfait_Water", "date_from": "2024-09-28", "date_to": "2024-09-30", "commodity": "Water", "Qty": 0.0, "Days": 3, "Qty_day": 0.0, "Uom": "jours", "price": 0.7534, "CHF": 2.2602857142857142, "TVA": 2.6},
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Forfait_Water", "date_from": "2024-10-01", "date_to": "2024-10-31", "commodity": "Water", "Qty": 0.0, "Days": 31, "Qty_day": 0.0, "Uom": "jours", "price": 0.7534, "CHF": 23.356285714285715, "TVA": 2.6},
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Forfait_Water", "date_from": "2024-11-01", "date_to": "2024-11-30", "commodity": "Water", "Qty": 0.0, "Days": 30, "Qty_day": 0.0, "Uom": "jours", "price": 0.7534, "CHF": 22.602857142857143, "TVA": 2.6},
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Forfait_Water", "date_from": "2024-12-01", "date_to": "2024-12-06", "commodity": "Water", "Qty": 0.0, "Days": 6, "Qty_day": 0.0, "Uom": "jours", "price": 0.7534, "CHF": 4.5205714285714285, "TVA": 2.6},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Water, Forfait_m3_Water, 2024-09-28 00:00:00, 2024-12-06 00:00:00, 19, m3, None -> 0.00
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Forfait_m3_Water", "date_from": "2024-09-28", "date_to": "2024-09-30", "commodity": "Water", "Qty": 0.8142857142857143, "Days": 3, "Qty_day": 0.2714285714285714, "Uom": "m3", "price": None, "CHF": 0.0, "TVA": 2.6},
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Forfait_m3_Water", "date_from": "2024-10-01", "date_to": "2024-10-31", "commodity": "Water", "Qty": 8.414285714285713, "Days": 31, "Qty_day": 0.2714285714285714, "Uom": "m3", "price": None, "CHF": 0.0, "TVA": 2.6},
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Forfait_m3_Water", "date_from": "2024-11-01", "date_to": "2024-11-30", "commodity": "Water", "Qty": 8.142857142857142, "Days": 30, "Qty_day": 0.2714285714285714, "Uom": "m3", "price": None, "CHF": 0.0, "TVA": 2.6},
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Forfait_m3_Water", "date_from": "2024-12-01", "date_to": "2024-12-06", "commodity": "Water", "Qty": 1.6285714285714286, "Days": 6, "Qty_day": 0.2714285714285714, "Uom": "m3", "price": None, "CHF": 0.0, "TVA": 2.6},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Water, Extra_m3_Water, 2024-09-28 00:00:00, 2024-12-06 00:00:00, 46, m3, 2.3200 -> 106.72
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Extra_m3_Water", "date_from": "2024-09-28", "date_to": "2024-09-30", "commodity": "Water", "Qty": 1.9714285714285715, "Days": 3, "Qty_day": 0.6571428571428571, "Uom": "m3", "price": 2.32, "CHF": 4.573714285714285, "TVA": 2.6},
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Extra_m3_Water", "date_from": "2024-10-01", "date_to": "2024-10-31", "commodity": "Water", "Qty": 20.37142857142857, "Days": 31, "Qty_day": 0.6571428571428571, "Uom": "m3", "price": 2.32, "CHF": 47.261714285714284, "TVA": 2.6},
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Extra_m3_Water", "date_from": "2024-11-01", "date_to": "2024-11-30", "commodity": "Water", "Qty": 19.714285714285715, "Days": 30, "Qty_day": 0.6571428571428571, "Uom": "m3", "price": 2.32, "CHF": 45.73714285714286, "TVA": 2.6},
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Extra_m3_Water", "date_from": "2024-12-01", "date_to": "2024-12-06", "commodity": "Water", "Qty": 3.942857142857143, "Days": 6, "Qty_day": 0.6571428571428571, "Uom": "m3", "price": 2.32, "CHF": 9.14742857142857, "TVA": 2.6},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Water, Forfait_Cleansing, 2024-09-28 00:00:00, 2024-12-06 00:00:00, 0, jours, 0.7123 -> 49.86
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Forfait_Cleansing", "date_from": "2024-09-28", "date_to": "2024-09-30", "commodity": "Water", "Qty": 0.0, "Days": 3, "Qty_day": 0.0, "Uom": "jours", "price": 0.7123, "CHF": 2.136857142857143, "TVA": 8.1},
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Forfait_Cleansing", "date_from": "2024-10-01", "date_to": "2024-10-31", "commodity": "Water", "Qty": 0.0, "Days": 31, "Qty_day": 0.0, "Uom": "jours", "price": 0.7123, "CHF": 22.080857142857145, "TVA": 8.1},
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Forfait_Cleansing", "date_from": "2024-11-01", "date_to": "2024-11-30", "commodity": "Water", "Qty": 0.0, "Days": 30, "Qty_day": 0.0, "Uom": "jours", "price": 0.7123, "CHF": 21.36857142857143, "TVA": 8.1},
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Forfait_Cleansing", "date_from": "2024-12-01", "date_to": "2024-12-06", "commodity": "Water", "Qty": 0.0, "Days": 6, "Qty_day": 0.0, "Uom": "jours", "price": 0.7123, "CHF": 4.273714285714286, "TVA": 8.1},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Water, Forfait_m3_Cleansing, 2024-09-28 00:00:00, 2024-12-06 00:00:00, 19, m3, None -> 0.00
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Forfait_m3_Cleansing", "date_from": "2024-09-28", "date_to": "2024-09-30", "commodity": "Water", "Qty": 0.8142857142857143, "Days": 3, "Qty_day": 0.2714285714285714, "Uom": "m3", "price": None, "CHF": 0.0, "TVA": 8.1},
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Forfait_m3_Cleansing", "date_from": "2024-10-01", "date_to": "2024-10-31", "commodity": "Water", "Qty": 8.414285714285713, "Days": 31, "Qty_day": 0.2714285714285714, "Uom": "m3", "price": None, "CHF": 0.0, "TVA": 8.1},
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Forfait_m3_Cleansing", "date_from": "2024-11-01", "date_to": "2024-11-30", "commodity": "Water", "Qty": 8.142857142857142, "Days": 30, "Qty_day": 0.2714285714285714, "Uom": "m3", "price": None, "CHF": 0.0, "TVA": 8.1},
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Forfait_m3_Cleansing", "date_from": "2024-12-01", "date_to": "2024-12-06", "commodity": "Water", "Qty": 1.6285714285714286, "Days": 6, "Qty_day": 0.2714285714285714, "Uom": "m3", "price": None, "CHF": 0.0, "TVA": 8.1},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Water, Extra_m3_Cleansing, 2024-09-28 00:00:00, 2024-12-06 00:00:00, 46, m3, 2.2800 -> 104.88
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Extra_m3_Cleansing", "date_from": "2024-09-28", "date_to": "2024-09-30", "commodity": "Water", "Qty": 1.9714285714285715, "Days": 3, "Qty_day": 0.6571428571428571, "Uom": "m3", "price": 2.28, "CHF": 4.494857142857143, "TVA": 8.1},
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Extra_m3_Cleansing", "date_from": "2024-10-01", "date_to": "2024-10-31", "commodity": "Water", "Qty": 20.37142857142857, "Days": 31, "Qty_day": 0.6571428571428571, "Uom": "m3", "price": 2.28, "CHF": 46.44685714285714, "TVA": 8.1},
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Extra_m3_Cleansing", "date_from": "2024-11-01", "date_to": "2024-11-30", "commodity": "Water", "Qty": 19.714285714285715, "Days": 30, "Qty_day": 0.6571428571428571, "Uom": "m3", "price": 2.28, "CHF": 44.94857142857143, "TVA": 8.1},
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Extra_m3_Cleansing", "date_from": "2024-12-01", "date_to": "2024-12-06", "commodity": "Water", "Qty": 3.942857142857143, "Days": 6, "Qty_day": 0.6571428571428571, "Uom": "m3", "price": 2.28, "CHF": 8.989714285714285, "TVA": 8.1},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Water, Forfait_WaterNet, 2024-09-28 00:00:00, 2024-12-06 00:00:00, 0, jours, 0.1205 -> 8.44
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Forfait_WaterNet", "date_from": "2024-09-28", "date_to": "2024-09-30", "commodity": "Water", "Qty": 0.0, "Days": 3, "Qty_day": 0.0, "Uom": "jours", "price": 0.1205, "CHF": 0.3617142857142857, "TVA": 8.1},
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Forfait_WaterNet", "date_from": "2024-10-01", "date_to": "2024-10-31", "commodity": "Water", "Qty": 0.0, "Days": 31, "Qty_day": 0.0, "Uom": "jours", "price": 0.1205, "CHF": 3.7377142857142855, "TVA": 8.1},
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Forfait_WaterNet", "date_from": "2024-11-01", "date_to": "2024-11-30", "commodity": "Water", "Qty": 0.0, "Days": 30, "Qty_day": 0.0, "Uom": "jours", "price": 0.1205, "CHF": 3.617142857142857, "TVA": 8.1},
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Forfait_WaterNet", "date_from": "2024-12-01", "date_to": "2024-12-06", "commodity": "Water", "Qty": 0.0, "Days": 6, "Qty_day": 0.0, "Uom": "jours", "price": 0.1205, "CHF": 0.7234285714285714, "TVA": 8.1},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Water, Forfait_m3_WaterNet, 2024-09-28 00:00:00, 2024-12-06 00:00:00, 19, m3, None -> 0.00
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Forfait_m3_WaterNet", "date_from": "2024-09-28", "date_to": "2024-09-30", "commodity": "Water", "Qty": 0.8142857142857143, "Days": 3, "Qty_day": 0.2714285714285714, "Uom": "m3", "price": None, "CHF": 0.0, "TVA": 8.1},
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Forfait_m3_WaterNet", "date_from": "2024-10-01", "date_to": "2024-10-31", "commodity": "Water", "Qty": 8.414285714285713, "Days": 31, "Qty_day": 0.2714285714285714, "Uom": "m3", "price": None, "CHF": 0.0, "TVA": 8.1},
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Forfait_m3_WaterNet", "date_from": "2024-11-01", "date_to": "2024-11-30", "commodity": "Water", "Qty": 8.142857142857142, "Days": 30, "Qty_day": 0.2714285714285714, "Uom": "m3", "price": None, "CHF": 0.0, "TVA": 8.1},
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Forfait_m3_WaterNet", "date_from": "2024-12-01", "date_to": "2024-12-06", "commodity": "Water", "Qty": 1.6285714285714286, "Days": 6, "Qty_day": 0.2714285714285714, "Uom": "m3", "price": None, "CHF": 0.0, "TVA": 8.1},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Water, Extra_m3_WaterNet, 2024-09-28 00:00:00, 2024-12-06 00:00:00, 46, m3, 0.4000 -> 18.40
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Extra_m3_WaterNet", "date_from": "2024-09-28", "date_to": "2024-09-30", "commodity": "Water", "Qty": 1.9714285714285715, "Days": 3, "Qty_day": 0.6571428571428571, "Uom": "m3", "price": 0.4, "CHF": 0.7885714285714285, "TVA": 8.1},
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Extra_m3_WaterNet", "date_from": "2024-10-01", "date_to": "2024-10-31", "commodity": "Water", "Qty": 20.37142857142857, "Days": 31, "Qty_day": 0.6571428571428571, "Uom": "m3", "price": 0.4, "CHF": 8.148571428571428, "TVA": 8.1},
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Extra_m3_WaterNet", "date_from": "2024-11-01", "date_to": "2024-11-30", "commodity": "Water", "Qty": 19.714285714285715, "Days": 30, "Qty_day": 0.6571428571428571, "Uom": "m3", "price": 0.4, "CHF": 7.885714285714285, "TVA": 8.1},
{"file": "..\\tests\\data\\Facture 2024-12.pdf", "item": "Extra_m3_WaterNet", "date_from": "2024-12-01", "date_to": "2024-12-06", "commodity": "Water", "Qty": 3.942857142857143, "Days": 6, "Qty_day": 0.6571428571428571, "Uom": "m3", "price": 0.4, "CHF": 1.577142857142857, "TVA": 8.1},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
        ]
    },
    {
        'file':'Facture 2019-12.pdf',
        'data':[
# vvvvv Power, Peak, 2018-09-27 00:00:00, 2018-12-19 00:00:00, 1'782, kWh, 0.1020 -> 181.76
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Peak", "date_from": "2018-09-27", "date_to": "2018-09-30", "commodity": "Power", "Qty": 84.85714285714286, "Days": 4, "Qty_day": 21.214285714285715, "Uom": "kWh", "price": 0.102, "CHF": 8.655238095238095, "TVA": None                  },
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Peak", "date_from": "2018-10-01", "date_to": "2018-10-31", "commodity": "Power", "Qty": 657.6428571428572, "Days": 31, "Qty_day": 21.214285714285715, "Uom": "kWh", "price": 0.102, "CHF": 67.07809523809524, "TVA": None                  },
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Peak", "date_from": "2018-11-01", "date_to": "2018-11-30", "commodity": "Power", "Qty": 636.4285714285714, "Days": 30, "Qty_day": 21.214285714285715, "Uom": "kWh", "price": 0.102, "CHF": 64.91428571428571, "TVA": None                  },
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Peak", "date_from": "2018-12-01", "date_to": "2018-12-19", "commodity": "Power", "Qty": 403.0714285714286, "Days": 19, "Qty_day": 21.214285714285715, "Uom": "kWh", "price": 0.102, "CHF": 41.11238095238095, "TVA": None                  },
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Power, Peak, 2018-09-27 00:00:00, 2018-12-19 00:00:00, 1'782, kWh, 0.0995 -> 177.31
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Peak", "date_from": "2018-09-27", "date_to": "2018-09-30", "commodity": "Power", "Qty": 84.85714285714286, "Days": 4, "Qty_day": 21.214285714285715, "Uom": "kWh", "price": 0.0995, "CHF": 8.443333333333333, "TVA": None                  },
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Peak", "date_from": "2018-10-01", "date_to": "2018-10-31", "commodity": "Power", "Qty": 657.6428571428572, "Days": 31, "Qty_day": 21.214285714285715, "Uom": "kWh", "price": 0.0995, "CHF": 65.43583333333333, "TVA": None                  },
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Peak", "date_from": "2018-11-01", "date_to": "2018-11-30", "commodity": "Power", "Qty": 636.4285714285714, "Days": 30, "Qty_day": 21.214285714285715, "Uom": "kWh", "price": 0.0995, "CHF": 63.325, "TVA": None                  },
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Peak", "date_from": "2018-12-01", "date_to": "2018-12-19", "commodity": "Power", "Qty": 403.0714285714286, "Days": 19, "Qty_day": 21.214285714285715, "Uom": "kWh", "price": 0.0995, "CHF": 40.10583333333334, "TVA": None                  },
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Power, Offpeak, 2018-09-27 00:00:00, 2018-12-19 00:00:00, 1'889, kWh, 0.0695 -> 131.29
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Offpeak", "date_from": "2018-09-27", "date_to": "2018-09-30", "commodity": "Power", "Qty": 89.95238095238095, "Days": 4, "Qty_day": 22.488095238095237, "Uom": "kWh", "price": 0.0695, "CHF": 6.251904761904761, "TVA": None                  },
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Offpeak", "date_from": "2018-10-01", "date_to": "2018-10-31", "commodity": "Power", "Qty": 697.1309523809524, "Days": 31, "Qty_day": 22.488095238095237, "Uom": "kWh", "price": 0.0695, "CHF": 48.4522619047619, "TVA": None                  },
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Offpeak", "date_from": "2018-11-01", "date_to": "2018-11-30", "commodity": "Power", "Qty": 674.6428571428571, "Days": 30, "Qty_day": 22.488095238095237, "Uom": "kWh", "price": 0.0695, "CHF": 46.889285714285705, "TVA": None                  },
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Offpeak", "date_from": "2018-12-01", "date_to": "2018-12-19", "commodity": "Power", "Qty": 427.2738095238095, "Days": 19, "Qty_day": 22.488095238095237, "Uom": "kWh", "price": 0.0695, "CHF": 29.696547619047614, "TVA": None                  },
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Power, Offpeak, 2018-09-27 00:00:00, 2018-12-19 00:00:00, 1'889, kWh, 0.0600 -> 113.34
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Offpeak", "date_from": "2018-09-27", "date_to": "2018-09-30", "commodity": "Power", "Qty": 89.95238095238095, "Days": 4, "Qty_day": 22.488095238095237, "Uom": "kWh", "price": 0.06, "CHF": 5.397142857142858, "TVA": None                  },
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Offpeak", "date_from": "2018-10-01", "date_to": "2018-10-31", "commodity": "Power", "Qty": 697.1309523809524, "Days": 31, "Qty_day": 22.488095238095237, "Uom": "kWh", "price": 0.06, "CHF": 41.82785714285715, "TVA": None                  },
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Offpeak", "date_from": "2018-11-01", "date_to": "2018-11-30", "commodity": "Power", "Qty": 674.6428571428571, "Days": 30, "Qty_day": 22.488095238095237, "Uom": "kWh", "price": 0.06, "CHF": 40.478571428571435, "TVA": None                  },
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Offpeak", "date_from": "2018-12-01", "date_to": "2018-12-19", "commodity": "Power", "Qty": 427.2738095238095, "Days": 19, "Qty_day": 22.488095238095237, "Uom": "kWh", "price": 0.06, "CHF": 25.636428571428574, "TVA": None                  },
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Power, Collectivity, 2018-09-27 00:00:00, 2018-12-19 00:00:00, 41.27, CHF, None -> 41.27
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Collectivity", "date_from": "2018-09-27", "date_to": "2018-09-30", "commodity": "Power", "Qty": 1.9652380952380955, "Days": 4, "Qty_day": 0.49130952380952386, "Uom": "CHF", "price": None                  , "CHF": 1.9652380952380955, "TVA": None                  },
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Collectivity", "date_from": "2018-10-01", "date_to": "2018-10-31", "commodity": "Power", "Qty": 15.23059523809524, "Days": 31, "Qty_day": 0.49130952380952386, "Uom": "CHF", "price": None                  , "CHF": 15.23059523809524, "TVA": None                  },
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Collectivity", "date_from": "2018-11-01", "date_to": "2018-11-30", "commodity": "Power", "Qty": 14.739285714285716, "Days": 30, "Qty_day": 0.49130952380952386, "Uom": "CHF", "price": None                  , "CHF": 14.739285714285716, "TVA": None                  },
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Collectivity", "date_from": "2018-12-01", "date_to": "2018-12-19", "commodity": "Power", "Qty": 9.334880952380953, "Days": 19, "Qty_day": 0.49130952380952386, "Uom": "CHF", "price": None                  , "CHF": 9.334880952380953, "TVA": None                  },
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Power, FederalTax, 2018-09-27 00:00:00, 2018-12-19 00:00:00, 3'671, kWh, 0.0230 -> 84.43
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "FederalTax", "date_from": "2018-09-27", "date_to": "2018-09-30", "commodity": "Power", "Qty": 174.8095238095238, "Days": 4, "Qty_day": 43.70238095238095, "Uom": "kWh", "price": 0.023, "CHF": 4.020476190476191, "TVA": None                  },
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "FederalTax", "date_from": "2018-10-01", "date_to": "2018-10-31", "commodity": "Power", "Qty": 1354.7738095238094, "Days": 31, "Qty_day": 43.70238095238095, "Uom": "kWh", "price": 0.023, "CHF": 31.15869047619048, "TVA": None                  },
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "FederalTax", "date_from": "2018-11-01", "date_to": "2018-11-30", "commodity": "Power", "Qty": 1311.0714285714284, "Days": 30, "Qty_day": 43.70238095238095, "Uom": "kWh", "price": 0.023, "CHF": 30.153571428571432, "TVA": None                  },
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "FederalTax", "date_from": "2018-12-01", "date_to": "2018-12-19", "commodity": "Power", "Qty": 830.3452380952381, "Days": 19, "Qty_day": 43.70238095238095, "Uom": "kWh", "price": 0.023, "CHF": 19.097261904761908, "TVA": None                  },
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Water, Forfait_Water, 2018-09-27 00:00:00, 2018-12-19 00:00:00, 4, jours, 0.7534 -> 63.29
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Forfait_Water", "date_from": "2018-09-27", "date_to": "2018-09-30", "commodity": "Water", "Qty": 0.19047619047619047, "Days": 4, "Qty_day": 0.047619047619047616, "Uom": "jours", "price": 0.7534, "CHF": 3.013809523809524, "TVA": 2.5},
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Forfait_Water", "date_from": "2018-10-01", "date_to": "2018-10-31", "commodity": "Water", "Qty": 1.476190476190476, "Days": 31, "Qty_day": 0.047619047619047616, "Uom": "jours", "price": 0.7534, "CHF": 23.35702380952381, "TVA": 2.5},
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Forfait_Water", "date_from": "2018-11-01", "date_to": "2018-11-30", "commodity": "Water", "Qty": 1.4285714285714284, "Days": 30, "Qty_day": 0.047619047619047616, "Uom": "jours", "price": 0.7534, "CHF": 22.603571428571428, "TVA": 2.5},
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Forfait_Water", "date_from": "2018-12-01", "date_to": "2018-12-19", "commodity": "Water", "Qty": 0.9047619047619047, "Days": 19, "Qty_day": 0.047619047619047616, "Uom": "jours", "price": 0.7534, "CHF": 14.315595238095238, "TVA": 2.5},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Water, Forfait_m3_Water, 2018-09-27 00:00:00, 2018-12-19 00:00:00, 23, m3, None -> 0.00
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Forfait_m3_Water", "date_from": "2018-09-27", "date_to": "2018-09-30", "commodity": "Water", "Qty": 1.0952380952380953, "Days": 4, "Qty_day": 0.27380952380952384, "Uom": "m3", "price": None                  , "CHF": 0.0, "TVA": 2.5},
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Forfait_m3_Water", "date_from": "2018-10-01", "date_to": "2018-10-31", "commodity": "Water", "Qty": 8.488095238095239, "Days": 31, "Qty_day": 0.27380952380952384, "Uom": "m3", "price": None                  , "CHF": 0.0, "TVA": 2.5},
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Forfait_m3_Water", "date_from": "2018-11-01", "date_to": "2018-11-30", "commodity": "Water", "Qty": 8.214285714285715, "Days": 30, "Qty_day": 0.27380952380952384, "Uom": "m3", "price": None                  , "CHF": 0.0, "TVA": 2.5},
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Forfait_m3_Water", "date_from": "2018-12-01", "date_to": "2018-12-19", "commodity": "Water", "Qty": 5.2023809523809526, "Days": 19, "Qty_day": 0.27380952380952384, "Uom": "m3", "price": None                  , "CHF": 0.0, "TVA": 2.5},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Water, Extra_m3_Water, 2018-09-27 00:00:00, 2018-12-19 00:00:00, 26, m3, 2.3200 -> 60.32
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Extra_m3_Water", "date_from": "2018-09-27", "date_to": "2018-09-30", "commodity": "Water", "Qty": 1.2380952380952381, "Days": 4, "Qty_day": 0.30952380952380953, "Uom": "m3", "price": 2.32, "CHF": 2.8723809523809525, "TVA": 2.5},
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Extra_m3_Water", "date_from": "2018-10-01", "date_to": "2018-10-31", "commodity": "Water", "Qty": 9.595238095238095, "Days": 31, "Qty_day": 0.30952380952380953, "Uom": "m3", "price": 2.32, "CHF": 22.260952380952382, "TVA": 2.5},
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Extra_m3_Water", "date_from": "2018-11-01", "date_to": "2018-11-30", "commodity": "Water", "Qty": 9.285714285714286, "Days": 30, "Qty_day": 0.30952380952380953, "Uom": "m3", "price": 2.32, "CHF": 21.542857142857144, "TVA": 2.5},
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Extra_m3_Water", "date_from": "2018-12-01", "date_to": "2018-12-19", "commodity": "Water", "Qty": 5.880952380952381, "Days": 19, "Qty_day": 0.30952380952380953, "Uom": "m3", "price": 2.32, "CHF": 13.643809523809525, "TVA": 2.5},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Water, Forfait_Cleansing, 2018-09-27 00:00:00, 2018-12-19 00:00:00, 4, jours, 0.7123 -> 59.84
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Forfait_Cleansing", "date_from": "2018-09-27", "date_to": "2018-09-30", "commodity": "Water", "Qty": 0.19047619047619047, "Days": 4, "Qty_day": 0.047619047619047616, "Uom": "jours", "price": 0.7123, "CHF": 2.84952380952381, "TVA": 7.7},
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Forfait_Cleansing", "date_from": "2018-10-01", "date_to": "2018-10-31", "commodity": "Water", "Qty": 1.476190476190476, "Days": 31, "Qty_day": 0.047619047619047616, "Uom": "jours", "price": 0.7123, "CHF": 22.083809523809524, "TVA": 7.7},
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Forfait_Cleansing", "date_from": "2018-11-01", "date_to": "2018-11-30", "commodity": "Water", "Qty": 1.4285714285714284, "Days": 30, "Qty_day": 0.047619047619047616, "Uom": "jours", "price": 0.7123, "CHF": 21.371428571428574, "TVA": 7.7},
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Forfait_Cleansing", "date_from": "2018-12-01", "date_to": "2018-12-19", "commodity": "Water", "Qty": 0.9047619047619047, "Days": 19, "Qty_day": 0.047619047619047616, "Uom": "jours", "price": 0.7123, "CHF": 13.535238095238096, "TVA": 7.7},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Water, Forfait_m3_Cleansing, 2018-09-27 00:00:00, 2018-12-19 00:00:00, 23, m3, None -> 0.00
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Forfait_m3_Cleansing", "date_from": "2018-09-27", "date_to": "2018-09-30", "commodity": "Water", "Qty": 1.0952380952380953, "Days": 4, "Qty_day": 0.27380952380952384, "Uom": "m3", "price": None                  , "CHF": 0.0, "TVA": 7.7},
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Forfait_m3_Cleansing", "date_from": "2018-10-01", "date_to": "2018-10-31", "commodity": "Water", "Qty": 8.488095238095239, "Days": 31, "Qty_day": 0.27380952380952384, "Uom": "m3", "price": None                  , "CHF": 0.0, "TVA": 7.7},
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Forfait_m3_Cleansing", "date_from": "2018-11-01", "date_to": "2018-11-30", "commodity": "Water", "Qty": 8.214285714285715, "Days": 30, "Qty_day": 0.27380952380952384, "Uom": "m3", "price": None                  , "CHF": 0.0, "TVA": 7.7},
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Forfait_m3_Cleansing", "date_from": "2018-12-01", "date_to": "2018-12-19", "commodity": "Water", "Qty": 5.2023809523809526, "Days": 19, "Qty_day": 0.27380952380952384, "Uom": "m3", "price": None                  , "CHF": 0.0, "TVA": 7.7},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Water, Extra_m3_Cleansing, 2018-09-27 00:00:00, 2018-12-19 00:00:00, 26, m3, 2.2800 -> 59.28
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Extra_m3_Cleansing", "date_from": "2018-09-27", "date_to": "2018-09-30", "commodity": "Water", "Qty": 1.2380952380952381, "Days": 4, "Qty_day": 0.30952380952380953, "Uom": "m3", "price": 2.28, "CHF": 2.822857142857143, "TVA": 7.7},
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Extra_m3_Cleansing", "date_from": "2018-10-01", "date_to": "2018-10-31", "commodity": "Water", "Qty": 9.595238095238095, "Days": 31, "Qty_day": 0.30952380952380953, "Uom": "m3", "price": 2.28, "CHF": 21.877142857142857, "TVA": 7.7},
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Extra_m3_Cleansing", "date_from": "2018-11-01", "date_to": "2018-11-30", "commodity": "Water", "Qty": 9.285714285714286, "Days": 30, "Qty_day": 0.30952380952380953, "Uom": "m3", "price": 2.28, "CHF": 21.17142857142857, "TVA": 7.7},
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Extra_m3_Cleansing", "date_from": "2018-12-01", "date_to": "2018-12-19", "commodity": "Water", "Qty": 5.880952380952381, "Days": 19, "Qty_day": 0.30952380952380953, "Uom": "m3", "price": 2.28, "CHF": 13.40857142857143, "TVA": 7.7},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Water, Forfait_WaterNet, 2018-09-27 00:00:00, 2018-12-19 00:00:00, 4, jours, 0.1205 -> 10.13
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Forfait_WaterNet", "date_from": "2018-09-27", "date_to": "2018-09-30", "commodity": "Water", "Qty": 0.19047619047619047, "Days": 4, "Qty_day": 0.047619047619047616, "Uom": "jours", "price": 0.1205, "CHF": 0.4823809523809524, "TVA": 7.7},
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Forfait_WaterNet", "date_from": "2018-10-01", "date_to": "2018-10-31", "commodity": "Water", "Qty": 1.476190476190476, "Days": 31, "Qty_day": 0.047619047619047616, "Uom": "jours", "price": 0.1205, "CHF": 3.7384523809523813, "TVA": 7.7},
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Forfait_WaterNet", "date_from": "2018-11-01", "date_to": "2018-11-30", "commodity": "Water", "Qty": 1.4285714285714284, "Days": 30, "Qty_day": 0.047619047619047616, "Uom": "jours", "price": 0.1205, "CHF": 3.617857142857143, "TVA": 7.7},
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Forfait_WaterNet", "date_from": "2018-12-01", "date_to": "2018-12-19", "commodity": "Water", "Qty": 0.9047619047619047, "Days": 19, "Qty_day": 0.047619047619047616, "Uom": "jours", "price": 0.1205, "CHF": 2.291309523809524, "TVA": 7.7},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Water, Forfait_m3_WaterNet, 2018-09-27 00:00:00, 2018-12-19 00:00:00, 23, m3, None -> 0.00
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Forfait_m3_WaterNet", "date_from": "2018-09-27", "date_to": "2018-09-30", "commodity": "Water", "Qty": 1.0952380952380953, "Days": 4, "Qty_day": 0.27380952380952384, "Uom": "m3", "price": None                  , "CHF": 0.0, "TVA": 7.7},
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Forfait_m3_WaterNet", "date_from": "2018-10-01", "date_to": "2018-10-31", "commodity": "Water", "Qty": 8.488095238095239, "Days": 31, "Qty_day": 0.27380952380952384, "Uom": "m3", "price": None                  , "CHF": 0.0, "TVA": 7.7},
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Forfait_m3_WaterNet", "date_from": "2018-11-01", "date_to": "2018-11-30", "commodity": "Water", "Qty": 8.214285714285715, "Days": 30, "Qty_day": 0.27380952380952384, "Uom": "m3", "price": None                  , "CHF": 0.0, "TVA": 7.7},
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Forfait_m3_WaterNet", "date_from": "2018-12-01", "date_to": "2018-12-19", "commodity": "Water", "Qty": 5.2023809523809526, "Days": 19, "Qty_day": 0.27380952380952384, "Uom": "m3", "price": None                  , "CHF": 0.0, "TVA": 7.7},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvv Water, Extra_m3_WaterNet, 2018-09-27 00:00:00, 2018-12-19 00:00:00, 26, m3, 0.4000 -> 10.40
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Extra_m3_WaterNet", "date_from": "2018-09-27", "date_to": "2018-09-30", "commodity": "Water", "Qty": 1.2380952380952381, "Days": 4, "Qty_day": 0.30952380952380953, "Uom": "m3", "price": 0.4, "CHF": 0.49523809523809526, "TVA": 7.7},
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Extra_m3_WaterNet", "date_from": "2018-10-01", "date_to": "2018-10-31", "commodity": "Water", "Qty": 9.595238095238095, "Days": 31, "Qty_day": 0.30952380952380953, "Uom": "m3", "price": 0.4, "CHF": 3.8380952380952382, "TVA": 7.7},
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Extra_m3_WaterNet", "date_from": "2018-11-01", "date_to": "2018-11-30", "commodity": "Water", "Qty": 9.285714285714286, "Days": 30, "Qty_day": 0.30952380952380953, "Uom": "m3", "price": 0.4, "CHF": 3.7142857142857144, "TVA": 7.7},
{"file": "..\\tests\\data\\Facture 2019-12.pdf", "item": "Extra_m3_WaterNet", "date_from": "2018-12-01", "date_to": "2018-12-19", "commodity": "Water", "Qty": 5.880952380952381, "Days": 19, "Qty_day": 0.30952380952380953, "Uom": "m3", "price": 0.4, "CHF": 2.3523809523809525, "TVA": 7.7},
# ^^^^^^^^^^^^^^^^^^^^^^^^^
        ]
    }
    ]
    # @formatter:on

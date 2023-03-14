import csv
import os

import pytest as pytest

from src.feature_extractor_package.feature_extractor import read_pdf_and_extract_parts_list


@pytest.mark.xfail(reason="Verifies the csv is created correctly from resources/assembly/assembly.pdf")
def test_read_pdf_and_extract_parts_list():
    read_pdf_and_extract_parts_list('../resources/assembly/assembly.pdf', '../resources/csv/parts_list.csv')
    with open('../resources/csv/parts_list.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                assert row[0] == 'Item'
                assert row[1] == 'Qty'
                assert row[2] == 'Part Number'
                assert row[3] == 'Material'
            elif line_count == 1:
                assert row[0] == '27'
                assert row[1] == '4'
                assert row[2] == 'M5 Cap Screw(4)'
                assert row[3] == 'Stainless Steel'
            elif line_count == 28:
                assert row[0] != 'Item'
                assert row[1] != 'Qty'
                assert row[2] != 'Part Number'
                assert row[3] != 'Material'
            line_count += 1

        os.remove('../resources/csv/parts_list.csv')
        assert line_count == 28
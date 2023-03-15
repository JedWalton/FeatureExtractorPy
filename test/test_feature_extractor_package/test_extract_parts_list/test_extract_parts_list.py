from src.feature_extractor_package.extract_parts_list.extract_parts_list import \
    extract_parts_list_and_headings_from_pdf, write_parts_list_to_csv
from src.feature_extractor_package.feature_extractor import read_pdf_from_file

import csv
import os


def test_extract_parts_list_and_headings_from_pdf():
    pdf = read_pdf_from_file('./test/resources/assembly/assembly_drawing.pdf')
    parts_list, parts_list_headings = extract_parts_list_and_headings_from_pdf(pdf)
    assert parts_list[0].item == '27', "Item not read correctly"
    assert parts_list[0].qty == '4', "Qty not read correctly"
    assert parts_list[0].part_number == 'M5 Cap Screw(4)', "Part Number not read correctly"
    assert parts_list[0].material == 'Stainless Steel', "Material not read correctly"

    assert parts_list_headings.itemHeading == 'Item', "Item heading not read correctly"
    assert parts_list_headings.qtyHeading == 'Qty', "Qty heading not read correctly"
    assert parts_list_headings.partNumberHeading == 'Part Number', "Part Number heading not read correctly"
    assert parts_list_headings.materialHeading == 'Material', "Material heading not read correctly"


def test_write_parts_list_to_csv():
    pdf = read_pdf_from_file('./test/resources/assembly/assembly_drawing.pdf')
    parts_list, parts_list_headings = extract_parts_list_and_headings_from_pdf(pdf)
    write_parts_list_to_csv(parts_list, parts_list_headings, './test/resources/csv/parts_list.csv')
    with open('./test/resources/csv/parts_list.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                assert row[0] == 'Item', "Heading, Item, not found in first row"
                assert row[1] == 'Qty', "Heading, Qty, not found in first row"
                assert row[2] == 'Part Number', "Heading, Part Number, not found in first row"
                assert row[3] == 'Material', "Heading, Material, not found in first row"
            elif line_count == 1:
                assert row[0] == '27', "Value, 27, not found in second row"
                assert row[1] == '4', "Value, 4, not found in second row"
                assert row[2] == 'M5 Cap Screw(4)', "Value, M5 Cap Screw(4), not found in second row"
                assert row[3] == 'Stainless Steel', "Value, Stainless Steel, not found in second row"
            line_count += 1

        os.remove('./test/resources/csv/parts_list.csv')
        assert line_count == 28

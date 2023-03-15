import csv
import os

from src.feature_extractor_package.feature_extractor import read_pdf_and_extract_parts_list, read_pdf_from_file


def test_read_pdf_and_extract_parts_list():
    read_pdf_and_extract_parts_list('./test/resources/assembly/assembly_drawing.pdf', './test/resources/csv/parts_list.csv')
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
            elif line_count == 28:
                assert row[0] != 'Item', "Heading, Item, found in last row. Should not be there."
                assert row[1] != 'Qty', "Heading, Qty, found in last row. Should not be there."
                assert row[2] != 'Part Number', "Heading, Part Number, found in last row. Should not be there."
                assert row[3] != 'Material', "Heading, Material, found in last row. Should not be there."
            line_count += 1

        os.remove('./test/resources/csv/parts_list.csv')
        assert line_count == 28


def test_read_pdf_from_file():
    pdf = read_pdf_from_file('./test/resources/assembly/assembly_drawing.pdf')
    assert pdf is not None, "PDF not read correctly"

from src.feature_extractor_package.extract_title_block.title_block_utils import extract_raw_title_block_data_from_pdf, \
    process_raw_title_block_data, parse_title_block
from src.feature_extractor_package.feature_extractor import read_pdf_from_file


def test_extract_raw_title_block_data_from_pdf():
    pdf = read_pdf_from_file('./test/resources/assembly/assembly_drawing.pdf')
    table_line_1, table_line_2, table_line_3, table_line_4 = extract_raw_title_block_data_from_pdf(pdf)
    assert table_line_1 == 'Title:\nWren 80i Gas Turbine Engine\nAssembly Drawing'
    assert table_line_2 == 'Date:\nScale:\nUnits:\n24/10/2020\n2:3\nmm'
    assert table_line_3 == 'Drawn By:\nHarvey Walton'
    assert table_line_4 == 'Orthographic Projection:\n3rd Angle'


def test_process_raw_title_block_data():
    table = 'Title:\nWren 80i Gas Turbine Engine\nAssembly Drawing', 'Date:\nScale:\nUnits:\n24/10/2020\n2:3\nmm', 'Drawn By:\nHarvey Walton', 'Orthographic Projection:\n3rd Angle'
    processed_title_block = process_raw_title_block_data(table)
    assert processed_title_block == ['Wren 80i Gas Turbine Engine Assembly Drawing',
                                     '24/10/2020',
                                     '2:3',
                                     'mm',
                                     'Harvey Walton',
                                     '3rd Angle']


def test_parse_title_block():
    pdf = read_pdf_from_file('./test/resources/assembly/assembly_drawing.pdf')
    table = extract_raw_title_block_data_from_pdf(pdf)
    processed_title_block = process_raw_title_block_data(table)
    title_block = parse_title_block(processed_title_block)
    assert title_block.title == 'Wren 80i Gas Turbine Engine Assembly Drawing'
    assert title_block.date == '24/10/2020'
    assert title_block.scale == '2:3'
    assert title_block.units == 'mm'
    assert title_block.drawn_by == 'Harvey Walton'
    assert title_block.orthographic_projection == '3rd Angle'

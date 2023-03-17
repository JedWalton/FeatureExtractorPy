from src.feature_extractor_package.extract_title_block.title_block_utils import extract_raw_title_block_data_from_pdf
from src.feature_extractor_package.feature_extractor import read_pdf_from_file


def test_extract_raw_title_block_data_from_pdf():
    pdf = read_pdf_from_file('./test/resources/assembly/assembly_drawing.pdf')
    table_line_1, table_line_2, table_line_3, table_line_4 = extract_raw_title_block_data_from_pdf(pdf)
    assert table_line_1 == 'Title:\nWren 80i Gas Turbine Engine\nAssembly Drawing'
    assert table_line_2 == 'Date:\nScale:\nUnits:\n24/10/2020\n2:3\nmm'
    assert table_line_3 == 'Drawn By:\nHarvey Walton'
    assert table_line_4 == 'Orthographic Projection:\n3rd Angle'
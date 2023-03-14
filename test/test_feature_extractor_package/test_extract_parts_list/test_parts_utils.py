from src.feature_extractor_package.extract_parts_list.extract_parts_list import read_pdf_from_file
from src.feature_extractor_package.extract_parts_list.parts_utils import *


def test_get_last_element():
    arr = [1, 2, 3]
    assert get_last_element(arr) == 3


# def test_get_parts_list_headings():
#     pdf = read_pdf_from_file('../../resources/assembly/assembly.pdf')
#     item, qty, part_number, material = read_pdf_and_generate_num_py_arrays_for_parts_list(pdf)
#     partsListHeading = get_parts_list_headings(item, qty, part_number, material)

# def test_read_pdf_and_generate_num_py_arrays_for_parts_list():
#     pdf = read_pdf_from_file('../../resources/assembly/assembly.pdf')
#     item, qty, part_number, material = read_pdf_and_generate_num_py_arrays_for_parts_list(pdf)
#     assert item[0] == 'Item'
#     assert qty[0] == 'Qty'
#     assert part_number[0] == 'Part Number'
#     assert material[0] == 'Material'


def test_parse_parts_lists():
    item = ['item1', 'item2']
    qty = ['qty1', 'qty2']
    part_number = ['part_number1', 'part_number2']
    material = ['material1', 'material2']
    parts = parse_parts_lists(item, qty, part_number, material)
    assert parts[0].item == 'item1'
    assert parts[0].qty == 'qty1'
    assert parts[0].part_number == 'part_number1'
    assert parts[0].material == 'material1'
    assert parts[1].item == 'item2'
    assert parts[1].qty == 'qty2'
    assert parts[1].part_number == 'part_number2'
    assert parts[1].material == 'material2'

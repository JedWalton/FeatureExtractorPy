from src.feature_extractor_package.extract_parts_list.extract_parts_list import read_pdf_from_file
from src.feature_extractor_package.extract_parts_list.parts_utils import *


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


def test_parse_parts_lists_headings():
    item = np.array(['1', '2', '3', 'Item'])
    qty = np.array(['1', '2', '3', 'Qty'])
    part_number = np.array(['1', '2', '3', 'Part Number'])
    material = np.array(['1', '2', '3', 'Material'])
    parts = parse_parts_lists(item, qty, part_number, material)
    assert parts[len(parts) - 1].item != 'Item'
    assert parts[len(parts) - 1].qty != 'Qty'
    assert parts[len(parts) - 1].part_number != 'Part Number'
    assert parts[len(parts) - 1].material != 'Material'


def test_parse_parts_lists():
    item = np.array(['1', '2', '3', 'Item'])
    qty = np.array(['1', '2', '3', 'Qty'])
    part_number = np.array(['1', '2', '3', 'Part Number'])
    material = np.array(['1', '2', '3', 'Material'])
    parts = parse_parts_lists(item, qty, part_number, material)
    assert parts[0].item == '1'
    assert parts[0].qty == '1'
    assert parts[0].part_number == '1'
    assert parts[0].material == '1'

    assert item[len(parts) - 1] == '3'
    assert qty[len(parts) - 1] == '3'
    assert part_number[len(parts) - 1] == '3'
    assert material[len(parts) - 1] == '3'

    assert len(parts) == 3

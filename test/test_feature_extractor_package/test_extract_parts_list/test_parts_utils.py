from src.feature_extractor_package.extract_parts_list.extract_parts_list import read_pdf_from_file
from src.feature_extractor_package.extract_parts_list.parts_utils import *


def is_string_present_in_array(npArray, string):
    for element in npArray:
        if element == string:
            return True

    return False


def test_extract_raw_parts_list_data_from_pdf():
    pdf = read_pdf_from_file('./test/resources/assembly/assembly.pdf')
    item, qty, part_number, material = extract_raw_parts_list_data_from_pdf(pdf)
    assert is_string_present_in_array(item, 'Item'), "Item not found in item array"
    assert is_string_present_in_array(qty, 'Qty'), "Qty not found in qty array"
    assert is_string_present_in_array(part_number, 'Part Number'), "Part Number not found in part_number array"
    assert is_string_present_in_array(material, 'Material'), "Material not found in material array"


def test_parse_parts_lists():
    item = np.array(['1', '2', '3'])
    qty = np.array(['1', '2', '3'])
    part_number = np.array(['1', '2', '3'])
    material = np.array(['1', '2', '3'])
    parts = parse_parts_lists(item, qty, part_number, material)
    assert parts[0].item == '1', "Item not read correctly in parts[0].item array"
    assert parts[0].qty == '1', "Qty not read correctly in parts[0].qty array"
    assert parts[0].part_number == '1', "Part Number not read correctly in parts[0].part_number array"
    assert parts[0].material == '1', "Material not read correctly in parts[0].material array"

    assert item[len(parts) - 1] == '3', "Item not found in item array"
    assert qty[len(parts) - 1] == '3', "Qty not found in qty array"
    assert part_number[len(parts) - 1] == '3', "Part Number not found in part_number array"
    assert material[len(parts) - 1] == '3', "Material not found in material array"

    assert len(parts) == 3, "Parts list not parsed correctly"

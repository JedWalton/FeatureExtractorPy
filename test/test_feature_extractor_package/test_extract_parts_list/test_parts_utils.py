from src.feature_extractor_package.feature_extractor import read_pdf_from_file
from src.feature_extractor_package.extract_parts_list.parts_utils import *


def is_string_present_in_array(npArray, string):
    for element in npArray:
        if element == string:
            return True

    return False


def get_parts_list_headings(item, qty, part_number, material):
    parts_list_headings = PartsListHeadings()
    parts_list_headings.itemHeading = item[0]
    parts_list_headings.qtyHeading = qty[0]
    parts_list_headings.partNumberHeading = part_number[0]
    parts_list_headings.materialHeading = material[0]
    return parts_list_headings


def test_parse_parts_lists():
    item = np.array(['1', '2', '3', "Parts List"])
    qty = np.array(['1', '2', '3'])
    part_number = np.array(['1', '2', '3'])
    material = np.array(['1', '2', '3'])

    parts = parse_parts_list(item, qty, part_number, material)
    assert parts[0].item == '1', "Item not read correctly in parts[0].item array"
    assert parts[0].qty == '1', "Qty not read correctly in parts[0].qty array"
    assert parts[0].part_number == '1', "Part Number not read correctly in parts[0].part_number array"
    assert parts[0].material == '1', "Material not read correctly in parts[0].material array"

    assert parts[1].item == '2', "Item not read correctly in parts[1].item array"
    assert parts[1].qty == '2', "Qty not read correctly in parts[1].qty array"
    assert parts[1].part_number == '2', "Part Number not read correctly in parts[1].part_number array"
    assert parts[1].material == '2', "Material not read correctly in parts[1].material array"

    assert len(parts) == 2, "Parts list not parsed correctly"


def test_trim_whitespace():
    item = np.array(['', '', '', '1', '2', '', '3', '', '', ''])
    qty = np.array(['', '', '', '1', '2', '', '3', '', ''])
    part_number = np.array(['', '', '', '1', '2', '', '3', '', ''])
    material = np.array(['', '', '', '1', '2', '', '3', '', ''])

    item, qty, part_number, material = trim_whitespace(item, qty, part_number, material)

    assert item[0] == '1', "Item not trimmed correctly in item[0] array"
    assert qty[0] == '1', "Qty not trimmed correctly in qty[0] array"
    assert part_number[0] == '1', "Part Number not trimmed correctly in part_number[0] array"
    assert material[0] == '1', "Material not trimmed correctly in material[0] array"
    assert item[2] == '3', "Item not trimmed correctly in item[2] array"
    assert qty[2] == '3', "Qty not trimmed correctly in qty[2] array"
    assert part_number[2] == '3', "Part Number not trimmed correctly in part_number[2] array"
    assert material[2] == '3', "Material not trimmed correctly in material[2] array"


def test_extract_raw_parts_list_data_from_pdf():
    pdf = read_pdf_from_file('./test/resources/assembly/assembly_drawing.pdf')
    item, qty, part_number, material = extract_raw_parts_list_data_from_pdf(pdf)
    assert is_string_present_in_array(item, 'Item'), "Item not found in item array"
    assert is_string_present_in_array(qty, 'Qty'), "Qty not found in qty array"
    assert is_string_present_in_array(part_number, 'Part Number'), "Part Number not found in part_number array"
    assert is_string_present_in_array(material, 'Material'), "Material not found in material array"

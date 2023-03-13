
from src.feature_extractor_package.extract_parts_list.parts_utils import *


def test_get_last_element():
    arr = [1, 2, 3]
    assert get_last_element(arr) == 3


def test_get_parts_list_headings():
    item = [1, 2, 3]
    qty = [1, 2, 3]
    part_number = [1, 2, 3]
    material = [1, 2, 3]
    parts_list_headings = get_parts_list_headings(item, qty, part_number, material)
    assert parts_list_headings.itemHeading == 3
    assert parts_list_headings.qtyHeading == 3
    assert parts_list_headings.partNumberHeading == 3
    assert parts_list_headings.materialHeading == 3





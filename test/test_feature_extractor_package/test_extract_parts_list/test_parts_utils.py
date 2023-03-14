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


def test_trim_numpy_array_elements():
    item = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    qty = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    part_number = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    material = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    item, qty, part_number, material = trim_numpy_array_elements(item, qty, part_number, material)
    assert item[0] == 2
    assert item[-1] == 8
    assert qty[0] == 2
    assert qty[-1] == 8
    assert part_number[0] == 2
    assert part_number[-1] == 8
    assert material[0] == 2
    assert material[-1] == 8

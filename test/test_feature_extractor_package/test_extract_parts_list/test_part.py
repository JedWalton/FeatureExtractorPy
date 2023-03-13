# test_part.py

from src.feature_extractor_package.extract_parts_list.part import Part


def test_part():
    item = 1
    qty = 2
    part_number = 3
    material = 4
    part = Part(item, qty, part_number, material)
    assert part.item == 1
    assert part.qty == 2
    assert part.part_number == 3
    assert part.material == 4
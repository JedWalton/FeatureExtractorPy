# test_part.py

from src.feature_extractor_package.extract_parts_list.part import Part


def test_part():
    part = Part('item', 'qty', 'part_number', 'material')
    assert part.item == 'item'
    assert part.qty == 'qty'
    assert part.part_number == 'part_number'
    assert part.material == 'material'

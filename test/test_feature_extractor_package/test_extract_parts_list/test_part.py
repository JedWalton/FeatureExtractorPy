# test_part.py

from src.feature_extractor_package.extract_parts_list.part import Part


def test_part():
    part = Part('item', 'qty', 'part_number', 'material')
    assert part.item == 'item', "Item not read correctly"
    assert part.qty == 'qty', "Qty not read correctly"
    assert part.part_number == 'part_number', "Part Number not read correctly"
    assert part.material == 'material', "Material not read correctly"

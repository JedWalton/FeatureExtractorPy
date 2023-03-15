from src.feature_extractor_package.extract_parts_list.partsListHeading import PartsListHeadings


def test_parts_list_heading():
    partsListHeading = PartsListHeadings('item', 'qty', 'part_number', 'material')
    assert partsListHeading.itemHeading == 'item', "Item not read correctly"
    assert partsListHeading.qtyHeading == 'qty', "Qty not read correctly"
    assert partsListHeading.partNumberHeading == 'part_number', "Part Number not read correctly"
    assert partsListHeading.materialHeading == 'material', "Material not read correctly"

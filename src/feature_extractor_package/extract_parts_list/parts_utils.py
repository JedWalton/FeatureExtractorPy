import numpy as np

from src.feature_extractor_package.extract_parts_list.part import Part
from src.feature_extractor_package.extract_parts_list.partsListHeading import PartsListHeadings


def get_last_element(arr):
    return arr[-1]


def delete_last_element(arr):
    arr = np.delete(arr, -1)
    return arr


def get_parts_list_headings(item, qty, part_number, material):
    item_heading = get_last_element(item)
    qty_heading = get_last_element(qty)
    part_heading = get_last_element(part_number)
    material_heading = get_last_element(material)
    return PartsListHeadings(item_heading, qty_heading, part_heading, material_heading)


def trim_numpy_array_elements(item, qty, part_number, material):
    item = item[1:-3]
    qty = qty[1:-3]
    part_number = part_number[1:-3]
    part_number = part_number.astype(str)
    part_number = np.char.replace(part_number, '\n', ' ')
    material = material[1:-3]
    return item, qty, part_number, material


def read_pdf_and_generate_num_py_arrays_for_parts_list(pdf):
    # print(tables[0].df)
    part_table = pdf[0].df
    data = part_table._data
    # Convert the data to Numpy arrays
    array_data = [block.values for block in data.blocks]
    # Access the Numpy arrays
    item = array_data[0][2]
    qty = array_data[0][3]
    part_number = array_data[0][4]
    material = array_data[0][6]
    return item, qty, part_number, material


def parse_parts_lists(item, qty, part_number, material):
    parts = []
    for i in range(len(item) - 1):
        parts.append(Part(item[i], qty[i], part_number[i], material[i]))
    return parts

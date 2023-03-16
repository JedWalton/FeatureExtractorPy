import numpy as np

from src.feature_extractor_package.extract_parts_list.part import Part
from src.feature_extractor_package.extract_parts_list.partsListHeading import PartsListHeadings


def remove_last_element(arr):
    arr = arr[:-1]
    return arr


def get_parts_list_headings(item, qty, part_number, material):
    item = np.delete(item, -1)
    item_heading = item[-1]
    qty_heading = qty[-1]
    part_heading = part_number[-1]
    material_heading = material[-1]
    return PartsListHeadings(item_heading, qty_heading, part_heading,
                             material_heading)


def parse_parts_list(item, qty, part_number, material):
    item = remove_last_element(item)
    item = remove_last_element(item)
    qty = remove_last_element(qty)
    part_number = remove_last_element(part_number)
    material = remove_last_element(material)
    parts = []
    for i in range(len(item)):
        parts.append(Part(item[i], qty[i], part_number[i], material[i]))
    return parts


def trim_whitespace(item, qty, part_number, material):
    # Use np.where() to find the indices of the non-empty elements in each array
    item_indices = np.where(item != '')[0]
    qty_indices = np.where(qty != '')[0]
    part_number_indices = np.where(part_number != '')[0]
    material_indices = np.where(material != '')[0]

    # Extract the non-empty elements using the indices
    item = item[item_indices]
    qty = qty[qty_indices]
    part_number = part_number[part_number_indices].astype(str)
    part_number = np.char.replace(part_number, '\n', ' ')
    material = material[material_indices]

    return item, qty, part_number, material


def extract_raw_parts_list_data_from_pdf(pdf):
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
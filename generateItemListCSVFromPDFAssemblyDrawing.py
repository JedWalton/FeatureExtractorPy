import numpy as np
import IO
from part import part
from parts_list_heading import parts_list_heading


def get_last_element(arr):
    return arr[-1]


def get_headings_and_remove_from_parts_list(item, material, part_number, qty):
    item_heading = get_last_element(item)
    qty_heading = get_last_element(qty)
    part_heading = get_last_element(part_number)
    material_heading = get_last_element(material)
    return parts_list_heading(item_heading, material_heading, part_heading, qty_heading)


def trim_empty_num_py_array_elements(item, material, part_number, qty):
    item = item[1:-3]
    qty = qty[1:-3]
    part_number = part_number[1:-3]
    part_number = part_number.astype(str)
    part_number = np.char.replace(part_number, '\n', ' ')
    material = material[1:-3]
    return item, material, part_number, qty


def read_pdf_and_generate_num_py_arrays_for_parts_list(tables):
    # print(tables[0].df)
    part_table = tables[0].df
    data = part_table._data
    # Convert the data to Numpy arrays
    array_data = [block.values for block in data.blocks]
    # Access the Numpy arrays
    item = array_data[0][2]
    qty = array_data[0][3]
    part_number = array_data[0][4]
    material = array_data[0][6]
    return item, material, part_number, qty


def parse_parts_lists(item, material, part_number, qty):
    parts = []
    for i in range(len(item)):
        parts.append(part(item[i], material[i], part_number[i], qty[i]))
    return parts


def process_pdf_and_write_to_csv():
    tables = IO.readpdf()
    item, material, part_number, qty = read_pdf_and_generate_num_py_arrays_for_parts_list(tables)
    item, material, part_number, qty = trim_empty_num_py_array_elements(item, material, part_number, qty)

    parts_list_headings = get_headings_and_remove_from_parts_list(item, material, part_number, qty)
    parts_list = parse_parts_lists(item, material, part_number, qty)
    IO.writePartsListToCsv(parts_list, parts_list_headings)

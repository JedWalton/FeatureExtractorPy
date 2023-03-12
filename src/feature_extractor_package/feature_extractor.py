from src.feature_extractor_package import IO
from src.feature_extractor_package.extract_parts_list.parts_list import get_parts_list_headings, trim_empty_num_py_array_elements, \
    read_pdf_and_generate_num_py_arrays_for_parts_list, parse_parts_lists


def extract_parts_list(pdf):
    item, qty, part_number, material = read_pdf_and_generate_num_py_arrays_for_parts_list(pdf)
    item, qty, part_number, material = trim_empty_num_py_array_elements(item, qty, part_number, material)

    parts_list_headings = get_parts_list_headings(item, qty, part_number, material)
    parts_list = parse_parts_lists(item, qty, part_number, material)
    IO.write_parts_list_to_csv(parts_list, parts_list_headings)

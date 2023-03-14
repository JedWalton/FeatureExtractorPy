import csv

from camelot import io as camelot

from src.feature_extractor_package.extract_parts_list.parts_utils import \
    read_pdf_and_generate_num_py_arrays_for_parts_list, trim_numpy_array_elements, get_parts_list_headings, \
    parse_parts_lists


def extract_parts_list_from_pdf_and_write_to_csv(pdf):
    item, qty, part_number, material = read_pdf_and_generate_num_py_arrays_for_parts_list(pdf)
    item, qty, part_number, material = trim_numpy_array_elements(item, qty, part_number, material)
    parts_list_headings = get_parts_list_headings(item, qty, part_number, material)
    parts_list = parse_parts_lists(item, qty, part_number, material)
    return parts_list, parts_list_headings


def read_pdf_from_file(url):
    pdf = camelot.read_pdf(url)
    return pdf


def write_parts_list_to_csv(parts_list, parts_list_headings, csv_url):
    # Write data to CSV file
    with open(csv_url, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow([parts_list_headings.itemHeading, parts_list_headings.qtyHeading, parts_list_headings.partNumberHeading, parts_list_headings.materialHeading])
        for part in parts_list:
            writer.writerow([part.item, part.qty, part.part_number, part.material])
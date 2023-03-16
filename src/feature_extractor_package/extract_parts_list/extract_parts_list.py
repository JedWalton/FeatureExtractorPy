import csv

from src.feature_extractor_package.extract_parts_list.parts_utils import \
    extract_raw_parts_list_data_from_pdf, trim_whitespace, get_parts_list_headings, \
    parse_parts_list


def extract_parts_list_and_headings_from_pdf(pdf):
    item, qty, part_number, material = extract_raw_parts_list_data_from_pdf(pdf)
    item, qty, part_number, material = trim_whitespace(item, qty, part_number, material)
    parts_list_headings = get_parts_list_headings(item, qty, part_number, material)
    parts_list = parse_parts_list(item, qty, part_number, material)
    return parts_list, parts_list_headings


def write_parts_list_to_csv(parts_list, parts_list_headings, csv_url):
    # Write data to CSV file
    with open(csv_url, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow([parts_list_headings.itemHeading, parts_list_headings.qtyHeading, parts_list_headings.partNumberHeading, parts_list_headings.materialHeading])
        for part in parts_list:
            writer.writerow([part.item, part.qty, part.part_number, part.material])

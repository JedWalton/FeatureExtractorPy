import src.feature_extractor_package.extract_parts_list.extract_parts_list
from src.feature_extractor_package.extract_parts_list.extract_parts_list import \
    extract_parts_list_from_pdf_and_write_to_csv
from src.feature_extractor_package.extract_parts_list.extract_parts_list import \
    write_parts_list_to_csv


def read_pdf_and_extract_parts_list(pdf_url):
    pdf = src.feature_extractor_package.\
        extract_parts_list.extract_parts_list\
        .read_pdf_from_file(pdf_url)

    parts_list, parts_list_headings = extract_parts_list_from_pdf_and_write_to_csv(pdf)
    write_parts_list_to_csv(parts_list, parts_list_headings)


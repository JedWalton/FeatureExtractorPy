import src.feature_extractor_package.extract_parts_list.extract_parts_list
from src.feature_extractor_package.extract_parts_list.extract_parts_list import \
    extract_parts_list_from_pdf_and_write_to_csv


def read_pdf_and_extract_parts_list():
    pdf = src.feature_extractor_package.\
        extract_parts_list.extract_parts_list\
        .read_pdf_from_file('../resources/assembly.pdf')

    extract_parts_list_from_pdf_and_write_to_csv(pdf)

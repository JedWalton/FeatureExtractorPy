from camelot import io as camelot

import src.feature_extractor_package.extract_parts_list.extract_parts_list
from src.feature_extractor_package.extract_parts_list.extract_parts_list import \
    extract_parts_list_and_headings_from_pdf
from src.feature_extractor_package.extract_parts_list.extract_parts_list import \
    write_parts_list_to_csv
from src.feature_extractor_package.extract_title_block.extract_title_block import extract_title_block_from_pdf, \
    write_title_block_to_csv


def read_pdf_and_extract_parts_list(pdf_url, csv_url):
    raw_pdf_table_data = read_pdf_from_file(pdf_url)

    parts_list, parts_list_headings = extract_parts_list_and_headings_from_pdf(raw_pdf_table_data)
    write_parts_list_to_csv(parts_list, parts_list_headings, csv_url)


def read_pdf_and_extract_title_block(pdf_url, csv_url):
    raw_pdf_table_block_data = read_pdf_from_file(pdf_url)
    title_block = extract_title_block_from_pdf(raw_pdf_table_block_data)
    write_title_block_to_csv(title_block, csv_url)


def read_pdf_from_file(url):
    pdf = camelot.read_pdf(url, backend='poppler')
    return pdf

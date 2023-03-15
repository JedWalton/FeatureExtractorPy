from src.feature_extractor_package.extract_title_block.title_block_utils import extract_raw_title_block_data_from_pdf


def extract_title_block_from_pdf(pdf):
    raw_title_block_data = extract_raw_title_block_data_from_pdf(pdf)
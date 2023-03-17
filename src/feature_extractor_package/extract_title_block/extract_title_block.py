import csv

from src.feature_extractor_package.extract_title_block.title_block_utils import extract_raw_title_block_data_from_pdf, \
    process_raw_title_block_data, parse_title_block


def extract_title_block_from_pdf(pdf):
    table = extract_raw_title_block_data_from_pdf(pdf)
    processed_title_block = process_raw_title_block_data(table)
    title_block = parse_title_block(processed_title_block)
    print("processed table: ", processed_title_block)
    return title_block


def write_title_block_to_csv(title_block, csv_url):
    # Write data to CSV file
    with open(csv_url, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(["Title", "Date", "Scale", "Units", "Drawn By", "Orthographic Projection"])
        writer.writerow([title_block.title, title_block.date, title_block.scale, title_block.units, title_block.drawn_by,
                         title_block.orthographic_projection])

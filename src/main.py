# This is a sample Python script.
from src.feature_extractor_package.feature_extractor import read_pdf_and_extract_parts_list

if __name__ == '__main__':
    read_pdf_and_extract_parts_list('../test/resources/assembly/assembly.pdf', '../test/resources/csv/parts_list.csv')
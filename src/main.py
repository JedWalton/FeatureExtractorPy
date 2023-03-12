# This is a sample Python script.
from src.feature_extractor_package import feature_extractor, IO

if __name__ == '__main__':
    pdf = IO.read_pdf_from_file('./resources/assembly.pdf')
    feature_extractor.extract_parts_list(pdf)


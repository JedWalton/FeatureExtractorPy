# This is a sample Python script.
import IO
import feature_extractor

if __name__ == '__main__':
    pdf = IO.read_pdf_from_file('./resources/assembly.pdf')
    feature_extractor.extract_parts_list_and_parts_list_headings(pdf)


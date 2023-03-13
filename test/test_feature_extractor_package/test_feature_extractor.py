# test_extract_parts_list.py

from src.feature_extractor_package import IO
from src.feature_extractor_package.feature_extractor import extract_parts_list
from unittest.mock import patch


def test_extract_parts_list():
    # Mock the behavior of IO.write_parts_list_to_csv to check if the function is called
    with patch.object(IO, 'write_parts_list_to_csv') as mock_write_csv:
        # Test the test_extract_parts_list function
        pdf = IO.read_pdf_from_file('./resources/assembly.pdf')
        extract_parts_list(pdf)

        # Verify that the write_parts_list_to_csv function was called with the correct arguments
        mock_write_csv.assert_called_once()

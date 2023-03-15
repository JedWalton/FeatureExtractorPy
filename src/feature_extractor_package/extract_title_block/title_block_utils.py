def extract_raw_title_block_data_from_pdf(pdf):
    # print(tables[0].df)
    pdf_data = pdf[0].df
    data = pdf_data._data
    # Convert the data to Numpy arrays
    array_data = [block.values for block in data.blocks]
    parts_list = array_data[0][1]
    return parts_list

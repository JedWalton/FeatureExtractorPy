from src.feature_extractor_package.extract_title_block.titleBlock import TitleBlock


def extract_raw_title_block_data_from_pdf(pdf):
    # print(tables[0].df)
    pdf_data = pdf[0].df
    data = pdf_data._data
    # Convert the data to Numpy arrays
    array_data = [block.values for block in data.blocks]
    table_line_1 = array_data[0][1][30]
    table_line_2 = array_data[0][1][31]
    table_line_3 = array_data[0][5][30]
    table_line_4 = array_data[0][5][31]
    return table_line_1, table_line_2, table_line_3, table_line_4


def process_raw_title_block_data(table):
    print("table: ", table)
    parts = []
    lines = table[0].split('\n')
    line = lines[1] + " " + lines[2]
    parts.append(line)
    lines = table[1].split('\n')
    line = lines[3]
    parts.append(line)
    line = lines[4]
    parts.append(line)
    line = lines[5]
    parts.append(line)
    lines = table[2].split('\n')
    line = lines[1]
    parts.append(line)
    lines = table[3].split('\n')
    line = lines[1]
    parts.append(line)
    return parts


def parse_title_block(unprocessed_table):
    return TitleBlock(unprocessed_table[0], unprocessed_table[1],
                      unprocessed_table[2], unprocessed_table[3], unprocessed_table[4], unprocessed_table[5])

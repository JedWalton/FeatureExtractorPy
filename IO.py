import csv

from camelot import io as camelot


def readpdf():
    tables = camelot.read_pdf('./resources/assembly.pdf')
    return tables


def writePartsListToCsv(item, material, partNumber, qty):
    # table_df.to_csv('./resources/assembly.csv', index=False, header=False)
    # Write data to CSV file
    with open('parts_list.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(len(item)):
            writer.writerow([item[i], qty[i], partNumber[i], material[i]])

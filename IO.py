import csv

from camelot import io as camelot


def readpdf():
    tables = camelot.read_pdf('./resources/assembly.pdf')
    return tables


def writePartsListToCsv(partsList, partsListHeadings):
    # table_df.to_csv('./resources/assembly.csv', index=False, header=False)
    # Write data to CSV file
    with open('parts_list.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow([partsListHeadings.itemHeading, partsListHeadings.materialHeading, partsListHeadings.partNumberHeading, partsListHeadings.qtyHeading])
        for part in partsList:
            writer.writerow([part.item, part.material, part.partNumber, part.qty])

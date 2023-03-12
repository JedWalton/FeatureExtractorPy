import csv

from camelot import io as camelot


def read_pdf_from_file(url):
    pdf = camelot.read_pdf(url)
    return pdf


def write_parts_list_to_csv(parts_list, parts_list_headings):
    # Write data to CSV file
    with open('./parts_list.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow([parts_list_headings.itemHeading, parts_list_headings.qtyHeading, parts_list_headings.partNumberHeading, parts_list_headings.materialHeading])
        for part in parts_list:
            writer.writerow([part.item, part.qty, part.part_number, part.material])

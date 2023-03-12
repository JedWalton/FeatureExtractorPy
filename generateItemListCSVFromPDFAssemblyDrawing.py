import numpy as np
import IO
from part import part


def getHeading(arr):
    # Get the last element of the array
    last_element = arr[-1]
    # Remove the last element from the array
    arr = arr[:-1]
    # Add the last element to the beginning of the array
    arr = np.concatenate(([last_element], arr))
    return arr


def getHeadingsAndRemoveFromPartsList(item, material, partNumber, qty):
    itemHeading = getHeading(item)
    qtyHeading = getHeading(qty)
    partHeading = getHeading(partNumber)
    materialHeading = getHeading(material)
    return item, material, partNumber, qty


def trimEmptyNumPyArrayElements(item, material, partNumber, qty):
    item = item[1:-3]
    qty = qty[1:-3]
    partNumber = partNumber[1:-3]
    partNumber = partNumber.astype(str)
    partNumber = np.char.replace(partNumber, '\n', ' ')
    material = material[1:-3]
    return item, material, partNumber, qty


def readPdfAndGenerateNumPyArraysForPartsList(tables):
    # print(tables[0].df)
    partTable = tables[0].df
    data = partTable._data
    # Convert the data to Numpy arrays
    array_data = [block.values for block in data.blocks]
    # Access the Numpy arrays
    item = array_data[0][2]
    qty = array_data[0][3]
    partNumber = array_data[0][4]
    material = array_data[0][6]
    return item, material, partNumber, qty


def parsePartsLists(item, material, partNumber, qty):
    parts = []
    for i in range(len(item)):
        parts.append(part(item[i], material[i], partNumber[i], qty[i]))
    return parts


def processPdfAndWriteToCsv():
    tables = IO.readpdf()
    item, material, partNumber, qty = readPdfAndGenerateNumPyArraysForPartsList(tables)
    item, material, partNumber, qty = trimEmptyNumPyArrayElements(item, material, partNumber, qty)
    item, material, partNumber, qty = getHeadingsAndRemoveFromPartsList(item, material, partNumber, qty)
    partsList = parsePartsLists(item, material, partNumber, qty)
    IO.writePartsListToCsv(partsList)

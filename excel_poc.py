import csv
from time import time

from openpyxl import load_workbook


def convert_excel_to_csv(excel_filepath):
    wb = load_workbook(excel_filepath, read_only=True)
    ws = wb.active
    with open(f"temp{int(time())}.csv", "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        for row in ws:
            values = (cell.value for cell in row)
            csvwriter.writerow(values)

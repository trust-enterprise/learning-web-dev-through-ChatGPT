import win32com.client
import os

# File paths
workbook_path = r'C:\Users\Tahseen Fatima\Desktop\file.xlsx'
output_path = r'C:\Users\Tahseen Fatima\Desktop\trial'

# Ensure the output directory exists
if not os.path.exists(output_path):
    os.makedirs(output_path)

# Open Excel
excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = False  # Run Excel in the background
wb = excel.Workbooks.Open(workbook_path)

# Access sheets
sheet1 = wb.Sheets('1')
sheet2 = wb.Sheets('2')

# Get total rows in Sheet1
last_row = sheet2.UsedRange.Rows.Count

# Loop through each row in Sheet1 (ignoring the header row)
for row in range(2, last_row + 1):
    # Read data from Sheet2
    sn = sheet2.Cells(row, 1).Value
    ph = sheet2.Cells(row, 2).Value
    roll_no = sheet2.Cells(row, 3).Value
    candidate = sheet2.Cells(row, 4).Value
    father = sheet2.Cells(row, 5).Value

    # Update data in Sheet1
    # sheet1.Cells(1, 4).Value = sn         # SN -> B1
    sheet1.Cells(16, 7).Value = ph    # Roll No -> B2
    sheet1.Cells(12, 4).Value = roll_no  # Candidate -> B3
    sheet1.Cells(13, 4).Value = candidate     # Father -> B4
    sheet1.Cells(14, 4).Value = father     # Father -> B4

    # Save Sheet2 as a PDF
    pdf_filename = os.path.join(output_path, f'admitCard_{roll_no}_{candidate}.pdf')
    sheet1.ExportAsFixedFormat(0, pdf_filename)  # 0 indicates PDF format
    print(f"PDF saved: {pdf_filename}")

# Close workbook and quit Excel
wb.Close(SaveChanges=False)
excel.Quit()

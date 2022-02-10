import openpyxl

workbookM = openpyxl.load_workbook("currrency.xlsx")
sheet = workbookM["EURUSD"]

totalRows = sheet.max_row
totalCols = sheet.max_column

print(totalRows)
print(totalCols)

print(sheet.cell(row=2,column = 1).value)


for rows in range(1, totalRows+1):
    print("")
    for cols in range(1,totalCols+1):
        print(str(sheet.cell(row = rows, column = cols).value) + " ",end = " ")

rows = totalRows+1
for cols in range(1,totalCols+1):
    sheet.cell(row = rows, column = cols).value = str(rows) + " Mahen is Kool " + str(cols)

workbookM.save("currrency.xlsx")
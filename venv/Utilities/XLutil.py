import openpyxl

def getRowCount(path,sheetName):
    workBook = openpyxl.load_workbook(path)
    sheet = workBook[sheetName]
    return sheet.max_row

def getColCount(path,sheetName):
    workBook = openpyxl.load_workbook(path)
    sheet = workBook[sheetName]
    return sheet.max_column

def getCellData(path,sheetName,rowNum,colNum):
    workBook = openpyxl.load_workbook ( path )
    sheet = workBook[sheetName]
    return sheet.cell(row=rowNum,column = colNum).value

def setCellData(path,sheetName,rowNum,colNum,newValue):
    workBook = openpyxl.load_workbook ( path )
    sheet = workBook[sheetName]
    sheet.cell( row = rowNum, column = colNum ).value = newValue
    workBook.save(path)

print(getRowCount("currrency.xlsx","EURUSD"))
print(getColCount("currrency.xlsx","EURUSD"))
print(getCellData("currrency.xlsx","EURUSD",3,3))

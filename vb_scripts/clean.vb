' Clean.vb
Dim ExcelApp, Workbook, Sheet
Set ExcelApp = CreateObject("Excel.Application")
ExcelApp.Visible = False ' Set to True for debugging

' Define workbook path
Dim WorkbookPath, FinalWorkbookPath
WorkbookPath = "datasets/wpsup_2020-01-01_to_2025-01-01.xlsx"
FinalWorkbookPath = "datasets/FINAL_wpsup_2020-01-01_to_2025-01-01.xlsx"

' Open workbook
Set Workbook = ExcelApp.Workbooks.Open(WorkbookPath)
Set Sheet = Workbook.Sheets(1)

' Format "period" column (column A) as date
Sheet.Columns("A:A").NumberFormat = "mm/dd/yyyy"

' Remove duplicates based on "period" (column 1) and "product-name" (column 4)
Sheet.Range("A1:I10000").RemoveDuplicates Columns:=Array(1, 4), Header:=xlYes

' Save and close
Workbook.SaveAs FinalWorkbookPath
Workbook.Close
ExcelApp.Quit

' Clean up
Set Sheet = Nothing
Set Workbook = Nothing
Set ExcelApp = Nothing
WScript.Echo "Cleaning completed."

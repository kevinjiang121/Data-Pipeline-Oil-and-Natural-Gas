' Transform.vb
Dim ExcelApp, Workbook, Sheet
Set ExcelApp = CreateObject("Excel.Application") 
ExcelApp.Visible = False ' Set to True for debugging

' Define workbook path
Dim WorkbookPath, FinalWorkbookPath
WorkbookPath = "datasets/FINAL_wpsup_2020-01-01_to_2025-01-01.xlsx"
FinalWorkbookPath = "datasets/FINAL_TRANSFORMED_wpsup_2020-01-01_to_2025-01-01.xlsx"

' Open workbook
Set Workbook = ExcelApp.Workbooks.Open(WorkbookPath)
Set Sheet = Workbook.Sheets(1)

' Filter data by region (e.g., "U.S.")
Sheet.Range("A1").AutoFilter Field:=3, Criteria1:="U.S."

' Convert units (column J: units, column I: value)
Dim LastRow, i
LastRow = Sheet.Cells(Sheet.Rows.Count, "A").End(-4162).Row ' -4162 = xlUp

For i = 2 To LastRow
    If Sheet.Cells(i, 10).Value = "MBBL/D" Then
        Sheet.Cells(i, 9).Value = Sheet.Cells(i, 9).Value * 1000 ' Convert value
        Sheet.Cells(i, 10).Value = "BBL/D" ' Update unit
    End If
Next

' Save and close
Workbook.SaveAs FinalWorkbookPath
Workbook.Close
ExcelApp.Quit

' Clean up
Set Sheet = Nothing
Set Workbook = Nothing
Set ExcelApp = Nothing
WScript.Echo "Transformation completed."

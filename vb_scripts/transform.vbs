Dim ExcelApp, Workbook, Sheet
Set ExcelApp = CreateObject("Excel.Application")
ExcelApp.Visible = False

Dim FSO, ScriptFolder, WorkbookPath, FinalWorkbookPath
Set FSO = CreateObject("Scripting.FileSystemObject")
ScriptFolder = FSO.GetParentFolderName(WScript.ScriptFullName)
WorkbookPath = ScriptFolder & "\..\datasets\FINAL_wpsup_2020-01-01_to_2025-01-01.xlsx"
FinalWorkbookPath = ScriptFolder & "\..\datasets\FINAL_TRANSFORMED_wpsup_2020-01-01_to_2025-01-01.xlsx"

Set Workbook = ExcelApp.Workbooks.Open(WorkbookPath)
Set Sheet = Workbook.Sheets(1)

Dim LastRow, i
LastRow = Sheet.Cells(Sheet.Rows.Count, "A").End(-4162).Row

For i = 2 To LastRow
    If Sheet.Cells(i, 3).Value <> "U.S." Then
        Sheet.Rows(i).EntireRow.Hidden = True
    End If
Next

For i = 2 To LastRow
    If Sheet.Cells(i, 10).Value = "MBBL/D" Then
        Sheet.Cells(i, 9).Value = Sheet.Cells(i, 9).Value * 1000
        Sheet.Cells(i, 10).Value = "BBL/D" 
    End If
Next

WScript.Echo "Saving transformed workbook to: " & FinalWorkbookPath
Workbook.SaveAs FinalWorkbookPath
Workbook.Close
ExcelApp.Quit

Set Sheet = Nothing
Set Workbook = Nothing
Set ExcelApp = Nothing
WScript.Echo "Transformation completed."

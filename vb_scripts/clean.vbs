Dim ExcelApp, Workbook, Sheet
Set ExcelApp = CreateObject("Excel.Application")
ExcelApp.Visible = False

Dim FSO, ScriptFolder, WorkbookPath, FinalWorkbookPath
Set FSO = CreateObject("Scripting.FileSystemObject")
ScriptFolder = FSO.GetParentFolderName(WScript.ScriptFullName)
WorkbookPath = ScriptFolder & "\..\datasets\wpsup_2020-01-01_to_2025-01-01.xlsx"
FinalWorkbookPath = ScriptFolder & "\..\datasets\FINAL_wpsup_2020-01-01_to_2025-01-01.xlsx"

Set Workbook = ExcelApp.Workbooks.Open(WorkbookPath)
Set Sheet = Workbook.Sheets(1)

Sheet.Columns("A:A").NumberFormat = "mm/dd/yyyy"

Dim LastRow, Row1, Row2
LastRow = Sheet.Cells(Sheet.Rows.Count, "A").End(-4162).Row '

For Row1 = LastRow To 2 Step -1
    For Row2 = Row1 - 1 To 1 Step -1
        If Sheet.Cells(Row1, 1).Value = Sheet.Cells(Row2, 1).Value And _
           Sheet.Cells(Row1, 4).Value = Sheet.Cells(Row2, 4).Value Then
            Sheet.Rows(Row1).Delete
            Exit For
        End If
    Next
Next

WScript.Echo "Saving cleaned workbook to: " & FinalWorkbookPath
Workbook.SaveAs FinalWorkbookPath
Workbook.Close
ExcelApp.Quit

Set Sheet = Nothing
Set Workbook = Nothing
Set ExcelApp = Nothing
WScript.Echo "Cleaning completed."

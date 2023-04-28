' ReadImageMetaData.vbs

Sub ReadImageMetadata()
    
    Dim objShell As Object
    Dim objFolder As Object
    Dim objFolderItem As Object
    Dim i As Integer
    Dim strData As String

    Set objShell = CreateObject("Shell.Application")
    Set objFolder = objShell.Namespace("D:\Temp")
    Set objFolderItem = objFolder.ParseName("Picture1.jpg")

    For i = 0 To 50
        If objFolder.GetDetailsOf(objFolder.Items, i) <> "" Then
            strData = strData & " " & i & ": " & objFolder.GetDetailsOf(objFolderItem, i)
        End If
    Next i
    MsgBox strData
End Sub

import os


class level4:
    def __init__(self, file, *args, **kwargs) -> None:
        super().__init__()
        self.file = file
        self.main()

    def main(self) -> None:
        # Level 4 as promised. (I lowkey skidded it from someone else but i cant remember who :skull:) W mans tho ong
        # Also I can remake this instead of using JScript, etc
        batch_code = """@if (@CodeSection == @Batch) @then


@echo off
setlocal DisableDelayedExpansion

if "%~1" equ "" echo Usage: Obfuscate filename.bat & goto :EOF
if not exist "%~1" echo File not found: "%~1" & goto :EOF

set "at=@"
set "pass=%random%"
(
    echo %at%if (@Pass == @X%pass%^) @begin
    echo    @echo off
    echo    CScript //nologo //E:JScript.Encode "%%~F0" ^> %pass%.bat
    echo    call %pass%
    echo    del /f /q %pass%.bat
    echo    exit /B
    echo %at%end 
    echo //**Start Encode**
    echo var a = new Array(^);

    set "i=0"
    for /F "usebackq delims=" %%a in ("%~1") do (
        set /A i+=1
        set "line=%%a"
        setlocal EnableDelayedExpansion
        echo a[!i!] = '!line:'=\x27!';
        endlocal
    )

    setlocal EnableDelayedExpansion
    echo for ( var i=1; i^<=!i!; ++i ^) WScript.Stdout.WriteLine(a[i]^);
) > "%~N1.tmp"

CScript //nologo //E:JScript "%~F0" "%~N1.tmp"
::rename "%~N1.tmp" "%~N1.bat"
::del "%~N1.tmp"
rename "%~N1.tmp" "%~N1.encoded.bat"
goto :EOF


@end

//Made by some guy on stack overflow (I can't find the post anymore + I delete the old comments I had :sob:)
//I had to edit it a lil bit to make it work again. (It didn't work at all for me before)

var fileToEncode = WScript.Arguments(0);

var oFSO = WScript.CreateObject("Scripting.FileSystemObject");
var oFile = oFSO.GetFile(fileToEncode);
var oStream = oFile.OpenAsTextStream(1);
var sSourceFile = oStream.ReadAll();
oStream.Close();

var oEncoder = WScript.CreateObject("Scripting.Encoder");
var sDest = oEncoder.EncodeScriptFile(".js", sSourceFile, 0, "")

var edited_name = fileToEncode.replace(".bat", ".encoded.bat");

var oStream = oFSO.OpenTextFile(fileToEncode, 2, true);
oStream.Write(sDest);
oStream.Close();"""
        with open("level4.bat", "w") as f:
            f.writelines(batch_code)
        os.system("level4.bat " + self.file)
        file_name = self.file.replace(".bat", ".encoded.bat")
        os.rename(f"{file_name}", f"{self.file}.level4.bat")
        os.remove("level4.bat")
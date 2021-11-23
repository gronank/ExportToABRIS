.\env\scripts\pyinstaller -F .\ExportToABRIS.py
del /S /Q ".\dist\ExportToABRIS\"
del /S /Q ".\dist\ExportToABRIS.zip"
if not exist ".\dist\ExportToABRIS\" mkdir ".\dist\ExportToABRIS\"
copy ".\disableCategories.json" ".\dist\ExportToABRIS\disableCategories.json"
copy ".\Specs\*" ".\dist\ExportToABRIS\"
cd dist
copy ".\ExportToABRIS.exe" ".\ExportToABRIS\ExportToABRIS.exe"
zip ExportToABRIS.zip ExportToABRIS\*
cd ..
"./env/scripts/pyinstaller" -F ./ExportToABRIS.py
del /S /Q "./dist/ExportToABRIS/"
if not exist "./dist/ExportToABRIS/" mkdir "./dist/ExportToABRIS/"
copy "./disableCategories.json" "./dist/ExportToABRIS/disableCategories.json"
copy /E "./Specs/*" "./dist/ExportToABRIS/"
cd dist
copy "./ExportToABRIS.exe" "./ExportToABRIS/ExportToABRIS.exe"
zip ExportToABRIS.zip ExportToABRIS/*
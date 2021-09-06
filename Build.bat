"./env/scripts/pyinstaller" -F ./RotorheadToABRIS.py
if not exist "./dist/RotorheadToABRIS/" mkdir "./dist/RotorheadToABRIS/"
copy "./README.txt" "./dist/RotorheadToABRIS/README.txt"
copy "./dist/RotorheadToABRIS.exe" "./dist/RotorheadToABRIS/RotorheadToABRIS.exe"
cd dist
zip RotorheadToABRIS.zip RotorheadToABRIS/*
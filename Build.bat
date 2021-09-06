"./env/scripts/pyinstaller" -F ./RotorheadToABRIS.py
copy ./dist/RotorheadToABRIS.exe ./dist/RotorheadToABRIS/RotorheadToABRIS.exe
cd dist
zip RotorheadToABRIS.zip RotorheadToABRIS/*
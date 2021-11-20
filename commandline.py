import os
import sys
folderPath=os.getcwd()
modifiers=set()
for arg in sys.argv[1:]:
	if arg.startswith('-'):
		modifiers.add(arg.lstrip('-').lower())
	else:
		break
pathStart=len(modifiers) +1
if(len(sys.argv)>pathStart):
	folderPath=' '.join(sys.argv[pathStart:]).strip('"')
databasePath=  os.path.join(folderPath, "Database\\")
os.makedirs(databasePath,exist_ok=True)
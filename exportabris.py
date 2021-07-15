from geometry import Line, NavPoint
from typing import List, Tuple
import uuid
import os
import sys
import serialize

folderPath=os.getcwd()
if(len(sys.argv)>1):
	folderPath=' '.join(sys.argv[1:]).strip('"')
databasePath=  os.path.join(folderPath, "Database\\")
os.makedirs(databasePath,exist_ok=True)

def save(name,varName,data):
	with open(databasePath + name,'w') as file:
		serialized = serialize.dumps(data,varname=varName,indent=0)
		file.write(serialized)

def getAbrisBase():
	return {
	"date":{
		"year":2016,
		"day":22,
		"month":6,
		},
	"expiration_date":{
		"year":2036,
		"day":22,
		"month":6,
		}
	}

def getNavPoint(navPoint):
	pt=getPoint(navPoint.point)
	pt["course"]=0
	pt["height"]=0
	return pt

def getPoint(pt:Tuple[float,float]):
	long,lat=pt
	return {
		"longitude":long,
		"latitude":lat
		}
# type 2 filled blue
def getLineObjects(lines):
	abrisLines = []
	for line in lines:
		lineGeometry = {
			"type":line.type,
			"name":line.name,
			"sub_type":0,
			"color":line.color,
			"class":"ABRIS_Linear_Object",
			"points":[getPoint(pt) for pt in line.points]
			}
		abrisLines.append(lineGeometry)
	return abrisLines

def getNavObjects(navPoints):
	referencePoints={}
	for navPoint in navPoints:
		refPoint={
			"type":navPoint.symbolType[1],
			"name":navPoint.name,
			"callsign":navPoint.name,
			"class":navPoint.symbolType[0],#"ABRIS_Waypoint",
			"position":getNavPoint(navPoint),
			"sub_type":navPoint.symbolType[2],
		}
		referencePoints[uuid.uuid4()]=refPoint
	return referencePoints

class AbrisAdditional:
	lines:List[Line] = []
	def AddLines(self,newLines:List[Line]):
		self.lines.extend(newLines)
	def Export(self):
		additional = getAbrisBase()
		
		additional["additional_objects"] = getLineObjects(self.lines)
		save("ADDITIONAL.lua",'additional', additional)

class AbrisNavigation:
	navPoints:List[Line] = []
	def AddNavPoints(self,newPoints:List[NavPoint]):
		self.navPoints.extend(newPoints)
	def Export(self):
		navigation = getAbrisBase()
		navigation["region"]=""
		navigation["waypoints"] = getNavObjects(self.navPoints)
		save("NAVIGATION.lua",'navigation', navigation)
		

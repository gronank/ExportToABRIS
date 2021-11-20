import pyclipper as pc
from typing import List,Tuple
from itertools import permutations

scale=1e4
NmToDegrees=1.0/60

def bufferZone(points:List[Tuple[float,float]], color, bufferSize):
	offset=pc.PyclipperOffset()
	clipperPoints = pc.scale_to_clipper(points,scale)
	for pt in clipperPoints:
		offset.AddPath([pt], pc.JT_ROUND, pc.ET_OPENROUND)
	clipperBufferSize=pc.scale_to_clipper(bufferSize*NmToDegrees,scale)
	linePoints = pc.scale_from_clipper(offset.Execute(clipperBufferSize),scale)
	lines=[]
	for points in linePoints:
		if(len(points)<3):
			continue
		points.append(points[0])
		lines.append(Line(points,color))
	return lines

def distanceSqr(pt0,pt1)->float:
	x=pt0[0]-pt1[0]
	y=pt0[1]-pt1[1]
	return x*x+y*y

def getPhaseLine(phaseLinePts):
	count=len(phaseLinePts)
	paths=[]
	# ugly n! brute force algorithm, good enough if there's only 3 points
	for combo in permutations(range(0,count)):
		dist=0
		for i, j in zip(combo[:-1],combo[1:]):
			dist=dist+distanceSqr(phaseLinePts[i],phaseLinePts[j])
		paths.append((dist,combo))
	bestPath = min(paths)[1]
	return [phaseLinePts[i] for i in bestPath]
	

	#segments = {}
	#for item in table:
	#	segment1 = segments.pop(item[1],None)
	#	segment2 = segments.pop(item[2],None)
	#	if segment1 and segment2:
	#		segment1.extend(segment2)
	#	elif segment1 and not segment2:
	#		segment1.append(item[2])
	#	elif segment2 and not segment1:
	#		segment1=segment2
	#		segment1.append(item[2])

	#	else:
	#		segments[item[1]]=[item[1],item[2]]
	#		segments[item[2]]=[item[2],item[1]]
	# segments[0]]

class Color:
	red={"R":255,
		 "G":0,
		 "B":0}
	yellow={"R":190,
		 "G":128,
		 "B":0}
	green={"R":0,
		   "G":255,
		   "B":0}
	white={"R":255,
		   "G":255,
		   "B":255}
	black={"R":0,
		   "G":0,
		   "B":0}

	def parse(self, propertyName):
		if not hasattr(self, propertyName):
			colorParts = propertyName.split(',')
			if(len(colorParts)!=3):
				raise Exception(f'Unable to parse color {propertyName}')
			colorComponents=[float(p) in colorParts]
			return {key: value for key, value in zip(['R','G','B'],colorComponents)}
		return getattr(self, propertyName)

class LineType:
	line=1
	filledHostile=2

	def parse(self, propertyName):
		if not hasattr(self, propertyName):
			raise Exception(f'Unkown line type {propertyName}')
		return getattr(self, propertyName)

class SymbolType:
	#Waypoints
	referencePoint=("ABRIS_Waypoint", 0, 8)
	initialPoint  =("ABRIS_Waypoint", 0, 1)
	landmark	  =("ABRIS_Waypoint", 0, 2)
	obstacle	  =("ABRIS_Waypoint", 0, 4)
	climbPoint	=("ABRIS_Waypoint", 0, 16)
	divePoint	 =("ABRIS_Waypoint", 0, 32)

	#Airdrome
	airbase	   =("ABRIS_Waypoint_Airdrome", 1, 6)
	farp		  =("ABRIS_Waypoint_Airdrome", 1, 10)
	navalbase	 =("ABRIS_Waypoint_Airdrome", 1, 18)
	airport	   =("ABRIS_Waypoint_Airdrome", 1, 5)
	heliport	  =("ABRIS_Waypoint_Airdrome", 1, 9)
	closed_airport=("ABRIS_Waypoint_Airdrome", 1, 32)
	common_airport=("ABRIS_Waypoint_Airdrome", 1, 4)
	new_airport   =("ABRIS_Waypoint_Airdrome", 1, 64)

	#Beacon
	vorPoint	   =("ABRIS_Waypoint_Beacon", 2, 1)
	dmePoint	   =("ABRIS_Waypoint_Beacon", 2, 2)
	tacanPoint	 =("ABRIS_Waypoint_Beacon", 2, 4)
	homerPoint	 =("ABRIS_Waypoint_Beacon", 2, 8)
	vorDmePoint	=("ABRIS_Waypoint_Beacon", 2, 3)
	vorTacanPoint  =("ABRIS_Waypoint_Beacon", 2, 5)
	airportHomer   =("ABRIS_Waypoint_Beacon", 2, 264)
	routeMarker	=("ABRIS_Waypoint_Beacon", 2, 528)
	ilsMarker	  =("ABRIS_Waypoint_Beacon", 2, 1040)

	#Town
	#town		   =("ABRIS_Waypoint_Town", 3, 0)

	#Datalink
	unknownHostile =("ABRIS_Datalink_Point", 4, 0)
	armouredHostile=("ABRIS_Datalink_Point", 4, 1)
	airDefenceHostile=("ABRIS_Datalink_Point", 4, 2)
	otherHostile   =("ABRIS_Datalink_Point", 4, 3)
	dlInitial	  =("ABRIS_Datalink_Point", 4, 4)
	groupMember	=("ABRIS_Datalink_Point", 4, 5)

	def parse(propertyName):
		if not hasattr(SymbolType, propertyName):
			raise Exception(f'Unkown symbol type {propertyName}')
		return getattr(SymbolType, propertyName)


class Line:
	name=""
	color=[]
	type=LineType.line
	points:List[Tuple[float,float]]=[]
	def __init__(self, points:List[Tuple[float,float]],color,name:str=""):
		self.points=points
		self.color=color
		self.name=name

class NavPoint:
	point:Tuple[float,float]=[]
	symbolType:SymbolType = SymbolType.referencePoint
	name:str=""


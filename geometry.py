import pyclipper as pc
from typing import List,Tuple
from itertools import permutations

scale=1e4
bufferSize=1.5#Nm
NmToDegrees=1.0/60

def bufferZone(points:List[Tuple[float,float]], color):
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

class LineType:
	line=1
	filledHostile=2

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
	type_id:str=""
	sub_type:str=""
	name:str=""


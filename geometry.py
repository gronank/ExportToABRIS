import pyclipper as pc
from typing import List,Tuple

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

class Color:
    red={"R":255,
	     "G":0,
	     "B":0}
    yellow={"R":255,
	     "G":255,
	     "B":0}

class Line:
    name=""
    color=[]
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


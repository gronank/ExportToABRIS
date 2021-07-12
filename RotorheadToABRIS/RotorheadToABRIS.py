from urllib.request import urlopen
import json
import serialize
import uuid
import pyclipper as pc
import re

def getSamName(unit):
	description=unit['properties']['description']
	fullName=description.split('Spotted: ')[1]
	name = fullName.split(' ')[0]
	return name
def getInfName(unit):
	description=unit['properties']['description']
	c=re.match("Infantry <br>(\d+) Alive",description).groups(1)
	return c[0]

def getVehcName(unit):
	description=unit['properties']['description']
	name = description.split(' ')[0]
	return name

def getObjName(unit):
	description=unit['properties']['description']
	obj=re.match("Objective Area: (\w+).+",description).groups(1)
	return obj[0]

def getPosition(unit):
	pos=unit['geometry']['coordinates']

	return {
		"longitude":pos[0],
		"latitude":pos[1],
		"course":0,
		"height":0
		}
def getZonePoint(pt):
	long,lat=pt
	return {
		"longitude":long,
		"latitude":lat
		}
red={
	"R":255,
	"G":0,
	"B":0}
def getDangerZones(solutions):
	zones=[]
	for solution in solutions:
		zone = {
			"type":1,
			"name":"",
			"sub_type":0,
			"color":red,
			"class":"ABRIS_Linear_Object",
			"points":[getZonePoint(pt) for pt in solution]
			}
		zone["points"].append(zone["points"][0])
		zones.append(zone)
	return zones

databasePath=r"C:\Users\ander\source\Saved Games\DCS\ABRIS\Database/"
url='http://rotorheads.ddns.net'
dangerZoneUrl=url+'/mapdata/mapred.json'
unitsUrl=url+'/mapdata/map.json'

#units
units=json.load(urlopen(unitsUrl));
referencePoints= {}
for unit in units['features']:
	if unit['properties']['description'].startswith('Objective Area'):
		type_id=0
		name=getObjName(unit)
		sub_type=8
	elif unit['properties']['icon']=='sam':
		type_id=4
		name=getSamName(unit)
		sub_type=2
	elif unit['properties']['icon']=='infant':
		type_id=4
		sub_type=0
		name=getInfName(unit)
	elif unit['properties']['icon']=='bvehicle':
		type_id=0
		sub_type=1
		name=getVehcName(unit)
	else:
		continue
	
	
	refPoint={
		"type":type_id,
		"name":name,
		"callsign":name,
		"class":"ABRIS_Datalink_Point",#"ABRIS_Waypoint",
		"position":getPosition(unit),
		"sub_type":sub_type,
		"color":red,
		}
	referencePoints[uuid.uuid4()]=refPoint
navigation={
	"date":{"year":2016,
		"day":22,
		"month":6,
	},
	"expiration_date":{"year":2036,
		"day":22,
		"month":6,
	},
	"region":"",
	"waypoints":referencePoints
    }

with open(databasePath+'NAVIGATION.lua','w') as file:
	data=serialize.dumps(navigation,varname='navigation',indent=0)
	file.write(data)

#danger zones
buffer=1.5/60
scale=1e4
dangePoints=json.load(urlopen(dangerZoneUrl));
offset=pc.PyclipperOffset()
for pt in dangePoints['features']:
	pos=(tuple(pt['geometry']['coordinates']),)
	offset.AddPath(pc.scale_to_clipper(pos,scale), pc.JT_ROUND, pc.ET_OPENROUND)

solution= pc.scale_from_clipper(offset.Execute(pc.scale_to_clipper(buffer,scale)),scale)

additional = {
	"date":{"year":2016,
		"day":22,
		"month":6,
	},
	"expiration_date":{"year":2036,
		"day":22,
		"month":6,
	},
	"additional_objects":getDangerZones(solution)
	}
with open(databasePath+'ADDITIONAL.lua','w') as file:
	data=serialize.dumps(additional,varname='additional',indent=0)
	file.write(data)
pass
#offset.AddPath(subj, pyclipper.JT_ROUND, pyclipper.ET_CLOSEDPOLYGON)

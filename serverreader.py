import json
from urllib.request import urlopen
import os
import sys

class PointFeature:
    description=""
    location=(0,0)
    icon=""

class ServerReader:
    url=""
    def __init__(self,url):
        self.url=url
    def readPoints(self, file):
        fileUrl=self.url+file
        objects=json.load(urlopen(fileUrl));
        features=[]
        for object in objects['features']:
            ptFtr=PointFeature()
            ptFtr.description=object['properties']['description']
            ptFtr.icon=object['properties'].get('icon')
            ptFtr.location=object['geometry']['coordinates']
            features.append(ptFtr)
        return features
import json
from urllib.request import urlopen
import os
import sys

class ServerReader:
    url=""
    def __init__(self,url):
        self.url=url
    def readPoints(self, file):
        fileUrl=self.url+file
        objects=json.load(urlopen(fileUrl));
        return objects['features']

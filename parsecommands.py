import os
import sys
import argparse
import json
class Disabler:
	modifiers = []
	def __init__(self, disable):
		if not disable:
			return
		for part in disable:
			self.modifiers.extend(part.strip('"').split())
	def disable(self, spec):
		return spec.get('disable') in self.modifiers
def mergeStrings(args):
	result = []
	stringParts = []
	for arg in args:
		if arg.startswith('"') or len(stringParts)>0 :
			stringParts.append(arg)
		else:
			result.append(arg)
		if arg.endswith('"'):
			result.append(' '.join(stringParts))
			stringParts = []
	return result

def parseArguments(args):
	with open("disableCategories.json",'r') as file:
		disableCategories = json.load(file);
	args = mergeStrings(args)
	parser = argparse.ArgumentParser(description='Exports tactical information from  the specified server to the DCS Ka-50 ABRIS system.')
	parser.add_argument('-path', nargs=1, default=os.getcwd(),help="Optional path to the ABRIS folder, use working directory if not specified")
	for category in disableCategories:
		parser.add_argument(f'-{category}',dest='disable', action='append_const', const=category)
	parser.add_argument('prog', nargs=1)
	parser.add_argument('specPath', nargs='+',help="Path to abrisspec.json file")
	return parser.parse_args(args)

class ConsoleCommands:
	disabler = None
	databasePath = ''
	def __init__(self, args):
		parsed = parseArguments(args)
		self.disabler = Disabler(parsed.disable)
		if isinstance(parsed.path,list):
			parsed.path = ' '.join(parsed.path)
		outPath = parsed.path.strip('"')
		self.databasePath = os.path.join(outPath, "Database\\")
		self.specPath = ' '.join(parsed.specPath).strip('"')
		

import os
import sys
import argparse
class Disabler:
	modifiers = []
	def __init__(self, disable):
		if not disable:
			return
		for part in disable:
			self.modifiers.extend(part.strip('"').split())
	def disable(spec):
		return spec.get('disable') in modifiers
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
	args = mergeStrings(args)
	parser = argparse.ArgumentParser(description='Exports tactical information from  the specified server to the DCS Ka-50 ABRIS system.')
	parser.add_argument('-path', nargs=1, default=os.getcwd(),help="Optional path to the ABRIS folder, use working directory if not specified")
	parser.add_argument('-disable', nargs='+',help="List of visualizations to disable")
	parser.add_argument('prog', nargs=1)
	parser.add_argument('specPath', nargs='+',help="Path to abrisspec.json file")
	return parser.parse_args(args)

class ConsoleCommands:
	disabler = None
	databasePath = ''
	def __init__(self, args):
		parsed = parseArguments(args)
		self.disabler = Disabler(parsed.disable)
		outPath = ' '.join(parsed.path).strip('"')
		self.databasePath = os.path.join(outPath, "Database\\")
		self.specPath = ' '.join(parsed.specPath).strip('"')
		

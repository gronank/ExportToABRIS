import unittest
import os
import json
from serverreader import ServerReader
from parsecommands import ConsoleCommands

class Test_test_url(unittest.TestCase):
    def test_load_file_url(self):
        cwd=os.getcwd()

        with open("Tests/testSpec.json",'r') as file:
            spec = json.load(file);
        reader = ServerReader(spec["serverUrl"])
        ftrs = reader.readPoints(spec["redUrl"])
        self.assertGreater(len(ftrs), 0)
    def test_loadArgs(self):
         cmd = ConsoleCommands(['app', '"aaa', 'bbbb"'])

if __name__ == '__main__':
    unittest.main()

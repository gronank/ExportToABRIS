import unittest
import os
from parsecommands import mergeStrings, parseArguments, ConsoleCommands


class Test_test_argymentParsing(unittest.TestCase):
    def runString(self,s):
        r = mergeStrings(s.split())
        self.assertEqual(s,' '.join(r))

    def test_mergeString(self):
        s =  'a b "aw q" wt'
        self.runString(s)

        self.runString('""')

        self.runString('"a "')
    def test_argumentParser(self):
        args = parseArguments('prog -disable jtac csar -path "some path" some other path'.split())
        self.assertTrue('jtac' in args.disable)
        self.assertTrue('csar' in args.disable)
        self.assertTrue('"some path"' in args.path)
        self.assertEqual('some other path', ' '.join(args.specPath))

    def test_argumentParserNoPath(self):
        args = parseArguments('prog some other path'.split())
        self.assertFalse(args.disable)
        self.assertTrue(os.getcwd() in args.path)
        self.assertEqual('some other path', ' '.join(args.specPath))

class Test_test_consoleCommands(unittest.TestCase):
    def test_simple(self):
        s = "prog my path"
        cmds = ConsoleCommands(s.split())
        self.assertTrue(len(cmds.disabler.modifiers)==0)
        self.assertEqual(os.path.join(os.getcwd(),"Database\\"), cmds.databasePath)
        self.assertEqual('my path', cmds.specPath)
    def test_quotePath(self):
        s = 'prog "my path"'
        cmds = ConsoleCommands(s.split())
        self.assertTrue(len(cmds.disabler.modifiers)==0)
        self.assertEqual(os.path.join(os.getcwd(),"Database\\"), cmds.databasePath)
        self.assertEqual('my path', cmds.specPath)
    def test_disable(self):
        s = 'prog my path -disable jtac sam '
        cmds = ConsoleCommands(s.split())
        self.assertTrue(len(cmds.disabler.modifiers)==2)
        self.assertTrue('jtac' in cmds.disabler.modifiers)
        self.assertTrue('sam' in cmds.disabler.modifiers)
        self.assertEqual(os.path.join(os.getcwd(),"Database\\"), cmds.databasePath)
        self.assertEqual('my path', cmds.specPath)
    def test_quotedisable(self):
        s = 'prog my path -disable "jtac sam" '
        cmds = ConsoleCommands(s.split())
        self.assertTrue(len(cmds.disabler.modifiers)==2)
        self.assertTrue('jtac' in cmds.disabler.modifiers)
        self.assertTrue('sam' in cmds.disabler.modifiers)
        self.assertEqual(os.path.join(os.getcwd(),"Database\\"), cmds.databasePath)
        self.assertEqual('my path', cmds.specPath)
    def test_quoteOutPath(self):
        s = 'prog my path -disable "jtac sam" -path "database path" '
        cmds = ConsoleCommands(s.split())
        self.assertTrue(len(cmds.disabler.modifiers)==2)
        self.assertTrue('jtac' in cmds.disabler.modifiers)
        self.assertTrue('sam' in cmds.disabler.modifiers)
        self.assertEqual(os.path.join("database path","Database\\"), cmds.databasePath)
        self.assertEqual('my path', cmds.specPath)
    def test_outPath(self):
        s = 'prog my path -disable "jtac sam" -path databasePath'
        cmds = ConsoleCommands(s.split())
        self.assertTrue(len(cmds.disabler.modifiers)==2)
        self.assertTrue('jtac' in cmds.disabler.modifiers)
        self.assertTrue('sam' in cmds.disabler.modifiers)
        self.assertEqual(os.path.join("databasePath","Database\\"), cmds.databasePath)
        self.assertEqual('my path', cmds.specPath)

if __name__ == '__main__':
    unittest.main()

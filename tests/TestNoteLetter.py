import sys
sys.path.append("C:\\Users\\ewatts3\\source\\repos\\ComPoYse\\compoyse\\midi\\Note_dependencies")
import unittest
from setuptools import find_packages
from NoteLetter import NoteLetter

class TestNoteLetter(unittest.TestCase):
    def test_find_midi_value__midi_value_is_100(self):
        test_nl = NoteLetter()
        test_mv = test_nl.find_midi_value('E', 7)
        self.assertEquals(test_mv, 100, "MIDI value is 100.")
        return
import unittest
from compoyse.midi.Beat_dependencies.NoteLetter import NoteLetter

class TestNoteLetter(unittest.TestCase):
    def test_find_midi_value__midi_value_is_100(self):
        test_nl = NoteLetter()
        test_mv = test_nl.find_midi_value('E', 7)
        self.assertEquals(test_mv, 100, "MIDI value is 100.")
        return
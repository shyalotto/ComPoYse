import unittest
from compoyse.midi.Beat_dependencies.NoteLetter import _NoteLetter

class TestNoteLetter(unittest.TestCase):
    def test_findMIDIValue_givenNoteAndOctave_shouldFindMIDIValue(self):
        test_nl = _NoteLetter('C', 0)
        test_mv = test_nl._find_midi_value('E', 7)
        self.assertEqual(test_mv, 100, "MIDI value is 100.")
        return
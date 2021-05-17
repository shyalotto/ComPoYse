import unittest
from compoyse.midi.Beat_dependencies.NoteLetter import _NoteLetter
from compoyse.midi.MIDIExceptions import ValueNotValidMIDIValue

class TestNoteLetter(unittest.TestCase):
    def setUp(self):
        self.test_note_letter = _NoteLetter('C', 0)
        return
    
    def test_findMIDIValue_givenNoteAndOctave_shouldFindMIDIValue(self):
        test_midi_value = self.test_note_letter._find_midi_value('E', 7)
        self.assertEqual(test_midi_value, 100, "MIDI value is 100.")
        return
    
    def test_newMIDIValueIsInMIDIValueRange_givenValidMIDIValue_shouldReturnTrue(self):
        self.assertTrue(self.test_note_letter._new_midi_value_is_in_midi_value_range('C', 4))
        return
    
    def test_newMIDIValueIsInMIDIValueRange_givenInvalidMIDIValueBelow127_shouldRaiseValueNotValidMIDIValueException(self):
        self.assertRaises(ValueNotValidMIDIValue, self.test_note_letter._new_midi_value_is_in_midi_value_range, 'C', -69)
        return
    
    def test_newMIDIValueIsInMIDIValueRange_givenInvalidMIDIValueAbove127_shouldRaiseValueNotValidMIDIValueException(self):
        self.assertRaises(ValueNotValidMIDIValue, self.test_note_letter._new_midi_value_is_in_midi_value_range, 'C', 420)
        return
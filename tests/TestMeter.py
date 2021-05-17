from compoyse.midi.MIDIExceptions import ValueNotValidRhythmicValue
import unittest
from compoyse.midi.Meter import _Meter

class TestMeter(unittest.TestCase):
    def setUp(self):
        self.test_meter = _Meter()
        self.test_meter._set_length_of_quarter_in_seconds(60)
        return
    
    def test_computeRhythmicValueLengthInSeconds_givenArrayOfRhythmicValues_shouldComputeCorrectLength(self):
        test_rhythm = ['quarter', 'quarter']
        test_length = self.test_meter._compute_rhythmic_value_length_in_seconds(test_rhythm)
        self.assertEqual(test_length, 2, 'Rhythm length in seconds is 2.')
        return
    
    def test_computeRhythmicValueLengthInSeconds_givenArrayOfRhythmicValuesWithTuplet_shouldComputeCorrectLength(self):
        test_rhythm = [3, 'quarter', 'quarter']
        test_length = self.test_meter._compute_rhythmic_value_length_in_seconds(test_rhythm)
        self.assertEqual(test_length, (2/3), 'Rhythm length in seconds is (2/3).')
        return
    
    def test_computeRhythmicValueLengthInSeconds_givenInvalidRhythmicValue_shouldRaiseValueNotValidRhythmicValueException(self):
        test_rhythm = ['thisisaninvalidrhythm']
        self.assertRaises(ValueNotValidRhythmicValue, self.test_meter._compute_rhythmic_value_length_in_seconds, test_rhythm)
        return
    
    def test_computeRhythmicValueLengthInSeconds_givenInvalidTupletRhythmicValue_shouldRaiseValueNotValidRhythmicValueException(self):
        test_rhythm = ['quarter', 3]
        self.assertRaises(ValueNotValidRhythmicValue, self.test_meter._compute_rhythmic_value_length_in_seconds, test_rhythm)
        return
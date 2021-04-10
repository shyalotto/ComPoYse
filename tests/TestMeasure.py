import sys
sys.path.append("C:\\Users\\ewatts3\\source\\repos\\ComPoYse\\compoyse\\midi")
import unittest
from setuptools import find_packages
from Note import Note
from Measure import Measure
from Meter import Meter
import pretty_midi

class TestMeasure(unittest.TestCase):
    def setUp(self):
        test_meter = Meter()
        test_meter.set_length_of_quarter_in_seconds(60)
        
        note_one = Note()
        note_one.set_letter('C')
        note_one.set_octave(4)
        note_one.set_rhythmic_value('quarter')
        note_one.set_velocity(100)
        note_one.get_midi_data(test_meter)

        note_two = Note()
        note_two.set_letter('D')
        note_two.set_octave(4)
        note_two.set_rhythmic_value('quarter')
        note_two.set_velocity(100)
        note_two.get_midi_data(test_meter)

        note_three = Note()
        note_three.set_letter('E')
        note_three.set_octave(4)
        note_three.set_rhythmic_value('quarter')
        note_three.set_velocity(100)
        note_three.get_midi_data(test_meter)
        
        self.test_measure = Measure()
        self.test_measure.add_note(note_one)
        self.test_measure.add_note(note_two)
        self.test_measure.add_note(note_three)
        return
        
    def test_get_length__length_is_correct(self):
        self.assertEquals(self.test_measure.get_length(), 3, 'Length is 3 seconds.')
        return
    
    def test_get_note_at_index__note_is_returned(self):
        self.assertEquals(self.test_measure.get_note_at_index(1).get_length_in_seconds(), 1, 'Notes length is 1.')
        return
    
    def test_add_note__note_is_added(self):
        test_meter = Meter()
        test_meter.set_length_of_quarter_in_seconds(60)
        note_four = Note()
        note_four.set_letter('E')
        note_four.set_octave(4)
        note_four.set_rhythmic_value('half')
        note_four.set_velocity(100)
        note_four.get_midi_data(test_meter)
        self.test_measure.add_note(note_four)
        self.assertEquals(self.test_measure.get_note_at_index(3).get_length_in_seconds(), 2, 'Notes length is 2.')
        return
    
    def test_get_midi_data__midi_data_is_returned(self):
        test_meter = Meter()
        test_meter.set_length_of_quarter_in_seconds(60)
        current_place_in_time = 0
        midi_instrument = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program('Cello'), name='voice')
        self.assertEquals(self.test_measure.get_midi_data(current_place_in_time, midi_instrument, test_meter).name, 'voice', 'Voice name is voice.')
        return
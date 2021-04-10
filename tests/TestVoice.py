import sys
sys.path.append("C:\\Users\\ewatts3\\source\\repos\\ComPoYse\\compoyse\\midi")
import unittest
from setuptools import find_packages
from Note import Note
from Measure import Measure
from Voice import Voice
from Meter import Meter
import pretty_midi

class TestVoice(unittest.TestCase):
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
        
        measure_one = Measure()
        measure_one.add_note(note_one)
        measure_one.add_note(note_two)
        measure_one.add_note(note_three)
        
        measure_two = Measure()
        measure_two.add_note(note_one)
        measure_two.add_note(note_two)
        measure_two.add_note(note_three)
        
        measure_three = Measure()
        measure_three.add_note(note_one)
        measure_three.add_note(note_two)
        measure_three.add_note(note_three)
        
        self.test_voice = Voice()
        self.test_voice.add_measure(measure_one)
        self.test_voice.add_measure(measure_two)
        self.test_voice.add_measure(measure_three)
        return
        
    def test_get_length__length_is_correct(self):
        self.assertEquals(self.test_voice.get_length(), 9, 'Length is 9 seconds.')
        return
    
    def test_get_measure_at_index__measure_is_returned(self):
        self.assertEquals(self.test_voice.get_measure_at_index(1).get_length(), 3, 'Measures length is 3.')
        return
    
    def test_add_measure__measure_is_added(self):
        test_meter = Meter()
        test_meter.set_length_of_quarter_in_seconds(60)
        
        note_four = Note()
        note_four.set_letter('E')
        note_four.set_octave(4)
        note_four.set_rhythmic_value('quarter')
        note_four.set_velocity(100)
        note_four.get_midi_data(test_meter)
        
        note_five = Note()
        note_five.set_letter('E')
        note_five.set_octave(4)
        note_five.set_rhythmic_value('quarter')
        note_five.set_velocity(100)
        note_five.get_midi_data(test_meter)

        measure_four = Measure()
        measure_four.add_note(note_four)
        measure_four.add_note(note_five)
        
        self.test_voice.add_measure(measure_four)
        
        self.assertEquals(self.test_voice.get_measure_at_index(3).get_length(), 2, 'Measures length is 2.')
        return
    
    def test_get_midi_data__midi_data_is_returned(self):
        test_meter = Meter()
        test_meter.set_length_of_quarter_in_seconds(60)
        self.assertEquals(self.test_voice.get_midi_data(test_meter).name, 'voice', 'Voices name is voice.')
        return
    
    def test_set_name__name_is_set(self):
        self.test_voice.set_name('Trombone')
        self.assertEquals(self.test_voice.get_name(), 'Trombone', 'Name is trombone.')
        return
import sys
sys.path.append("C:\\Users\\ewatts3\\source\\repos\\ComPoYse\\compoyse\\midi")
import unittest
from setuptools import find_packages
from Note import Note
from Measure import Measure
from Voice import Voice
from Composition import Composition
from Meter import Meter
import pretty_midi
import os.path
from os import path

class TestComposition(unittest.TestCase):
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
        
        
        voice_one = Voice()
        voice_one.add_measure(measure_one)
        voice_one.add_measure(measure_two)
        voice_one.add_measure(measure_three)
        
        voice_two = Voice()
        voice_two.add_measure(measure_one)
        voice_two.add_measure(measure_two)
        voice_two.add_measure(measure_three)
        
        voice_three = Voice()
        voice_three.add_measure(measure_one)
        voice_three.add_measure(measure_two)
        voice_three.add_measure(measure_three)
        
        
        self.test_composition = Composition()
        self.test_composition.add_voice(voice_one)
        self.test_composition.add_voice(voice_two)
        self.test_composition.add_voice(voice_three)
        return
    
    def test_get_length__length_is_correct(self):
        self.assertEquals(self.test_composition.get_length(), 9, 'Length is 9.')
        return
    
    def test_get_voice_at_index__voice_is_returned(self):
        self.assertEquals(self.test_composition.get_voice_at_index(1).get_length(), 9, 'Length is 9.')
        return
    
    def test_add_voice__voice_is_added(self):
        test_meter = Meter()
        test_meter.set_length_of_quarter_in_seconds(60)
        
        note_four = Note()
        note_four.set_letter('E')
        note_four.set_octave(4)
        note_four.set_rhythmic_value('quarter')
        note_four.set_velocity(100)
        note_four.get_midi_data(test_meter)
        
        measure_four = Measure()
        measure_four.add_note(note_four)
        
        voice_four = Voice()
        voice_four.add_measure(measure_four)
        
        self.test_composition.add_voice(voice_four)
        self.assertEquals(self.test_composition.get_voice_at_index(3).get_length(), 1, 'Length is 1.')
        return
    
    def test_write_midi_data__midi_data_is_written(self):
        self.test_composition.set_quarter_note_bpm(60)
        self.test_composition.write_midi_data()
        self.assertTrue(os.path.exists("compoyse_composition.mid"))
        os.remove("compoyse_composition.mid")
        return
        
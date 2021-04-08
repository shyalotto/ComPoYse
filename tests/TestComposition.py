import sys
sys.path.append("C:\\Users\\ewatts3\\source\\repos\\ComPoYse\\compoyse\\midi")
import unittest
from setuptools import find_packages
from Note import Note
from Voice import Voice
from Composition import Composition
import pretty_midi
import os.path
from os import path

class TestComposition(unittest.TestCase):
    def setUp(self):
        voice_one = Voice()
        voice_two = Voice()
        voice_three = Voice()

        note_one = Note()
        note_one.set_letter('C')
        note_one.set_octave(4)
        note_one.set_length(5)
        note_one.set_velocity(100)

        note_two = Note()
        note_two.set_letter('D')
        note_two.set_octave(4)
        note_two.set_length(5)
        note_two.set_velocity(100)

        note_three = Note()
        note_three.set_letter('E')
        note_three.set_octave(4)
        note_three.set_length(10)
        note_three.set_velocity(100)

        voice_one.add_note(note_one)
        voice_two.add_note(note_two)
        voice_three.add_note(note_three)
        
        self.test_composition = Composition()
        self.test_composition.add_voice(voice_one)
        self.test_composition.add_voice(voice_two)
        self.test_composition.add_voice(voice_three)
        return
    
    def test_get_length__length_is_correct(self):
        self.assertEquals(self.test_composition.get_length(), 10, 'Length is 10.')
        return
    
    def test_get_voice_at_index__voice_is_returned(self):
        self.assertEquals(self.test_composition.get_voice_at_index(1).get_length(), 5, 'Length is 5.')
        return
    
    def test_add_voice__voice_is_added(self):
        note_four = Note()
        note_four.set_letter('E')
        note_four.set_octave(4)
        note_four.set_length(20)
        note_four.set_velocity(100)
        voice_four = Voice()
        voice_four.add_note(note_four)
        self.test_composition.add_voice(voice_four)
        self.assertEquals(self.test_composition.get_voice_at_index(3).get_length(), 20, 'Length is 20.')
        return
    
    def test_write_midi_data__midi_data_is_written(self):
        self.test_composition.write_midi_data()
        self.assertTrue(os.path.exists("compoyse_composition.mid"))
        os.remove("compoyse_composition.mid")
        return
        
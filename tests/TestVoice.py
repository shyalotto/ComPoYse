import sys
sys.path.append("C:\\Users\\ewatts3\\source\\repos\\ComPoYse\\compoyse\\midi")
import unittest
from setuptools import find_packages
from Note import Note
from Voice import Voice
import pretty_midi

class TestVoice(unittest.TestCase):
    def setUp(self):
        self.test_voice = Voice()
        
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
        
        self.test_voice.add_note(note_one)
        self.test_voice.add_note(note_two)
        self.test_voice.add_note(note_three)
        return
        
    def test_get_length__length_is_correct(self):
        self.assertEquals(self.test_voice.get_length(), 20, 'Length is 20 seconds.')
        return
    
    def test_get_note_at_index__note_is_returned(self):
        self.assertEquals(self.test_voice.get_note_at_index(1).get_length(), 5, 'Notes length is 5.')
        return
    
    def test_add_note__note_is_added(self):
        note_four = Note()
        note_four.set_letter('E')
        note_four.set_octave(4)
        note_four.set_length(20)
        note_four.set_velocity(100)
        self.test_voice.add_note(note_four)
        self.assertEquals(self.test_voice.get_note_at_index(3).get_length(), 20, 'Notes length is 20.')
        return
    
    def test_get_midi_data__midi_data_is_returned(self):
        self.assertEquals(self.test_voice.get_midi_data().name, 'instrument', 'Instrument name is Cello.')
        return
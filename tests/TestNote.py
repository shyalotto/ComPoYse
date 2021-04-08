import sys
sys.path.append("C:\\Users\\ewatts3\\source\\repos\\ComPoYse\\compoyse")
sys.path.append("C:\\Users\\ewatts3\\source\\repos\\ComPoYse\\compoyse\\midi")
import unittest
from setuptools import find_packages
from Exceptions import ValueNotValidMIDIValue
from Note import Note
import pretty_midi

class TestNote(unittest.TestCase):
    def test___init___no_parameters__defaults_are_set(self):
        test_note = Note()
        self.assertEquals(test_note.get_note_data(), [0,'C#', 0, 0, 0, 0], "Notes values are the default parameters.")
        return
    
    def test_set_note__five_parameters__note_is_made(self):
        test_note = Note()
        test_note.set_note(100, 'C', 5, 0, 10)
        self.assertEquals(test_note.get_note_data(), [100, 'C', 5, 0, 10, 10], "Note is a C5, lasting ten seconds, at velocity level 100.")
        return
    
    def test_set_velocity__velocity_is_set(self):
        test_note = Note()
        test_note.set_velocity(100)
        self.assertEquals(test_note.get_velocity(), 100, "Velocity is 100.")
        return
    
    def test_set_letter__letter_is_set(self):
        test_note = Note()
        test_note.set_letter('C')
        self.assertEquals(test_note.get_letter(), 'C', "Note is D.")
        return
    
    def test_set_octave__octave_is_set(self):
        test_note = Note()
        test_note.set_octave(5)
        self.assertEquals(test_note.get_octave(), 5, "Octave is 5.")
        return
    
    def test_set_midi_value__midi_value_is_set(self):
        test_note = Note()
        test_note.set_midi_value(100)
        self.assertEquals(test_note.get_midi_value(), 100, "Midi value is 100.")
        return
        
    def test_set_start__start_is_set(self):
        test_note = Note()
        test_note.set_start(100)
        self.assertEquals(test_note.get_start(), 100, "Note starts at 100.")
        return
    
    def test_set_length__length_is_set(self):
        test_note = Note()
        test_note.set_length(10)
        self.assertEquals(test_note.get_length(), 10, "Note is 10 seconds long.")
        return
    
    def test_get_midi_data__midi_data_is_returned(self):
        test_note = Note(100, 'C', 5, 0, 10)
        test_note_midi_data = test_note.get_midi_data()
        self.assertEquals(test_note_midi_data.get_duration(), 10, "MIDI note calls pretty_midi function and is 10 seconds long.")
        return
    
    def test_alter_velocity__increase_by_ten__velocity_is_increased_by_ten(self):
        test_note = Note(velocity=100)
        test_note.alter_velocity(10)
        self.assertEquals(test_note.get_velocity(), 110, "Velocity is 110.")
        return
    
    def test_alter_velocity__decrease_by_ten__velocity_is_decreased_by_ten(self):
        test_note = Note(velocity=100)
        test_note.alter_velocity(-10)
        self.assertEquals(test_note.get_velocity(), 90, "Velocity is -10.")
        return
    
    def test_alter_velocity__exceed_midi_value_range_above__value_not_valid_midi_value_exception_raised(self):
        test_note = Note(velocity=100)
        self.assertRaises(ValueNotValidMIDIValue, test_note.alter_velocity, 100)
        return
    
    def test_alter_velocity__exceed_midi_value_range_below__value_not_valid_midi_value_exception_raised(self):
        test_note = Note(velocity=100)
        self.assertRaises(ValueNotValidMIDIValue, test_note.alter_velocity, -200)
        return
    
    def test_alter_octave__increase_by_one__octave_is_increased_by_one(self):
        test_note = Note(octave=1)
        test_note.alter_octave(1)
        self.assertEquals(test_note.get_octave(), 2, "Octave is 2.")
        return
    
    def test_alter_velocity__decrease_by_one__octave_is_decreased_by_one(self):
        test_note = Note(octave=1)
        test_note.alter_octave(-1)
        self.assertEquals(test_note.get_octave(), 0, "Octave is 0.")
        return
    
    def test_alter_octave__exceed_midi_value_range_above__value_not_valid_midi_value_exception_raised(self):
        test_note = Note(octave=1)
        self.assertRaises(ValueNotValidMIDIValue, test_note.alter_octave, 100)
        return
    
    def test_alter_octave__exceed_midi_value_range_below__value_not_valid_midi_value_exception_raised(self):
        test_note = Note(octave=1)
        self.assertRaises(ValueNotValidMIDIValue, test_note.alter_octave, -100)
        return
    
    def test_alter_start__increase_by_ten__start_is_increased_by_ten(self):
        test_note = Note(start=0)
        test_note.alter_start(10)
        self.assertEquals(test_note.get_start(), 10, "Start is at 10.")
        return
    
    def test_alter_start__decrease_by_ten__start_is_decreased_by_ten(self):
        test_note = Note(start=10)
        test_note.alter_start(-10)
        self.assertEquals(test_note.get_start(), 0, "Start is at 0.")
        return
    
    def test_alter_length__increase_by_ten__length_is_increased_by_ten(self):
        test_note = Note(length=10)
        test_note.alter_length(10)
        self.assertEquals(test_note.get_length(), 20, "Length is 20.")
        return
    
    def test_alter_length__decrease_by_ten__start_is_decreased_by_ten(self):
        test_note = Note(length=20)
        test_note.alter_length(-10)
        self.assertEquals(test_note.get_length(), 10, "Length is 10.")
        return
    
    def test_augment_length__increase_by_factor_of_two__length_is_twice_as_long(self):
        test_note = Note(length=10)
        test_note.augment_length(2)
        self.assertEquals(test_note.get_length(), 20, "Length is 20.")
        return    
    
    def test_diminish_length__decrease_by_factor_of_two__length_is_half_as_long(self):
        test_note = Note(length=10)
        test_note.diminish_length(2)
        self.assertEquals(test_note.get_length(), 5, "Length is 5.")
        return    
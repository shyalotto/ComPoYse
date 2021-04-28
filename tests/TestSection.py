import unittest
import pretty_midi
import os.path
from os import path
from compoyse.midi.Note import Note
from compoyse.midi.Measure import Measure
from compoyse.midi.Voice import Voice
from compoyse.midi.Section import Section
from compoyse.midi.Meter import _Meter

class TestSection(unittest.TestCase):
    def setUp(self):
        test_meter =  _Meter()
        test_meter._set_length_of_quarter_in_seconds(60)
        
        note_one = Note()
        note_one.set_letter('C')
        note_one.set_octave(4)
        note_one.set_rhythmic_value(['quarter'])
        note_one._set_start_and_end(0, test_meter)
        note_one.set_velocity(100)

        note_two = Note()
        note_two.set_letter('D')
        note_two.set_octave(4)
        note_two.set_rhythmic_value(['quarter'])
        note_two._set_start_and_end(1, test_meter)
        note_two.set_velocity(100)

        note_three = Note()
        note_three.set_letter('E')
        note_three.set_octave(4)
        note_three.set_rhythmic_value(['quarter'])
        note_three._set_start_and_end(2, test_meter)
        note_three.set_velocity(100)
        
        measure_one = Measure()
        measure_one.add_beat(note_one)
        measure_one.add_beat(note_two)
        measure_one.add_beat(note_three)
        
        note_four = Note()
        note_four.set_letter('C')
        note_four.set_octave(4)
        note_four.set_rhythmic_value(['quarter'])
        note_four._set_start_and_end(3, test_meter)
        note_four.set_velocity(100)

        note_five = Note()
        note_five.set_letter('D')
        note_five.set_octave(4)
        note_five.set_rhythmic_value(['quarter'])
        note_five._set_start_and_end(4, test_meter)
        note_five.set_velocity(100)

        note_six = Note()
        note_six.set_letter('E')
        note_six.set_octave(4)
        note_six.set_rhythmic_value(['quarter'])
        note_six._set_start_and_end(5, test_meter)
        note_six.set_velocity(100)
        
        measure_two = Measure()
        measure_two.add_beat(note_four)
        measure_two.add_beat(note_five)
        measure_two.add_beat(note_six)
        
        note_seven = Note()
        note_seven.set_letter('C')
        note_seven.set_octave(4)
        note_seven.set_rhythmic_value(['quarter'])
        note_seven._set_start_and_end(6, test_meter)
        note_seven.set_velocity(100)

        note_eight = Note()
        note_eight.set_letter('D')
        note_eight.set_octave(4)
        note_eight.set_rhythmic_value(['quarter'])
        note_eight._set_start_and_end(6, test_meter)
        note_eight.set_velocity(100)

        note_nine = Note()
        note_nine.set_letter('E')
        note_nine.set_octave(4)
        note_nine.set_rhythmic_value(['quarter'])
        note_nine._set_start_and_end(7, test_meter)
        note_nine.set_velocity(100)
        
        measure_three = Measure()
        measure_three.add_beat(note_one)
        measure_three.add_beat(note_eight)
        measure_three.add_beat(note_nine)
        
        
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
        
        
        self.test_section = Section()
        self.test_section.add_voice(voice_one)
        self.test_section.add_voice(voice_two)
        self.test_section.add_voice(voice_three)
        return
    
    def test_getLength_whenCalled_shouldReturnLength(self):
        self.assertEquals(self.test_section.get_length(), 9, 'Length is 9.')
        return
    
    def test_getVoiceAtIndex_givenIndex_shouldReturnVoice(self):
        self.assertEquals(self.test_section.get_voice_at_index(1).get_length(), 9, 'Length is 9.')
        return
    
    def test_getNumberOfVoices_whenCalled_shouldReturnNumberOfVoices(self):
        self.assertEquals(self.test_section.get_number_of_voices(), 3, 'There are 3 voices.')
        return
    
    def test_addVoice_givenVoice_shouldAddVoice(self):
        test_meter =  _Meter()
        test_meter._set_length_of_quarter_in_seconds(60)
        
        note_four = Note()
        note_four.set_letter('E')
        note_four.set_octave(4)
        note_four.set_rhythmic_value(['quarter'])
        note_four._set_start_and_end(0, test_meter)
        note_four.set_velocity(100)
        
        measure_four = Measure()
        measure_four.add_beat(note_four)
        
        voice_four = Voice()
        voice_four.add_measure(measure_four)
        
        self.test_section.add_voice(voice_four)
        self.assertEquals(self.test_section.get_voice_at_index(3).get_length(), 1, 'Length is 1.')
        return
    
    def test_setIdentifier_givenIdentifier_identifierIsSet(self):
        self.test_section.set_identifier('A')
        self.assertEquals(self.test_section.get_identifier(), 'A', 'Identifier is A.')
        return
    
    def test_getMIDIData_whenCalled_shouldReturnMIDIData(self):
        self.test_section.set_quarter_note_bpm(60)
        self.assertEquals(len(self.test_section._get_midi_data(0)), 3, 'There are 3 midi instruments.')
        return
        
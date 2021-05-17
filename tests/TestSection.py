from tests.TestMIDI import TestMIDI
from compoyse.midi.Note import Note
from compoyse.midi.Measure import Measure
from compoyse.midi.Voice import Voice
from compoyse.midi.Section import Section
from compoyse.midi.Meter import _Meter
import os

class TestSection(TestMIDI):
    def test_getVoiceAtIndex_givenIndex_shouldReturnVoice(self):
        self.assertEqual(self.test_section.get_voice_at_index(1).get_number_of_measures(), 3, 'Number of measures is 3.')
        return
    
    def test_getNumberOfVoices_whenCalled_shouldReturnNumberOfVoices(self):
        self.assertEqual(self.test_section.get_number_of_voices(), 3, 'There are 3 voices.')
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
        self.assertEqual(self.test_section.get_voice_at_index(3).get_number_of_measures(), 1, 'Number of measures is 1.')
        return
    
    def test_setIdentifier_givenIdentifier_identifierIsSet(self):
        self.test_section.set_identifier('A')
        self.assertEqual(self.test_section.get_identifier(), 'A', 'Identifier is A.')
        return
    
    def test_getMIDIData_whenCalled_shouldReturnMIDIData(self):
        self.test_section.set_quarter_note_bpm(60)
        self.assertEqual(len(self.test_section._get_midi_data(0)), 3, 'There are 3 midi instruments.')
        return
        
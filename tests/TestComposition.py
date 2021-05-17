from tests.TestMIDI import TestMIDI
from compoyse.midi.Note import Note
from compoyse.midi.Measure import Measure
from compoyse.midi.Voice import Voice
from compoyse.midi.Section import Section
from compoyse.midi.Composition import Composition
from compoyse.midi.Meter import _Meter
import os.path

class TestComposition(TestMIDI):
    def test_getSectionAtIndex_givenIndex_shouldReturnSection(self):
        self.assertEqual(self.test_composition.get_section_at_index(1).get_number_of_voices(), 3, 'Number of voices is 3.')
        return
    
    def test_getNumberOfSections_whenCalled_shouldReturnNumberOfSections(self):
        self.assertEqual(self.test_composition.get_number_of_sections(), 3, 'There are 3 sections.')
        return
        
    def test_addSection_givenSection_shouldAddSection(self):
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
        
        section_four = Section()
        section_four.add_voice(voice_four)
        
        self.test_composition.add_section(section_four)
        self.assertEqual(self.test_composition.get_section_at_index(3).get_voice_at_index(0).get_measure_at_index(0).get_beat_at_index(0).get_letter(),
                          'E', 'Note is E.')
        return
    
    def test_getLength_givenCompositionHasSections_shouldReturnLength(self):
        test_length = self.test_composition.get_length()
        self.assertEqual(test_length, 27, 'Compositions length is 27.')
    
    def test_writeMIDIData_whenCalled_writesMIDIData(self):
        self.test_composition.write_midi_data()
        self.assertTrue(os.path.exists("compoyse_composition.mid"))
        os.remove("compoyse_composition.mid")
        return
        
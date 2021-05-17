from tests.TestMIDI import TestMIDI
from compoyse.midi.Note import Note
from compoyse.midi.Measure import Measure
from compoyse.midi.Voice import Voice
from compoyse.midi.Meter import _Meter

class TestVoice(TestMIDI):
    def test_getMeasureAtIndex_givenIndex_shouldReturnMeasure(self):
        self.assertEqual(self.test_voice.get_measure_at_index(1).get_number_of_beats(), 3, 'Number of beats is 3.')
        return
    
    def test_getNumberOfMeasures_whenCalled_shouldReturnNumberOfMeasures(self):
        self.assertEqual(self.test_voice.get_number_of_measures(), 3, 'There are 3 measures.')
        return
    
    def test_addMeasure_givenMeasure_shouldAddMeasure(self):
        test_meter =  _Meter()
        test_meter._set_length_of_quarter_in_seconds(60)
        
        note_ten = Note()
        note_ten.set_letter('E')
        note_ten.set_octave(4)
        note_ten.set_rhythmic_value(['quarter'])
        note_ten._set_start_and_end(9, test_meter)
        note_ten.set_velocity(100)
        
        note_eleven = Note()
        note_eleven.set_letter('E')
        note_eleven.set_octave(4)
        note_eleven.set_rhythmic_value(['quarter'])
        note_eleven._set_start_and_end(10, test_meter)
        note_eleven.set_velocity(100)

        measure_four = Measure()
        measure_four.add_beat(note_ten)
        measure_four.add_beat(note_eleven)
        
        self.test_voice.add_measure(measure_four)
        
        self.assertEqual(self.test_voice.get_measure_at_index(3).get_number_of_beats(), 2, 'Number of beats is 2.')
        return
    
    def test_getMIDIData_whenCalled_shouldReturnMIDIData(self):
        test_meter =  _Meter()
        test_meter._set_length_of_quarter_in_seconds(60)
        self.assertEqual(self.test_voice._get_midi_data(test_meter, 0).name, 'voice', 'Voices name is voice.')
        return
    
    def test_setName_givenName_shouldSetName(self):
        self.test_voice.set_name('Trombone')
        self.assertEqual(self.test_voice.get_name(), 'Trombone', 'Name is trombone.')
        return
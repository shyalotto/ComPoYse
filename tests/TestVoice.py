import unittest
import pretty_midi
from compoyse.midi.Note import Note
from compoyse.midi.Measure import Measure
from compoyse.midi.Voice import Voice
from compoyse.midi.Meter import _Meter

class TestVoice(unittest.TestCase):
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
        
        self.test_voice = Voice()
        self.test_voice.add_measure(measure_one)
        self.test_voice.add_measure(measure_two)
        self.test_voice.add_measure(measure_three)
        return
    
    def test_getMeasureAtIndex_givenIndex_shouldReturnMeasure(self):
        self.assertEquals(self.test_voice.get_measure_at_index(1).get_number_of_beats(), 3, 'Number of beats is 3.')
        return
    
    def test_getNumberOfMeasures_whenCalled_shouldReturnNumberOfMeasures(self):
        self.assertEquals(self.test_voice.get_number_of_measures(), 3, 'There are 3 measures.')
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
        
        self.assertEquals(self.test_voice.get_measure_at_index(3).get_number_of_beats(), 2, 'Number of beats is 2.')
        return
    
    def test_getMIDIData_whenCalled_shouldReturnMIDIData(self):
        test_meter =  _Meter()
        test_meter._set_length_of_quarter_in_seconds(60)
        self.assertEquals(self.test_voice._get_midi_data(test_meter, 0).name, 'voice', 'Voices name is voice.')
        return
    
    def test_setName_givenName_shouldSetName(self):
        self.test_voice.set_name('Trombone')
        self.assertEquals(self.test_voice.get_name(), 'Trombone', 'Name is trombone.')
        return
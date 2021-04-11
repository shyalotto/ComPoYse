import unittest
import pretty_midi
from compoyse.midi.Note import Note
from compoyse.midi.Measure import Measure
from compoyse.midi.Meter import Meter

class TestMeasure(unittest.TestCase):
    def setUp(self):
        test_meter = Meter()
        test_meter.set_length_of_quarter_in_seconds(60)
        
        note_one = Note()
        note_one.set_letter('C')
        note_one.set_octave(4)
        note_one.set_rhythmic_value(['quarter'])
        note_one.set_start_and_end(0, test_meter)
        note_one.set_velocity(100)

        note_two = Note()
        note_two.set_letter('D')
        note_two.set_octave(4)
        note_two.set_rhythmic_value(['quarter'])
        note_two.set_start_and_end(1, test_meter)
        note_two.set_velocity(100)

        note_three = Note()
        note_three.set_letter('E')
        note_three.set_octave(4)
        note_three.set_rhythmic_value(['quarter'])
        note_three.set_start_and_end(2, test_meter)
        note_three.set_velocity(100)
        
        self.test_measure = Measure()
        self.test_measure.add_beat(note_one)
        self.test_measure.add_beat(note_two)
        self.test_measure.add_beat(note_three)
        return
        
    def test_get_length__length_is_correct(self):
        self.assertEquals(self.test_measure.get_length(), 3, 'Length is 3 seconds.')
        return
    
    def test_get_beat_at_index__beat_is_returned(self):
        self.assertEquals(self.test_measure.get_beat_at_index(1).get_length_in_seconds(), 1, 'Beats length is 1.')
        return
    
    def test_add_beat__beat_is_added(self):
        test_meter = Meter()
        test_meter.set_length_of_quarter_in_seconds(60)
        note_four = Note()
        note_four.set_letter('E')
        note_four.set_octave(4)
        note_four.set_rhythmic_value(['half'])
        note_four.set_start_and_end(0, test_meter)
        note_four.set_velocity(100)
        self.test_measure.add_beat(note_four)
        self.assertEquals(self.test_measure.get_beat_at_index(3).get_length_in_seconds(), 2, 'Beats length is 2.')
        return
    
    def test_get_midi_data__midi_data_is_returned(self):
        test_meter = Meter()
        test_meter.set_length_of_quarter_in_seconds(60)
        current_place_in_time = 0
        midi_instrument = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program('Cello'), name='voice')
        self.assertEquals(self.test_measure.get_midi_data(current_place_in_time, midi_instrument, test_meter).name, 'voice', 'Voice name is voice.')
        return
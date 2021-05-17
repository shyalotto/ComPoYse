from tests.TestMIDI import TestMIDI
import pretty_midi
from compoyse.midi.Rest import Rest

class TestMeasure(TestMIDI):
    def test_getBeatAtIndex_givenIndex_shouldReturnBeat(self):
        self.assertEqual(self.test_measure.get_beat_at_index(1).get_rhythmic_value(), ['quarter'], 'Beats rhythmic value is [\'quarter\'].')
        return
    
    def test_getNumberOfBeats_whenCalled_shouldReturnNumberOfNotes(self):
        self.assertEqual(self.test_measure.get_number_of_beats(), 3, 'There are 3 notes.')
        return
    
    def test_addBeat_givenNote_shouldAddNote(self):
        self.test_measure.add_beat(self.note_to_add)
        self.assertEqual(self.test_measure.get_beat_at_index(3)._get_length_in_seconds(), 1, 'Beats length is 1.')
        return
    
    def test_addBeat_givenRest_shouldAddRest(self):
        rest_to_add = Rest()
        rest_to_add.set_rhythmic_value(['half'])
        rest_to_add._set_start_and_end(0, self.test_meter)
        self.test_measure.add_beat(rest_to_add)
        self.assertEqual(self.test_measure.get_beat_at_index(3)._get_length_in_seconds(), 2, 'Rests length is 2.')
        return
    
    def test_getMIDIData_whenCalled_shouldReturnMIDIData(self):
        test_current_place_in_time = 0
        midi_instrument = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program('Cello'), name='voice')
        self.assertEqual(self.test_measure._get_midi_data(test_current_place_in_time, midi_instrument, self.test_meter).name, 'voice', 'Voice name is voice.')
        return
    
    def test_getLength_whenCalled_shouldReturnLength(self):
        self.assertEqual(self.test_measure._get_length(self.test_meter), 3, 'Measures length is 3.')
from tests.TestMIDI import TestMIDI
import pretty_midi
from compoyse.midi.Note import Note
from compoyse.midi.Rest import Rest
from compoyse.midi.Measure import Measure
from compoyse.midi.Meter import _Meter

class TestMeasure(TestMIDI):
    def test_getBeatAtIndex_givenIndex_shouldReturnBeat(self):
        self.assertEqual(self.test_measure.get_beat_at_index(1).get_rhythmic_value(), ['quarter'], 'Beats rhythmic value is [\'quarter\'].')
        return
    
    def test_getNumberOfBeats_whenCalled_shouldReturnNumberOfNotes(self):
        self.assertEqual(self.test_measure.get_number_of_beats(), 3, 'There are 3 notes.')
        return
    
    def test_addBeat_givenNote_shouldAddNote(self):
        test_meter =  _Meter()
        test_meter._set_length_of_quarter_in_seconds(60)
        note_four = Note()
        note_four.set_letter('E')
        note_four.set_octave(4)
        note_four.set_rhythmic_value(['half'])
        note_four._set_start_and_end(0, test_meter)
        note_four.set_velocity(100)
        self.test_measure.add_beat(note_four)
        self.assertEqual(self.test_measure.get_beat_at_index(3)._get_length_in_seconds(), 2, 'Beats length is 2.')
        return
    
    def test_addBeat_givenRest_shouldAddRest(self):
        test_meter =  _Meter()
        test_meter._set_length_of_quarter_in_seconds(60)
        rest_four = Rest()
        rest_four.set_rhythmic_value(['half'])
        rest_four._set_start_and_end(0, test_meter)
        self.test_measure.add_beat(rest_four)
        self.assertEqual(self.test_measure.get_beat_at_index(3)._get_length_in_seconds(), 2, 'Rests length is 2.')
        return
    
    def test_getMIDIData_whenCalled_returnsMIDIData(self):
        test_meter =  _Meter()
        test_meter._set_length_of_quarter_in_seconds(60)
        current_place_in_time = 0
        midi_instrument = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program('Cello'), name='voice')
        self.assertEqual(self.test_measure._get_midi_data(current_place_in_time, midi_instrument, test_meter).name, 'voice', 'Voice name is voice.')
        return
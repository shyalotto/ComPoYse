import sys
sys.path.append("C:\\Users\\ewatts3\\source\\repos\\ComPoYse\\compoyse\\midi")
import pretty_midi
from Measure import Measure

class Voice:
    def __init__(self):
        self.measures = []
        return

    def get_length(self):
        length = 0
        for i in range(0, len(self.measures)):
            length = length + self.measures[i].get_length()
        return length

    def get_measure_at_index(self, index):
        return self.measure[index]

    def add_measure(self, measure):
        self.measures.append(measure)
        return

    def get_midi_data(self):
        current_place_in_time = 0
        midi_instrument = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program('Cello'), name='instrument')
        for i in range(0, len(self.measures)):
            current_measure = self.measures[i]
            midi_instrument = self.append_notes_in_measure_to_midi_instrument(current_measure, current_place_in_time, midi_instrument)
            current_place_in_time = current_place_in_time + current_measure.get_length()
        return midi_instrument
    
    def append_notes_in_measure_to_midi_instrument(self, current_measure, current_place_in_time, midi_instrument):
        midi_instrument = current_measure.get_midi_data(current_place_in_time, midi_instrument)
        return midi_instrument
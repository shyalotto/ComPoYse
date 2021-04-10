import sys
sys.path.append("C:\\Users\\ewatts3\\source\\repos\\ComPoYse\\compoyse\\midi")
import pretty_midi
from Measure import Measure

class Voice:
    def __init__(self):
        self.measures = []
        self.name = 'voice'
        return
    
    def get_name(self):
        return self.name

    def get_length(self):
        length = 0
        for i in range(0, len(self.measures)):
            length = length + self.measures[i].get_length()
        return length

    def get_measure_at_index(self, index):
        return self.measures[index]
    
    def set_name(self, name):
        self.name = name
        return

    def add_measure(self, measure):
        self.measures.append(measure)
        return

    def get_midi_data(self, meter):
        current_place_in_time = 0
        midi_instrument = self.create_midi_instrument()
        for i in range(0, len(self.measures)):
            current_measure = self.get_measure_at_index(i)
            midi_instrument = self.append_notes_in_measure_to_midi_instrument(current_measure, 
                                                                              current_place_in_time, 
                                                                              midi_instrument, 
                                                                              meter)
            current_place_in_time = current_place_in_time + current_measure.get_length()
        return midi_instrument
    
    def create_midi_instrument(self):
        return pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program('Cello'), name=self.name)
    
    def append_notes_in_measure_to_midi_instrument(self, 
                                                   current_measure, 
                                                   current_place_in_time, 
                                                   midi_instrument, 
                                                   meter):
        midi_instrument = current_measure.get_midi_data(current_place_in_time, 
                                                        midi_instrument, 
                                                        eter)
        return midi_instrument
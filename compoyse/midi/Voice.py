import pretty_midi
from compoyse.midi.Measure import Measure

class Voice:
    def __init__(self):
        self.measures = []
        self.name = 'voice'
        return
    
    def get_name(self):
        return self.name

    def get_measure_at_index(self, index):
        return self.measures[index]
    
    def get_number_of_measures(self):
        return len(self.measures)
    
    def set_name(self, name):
        self.name = name
        return

    def add_measure(self, measure):
        self.measures.append(measure)
        return

    def _get_midi_data(self, meter, starting_place):
        current_place_in_time = starting_place
        midi_instrument = self._create_midi_instrument()
        for i in range(0, len(self.measures)):
            current_measure = self.get_measure_at_index(i)
            midi_instrument = self._append_notes_in_measure_to_midi_instrument(current_measure, 
                                                                              current_place_in_time, 
                                                                              midi_instrument, 
                                                                              meter)
            current_place_in_time = current_place_in_time + current_measure._get_length()
        self.length = current_place_in_time
        return midi_instrument
    
    def _create_midi_instrument(self):
        return pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program('Cello'), name=self.name)
    
    def _append_notes_in_measure_to_midi_instrument(self, 
                                                   current_measure, 
                                                   current_place_in_time, 
                                                   midi_instrument, 
                                                   meter):
        midi_instrument = current_measure._get_midi_data(current_place_in_time, 
                                                        midi_instrument, 
                                                        meter)
        return midi_instrument
    
    def _get_length(self):
        return self.length
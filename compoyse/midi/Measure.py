class Measure:
    def __init__(self):
        self.beats = []
        return
    
    def get_beat_at_index(self, index):
        return self.beats[index]
    
    def get_number_of_beats(self):
        return len(self.beats)

    def add_beat(self, note):
        self.beats.append(note)
        return
    
    def _get_midi_data(self, current_place_in_time, midi_instrument, meter):
        current_place_in_time = current_place_in_time
        for i in range(0, len(self.beats)):
            current_beat = self.get_beat_at_index(i)
            current_beat._set_start_and_end(current_place_in_time, meter)
            if current_beat._is_note():
                midi_instrument.notes.append(current_beat._get_midi_data())
            current_place_in_time = current_place_in_time + current_beat._get_length_in_seconds()
        return midi_instrument
    
    def _get_length(self, meter):
        current_length = 0
        for i in range(0, len(self.beats)):
            current_beat = self.beats[i]
            current_beat._set_start_and_end(0, meter)
            current_length = current_length + self.beats[i]._get_length_in_seconds()
        return current_length
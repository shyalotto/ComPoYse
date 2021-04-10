import sys
sys.path.append("C:\\Users\\ewatts3\\source\\repos\\ComPoYse\\compoyse\\midi")
import pretty_midi
from Beat import Beat
class Measure:
    def __init__(self):
        self.beats = []
        return
    
    def get_length(self):
        length = 0
        for i in range(0, len(self.beats)):
            length = length + self.beats[i].get_length_in_seconds()
        return length
    
    def get_beat_at_index(self, index):
        return self.beats[index]

    def add_beat(self, note):
        self.beats.append(note)
        return
    
    def get_midi_data(self, current_place_in_time, midi_instrument, meter):
        current_place_in_time = current_place_in_time
        for i in range(0, len(self.beats)):
            current_beat = self.get_beat_at_index(i)
            current_beat.set_start_and_end(current_place_in_time, meter)
            if current_beat.is_note():
                midi_instrument.notes.append(current_beat.get_midi_data())
            current_place_in_time = current_place_in_time + current_beat.get_length_in_seconds()
        return midi_instrument
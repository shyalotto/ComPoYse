import sys
sys.path.append("C:\\Users\\ewatts3\\source\\repos\\ComPoYse\\compoyse\\midi")
import pretty_midi
from Note import Note

class Measure:
    def __init__(self):
        self.notes = []
        return
    
    def get_length(self):
        length = 0
        for i in range(0, len(self.notes)):
            length = length + self.notes[i].get_length_in_seconds()
        return length
    
    def get_note_at_index(self, index):
        return self.notes[index]

    def add_note(self, note):
        self.notes.append(note)
        return
    
    def get_midi_data(self, current_place_in_time, midi_instrument, meter):
        current_place_in_time = current_place_in_time
        for i in range(0, len(self.notes)):
            current_note = self.get_note_at_index(i)
            current_note.set_start(current_place_in_time)
            midi_instrument.notes.append(current_note.get_midi_data(meter))
            current_place_in_time = current_place_in_time + current_note.get_length_in_seconds()
        return midi_instrument
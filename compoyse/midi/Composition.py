import pretty_midi
from compoyse.midi.Voice import Voice
from compoyse.midi.Meter import Meter

class Composition:
    def __init__(self):
        self.voices = []
        return
    
    def get_length(self):
        length_of_each_voice = []
        for i in range(0, len(self.voices)):
            length_of_each_voice.append(self.voices[i].get_length())
        return max(length_of_each_voice)
    
    def get_voice_at_index(self, index):
        return self.voices[index]
    
    def get_number_of_voices(self):
        return len(self.voices)
    
    def add_voice(self, voice):
        self.voices.append(voice)
        return
    
    def set_quarter_note_bpm(self, quarter_note_bpm):
        self.meter = Meter()
        self.meter.set_length_of_quarter_in_seconds(quarter_note_bpm)
        return
    
    def write_midi_data(self, fileName='compoyse_composition'):
        pm = pretty_midi.PrettyMIDI()
        for i in range(0, len(self.voices)):
            pm.instruments.append(self.get_voice_at_index(i).get_midi_data(self.meter))
        pm.write(fileName + '.mid')
        return
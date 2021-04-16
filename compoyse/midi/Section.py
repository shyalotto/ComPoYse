import pretty_midi
from compoyse.midi.Voice import Voice
from compoyse.midi.Meter import Meter

class Section:
    def __init__(self):
        self.voices = []
        self.identifier = ''
        return
    
    def get_length(self):
        lengths_of_each_voice = []
        for i in range(0, len(self.voices)):
            lengths_of_each_voice.append(self.voices[i].get_length())
        return max(lengths_of_each_voice)
    
    def get_voice_at_index(self, index):
        return self.voices[index]
    
    def get_number_of_voices(self):
        return len(self.voices)
    
    def get_identifier(self):
        return self.identifier
    
    def add_voice(self, voice):
        self.voices.append(voice)
        return
    
    def set_identifier(self, identifier):
        self.identifier = identifier
        return
    
    def get_midi_data(self, meter, starting_place):
        #pm = pretty_midi.PrettyMIDI()
        midi_instruments = []
        for i in range(0, len(self.voices)):
            midi_instruments.append(self.get_voice_at_index(i).get_midi_data(meter, starting_place))
        return midi_instruments
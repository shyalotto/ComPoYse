import pretty_midi
from compoyse.midi.Voice import Voice
from compoyse.midi.Section import Section
from compoyse.midi.Meter import _Meter

class Composition:
    def __init__(self):
        self.sections = []
        return
    
    def get_section_at_index(self, index):
        return self.sections[index]
    
    def get_number_of_sections(self):
        return len(self.sections)
    
    def add_section(self, section):
        self.sections.append(section)
        return
    
    def get_length(self):
        current_length = 0
        for i in range(0, len(self.sections)):
            current_length = current_length + self.get_section_at_index(i)._get_length()
        return current_length
    
    def write_midi_data(self, fileName='compoyse_composition'):
        current_place_in_time = 0
        pm = pretty_midi.PrettyMIDI()
        
        for i in range(0, len(self.sections)):
            midi_instruments_in_section = self.get_section_at_index(i)._get_midi_data(current_place_in_time)
            for j in range(0, len(midi_instruments_in_section)):
                pm.instruments.append(midi_instruments_in_section[j])
            current_place_in_time = current_place_in_time + self.get_section_at_index(i)._get_length()
        
        pm.write(fileName + '.mid')
        return
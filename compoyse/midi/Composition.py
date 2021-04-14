import pretty_midi
from compoyse.midi.Section import Section
from compoyse.midi.Meter import Meter

class Composition:
    def __init__(self):
        self.sections = []
        return
    
    def get_length(self):
        lengths_of_each_section = []
        for i in range(0, len(self.sections)):
            lengths_of_each_section.append(self.sections[i].get_length())
        return sum(lengths_of_each_section)
    
    def get_section_at_index(self, index):
        return self.sections[index]
    
    def get_number_of_sections(self):
        return len(self.sections)
    
    def add_section(self, section):
        self.sections.append(section)
        return
    
    def set_quarter_note_bpm(self, quarter_note_bpm):
        self.meter = Meter()
        self.meter.set_length_of_quarter_in_seconds(quarter_note_bpm)
        return
    
    def write_midi_data(self, fileName='compoyse_composition'):
        pm = pretty_midi.PrettyMIDI()
        for i in range(0, len(self.sections)):
            midi_instruments_in_section = self.get_section_at_index(i).get_midi_data(self.meter)
            for j in range(0, len(midi_instruments_in_section)):
                pm.instruments.append(midi_instruments_in_section[j])
        pm.write(fileName + '.mid')
        return
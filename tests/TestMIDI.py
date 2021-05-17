import unittest
from compoyse.midi.Note import Note
from compoyse.midi.Measure import Measure
from compoyse.midi.Voice import Voice
from compoyse.midi.Section import Section
from compoyse.midi.Composition import Composition

class TestMIDI(unittest.TestCase):
 def setUp(self):
        self.test_note = Note()
        self.test_note.set_letter('C')
        self.test_note.set_octave(4)
        self.test_note.set_rhythmic_value(['quarter'])
        self.test_note.set_velocity(100)
        
        self.test_measure = Measure()
        self.test_measure.add_beat(self.test_note)
        self.test_measure.add_beat(self.test_note)
        self.test_measure.add_beat(self.test_note)
        
        self.test_voice = Voice()
        self.test_voice.add_measure(self.test_measure)
        self.test_voice.add_measure(self.test_measure)
        self.test_voice.add_measure(self.test_measure)
        
        self.test_section = Section()
        self.test_section.set_identifier('A')
        self.test_section.add_voice(self.test_voice)
        self.test_section.add_voice(self.test_voice)
        self.test_section.add_voice(self.test_voice)
        self.test_section.set_quarter_note_bpm(60)
        
        self.test_composition = Composition()
        self.test_composition.add_section(self.test_section)
        self.test_composition.add_section(self.test_section)
        self.test_composition.add_section(self.test_section)
        return
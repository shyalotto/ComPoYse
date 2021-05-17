import unittest
from compoyse.midi.Note import Note
from compoyse.midi.Measure import Measure
from compoyse.midi.Voice import Voice
from compoyse.midi.Section import Section
from compoyse.midi.Composition import Composition
from compoyse.midi.Meter import _Meter

class TestMIDI(unittest.TestCase):
      def setUp(self):
            self.test_meter =  _Meter()
            self.test_meter._set_length_of_quarter_in_seconds(60)
            
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
            
            
            self.note_to_add = Note()
            self.note_to_add.set_letter('E')
            self.note_to_add.set_octave(4)
            self.note_to_add.set_rhythmic_value(['quarter'])
            self.note_to_add._set_start_and_end(0, self.test_meter)
            self.note_to_add.set_velocity(100)
            
            self.measure_to_add = Measure()
            self.measure_to_add.add_beat(self.note_to_add)
            
            self.voice_to_add = Voice()
            self.voice_to_add.add_measure(self.measure_to_add)
            
            self.section_to_add = Section()
            self.section_to_add.add_voice(self.voice_to_add)
            self.section_to_add.set_quarter_note_bpm(60)
            return
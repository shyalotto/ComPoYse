import unittest
import pretty_midi
import os.path
from os import path
from compoyse.midi.Note import Note
from compoyse.midi.Measure import Measure
from compoyse.midi.Voice import Voice
from compoyse.midi.Section import Section
from compoyse.midi.Composition import Composition
from compoyse.midi.Meter import Meter

class TestComposition(unittest.TestCase):
    def setUp(self):
        test_meter = Meter()
        test_meter.set_length_of_quarter_in_seconds(60)
        
        note_one = Note()
        note_one.set_letter('C')
        note_one.set_octave(4)
        note_one.set_rhythmic_value(['quarter'])
        note_one.set_start_and_end(0, test_meter)
        note_one.set_velocity(100)

        note_two = Note()
        note_two.set_letter('D')
        note_two.set_octave(4)
        note_two.set_rhythmic_value(['quarter'])
        note_two.set_start_and_end(1, test_meter)
        note_two.set_velocity(100)

        note_three = Note()
        note_three.set_letter('E')
        note_three.set_octave(4)
        note_three.set_rhythmic_value(['quarter'])
        note_three.set_start_and_end(2, test_meter)
        note_three.set_velocity(100)
        
        measure_one = Measure()
        measure_one.add_beat(note_one)
        measure_one.add_beat(note_two)
        measure_one.add_beat(note_three)
        
        note_four = Note()
        note_four.set_letter('C')
        note_four.set_octave(4)
        note_four.set_rhythmic_value(['quarter'])
        note_four.set_start_and_end(3, test_meter)
        note_four.set_velocity(100)

        note_five = Note()
        note_five.set_letter('D')
        note_five.set_octave(4)
        note_five.set_rhythmic_value(['quarter'])
        note_five.set_start_and_end(4, test_meter)
        note_five.set_velocity(100)

        note_six = Note()
        note_six.set_letter('E')
        note_six.set_octave(4)
        note_six.set_rhythmic_value(['quarter'])
        note_six.set_start_and_end(5, test_meter)
        note_six.set_velocity(100)
        
        measure_two = Measure()
        measure_two.add_beat(note_four)
        measure_two.add_beat(note_five)
        measure_two.add_beat(note_six)
        
        note_seven = Note()
        note_seven.set_letter('C')
        note_seven.set_octave(4)
        note_seven.set_rhythmic_value(['quarter'])
        note_seven.set_start_and_end(6, test_meter)
        note_seven.set_velocity(100)

        note_eight = Note()
        note_eight.set_letter('D')
        note_eight.set_octave(4)
        note_eight.set_rhythmic_value(['quarter'])
        note_eight.set_start_and_end(6, test_meter)
        note_eight.set_velocity(100)

        note_nine = Note()
        note_nine.set_letter('E')
        note_nine.set_octave(4)
        note_nine.set_rhythmic_value(['quarter'])
        note_nine.set_start_and_end(7, test_meter)
        note_nine.set_velocity(100)
        
        measure_three = Measure()
        measure_three.add_beat(note_one)
        measure_three.add_beat(note_eight)
        measure_three.add_beat(note_nine)
        
        
        voice_one = Voice()
        voice_one.add_measure(measure_one)
        voice_one.add_measure(measure_two)
        voice_one.add_measure(measure_three)
        
        voice_two = Voice()
        voice_two.add_measure(measure_one)
        voice_two.add_measure(measure_two)
        voice_two.add_measure(measure_three)
        
        voice_three = Voice()
        voice_three.add_measure(measure_one)
        voice_three.add_measure(measure_two)
        voice_three.add_measure(measure_three)
        
        
        section_one = Section()
        section_one.set_identifier('A')
        section_one.add_voice(voice_one)
        section_one.add_voice(voice_two)
        section_one.add_voice(voice_three)
        section_one.set_quarter_note_bpm(60)
        
        section_two = Section()
        section_two.set_identifier('B')
        section_two.add_voice(voice_one)
        section_two.add_voice(voice_two)
        section_two.add_voice(voice_three)
        section_two.set_quarter_note_bpm(60)
        
        section_three = Section()
        section_three.set_identifier('C')
        section_three.add_voice(voice_one)
        section_three.add_voice(voice_two)
        section_three.add_voice(voice_three)
        section_three.set_quarter_note_bpm(60)
        
        
        self.test_composition = Composition()
        self.test_composition.add_section(section_one)
        self.test_composition.add_section(section_two)
        self.test_composition.add_section(section_three)
        return
    
    def test_get_length__length_is_correct(self):
        self.assertEquals(self.test_composition.get_length(), 27, 'Length is 27.')
        return
    
    def test_get_section_at_index__section_is_returned(self):
        self.assertEquals(self.test_composition.get_section_at_index(1).get_length(), 9, 'Length is 9.')
        return
    
    def test_get_number_of_sections__number_of_sections_is_returned(self):
        self.assertEquals(self.test_composition.get_number_of_sections(), 3, 'There are 3 sections.')
        return
    
    def test_get_current_order_of_sections__order_of_sections_is_returned(self):
        self.assertEquals(self.test_composition.get_current_order_of_sections(), 'ABC', 'Order is ABC.')
        return
        
    def test_add_section__section_is_added(self):
        test_meter = Meter()
        test_meter.set_length_of_quarter_in_seconds(60)
        
        note_four = Note()
        note_four.set_letter('E')
        note_four.set_octave(4)
        note_four.set_rhythmic_value(['quarter'])
        note_four.set_start_and_end(0, test_meter)
        note_four.set_velocity(100)
        
        measure_four = Measure()
        measure_four.add_beat(note_four)
        
        voice_four = Voice()
        voice_four.add_measure(measure_four)
        
        section_four = Section()
        section_four.add_voice(voice_four)
        
        self.test_composition.add_section(section_four)
        self.assertEquals(self.test_composition.get_section_at_index(3).get_length(), 1, 'Length is 1.')
        return
    
    def test_arrange_sections__sections_are_arranged(self):
        order_to_arrange_in = 'CBA'
        self.test_composition.arrange_sections(order_to_arrange_in)
        list_of_section_names_in_order = ''
        for i in range(0, self.test_composition.get_number_of_sections()):
            section_identifier = self.test_composition.get_section_at_index(i).get_identifier()
            list_of_section_names_in_order = list_of_section_names_in_order + section_identifier
        self.assertEquals(list_of_section_names_in_order, order_to_arrange_in, 'Order is CBA.')
        return
    
    def test_write_midi_data__midi_data_is_written(self):
        self.test_composition.write_midi_data()
        self.assertTrue(os.path.exists("compoyse_composition.mid"))
        os.remove("compoyse_composition.mid")
        return
        
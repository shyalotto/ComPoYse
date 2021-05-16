import unittest
from compoyse.midi.MIDIUtility import MIDIUtility
from compoyse.midi.Section import Section
from compoyse.midi.Composition import Composition

class TestMIDIUtility(unittest.TestCase):
    def setUp(self):
        self.test_mu = MIDIUtility()
        return
    
    def test_getCurrentDateAndTimeFormatted(self):
        self.assertTrue(self.test_mu.get_current_date_and_time_formatted() is not None)
        return
    
    def test_getAll12TETPitchesAsArray_whenCalled_shouldReturnCorrectArray(self):
        self.assertEqual(self.test_mu.get_all_12tet_pitches_as_array(), 
                         ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'])
        return
    
    def test_arrangeSectionsInGivenOrderInComposition_givenOrderAndComposition_shouldArrangeCompositionInCorrectOrder(self):
        a_section = Section()
        b_section = Section()
        test_composition = Composition()
        
        a_section.set_identifier('A')
        b_section.set_identifier('B')
        
        test_composition.add_section(a_section)
        test_composition.add_section(b_section)
        
        test_order = 'ABBA'
        test_composition = self.test_mu.arrange_sections_in_given_order_in_composition(test_order, test_composition)
        
        final_order = ''
        for i in range(0, test_composition.get_number_of_sections()):
            final_order = final_order + test_composition.get_section_at_index(i).get_identifier()
        self.assertEqual(test_order, 'ABBA')
        return
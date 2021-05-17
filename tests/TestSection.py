from tests.TestMIDI import TestMIDI

class TestSection(TestMIDI):
    def test_getVoiceAtIndex_givenIndex_shouldReturnVoice(self):
        self.assertEqual(self.test_section.get_voice_at_index(1).get_number_of_measures(), 3, 'Number of measures is 3.')
        return
    
    def test_getNumberOfVoices_whenCalled_shouldReturnNumberOfVoices(self):
        self.assertEqual(self.test_section.get_number_of_voices(), 3, 'There are 3 voices.')
        return
    
    def test_setIdentifier_givenIdentifier_identifierIsSet(self):
        self.assertEqual(self.test_section.get_identifier(), 'A', 'Identifier is A.')
        return
    
    def test_addVoice_givenVoice_shouldAddVoice(self):
        self.test_section.add_voice(self.voice_to_add)
        self.assertEqual(self.test_section.get_voice_at_index(3).get_number_of_measures(), 1, 'Number of measures is 1.')
        return
    
    def test_getMIDIData_whenCalled_shouldReturnMIDIData(self):
        self.test_section.set_quarter_note_bpm(60)
        self.assertEqual(len(self.test_section._get_midi_data(0)), 3, 'There are 3 midi instruments.')
        return
        
    def test_getLength_whenCalled_shouldReturnLength(self):
        self.assertEqual(self.test_section._get_length(), 9, 'Sections length is 9.')
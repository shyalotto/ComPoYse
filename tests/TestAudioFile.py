import os
import unittest
from compoyse.wav.AudioFile import AudioFile

class TestAudioFile(unittest.TestCase):
    def test_set_file_name__file_name_is_set(self):
        test_af = AudioFile()
        test_af.set_file_name('test_file.wav')
        self.assertEquals(test_af.get_file_name(), 'test_file.wav', "File is named test_file.wav.")
        return
    
    def test_set_file_directory__file_directory_is_set(self):
        test_af = AudioFile()
        test_af.set_file_directory('tests\\test_directory')
        self.assertEquals(test_af.get_file_directory(), 'tests\\test_directory', "Directory is the test_directory subfolder of tests.")
        return 
    
    def test_get_file_real_path__file_real_path_is_correct(self):
        test_af = AudioFile()
        test_af.set_file_name('test_file.wav')
        test_af.set_file_directory('tests\\test_directory')
        correct_real_path = os.path.realpath(test_af.get_file_directory() + '\\\\' + test_af.get_file_name())
        self.assertEquals(test_af.get_file_real_path(), correct_real_path, "Real path is correct full directory.")
    
    def set_duration_of_file__duration_of_file_is_correct(self):
        test_af = AudioFile()
        test_af.set_file_name('test_file.wav')
        test_af.set_file_directory('tests\\test_directory')
        self.assertEquals(test_af.get_duration(), '60.070022675736965', 'Audio file is 60.070022675736965 seconds long.')
        return
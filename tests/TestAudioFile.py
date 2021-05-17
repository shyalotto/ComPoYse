import os
import unittest
from compoyse.wav.AudioFile import AudioFile

class TestAudioFile(unittest.TestCase):
    def setUp(self):
        self.test_af = AudioFile()
        return
    
    def test_setFileName_givenFileName_shouldSetFileName(self):
        self.test_af.set_file_name('test_file.wav')
        self.assertEqual(self.test_af.get_file_name(), 'test_file.wav', "File is named test_file.wav.")
        return
    
    def test_setFileDirectory_givenFileDirector_shouldSetFileDirectory(self):
        self.test_af.set_file_directory('tests\\test_directory')
        self.assertEqual(self.test_af.get_file_directory(), 'tests\\test_directory', "Directory is the test_directory subfolder of tests.")
        return 
    
    def test_getFileRealPath_givenNameAndDirectorySet_shouldReturnRealPath(self):
        self.test_af.set_file_name('test_file.wav')
        self.test_af.set_file_directory('tests\\test_directory')
        correct_real_path = os.path.realpath(self.test_af.get_file_directory() + '\\\\' + self.test_af.get_file_name())
        self.assertEqual(self.test_af._get_file_real_path(), correct_real_path, "Real path is correct full directory.")
    
    def test_setDurationOfFile_givenNameAndDirectorySet_shouldSetDuration(self):
        self.test_af.set_file_name('test_file.wav')
        self.test_af.set_file_directory('tests\\test_directory')
        self.assertEqual(self.test_af.get_duration(), 60.070022675736965, 'Audio file is 60.070022675736965 seconds long.')
        return
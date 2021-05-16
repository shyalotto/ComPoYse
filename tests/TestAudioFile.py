import os
import unittest
from compoyse.wav.AudioFile import AudioFile

class TestAudioFile(unittest.TestCase):
    def test_setFileName_givenFileName_shouldSetFileName(self):
        test_af = AudioFile()
        test_af.set_file_name('test_file.wav')
        self.assertEqual(test_af.get_file_name(), 'test_file.wav', "File is named test_file.wav.")
        return
    
    def test_setFileDirectory_givenFileDirector_shouldSetFileDirectory(self):
        test_af = AudioFile()
        test_af.set_file_directory('tests\\test_directory')
        self.assertEqual(test_af.get_file_directory(), 'tests\\test_directory', "Directory is the test_directory subfolder of tests.")
        return 
    
    def test_getFileRealPath_givenNameAndDirectorySet_shouldReturnRealPath(self):
        test_af = AudioFile()
        test_af.set_file_name('test_file.wav')
        test_af.set_file_directory('tests\\test_directory')
        correct_real_path = os.path.realpath(test_af.get_file_directory() + '\\\\' + test_af.get_file_name())
        self.assertEqual(test_af._get_file_real_path(), correct_real_path, "Real path is correct full directory.")
    
    def test_setDurationOfFile_givenNameAndDirectorySet_shouldSetDuration(self):
        test_af = AudioFile()
        test_af.set_file_name('test_file.wav')
        test_af.set_file_directory('tests\\test_directory')
        self.assertEqual(test_af.get_duration(), 60.070022675736965, 'Audio file is 60.070022675736965 seconds long.')
        return
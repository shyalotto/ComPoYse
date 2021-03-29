import sys
sys.path.append("C:\\Users\\ewatts3\\source\\repos\\ComPoYse\\compoyse")
import unittest
import os
from setuptools import find_packages
from AudioClip import AudioClip
from AudioFile import AudioFile

class TestAudioClip(unittest.TestCase):
    def test_set_audio_file__audio_file_is_set(self):
        test_ac = AudioClip()
        test_af = AudioFile()
        test_ac.set_audio_file(test_af)
        self.assertEquals(test_ac.get_audio_file(), test_af, "Audio file is test_af.")
        return
    
    def test_set_start__start_is_set(self):
        test_ac = AudioClip()
        test_ac.set_start(10)
        self.assertEquals(test_ac.get_start(), 10, "Start is 10.")
        return
    
    def test_set_duration_of_playtime__duration_of_playtime_is_set(self):
        test_ac = AudioClip()
        test_ac.set_duration_of_playtime(10)
        self.assertEquals(test_ac.get_duration_of_playtime(), 10, "Duration of playtime is 10.")
        return
    
    def test_get_file_real_path__file_real_path_is_got(self):
        test_ac = AudioClip()
        test_af = AudioFile()
        test_af.set_file_name('test_file.wav')
        test_af.set_file_directory('tests\\test_directory')
        test_ac.set_audio_file(test_af)
        correct_real_path = os.path.realpath(test_af.get_file_directory() + '\\\\' + test_af.get_file_name())
        self.assertEquals(test_ac.get_file_real_path(), correct_real_path, "Real path is correct full directory.")
        return
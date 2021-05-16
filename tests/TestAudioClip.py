import unittest
import os
from compoyse.wav.AudioClip import AudioClip
from compoyse.wav.AudioFile import AudioFile

class TestAudioClip(unittest.TestCase):
    def test_setAudioFile_givenAudioFile_shouldSetAudioFile(self):
        test_ac = AudioClip()
        test_af = AudioFile()
        test_ac.set_audio_file(test_af)
        self.assertEqual(test_ac.get_audio_file(), test_af, "Audio file is test_af.")
        return
    
    def test_setStart_givenStart_shouldSetStart(self):
        test_ac = AudioClip()
        test_ac.set_start(10)
        self.assertEqual(test_ac._get_start(), 10, "Start is 10.")
        return
    
    def test_setDurationOfPlaytime_givenDuration_shouldSetDurationOfPlaytime(self):
        test_ac = AudioClip()
        test_ac.set_duration_of_playtime(10)
        self.assertEqual(test_ac.get_duration_of_playtime(), 10, "Duration of playtime is 10.")
        return
    
    def test_getFileRealPath_whenCalled_shouldReturnFileRealPath(self):
        test_ac = AudioClip()
        test_af = AudioFile()
        test_af.set_file_name('test_file.wav')
        test_af.set_file_directory('tests\\test_directory')
        test_ac.set_audio_file(test_af)
        correct_real_path = os.path.realpath(test_af.get_file_directory() + '\\\\' + test_af.get_file_name())
        self.assertEqual(test_ac._get_file_real_path(), correct_real_path, "Real path is correct full directory.")
        return
    
    def test_setOutputDeviceIndex_givenIndex_shouldSetOutputDeviceIndex(self):
        test_ac = AudioClip()
        test_ac.set_output_device_index(0)
        self.assertEqual(test_ac.get_output_device_index(), 0, "Output device index is 0.")
        return
import unittest
from compoyse.wav.AudioPlayer import AudioPlayer
from compoyse.wav.AudioFile import AudioFile
from compoyse.wav.AudioClip import AudioClip
import os
import threading

class TestAudioPlayer(unittest.TestCase):
    def setUp(self):
        test_af = AudioFile()
        test_af.set_file_name('test_file.wav')
        test_af.set_file_directory(os.path.realpath('tests\\test_directory'))
        
        self.test_ac = AudioClip()
        self.test_ac.set_audio_file(test_af)
        self.test_ac.set_start(0)
        self.test_ac.set_duration_of_playtime(test_af.get_duration())
        
        self.test_ap = AudioPlayer()
        return
    
    def test_play_givenAudioFile_shouldCalculateValuesToUseWhenPlaying(self):
        test_thread = threading.Thread(target=self.test_ap.play, args=(self.test_ac,), daemon=True)
        test_thread.start()
        self.assertTrue(test_thread.is_alive())
        return
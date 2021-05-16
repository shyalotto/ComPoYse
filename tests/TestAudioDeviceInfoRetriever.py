import unittest
from compoyse.wav.AudioDeviceInfoRetriever import AudioDeviceInfoRetriever

class TestAudioClip(unittest.TestCase):
    def setUp(self):
        self.test_adir = AudioDeviceInfoRetriever()
    
    def test_getDeviceCount_whenCalled_shouldReturnDeviceCount(self):
        self.assertTrue(self.test_adir.get_device_count() is not None)
        return
    
    def test_getDeviceInfoByIndex_givenIndex_shouldReturnDeviceWithThatIndex(self):
        self.assertTrue(self.test_adir.get_device_info_by_index(0) is not None)
        return
    
    def test_getDefaultOutputDeviceInfo_whenCalled_shouldReturnDefaultOutputDeviceInfo(self):
        self.assertTrue(self.test_adir.get_default_output_device_info() is not None)
        return
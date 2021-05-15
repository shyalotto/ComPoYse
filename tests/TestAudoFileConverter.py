import os
import unittest
from compoyse.wav.AudioFileConverter import AudioFileConverter

class TestAudioConverter(unittest.TestCase):
    def test_convertOrCopyFiles_givenMP3AndWAVFiles_shouldConvertMP3AndCopyWAV(self):
        test_directory_real_path = os.path.realpath('tests\\test_directory')
        converted_mp3_file_path = test_directory_real_path + '\\\\' + 'wav_files' + '\\\\' + 'test_mp3_file.wav'
        copied_wav_file_path = test_directory_real_path + '\\\\' + 'wav_files' + '\\\\' + 'test_file.wav'
        
        test_afc = AudioFileConverter()
        test_afc.convert_or_copy_files(test_directory_real_path)
        
        self.assertTrue(os.path.exists(converted_mp3_file_path), 'The MP3 file was not correctly converted.')
        self.assertTrue(os.path.exists(copied_wav_file_path), 'The WAV file was not correctly copied.')
        
        os.remove(converted_mp3_file_path)
        os.remove(copied_wav_file_path)
        
        #we rename the created directory so there are no references to it and it can be deleted
        os.chdir(test_directory_real_path)
        os.rename('wav_files', 'remove_this_directory')
        os.rmdir('remove_this_directory')
        return
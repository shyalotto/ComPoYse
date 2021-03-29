import wave
import os
from Play import Play

class AudioClip:
    def __init__(self, 
                 audio_file=None,
                 start=0,
                 duration_of_playtime=0):
        self.audio_file = audio_file
        self.start = start
        self.duration_of_playtime = duration_of_playtime
        return
    
    def get_audio_file(self):
        return self.audio_file
    
    def get_start(self):
        return self.start
    
    def get_duration_of_playtime(self):
        return self.duration_of_playtime
    
    def get_file_real_path(self):
        return self.audio_file.get_file_real_path()
    
    def set_audio_file(self, audio_file):
        self.audio_file = audio_file
        return
        
    def set_start(self, start):
        self.start = start
        return
    
    def set_duration_of_playtime(self, duration):
        self.duration_of_playtime = duration
        return
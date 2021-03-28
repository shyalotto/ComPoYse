import wave
import os
from Play import Play

class AudioFile:
    def __init__(self,
                 file_name='',
                 file_directory='',
                 start=0,
                 duration_of_playtime=-1):
        self.file_real_path = ''
        self.file_name = file_name
        self.file_directory = file_directory
        self.set_duration_of_file()
        self.start=start
        if(duration_of_playtime == -1):
            self.duration_of_playtime = self.duration
        else:
            self.duration_of_playtime = duration_of_playtime
        return
    
    def get_file_name(self):
        return self.file_name
    
    def get_file_directory(self):
        return self.file_directory
    
    def get_file_real_path(self):
        return self.file_real_path
    
    def get_duration_of_file(self):
        return self.duration
    
    def get_start(self):
        return self.start
    
    def get_duration_of_playtime(self):
        return self.duration_of_playtime
    
    def set_file_name(self, file_name):
        self.file_name = file_name
        self.set_file_real_path()
        return
    
    def set_file_directory(self, file_directory):
        self.file_directory = file_directory
        self.set_file_real_path()
        return
    
    def set_file_real_path(self):
        if(self.file_name != '' and self.file_directory != ''):
            self.file_real_path = os.path.realpath(self.file_directory + '\\' + self.file_name)
        return
    
    def set_duration_of_file(self):
        if(self.get_file_real_path() != ''):
            file = wave.open(self.get_file_real_path(), "rb")
            self.duration = (file.getnframes() / file.getframerate())
            file.close()
        else:
            self.duration = -1
        return
    
    def set_start(self, start):
        self.start = start
        return
    
    def set_duration_of_playtime(self, duration):
        self.duration_of_playtime = duration
        return
    
    def play(self):
        Play(self.get_file_real_path(),
             self.get_start(),
             self.get_duration_of_playtime())
        return
    
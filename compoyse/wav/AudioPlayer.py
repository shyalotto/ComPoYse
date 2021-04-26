import pyaudio
import wave
import threading

class AudioPlayer:
    def __init__(self):
        return
    
    def play(self, audio_clip):
        self.open_file(audio_clip.get_file_real_path())
        self.open_stream(audio_clip)
        self.set_starting_position(audio_clip.get_start())
        self.write_file_to_stream(audio_clip.get_duration_of_playtime())
        self.close_all_open_data()
        return

    def open_file(self, file_path):
        self.file = wave.open(file_path, "rb") #rb = read only
        return 
    
    def open_stream(self, audio_clip):
        pya = pyaudio.PyAudio()
        self.stream = pya.open(format=pyaudio.get_format_from_width(self.file.getsampwidth()),
                             channels=self.file.getnchannels(),
                             rate=self.file.getframerate(),
                             output=True,
                             output_device_index=audio_clip.get_output_device_index())
        return 
    
    def set_starting_position(self, start):
        self.file.setpos(self.get_starting_position(start))
        return
    
    def get_starting_position(self, start):
        return start * self.file.getframerate()
    
    def write_file_to_stream(self, duration):
        self.stream.write(self.get_frames_to_write(duration))
        return
    
    def get_frames_to_write(self, duration):
        return self.file.readframes(duration * self.file.getframerate())
        
    def close_all_open_data(self):
        # normally it's good housekeeping to close all open data,
        # but closing these in one place will cause them to close elsewhere
        # self.stream.close()
        # self.pya.terminate()
        
        self.file.close()
        return
    
import pyaudio
import wave

class Play:
    def __init__(self, file_path, start, duration):
        self.file = self.open_file(file_path)
        self.play_file(start, duration)
        self.close_all_open_data()
        return

    def open_file(self, file_path):
        return wave.open(file_path, "rb") #rb = read only
        
    def play_file(self, start, duration):
        self.open_stream()
        self.set_starting_position(start)
        self.write_file_to_stream(duration)
        return
    
    def open_stream(self):
        self.pya = pyaudio.PyAudio()
        self.stream = self.pya.open(format=pyaudio.get_format_from_width(self.file.getsampwidth()),
                             channels=self.file.getnchannels(),
                             rate=self.file.getframerate(),
                             output=True)
        return 
    
    def set_starting_position(self, start):
        self.file.setpos(start * self.file.getframerate())
        return
    
    def write_file_to_stream(self, duration):
        self.stream.write(self.file.readframes(duration * self.file.getframerate()))
        return
        
    def close_all_open_data(self):
        self.stream.close()
        self.pya.terminate()
        self.file.close()
        return
    
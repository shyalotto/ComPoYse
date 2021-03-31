import pyaudio
import wave
import threading

class Play:
    def __init__(self):
        return
    
    def play(self, audio_clip):
        audio_player = AudioPlayer()
        play_thread = self.create_play_thread(audio_player, audio_clip)
        play_thread.start()
        return
    
    def create_play_thread(self, audio_player, audio_clip):
        return threading.Thread(target=audio_player.play_audio, args=(audio_clip,), daemon=False)
    
class AudioPlayer:
    def __init__(self):
        return
    
    def play_audio(self, audio_clip):
        self.open_file(audio_clip.get_file_real_path())
        self.open_stream()
        self.set_starting_position(audio_clip.get_start())
        self.write_file_to_stream(audio_clip.get_duration_of_playtime())
        self.close_all_open_data()
        return

    def open_file(self, file_path):
        self.file = wave.open(file_path, "rb") #rb = read only
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
    
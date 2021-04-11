import pretty_midi
from compoyse.midi.Beat import Beat
from compoyse.midi.Beat_dependencies.Velocity import Velocity
from compoyse.midi.Beat_dependencies.NoteLetter import NoteLetter

class Note(Beat):
    def __init__(self):
        self.velocity = Velocity()
        self.velocity.set_velocity(0)
        
        self.note_letter = NoteLetter()
        self.note_letter.set_letter('C')
        self.note_letter.set_octave(0)
        
        super().__init__()
        return
    
    def get_note_data(self):
        return [self.velocity.get_velocity(), 
                self.note_letter.get_letter(), 
                self.note_letter.get_octave(), 
                self.time.get_rhythmic_value()]
    
    def get_velocity(self):
        return self.velocity.get_velocity()
    
    def get_letter(self):
        return self.note_letter.get_letter()
    
    def get_octave(self):
        return self.note_letter.get_octave()
    
    def get_midi_value(self):
        return self.note_letter.get_midi_value()
    
    def get_midi_data(self):
        note = pretty_midi.Note(velocity=self.velocity.get_velocity(),
                                pitch=self.note_letter.get_midi_value(),
                                start=self.time.get_start(),
                                end=self.time.get_end())
        return note
    
    def set_velocity(self, velocity):
        self.velocity.set_velocity(velocity)
        return
    
    def set_letter(self, letter):
        self.note_letter.set_letter(letter)
        return
    
    def set_octave(self, octave):
        self.note_letter.set_octave(octave)
        return
    
    def set_midi_value(self, midi_value):
        self.note_letter.set_midi_value(midi_value)
        return
    
    def alter_velocity(self, amount_to_alter_by):
        self.velocity.alter_velocity(amount_to_alter_by)
        return
    
    def alter_octave(self, amount_to_alter_by):
        self.note_letter.alter_octave(amount_to_alter_by)
        return
    
    def is_note(self):
        return True
    
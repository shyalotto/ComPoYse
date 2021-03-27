import pretty_midi

class Note:
    def __init__(self,
                 velocity=0,
                 letter='C#',
                 octave=-2,
                 start=0,
                 length=0):
        self.velocity = velocity
        self.letter = letter
        self.octave = octave
        self.midi_value = pretty_midi.note_name_to_number(self.letter + str(self.octave))
        self.start = start
        self.length = length
        self.end = start + length
        return
    
    def set_note(self, letter, octave, start, length, velocity):
        self.velocity = velocity
        self.letter = letter
        self.octave = octave
        self.midi_value = pretty_midi.note_name_to_number(self.letter + str(self.octave))
        self.start = start
        self.length = length
        self.end = start + length
        return
    
    def set_velocity(self, velocity):
        self.velocity = velocity
        return
        
    def alter_velocity(self, amountToAlterBy):
        if(new_velocity_is_in_midi_value_range(amountToAlterBy)):
            self.velocity = self.velocity + amountToAlterBy
        return
    
    def new_velocity_is_in_midi_value_range(self, amountToAlterBy):
        newVelocity = self.velocity + amountToAlterBy
        if(newVelocity >= 0 and newVelocity <= 127):
            return True
        else:
            return False
        
    def set_note_letter(self, letter):
        self.letter = letter
        return
    
    def set_octave(self, octave):
        self.octave = octave
        return
    
    def alter_octave(self, amountToAlterBy):
        if(new_octave_is_in_midi_value_range(amountToAlterBy)):
            self.octave = self.octave + amountToAlterBy
        return
    
    def new_octave_is_in_midi_value_range(self, amountToAlterBy):
        new_midi_value = pretty_midi.note_name_to_number(self.letter + str(self.octave + amountToAlterBy))
        if(new_midi_value >= 0 and new_midi_value <= 127):
            return True
        else:
            return False
        return
    
    def set_start(self, start):
        self.start = start
        return
    
    def alter_start(self, amountToAlterBy):
        self.start = self.start + amountToAlterBy
        return
    
    def set_length(self, length):
        self.length = length
        return
    
    def alter_length(self, amountToAlterBy):
        self.length = self.length + amountToAlterBy
        return
    
    def augment_length(self, amountToAugmentBy):
        self.length = self.length * amountToAugmentBy
        return
    
    def diminish_length(self, amountToDiminishBy):
        self.length = self.length / amountToDiminishBy
        return
    
    def set_end(self, end):
        self.end = end
        return
    
    def alter_end(self, amountToAlterBy):
        self.end = self.end + amountToAlterBy
        return
    
    def get_note_data(self):
        return [self.velocity, self.letter, self.octave, self.start, self.length, self.end]
    
    def get_velocity(self):
        return self.velocity
    
    def get_letter(self):
        return self.letter
    
    def get_octave(self):
        return self.octave
    
    def get_start(self):
        return self.start
    
    def get_length(self):
        return self.length
    
    def get_end(self):
        return self.end
    
    def get_midi_data(self):
        note = pretty_midi.Note(velocity=self.velocity,
                                pitch=pretty_midi.note_name_to_number(self.letter + str(self.octave)),
                                start=self.start,
                                end=self.end)
        return note
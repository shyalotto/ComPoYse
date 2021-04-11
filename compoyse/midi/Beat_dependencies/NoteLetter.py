import pretty_midi
from compoyse.midi.MIDIExceptions import ValueNotValidMIDIValue

class NoteLetter:
    def __init__(self):
        self.letter = 'C'
        self.octave = 0
        return
    
    def get_letter(self):
        return self.letter
    
    def get_octave(self):
        return self.octave
            
    def get_midi_value(self):
        return self.midi_value
    
    def set_letter(self, letter):
        new_midi_value = self.find_midi_value(letter, self.octave)
        if(self.new_midi_value_is_in_midi_value_range(new_midi_value)):
            self.letter = letter
            self.set_midi_value(new_midi_value)
        return
    
    def set_octave(self, octave):
        new_midi_value = self.find_midi_value(self.letter, octave)
        if(self.new_midi_value_is_in_midi_value_range(new_midi_value)):
            self.octave = octave
            self.set_midi_value(new_midi_value)
        return
        
    def alter_octave(self, amount_to_alter_by):
        new_octave = self.octave + amount_to_alter_by
        new_midi_value = self.find_midi_value(self.letter, new_octave)
        if(self.new_midi_value_is_in_midi_value_range(new_midi_value)):
            self.octave = new_octave
            self.set_midi_value(new_midi_value)
        return
        
    def set_midi_value(self, midi_value):
        self.midi_value = midi_value
        return
    
    def find_midi_value(self, letter, octave):
        return pretty_midi.note_name_to_number(letter + str(octave))
    
    def new_midi_value_is_in_midi_value_range(self, value):
        if(value >= 0 and value <= 127):
            return True
        else:
            raise ValueNotValidMIDIValue(str(value) +
                                         " is not a valid value for a note (must be greater than or equal to 0 or lesser than or equal to 127).")
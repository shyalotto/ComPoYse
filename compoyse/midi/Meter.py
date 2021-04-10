class Meter:
    def __init__(self):
        return
    
    def set_length_of_quarter_in_seconds(self, bpm_length_of_quarter):
        NUMBER_OF_SECONDS_IN_A_MINUTE = 60
        self.length_of_quarter_in_seconds = (NUMBER_OF_SECONDS_IN_A_MINUTE / bpm_length_of_quarter)
        return
    
    def compute_rhythmic_value_length_in_seconds(self, rhythmic_value):
        length = 0
        for i in range(0, len(rhythmic_value)):
            if(rhythmic_value[i] == 'two_hundred_fifty_sixth'):
                length = length + (self.length_of_quarter_in_seconds / 64)
            elif(rhythmic_value[i] == 'one_hundred_twenty_eighth'):
                length = length + (self.length_of_quarter_in_seconds / 32)
            elif(rhythmic_value[i] == 'sixty_fourth'):
                length = length + (self.length_of_quarter_in_seconds / 16)
            elif(rhythmic_value[i] == 'thirty_secondth'):
                length = length + (self.length_of_quarter_in_seconds / 8)
            elif(rhythmic_value[i] == 'sixteenth'):
                length = length + (self.length_of_quarter_in_seconds / 4)
            elif(rhythmic_value[i] == 'eighth'):
                length = length + (self.length_of_quarter_in_seconds / 2)
            elif(rhythmic_value[i] == 'quarter'):
                length = length + (self.length_of_quarter_in_seconds * 1)
            elif(rhythmic_value[i] == 'half'):
                length = length + (self.length_of_quarter_in_seconds * 2)
            elif(rhythmic_value[i] == 'whole'):
                length = length + (self.length_of_quarter_in_seconds * 4)
        return length
from compoyse.midi.Beat import Beat

class Rest(Beat):
    def __init__(self):
        super().__init__()
        return
    
    def is_note(self):
        return False
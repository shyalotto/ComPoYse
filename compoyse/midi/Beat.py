import sys
sys.path.append("C:\\Users\\ewatts3\\source\\repos\\ComPoYse\\compoyse\\midi\\Note_dependencies")
from Time import Time

class Beat:
    def __init__(self):
        self.time = Time()
        return
    
    def get_rhythmic_value(self):
        return self.time.get_rhythmic_value()
    
    def get_start(self):
        return self.time.get_start()
    
    def set_start_and_end(self, start, meter):
        self.time.set_start_and_end(start, meter)
        return
    
    def get_length_in_seconds(self):
        return self.time.get_length_in_seconds()
    
    def set_rhythmic_value(self, rhythmic_value):
        self.time.set_rhythmic_value(rhythmic_value)
        return
    
    def set_start(self, start):
        self.time.set_start(start)
        return
    
    def is_note(self):
        return
    


class Time:
    def __init__(self):
        self.set_start(0)
        self.set_rhythmic_value('')
        self.length = 0
        return
    
    def get_start(self):
        return self.start
    
    def get_rhythmic_value(self):
        return self.rhythmic_value
    
    def get_end(self, meter):
        self.length = meter.compute_rhythmic_value_length_in_seconds(self.get_rhythmic_value())
        end = self.start + self.length
        print(end)
        return end
    
    def get_length_in_seconds(self):
        return self.length
    
    def set_start(self, start):
        self.start = start
        return
    
    def set_rhythmic_value(self, value):
        self.rhythmic_value = value
        return
    
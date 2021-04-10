class Time:
    def __init__(self):
        self.start = 0
        self.set_rhythmic_value('')
        self.length_in_seconds = 0
        return
    
    def get_start(self):
        return self.start
    
    def get_rhythmic_value(self):
        return self.rhythmic_value
    
    def get_length_in_seconds(self):
        return self.length_in_seconds

    def get_end(self):
        end = self.start + self.length_in_seconds
        return end
    
    def set_rhythmic_value(self, value):
        self.rhythmic_value = value
        return
    
    def set_start_and_end(self, start, meter):
        self.start = start
        self.length_in_seconds = meter.compute_rhythmic_value_length_in_seconds(self.get_rhythmic_value())
        return
    
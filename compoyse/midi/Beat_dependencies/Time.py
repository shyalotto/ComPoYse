class _Time:
    def __init__(self, rhythmic_value):
        self.start = 0
        self._set_rhythmic_value(rhythmic_value)
        self.length_in_seconds = 0
        return
    
    def _get_start(self):
        return self.start
    
    def _get_rhythmic_value(self):
        return self.rhythmic_value
    
    def _get_length_in_seconds(self):
        return self.length_in_seconds

    def _get_end(self):
        end = self.start + self.length_in_seconds
        return end
    
    def _set_rhythmic_value(self, value):
        self.rhythmic_value = value
        return
    
    def _set_start_and_end(self, start, meter):
        self.start = start
        self.length_in_seconds = meter._compute_rhythmic_value_length_in_seconds(self._get_rhythmic_value())
        return
    
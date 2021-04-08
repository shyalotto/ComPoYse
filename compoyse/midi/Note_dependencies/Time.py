class Time:
    def __init__(self):
        self.set_start(0)
        self.set_start(0)
        return
    
    def get_start(self):
        return self.start
    
    def get_length(self):
        return self.length
    
    def get_end(self):
        end = self.start + self.length
        return end
    
    def set_start(self, start):
        self.start = start
        return
    
    def set_length(self, length):
        self.length = length
        return
    
    def alter_start(self, amount_to_alter_by):
        self.start = self.start + amount_to_alter_by
        return
    
    def alter_length(self, amount_to_alter_by):
        self.length = self.length + amount_to_alter_by
        return
    
    def augment_length(self, factor_to_augment_by):
        self.length = self.length * factor_to_augment_by
        return
    
    def diminish_length(self, factor_to_diminish_by):
        self.length = self.length / factor_to_diminish_by
        return
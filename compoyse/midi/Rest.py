import sys
sys.path.append("C:\\Users\\ewatts3\\source\\repos\\ComPoYse\\compoyse")
from Beat import Beat

class Rest(Beat):
    def __init__(self):
        super().__init__()
        return
    
    def is_note(self):
        return False
import unittest
from compoyse.midi.Rest import Rest

class TestRest(unittest.TestCase):
    def test__is_note_returns_false(self):
        test_rest = Rest()
        self.assertEquals(test_rest._is_note(), False, "This is not a note.")
        return
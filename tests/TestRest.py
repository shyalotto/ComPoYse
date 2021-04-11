import unittest
from compoyse.midi.Rest import Rest

class TestRest(unittest.TestCase):
    def test_is_note__returns_false(self):
        test_rest = Rest()
        self.assertEquals(test_rest.is_note(), False, "This is not a note.")
        return
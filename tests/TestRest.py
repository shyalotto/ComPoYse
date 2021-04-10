import sys
sys.path.append("C:\\Users\\ewatts3\\source\\repos\\ComPoYse\\compoyse")
import unittest
from setuptools import find_packages
from Rest import Rest

class TestRest(unittest.TestCase):
    def test_is_note__returns_false(self):
        test_rest = Rest()
        self.assertEquals(test_rest.is_note(), False, "This is not a note.")
        return
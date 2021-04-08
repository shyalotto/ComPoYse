import sys
sys.path.append("C:\\Users\\ewatts3\\source\\repos\\ComPoYse\\compoyse\\wavgit")
import unittest
from setuptools import find_packages
import pyaudio
import wave

class TestAudioPlayer(unittest.TestCase):
    def __init__(self):
        return
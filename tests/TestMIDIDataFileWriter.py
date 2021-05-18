from tests.TestMIDI import TestMIDI
from compoyse.midi.MIDIDataFileWriter import MIDIDataFileWriter
import os.path

class TestMIDIDataFileWriter(TestMIDI):
    def test_init_whenCalled_shouldWriteMIDIData(self):
        MIDIDataFileWriter(self.test_composition)
        self.assertTrue(os.path.exists("compoyse_composition.mid"))
        os.remove("compoyse_composition.mid")
        return
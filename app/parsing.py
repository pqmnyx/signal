
from dataclasses import dataclass
from pathlib import Path
from scipy.io import wavfile

import numpy as np

@dataclass
class Signal:
    bitrate: int
    data: np.ndarray
    MAX_VALUE: int = 32768

    def get_normalized(self) -> "Signal":
        return Signal(bitrate=self.bitrate, data=self.data / self.MAX_VALUE)


def parse_wavfile(path: Path) -> Signal:
    bitrate, data = wavfile.read(path)
    return Signal(bitrate=bitrate, data=data).get_normalized()

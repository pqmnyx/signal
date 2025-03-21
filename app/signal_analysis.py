import numpy as np

from app.parsing import Signal

def compute_amplitude_spectrum(signal: Signal) -> np.ndarray:
    return np.abs(np.fft.rfft(signal.data))[:len(signal.data) // 2]

def compute_frequency_spectrum(signal: Signal) -> np.ndarray:
    return np.fft.rfftfreq(len(signal.data), 1 / signal.bitrate)[:len(signal.data) // 2]

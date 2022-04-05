import pyaudio
import numpy as np

def __init__(self):
    self.str = "hi"

def generate_sound(f, r, t):
    """
    Generate a single sound using pyaudio and a sine wave from numpy.
    :param f: the frequency
    :param r: sampling rate
    :param t: the duration of the sound in seconds
    :return:
    """
    sound = (np.sin(2 * np.pi * np.arange(r * t) * f / r)).astype(np.float32)

def get_frequency(f0, n):
    """
    Get the frequency of note n semitones from f0.
    :param f0: the base frequency (probably 440 Hz)
    :param n: number of semitones from f0
    :return: the frequency of n
    """

    
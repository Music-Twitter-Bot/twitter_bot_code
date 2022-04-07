import pyaudio
import numpy as np


class AudioControl:
    def __init__(self, f0, r, max_time):
        """
        Initializes the AudioControl object and constants.
        :param f0: the base frequency of the sound
        :param r: sampling rate
        :param max_time: the maximum length of the resulting sound clip
        """
        self.f0 = f0
        self.r = r
        self.max_time = max_time

    def generate_sound(self, list_of_semitones, list_of_durations, volume):
        """
        Generates a sound from list of semitones and durations for the notes.
        :param list_of_semitones: the notes to generate, given by semitones from f0
        :param list_of_durations: the durations of each note
        :return: an array with the resulting sine waves ordered
        """
        generated_notes = []
        for i in range(len(list_of_semitones)):
            note = self.generate_wave(self.get_frequency(list_of_semitones(i)), list_of_durations(i))
            generated_notes.append(note)

        #output generated notes
        # for paFloat32 sample values must be in range [-1.0, 1.0]
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=self.r,
                        output=True)

        # play. May repeat with different volume values (if done interactively)
        stream.write(volume * generated_notes)

        stream.stop_stream()
        stream.close()

    def generate_wave(self, f, t):
        """
        Generate a sine wave with given frequency, sampling rate, and duration, using numpy.
        :param f: the frequency
        :param r: sampling rate
        :param t: the duration of the sound in seconds
        :return:
        """
        return (np.sin(2 * np.pi * np.arange(self.r * t) * f / self.r)).astype(np.float32)

    def get_frequency(self, n):
        """
        Get the frequency of note n semitones from f0.
        :param n: number of semitones from f0
        :return: the frequency of n
        """
        return self.f0 * (2 ** (n/12))





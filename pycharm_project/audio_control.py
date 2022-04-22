import wave
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

    def generate_sound(self, list_of_semitones, list_of_durations, wav_name):
        """
        Generates a sound from list of semitones and durations for the notes.
        :param list_of_semitones: the notes to generate, given by semitones from f0
        :param list_of_durations: the durations of each note
        :param wav_name: the file name of the wav file
        :return: an array with the resulting sine waves ordered
        """
        generated_notes = []
        for i in range(len(list_of_semitones)):
            for j in range(len(list_of_semitones[i])):
                note = self.generate_wave(self.get_frequency(list_of_semitones[i][j]), list_of_durations[i])
                generated_notes.append(note)
            #generate a rest
            rest = self.generate_wave(0, 0.25)
            generated_notes.append(rest)

        wav = wave.open(wav_name, 'w')
        wav.setnchannels(1)  # mono
        wav.setsampwidth(4)
        wav.setframerate(self.r)
        for i in range(len(generated_notes)):
            wav.writeframesraw(generated_notes[i])
        wav.close()

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
        if n > 0:
            n = n % 12
        else:
            n = n % -12
        return self.f0 * (2 ** (n/12))





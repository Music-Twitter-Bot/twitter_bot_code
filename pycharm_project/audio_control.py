import wave
import numpy as np


class AudioControl:
    def __init__(self, f0, r, max_time, c0):
        """
        Initializes the AudioControl object and constants.
        :param f0: the base frequency of the sound
        :param r: sampling rate
        :param max_time: the maximum length of the resulting sound clip
        :param c0: the base character for the ascii
        """
        self.f0 = f0
        self.r = r
        self.max_time = max_time
        self.c0 = c0

    def convert_text_to_wav(self, text):
        """
        Converts given text to a wav file.
        :param text: The text to convert.
        :return: Nothing.
        """
        #find the words in text
        words = []
        last_space = False
        while not last_space:
            if text.find(" ") != -1:
                words.append(text[:text.index(" ")])
                text = text[text.index(" ") + 1:]
            else:
                last_space = True
                words.append(text)

        #convert words to notes
        notes = []
        durations = []
        for word in words:
            notes.append(self.convert_word_to_semitones(word))
            durations.append(2/len(word))
            print(f"{notes}, {durations}")

        #play the notes
        self.generate_sound(notes, durations)


    def convert_word_to_semitones(self, word):
        """
        Converts the given word to an array of semitones.
        :param word: The word to parse.
        :return: Array of semitones for each letter.
        """
        semitones = []
        for c in word:
            semitones.append(ord(c) - ord(self.c0))
        return semitones

    def generate_sound(self, list_of_semitones, list_of_durations):
        """
        Generates a sound from list of semitones and durations for the notes.
        :param list_of_semitones: the notes to generate, given by semitones from f0
        :param list_of_durations: the durations of each note
        :return: an array with the resulting sine waves ordered
        """
        generated_notes = []
        print("hi")
        print(f"{range(len(list_of_semitones))}")
        print(f"{list_of_semitones}, {list_of_durations}")
        for i in range(len(list_of_semitones)):
            print("i")
            for j in range(len(list_of_semitones[i])):
                print("j")
                note = self.generate_wave(self.get_frequency(list_of_semitones[i][j]), list_of_durations[i])
                print(f"i: {i}, j: {j}, semitone: {list_of_semitones[i][j]}, duration: {list_of_durations[i]}")
                generated_notes.append(note)
            #generate a rest
            rest = self.generate_wave(0, 0.5)
            generated_notes.append(rest)

        wav = wave.open(f'sound_full.wav', 'w')
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
        return self.f0 * (2 ** (n/12))





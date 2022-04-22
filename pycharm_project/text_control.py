from audio_control import AudioControl


class TextControl:
    def __init__(self, f0, r, max_time, c0):
        """
        Initializes the TextControl object and constants.
        :param f0: the base frequency of the sound
        :param r: sampling rate
        :param max_time: the maximum length of the resulting sound clip
        :param c0: the base character for the ascii
        """
        self.audio_control = AudioControl(f0, r, max_time)
        self.c0 = c0

    def convert_text_to_wav(self, text, wav_name):
        """
        Converts given text to a wav file.
        :param text: The text to convert.
        :param wav_name: The file name for the wav file.
        :return: Nothing.
        """
        print(f"Converting \"{text}\" into a wav file ...")

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

        #determine the duration of each note and each rest

        #convert words to notes
        notes = []
        durations = []
        for word in words:
            if len(word) != 0:
                notes.append(self.convert_word_to_semitones(word))
                durations.append(1/len(word))

        #play the notes
        self.audio_control.generate_sound(notes, durations, wav_name)

        print("Converted.")

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


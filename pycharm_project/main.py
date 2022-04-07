from audio_control import AudioControl

print("Hello world!")
a = AudioControl(440, 44100, 20)
a.generate_sound([0, 3, 1, 5, 3], [1, 2, 1, 0.5, 1], 1)


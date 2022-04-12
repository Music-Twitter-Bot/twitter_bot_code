from audio_control import AudioControl

print("Hello world!")
a = AudioControl(440, 44100, 20, "a")
a.convert_text_to_wav("Hello how are you today?!")


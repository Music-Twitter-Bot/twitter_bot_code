from audio_control import AudioControl
import ffmpeg

print("Hello world!")
a = AudioControl(440, 44100, 20, "a")
a.convert_text_to_wav("Hello how are you today?!")

#convert wav to mp4

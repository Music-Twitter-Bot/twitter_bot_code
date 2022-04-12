import ffmpy
from audio_control import AudioControl

import ffmpeg
from ffmpy import FFmpeg


a = AudioControl(440, 44100, 20, "a")
a.convert_text_to_wav("Hello how are you today?!")

#convert wav to mp4
audio_file = "sound_full.wav"
image_file = "image.jpg"
ff = ffmpy.FFmpeg(executable='ffmpeg/ffmpeg.exe', inputs={'sound_full.wav': None}, outputs={'video.mp4': ["-filter:a", "atempo=0.5"]})
ff.run()


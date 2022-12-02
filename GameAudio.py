import board
import audiocore
import audioio
import digitalio

# Required for CircuitPlayground Express to play sounds
speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.switch_to_output(value=True)
a = audioio.AudioOut(board.SPEAKER)

pathA = "RPG_CPX_ME30_Project/audio/"

# def play_sound(filename):
#     with open (pathA + filename, "rb") as wave_file:
#         wave = audiocore.WaveFile(wave_file)
#         a = audioio.AudioOut(board.SPEAKER)
#         a.play(wave)
#     return a
# with open (pathA + sounds[0], "rb") as wave_file:
#     wave = audiocore.WaveFile(wave_file)
# a = audioio.AudioOut(board.SPEAKER)
# a.play(wave)
# data = open(pathA + sounds[0], "rb")
# wave = audiocore.WaveFile(data)
# a.play(wave)

# play_sound(sounds[0])

class Audio:
    '''Creates Audio Object'''
    def __init__(self, muted = False):
        self.muted = muted
    def play_sound(self, filename):
        if not self.muted:
            data = open(pathA + filename, "rb")
            wave = audiocore.WaveFile(data)
            a.play(wave)

    def play_sound_rand(self, filename):
        pass
    def isPlaying(self):
        return a.playing

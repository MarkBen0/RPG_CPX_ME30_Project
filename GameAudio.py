import board
import audiocore
import audioio
import digitalio

# Required for CircuitPlayground Express to play sounds
speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.switch_to_output(value=True)
a = audioio.AudioOut(board.SPEAKER)

# Path to audio folder
pathA = "RPG_CPX_ME30_Project/audio/"

class Audio:
    '''Creates Audio Object'''
    def __init__(self, muted = False):
        self.muted = muted
    def play_sound(self, filename):
        if not self.muted:
            data = open(pathA + filename, "rb")
            wave = audiocore.WaveFile(data)
            a.play(wave)
    #plays sound randomly
    def play_sound_rand(self, filename):
        pass
    def isPlaying(self):
        return a.playing

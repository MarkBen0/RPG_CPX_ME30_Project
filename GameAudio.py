import board
import time
import random
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
    randSoundRange = (.5, 2)
    def __init__(self, muted = False):
        self.muted = muted
        self.startTime = time.monotonic()
        self.endTime = random.uniform(self.randSoundRange[0], self.randSoundRange[1])
    def play_sound(self, filename):
        if not self.muted:
            data = open(pathA + filename, "rb")
            wave = audiocore.WaveFile(data)
            a.play(wave)
    #plays sound randomly
    def play_sound_rand(self, *filename):
        if (time.monotonic() - self.startTime) > self.endTime and not a.playing:
            self.play_sound(filename[random.randrange(len(filename))])
            self.startTime = time.monotonic()
            self.endTime = random.uniform(self.randSoundRange[0], self.randSoundRange[1])
    def isPlaying(self):
        return a.playing

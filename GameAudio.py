import board
import audiocore
import audioio
import digitalio

# Required for CircuitPlayground Express to play sounds
speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.switch_to_output(value=True)
a = audioio.AudioOut(board.SPEAKER)

pathA = "RPG_CPX_ME30_Project/audio/"

sounds = [#"HinaCC0_011_Fallen_leaves_comp(2).wav",
            "Step1.wav",
            "Step2.wav"]


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
    def play_sound(filename):
        data = open(pathA + filename, "rb")
        wave = audiocore.WaveFile(data)
        a.play(wave)

    def isPlaying():
        return a.playing

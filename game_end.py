from RPG_CPX_ME30_Project import GameAudio
p=GameAudio.Audio()
class game_end:
    # Write your code here :-)
    def __init__(self,pixels,buttonA):
        self.pixels=pixels
        self.Button_A=buttonA
    def wining(self):
        p.play_sound("Wow.wav")

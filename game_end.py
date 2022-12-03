from RPG_CPX_ME30_Project import GameAudio
import supervisor
import time
p=GameAudio.Audio()
class game_end:
    # Write your code here :-)
    def __init__(self,pixels,buttonA):
        self.pixels=pixels
        self.win=False
        self.lose=False
        self.Button_A=buttonA
    def reset(self):
        supervisor.reload()
    def coloring(self):
        if self.win:
            self.pixels.fill((255,255,255))
            pass
        elif self.lose:
            self.pixels.fill((255,0,0))
            pass
        self.pixels.show()
    def wining(self):
        p.play_sound("Wow.wav")
        self.win=True
        self.coloring()
        while True:
            #print("Wining")
            self.pixels
            time.sleep(.5)
            if self.Button_A.value:
                #time.sleep(2)
                self.reset()
    def losing(self):
        self.lose=True
        self.coloring()
        while True:
            time.sleep(1)
            if self.Button_A.value:
                self.reset()

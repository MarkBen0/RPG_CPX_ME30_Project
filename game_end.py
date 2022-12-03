import supervisor
import time

supervisor.disable_autoreload()

class game_end:
    # Write your code here :-)
    def __init__(self,pixels,buttonA,AudioObj):
        self.pixels=pixels
        self.win=False
        self.lose=False
        self.Button_A=buttonA
        self.p=AudioObj
    def wining(self):
        self.p.play_sound("Wow.wav")
        self.pixels.fill((255,255,255))
        self.pixels.show()
        while True:
            #print("Wining")
            time.sleep(.5)
            if self.Button_A.value:
                #time.sleep(2)
                supervisor.reload()
    def losing(self):
        self.p.play_sound("BigL.wav")
        self.pixels.fill((255,0,0))
        self.pixels.show()
        while True:
            time.sleep(1)
            if self.Button_A.value:
                supervisor.reload()

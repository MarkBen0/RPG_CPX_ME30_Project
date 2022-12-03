import supervisor

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
            if self.Button_A.value:
                #time.sleep(2)
                supervisor.reload()
    def losing(self):
        self.p.play_sound("BigL.wav")
        self.pixels.fill((255,0,0))
        self.pixels.show()
        while True:
            if self.Button_A.value:
                supervisor.reload()

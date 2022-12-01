import math
# import board
# import audiocore
# import audioio
# import digitalio
from RPG_CPX_ME30_Project import GameAudio

p = GameAudio.Audio()
# speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
# speaker_enable.switch_to_output(value=True)
# a = audioio.AudioOut(board.SPEAKER)

# pathA = "RPG_CPX_ME30_Project/audio/"

# sounds = [#"HinaCC0_011_Fallen_leaves_comp(2).wav",
#             "Step1.wav",
#             "Step2.wav"]
class Player:
    '''Creates and handles the player'''
    def __init__(self, pos, player_scale, sensitivity, speed, land, facing = 0):
        self.pos = pos
        self.facing = facing + -(math.pi)/2
        self.player_scale = player_scale
        self.sensitivity = sensitivity
        self.speed = speed
        self.foot = True
        self.land = land

    def move(self, deltaTime):
        xDel = (math.cos(self.facing-((math.pi)/2))*self.speed)*deltaTime+self.pos[0]
        yDel = (math.sin(self.facing-((math.pi)/2))*self.speed)*deltaTime+self.pos[1]
        hitWall = False
        if self.land[int(self.pos[0])][int(yDel)] == 1:
            yDel = self.pos[1]
            hitWall = True
        if self.land[int(xDel)][int(self.pos[1])] == 1:
            xDel = self.pos[0]
            hitWall = True
        self.pos = [xDel, yDel]
        if self.land[int(self.pos[0])][int(self.pos[1])] == 2:
            print("enter Battle")
            self.B.startBattle()
        if(not p.isPlaying()) and (not hitWall):
            if self.foot:
                p.play_sound("Step1.wav")
                self.foot = not self.foot
            else:
                p.play_sound("Step2.wav")
                self.foot = not self.foot

        print(self.pos)
        #print(dim)
        print(self.facing*(180/math.pi))

    def turn(self, direction, deltaTime):
        if direction == "Right":
            self.facing -= self.sensitivity*deltaTime
            if self.facing < -math.pi:
                self.facing += 2*math.pi
        elif direction == "Left":
            self.facing += self.sensitivity*deltaTime
            if self.facing > math.pi:
                self.facing -= 2*math.pi
    def battleObject(self, Bobject):
        self.B = Bobject
class Enemy:
    pass


import math
import time
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
    def __init__(self, world, player_scale, sensitivity, speed, facing = 0, LightScale = 2.5, shadeLim = .05):
        self.world = world
        self.pos = world[0][0]
        self.room = world[0][1]
        self.facing = facing + -(math.pi)/2
        self.player_scale = player_scale
        self.sensitivity = sensitivity
        self.speed = speed
        self.foot = True
        self.LightScale = LightScale
        self.shadeLim = shadeLim
        self.roomNum = 0
        self.deltaTime = 1

    def move(self):
        xDel = (math.cos(self.facing-((math.pi)/2))*self.speed)*self.deltaTime+self.pos[0]
        yDel = (math.sin(self.facing-((math.pi)/2))*self.speed)*self.deltaTime+self.pos[1]
        hitWall = False
        if self.room[int(self.pos[0])][int(yDel)] == 1:
            yDel = self.pos[1]
            hitWall = True
        if self.room[int(xDel)][int(self.pos[1])] == 1:
            xDel = self.pos[0]
            hitWall = True
        self.pos = (xDel, yDel)
        if self.room[int(self.pos[0])][int(self.pos[1])] == 2:
            print("enter Battle")
            self.B.startBattle()
            self.room[int(self.pos[0])][int(self.pos[1])] = 0
        if self.room[int(self.pos[0])][int(self.pos[1])] == 3:
            print("Next floor")
            self.roomNum += 1
            print(self.roomNum)
            self.pos = self.world[self.roomNum][0]
            self.room = self.world[self.roomNum][1]
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

    def turn(self, direction):
        if direction == "Right":
            self.facing -= self.sensitivity*self.deltaTime
            if self.facing < -math.pi:
                self.facing += 2*math.pi
        elif direction == "Left":
            self.facing += self.sensitivity*self.deltaTime
            if self.facing > math.pi:
                self.facing -= 2*math.pi

    def display(self, tiles, pixels):
        startF = time.monotonic_ns()
        dist = []
        tint = []
        for i in range(12):
            tint.append(((math.sin((math.cos(((math.pi*i)/6)+self.facing)*self.player_scale+self.pos[0])*self.LightScale)+math.cos((math.sin(((math.pi*i)/6)+self.facing)*self.player_scale+self.pos[1])*self.LightScale))/4)+.5)
            try:
                dist.append(self.room[int(math.cos(((math.pi*i)/6)+self.facing)*self.player_scale+self.pos[0])][int(math.sin(((math.pi*i)/6)+self.facing)*self.player_scale+self.pos[1])])
            except IndexError:
                dist.append(1)
        for i in range(5):
            shade = tint[i+1]
            if shade < self.shadeLim:
                shade =self.shadeLim
            pixels[i] = (tiles[dist[i+1]][0]*shade, tiles[dist[i+1]][1]*shade, tiles[dist[i+1]][2]*shade)
        for i in range(5, 10):
            shade = tint[i+2]
            if shade < self.shadeLim:
                shade = self.shadeLim
            pixels[i] = (tiles[dist[i+2]][0]*shade, tiles[dist[i+2]][1]*shade, tiles[dist[i+2]][2]*shade)
        pixels.show()
        if 2 in dist:
            p.play_sound_rand("Monster.wav")
        #return room[p[0]][p[1]]
        endF = time.monotonic_ns()
        self.deltaTime = (endF-startF)/(10**9)
        return (dist, tint)
    def battleObject(self, Bobject):
        self.B = Bobject
# class Player:
#     '''Creates and handles the player'''
#     def __init__(self, pos, player_scale, sensitivity, speed, land, facing = 0):
#         self.pos = pos
#         self.facing = facing + -(math.pi)/2
#         self.player_scale = player_scale
#         self.sensitivity = sensitivity
#         self.speed = speed
#         self.foot = True
#         self.land = land

#     def move(self, self.deltaTime):
#         xDel = (math.cos(self.facing-((math.pi)/2))*self.speed)*self.deltaTime+self.pos[0]
#         yDel = (math.sin(self.facing-((math.pi)/2))*self.speed)*self.deltaTime+self.pos[1]
#         hitWall = False
#         if self.land[int(self.pos[0])][int(yDel)] == 1:
#             yDel = self.pos[1]
#             hitWall = True
#         if self.land[int(xDel)][int(self.pos[1])] == 1:
#             xDel = self.pos[0]
#             hitWall = True
#         self.pos = [xDel, yDel]
#         if self.land[int(self.pos[0])][int(self.pos[1])] == 2:
#             print("enter Battle")
#             self.B.startBattle()
#         if(not p.isPlaying()) and (not hitWall):
#             if self.foot:
#                 p.play_sound("Step1.wav")
#                 self.foot = not self.foot
#             else:
#                 p.play_sound("Step2.wav")
#                 self.foot = not self.foot

#         print(self.pos)
###        print(dim)
#         print(self.facing*(180/math.pi))

#     def turn(self, direction, self.deltaTime):
#         if direction == "Right":
#             self.facing -= self.sensitivity*self.deltaTime
#             if self.facing < -math.pi:
#                 self.facing += 2*math.pi
#         elif direction == "Left":
#             self.facing += self.sensitivity*self.deltaTime
#             if self.facing > math.pi:
#                 self.facing -= 2*math.pi
#     def battleObject(self, Bobject):
#         self.B = Bobject
class Enemy:
    pass


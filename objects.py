import math
import time
from RPG_CPX_ME30_Project import GameAudio

p = GameAudio.Audio(True)

class Player:
    '''Creates and handles the player'''
    def __init__(self, world, player_scale, sensitivity, speed, facing = 0):
        self.world = world
        self.pos = world[0][0]
        self.room = world[0][1]
        self.facing = facing + -(math.pi)/2
        self.player_scale = player_scale
        self.sensitivity = sensitivity
        self.speed = speed
        self.foot = True
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
            self.B.startBattle()
            self.room[int(self.pos[0])][int(self.pos[1])] = 0
        if self.room[int(self.pos[0])][int(self.pos[1])] == 3:
            self.roomNum += 1
            print(f"Next floor. Floor {self.roomNum}")
            p.play_sound("TravelV2.wav")
            time.sleep(.5)
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
        for i in range(12):
            try:
                dist.append(self.room[int(math.cos(((math.pi*i)/6)+self.facing)*self.player_scale+self.pos[0])][int(math.sin(((math.pi*i)/6)+self.facing)*self.player_scale+self.pos[1])])
            except IndexError:
                dist.append(1)
        for i in range(5):
            pixels[i] = (tiles[dist[i+1]][0], tiles[dist[i+1]][1], tiles[dist[i+1]][2])
        for i in range(5, 10):
            pixels[i] = (tiles[dist[i+2]][0], tiles[dist[i+2]][1], tiles[dist[i+2]][2])
        pixels.show()
        if 2 in dist:
            p.play_sound_rand("mnstr1.wav", "mnstr4.wav")
        #return room[p[0]][p[1]]
        endF = time.monotonic_ns()
        self.deltaTime = (endF-startF)/(10**9)
    def battleObject(self, Bobject):
        self.B = Bobject


#from adafruit_circuitplayground import cp
from RPG_CPX_ME30_Project import objects
from RPG_CPX_ME30_Project import Battle
#from RPG_CPX_ME30_Project import GameAudio
import board
import digitalio
import neopixel
import adafruit_lis3dh
import busio
#import time
import math

#p = GameAudio.Audio()

button_b = digitalio.DigitalInOut(board.BUTTON_B)
button_b.switch_to_input(pull=digitalio.Pull.DOWN)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)

i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)  # uses board.SCL and board.SDA
int1 = digitalio.DigitalInOut(board.ACCELEROMETER_INTERRUPT)
accelerometer = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19, int1=int1)
accelerometer.range = adafruit_lis3dh.RANGE_8_G



pixels.brightness = .1
world = {0 :
        ((2.5, 2.5),
        [[1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 3, 3, 3, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]]),
        1 :
        ((1.5, 1.5),
        [[1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 2, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 2, 0, 1, 0, 1, 1],
        [1, 1, 0, 1, 0, 1, 1],
        [1, 2, 0, 0, 2, 3, 1],
        [1, 1, 1, 1, 2, 1, 1]])
        }
tiles = {0: (0, 255, 0), 1: (10, 130, 220), 2: (255, 0, 0), 3: (0, 0, 0)}
#deltaTime = 1
# pos = [2.5, 2.5]
# facing = -(math.pi)/2
# player_scale = .75
# foot = True

##################################Player_Object######################################
# class Player:
#     '''Creates and handles the player'''
#     def __init__(self, room, player_scale, sensitivity, speed, facing = 0, LightScale = 2.5, shadeLim = .05):
#         self.pos = room[0]
#         self.room = room[1]
#         self.facing = facing + -(math.pi)/2
#         self.player_scale = player_scale
#         self.sensitivity = sensitivity
#         self.speed = speed
#         self.foot = True
#         self.LightScale = LightScale
#         self.shadeLim = shadeLim
#         self.roomNum = 0

#     def move(self):
#         xDel = (math.cos(self.facing-((math.pi)/2))*self.speed)*deltaTime+self.pos[0]
#         yDel = (math.sin(self.facing-((math.pi)/2))*self.speed)*deltaTime+self.pos[1]
#         hitWall = False
#         if self.room[int(self.pos[0])][int(yDel)] == 1:
#             yDel = self.pos[1]
#             hitWall = True
#         if self.room[int(xDel)][int(self.pos[1])] == 1:
#             xDel = self.pos[0]
#             hitWall = True
#         self.pos = (xDel, yDel)
#         if self.room[int(self.pos[0])][int(self.pos[1])] == 2:
#             print("enter Battle")
#             self.B.startBattle()
#             self.room[int(self.pos[0])][int(self.pos[1])] = 0
#         if self.room[int(self.pos[0])][int(self.pos[1])] == 3:
#             print("Next floor")
#             self.roomNum += 1
#             print(self.roomNum)
#             self.pos = world[self.roomNum][0]
#             self.room = world[self.roomNum][1]
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

#     def turn(self, direction):
#         if direction == "Right":
#             self.facing -= self.sensitivity*deltaTime
#             if self.facing < -math.pi:
#                 self.facing += 2*math.pi
#         elif direction == "Left":
#             self.facing += self.sensitivity*deltaTime
#             if self.facing > math.pi:
#                 self.facing -= 2*math.pi

#     def display(self):
#         dist = []
#         tint = []
#         for i in range(12):
#             tint.append(((math.sin((math.cos(((math.pi*i)/6)+self.facing)*self.player_scale+self.pos[0])*self.LightScale)+math.cos((math.sin(((math.pi*i)/6)+self.facing)*self.player_scale+self.pos[1])*self.LightScale))/4)+.5)
#             try:
#                 dist.append(self.room[int(math.cos(((math.pi*i)/6)+self.facing)*self.player_scale+self.pos[0])][int(math.sin(((math.pi*i)/6)+self.facing)*self.player_scale+self.pos[1])])
#             except IndexError:
#                 dist.append(1)
#         for i in range(5):
#             shade = tint[i+1]
#             if shade < self.shadeLim:
#                 shade =self.shadeLim
#             pixels[i] = (tiles[dist[i+1]][0]*shade, tiles[dist[i+1]][1]*shade, tiles[dist[i+1]][2]*shade)
#         for i in range(5, 10):
#             shade = tint[i+2]
#             if shade < self.shadeLim:
#                 shade = self.shadeLim
#             pixels[i] = (tiles[dist[i+2]][0]*shade, tiles[dist[i+2]][1]*shade, tiles[dist[i+2]][2]*shade)
#         pixels.show()
#         if 2 in dist:
#             p.play_sound_rand("Monster.wav")
###        return room[p[0]][p[1]]
#         return (dist, tint)
#     def battleObject(self, Bobject):
#         self.B = Bobject
#####################################################################################

# LightScale = 2.5
# shadeLim = .05
# sensitivity = 1.2
# speed = 1.2
hero = objects.Player(world, player_scale = .75, sensitivity = 1.2, speed = 1.2)
enemy = None
B = Battle.BattleHandler(hero, enemy, pixels)
hero.battleObject(B)
# while True:
#     x, y, z = cp.acceleration
#     print((y, ))
#     time.sleep(.05)

# def display(p, room, facing):
#     dist = []
#     tint = []
#     for i in range(12):
#         tint.append(((math.sin((math.cos(((math.pi*i)/6)+facing)*hero.player_scale+p[0])*LightScale)+math.cos((math.sin(((math.pi*i)/6)+facing)*hero.player_scale+p[1])*LightScale))/4)+.5)
#         try:
#             dist.append(room[int(math.cos(((math.pi*i)/6)+facing)*hero.player_scale+p[0])][int(math.sin(((math.pi*i)/6)+facing)*hero.player_scale+p[1])])
#         except IndexError:
#             dist.append(1)
#     for i in range(5):
#         shade = tint[i+1]
#         if shade < shadeLim:
#             shade = shadeLim
#         pixels[i] = (tiles[dist[i+1]][0]*shade, tiles[dist[i+1]][1]*shade, tiles[dist[i+1]][2]*shade)
#     for i in range(5, 10):
#         shade = tint[i+2]
#         if shade < shadeLim:
#             shade = shadeLim
#         pixels[i] = (tiles[dist[i+2]][0]*shade, tiles[dist[i+2]][1]*shade, tiles[dist[i+2]][2]*shade)
#     pixels.show()
###    return room[p[0]][p[1]]
#     return (dist, tint)

#print(hero.display())
while True:
    #startF = time.monotonic_ns()
    dim = hero.display(tiles, pixels)[1]
    if button_b.value:
        hero.move()
    x, y, z = accelerometer.acceleration
    if(y >= 3):
        hero.turn("Right")
        print(hero.pos)
        print(hero.facing*(180/math.pi))
    if(y <= -3):
        hero.turn("Left")
        print(hero.pos)
        print(hero.facing*(180/math.pi))
#     endF = time.monotonic_ns()
#     FPS = (1/((endF-startF)/(10**9)))
    ##print(FPS)
#     deltaTime = 1/FPS


#from adafruit_circuitplayground import cp
from RPG_CPX_ME30_Project import objects
from RPG_CPX_ME30_Project import Battle
import board
import digitalio
import neopixel
import adafruit_lis3dh
import busio
import time
import math

button_b = digitalio.DigitalInOut(board.BUTTON_B)
button_b.switch_to_input(pull=digitalio.Pull.DOWN)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)

i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)  # uses board.SCL and board.SDA
int1 = digitalio.DigitalInOut(board.ACCELEROMETER_INTERRUPT)
accelerometer = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19, int1=int1)
accelerometer.range = adafruit_lis3dh.RANGE_8_G

pixels.brightness = .1

world = ((1, 1, 1, 1, 1, 1, 1),
        (1, 0, 0, 0, 0, 0, 1),
        (1, 0, 0, 0, 0, 0, 1),
        (1, 0, 0, 2, 0, 0, 1),
        (1, 0, 0, 0, 0, 0, 1),
        (1, 0, 0, 0, 0, 0, 1),
        (1, 1, 1, 1, 1, 1, 1))
tiles = {0: (0, 255, 0), 1: (255, 0, 0), 2: (0, 0, 255)}
deltaTime = 1
# pos = [2.5, 2.5]
# facing = -(math.pi)/2
# player_scale = .75
# foot = True
Lscale = 2.5
shadeLim = .05
# sensitivity = 1.2
# speed = 1.2
hero = objects.Player([2.5, 2.5], player_scale = .75, sensitivity = 1.2, speed = 1.2, land = world)
enemy = objects.Enemy
B = Battle.BattleHandler(hero, enemy, pixels)
hero.battleObject(B)
# while True:
#     x, y, z = cp.acceleration
#     print((y, ))
#     time.sleep(.05)

def display(p, area, angle):
    dist = []
    tint = []
    for i in range(12):
        tint.append(((math.sin((math.cos(((math.pi*i)/6)+angle)*hero.player_scale+p[0])*Lscale)+math.cos((math.sin(((math.pi*i)/6)+angle)*hero.player_scale+p[1])*Lscale))/4)+.5)
        try:
            dist.append(area[int(math.cos(((math.pi*i)/6)+angle)*hero.player_scale+p[0])][int(math.sin(((math.pi*i)/6)+angle)*hero.player_scale+p[1])])
        except IndexError:
            dist.append(1)
    for i in range(5):
        shade = tint[i+1]
        if shade < shadeLim:
            shade = shadeLim
        pixels[i] = (tiles[dist[i+1]][0]*shade, tiles[dist[i+1]][1]*shade, tiles[dist[i+1]][2]*shade)
    for i in range(5, 10):
        shade = tint[i+2]
        if shade < shadeLim:
            shade = shadeLim
        pixels[i] = (tiles[dist[i+2]][0]*shade, tiles[dist[i+2]][1]*shade, tiles[dist[i+2]][2]*shade)
    pixels.show()
    #return area[p[0]][p[1]]
    return (dist, tint)

print(display(hero.pos, world, hero.facing))
while True:
    startF = time.monotonic_ns()
    dim = display(hero.pos, world, hero.facing)[1]
    if button_b.value:
        hero.move(deltaTime)
    x, y, z = accelerometer.acceleration
    if(y >= 3):
        hero.turn("Right", deltaTime)
        print(hero.pos)
        print(hero.facing*(180/math.pi))
    if(y <= -3):
        hero.turn("Left", deltaTime)
        print(hero.pos)
        print(hero.facing*(180/math.pi))
    endF = time.monotonic_ns()
    FPS = (1/((endF-startF)/(10**9)))
    #print(FPS)
    deltaTime = 1/FPS


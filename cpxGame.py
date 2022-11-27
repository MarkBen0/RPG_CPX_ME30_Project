#from adafruit_circuitplayground import cp
import board
import audiocore
import audioio
import digitalio
import neopixel
import adafruit_lis3dh
import busio
import time
import math

# Required for CircuitPlayground Express
speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.switch_to_output(value=True)
a = audioio.AudioOut(board.SPEAKER)

button_b = digitalio.DigitalInOut(board.BUTTON_B)
button_b.switch_to_input(pull=digitalio.Pull.DOWN)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)

i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)  # uses board.SCL and board.SDA
int1 = digitalio.DigitalInOut(board.ACCELEROMETER_INTERRUPT)
accelerometer = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19, int1=int1)
accelerometer.range = adafruit_lis3dh.RANGE_8_G

pathA = "RPG_CPX_ME30_Project/audio/"

sounds = ["HinaCC0_011_Fallen_leaves_comp(2).wav",
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

#play_sound(sounds[0])


pixels.brightness = .1

world = ((1, 1, 1, 1, 1, 1, 1),
        (1, 0, 0, 0, 0, 0, 1),
        (1, 0, 0, 0, 0, 0, 1),
        (1, 0, 0, 2, 0, 0, 1),
        (1, 0, 0, 0, 0, 0, 1),
        (1, 0, 0, 0, 0, 0, 1),
        (1, 1, 1, 1, 1, 1, 1))
deltaTime = 1
pos = [2.5, 2.5]
facing = -(math.pi)/2
player_scale = .75
foot = True
Lscale = 2.5
shadeLim = .05
sensitivity = 1.2
speed = 1.2
tiles = {0: (0, 255, 0), 1: (255, 0, 0), 2: (0, 0, 255)}
# while True:
#     x, y, z = cp.acceleration
#     print((y, ))
#     time.sleep(.05)

def display(p, area, angle):
    dist = []
    tint = []
    for i in range(12):
        tint.append(((math.sin((math.cos(((math.pi*i)/6)+angle)*player_scale+p[0])*Lscale)+math.cos((math.sin(((math.pi*i)/6)+angle)*player_scale+p[1])*Lscale))/4)+.5)
        try:
            dist.append(area[int(math.cos(((math.pi*i)/6)+angle)*player_scale+p[0])][int(math.sin(((math.pi*i)/6)+angle)*player_scale+p[1])])
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

print(display(pos, world, facing))
while True:
    startF = time.monotonic_ns()
    dim = display(pos, world, facing)[1]
    if button_b.value:
        xDel = (math.cos(facing-((math.pi)/2))*speed)*deltaTime+pos[0]
        yDel = (math.sin(facing-((math.pi)/2))*speed)*deltaTime+pos[1]
        hitWall = False
        if world[int(pos[0])][int(yDel)] == 1:
            yDel = pos[1]
            hitWall = True
        if world[int(xDel)][int(pos[1])] == 1:
            xDel = pos[0]
            hitWall = True
        pos = [xDel, yDel]
        if world[int(pos[0])][int(pos[1])] == 1:
            print("enter Battle")
        if(not a.playing) and (not hitWall):
            if foot:
                data = open(pathA + sounds[1], "rb")
                wave = audiocore.WaveFile(data)
                a.play(wave)
                foot = not foot
            else:
                data = open(pathA + sounds[2], "rb")
                wave = audiocore.WaveFile(data)
                a.play(wave)
                foot = not foot
        # prevPos = pos
#         pos = [(math.cos(facing-((math.pi)/2))*speed)*deltaTime+pos[0], (math.sin(facing-((math.pi)/2))*speed)*deltaTime+pos[1]]
#         if(world[int(pos[0])][int(pos[1])] == 1):
#             pos = prevPos
        #pos[0] -= speed
        print(pos)
        #print(dim)
        print(facing*(180/math.pi))
    # if cp.button_a:
#         pos[0] += speed
#         print(pos)
    x, y, z = accelerometer.acceleration
    if(y >= 3):
        facing -= sensitivity*deltaTime#*abs(y/3)
        print(pos)
        print(facing*(180/math.pi))
    if(y <= -3):
        facing += sensitivity*deltaTime#*abs(y/3)
        print(pos)
        print(facing*(180/math.pi))
    endF = time.monotonic_ns()
    FPS = (1/((endF-startF)/(10**9)))
    #print(FPS)
    deltaTime = 1/FPS


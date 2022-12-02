from RPG_CPX_ME30_Project import objects
from RPG_CPX_ME30_Project import Battle
import board
import digitalio
import neopixel
import adafruit_lis3dh
import busio
import math

#Define button B for use of walking
button_b = digitalio.DigitalInOut(board.BUTTON_B)
button_b.switch_to_input(pull=digitalio.Pull.DOWN)

#Makes it so you can use the LEDs with pixel.show()
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)

#Makes it so you can use the accelerometer to turn
i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)  # uses board.SCL and board.SDA
int1 = digitalio.DigitalInOut(board.ACCELEROMETER_INTERRUPT)
accelerometer = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19, int1=int1)
accelerometer.range = adafruit_lis3dh.RANGE_8_G

pixels.brightness = .1

#World contains room layouts and room spawn
world = (((2.5, 2.5),#room 0 spawn
        #room 0
        [[1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 3, 3, 3, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]]),
        #room 1 spawn
        ((1.5, 1.5),
        #room 1
        [[1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 2, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 2, 0, 1, 0, 1, 1],
        [1, 1, 0, 1, 0, 1, 1],
        [1, 2, 0, 0, 2, 3, 1],
        [1, 1, 1, 1, 1, 1, 1]]),
        #room 2 spawn
        ((1.5, 1.5),
        #room 2
        [[1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 2, 1, 0, 2, 1, 1],
        [1, 0, 0, 1, 0, 0, 1, 1],
        [1, 0, 0, 0, 2, 0, 0, 1],
        [1, 0, 2, 0, 0, 0, 3, 1],
        [1, 0, 0, 1, 0, 0, 1, 1],
        [1, 0, 2, 1, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]])
        )

#Tile map
#floor, 0: Green
#wall, 1: Light Blue
#enemy, 2: Red
#stairs, 3: No color
tiles = {0: (0, 255, 0), 1: (10, 130, 220), 2: (255, 0, 0), 3: (0, 0, 0)}

#Hreo and Battle objects
hero = objects.Player(world, player_scale = .75, sensitivity = 1.2, speed = 1.2)
B = Battle.BattleHandler(pixels, hero.roomNum)
hero.battleObject(B)

#Main game loop
while True:
    #Render
    hero.display(tiles, pixels)

    #Movement
    if button_b.value:
        hero.move()
    x, y, z = accelerometer.acceleration
    if(y >= 3):
        hero.turn("Right")
        print(hero.pos)
        print(hero.facing*(180/math.pi))
    if(y <= -3):
        hero.turn("Left")
        #print(hero.pos)
        #print(hero.facing*(180/math.pi))
        print(hero.pos)
        print(hero.facing*(180/math.pi))
#     endF = time.monotonic_ns()
#     FPS = (1/((endF-startF)/(10**9)))
    ##print(FPS)
#     deltaTime = 1/FPS


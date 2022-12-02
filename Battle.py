import board
import digitalio
#import neopixel
import time

#pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)

button_a = digitalio.DigitalInOut(board.BUTTON_A)
button_a.switch_to_input(pull=digitalio.Pull.DOWN)

class BattleHandler:
    def __init__(self, player, enemy, Pixels):
        self.Pixels = Pixels
        self.player = player
        self.enemy = enemy
    def startBattle(self):
        self.Pixels.fill((100, 100, 100))
        self.Pixels.show()
        while True:
            time.sleep(1)
            print("worked")

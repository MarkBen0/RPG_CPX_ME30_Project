import board
import digitalio
#import neopixel
import time

#pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)

button_a = digitalio.DigitalInOut(board.BUTTON_A)
button_a.switch_to_input(pull=digitalio.Pull.DOWN)

<<<<<<< HEAD
=======
# pixels.brightness = .2
# pixels.fill((0, 0, 0))

## the timer for the game starts
'''timeStart = time.time() #the timer for the game starts
#the game starts for the player's attack
while True:
    #the charge up phase, if button a is pressed too early, no damage will be dealt to the enemy
    if ((time.time()-timeStart) > 0) and ((time.time()-timeStart) < 6):
        pass
        #cp.pixels.fill((100, 0, 0))
    #if the player doesn't press the button, no damage will be dealt to the enemy
    elif((time.time()-timeStart) > 9):
        print("Miss, no damage dealt")
        break
    #the attack is ready to be released when the light turns green
    elif((time.time()-timeStart) > 6):
        #pixels.fill((0, 0, 0))
        pass
        #pixels[2] = (0, 100, 0)
    if((button_a)):
        break


# different messages will be printed based on the timing of the button press letting the player know of the outcome
if time.time()-timeStart == 7:
    print("Critical Hit!")
elif time.time()-timeStart == 8:
    print("Nice! Reduced damage dealt.")
elif time.time()-timeStart < 7:
    print("Oh NO?!?!?!?!?! No damage dealt")'''
>>>>>>> aba65393425463b7131237f69bef69cf9859e896
class BattleHandler:
    def __init__(self, player, enemy, Pixels):
        self.Pixels = Pixels
        self.player = player
        self.enemy = enemy
    def startBattle(self):
        self.Pixels.fill((100, 100, 100))
        self.Pixels.show()
<<<<<<< HEAD
        while True:
            time.sleep(1)
            print("worked")
=======
        time.sleep(1)
>>>>>>> aba65393425463b7131237f69bef69cf9859e896

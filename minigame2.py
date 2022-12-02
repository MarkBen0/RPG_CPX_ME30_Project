import board
import digitalio
import neopixel
import time
import random

button_a = digitalio.DigitalInOut(board.BUTTON_A)
button_a.switch_to_input(pull=digitalio.Pull.DOWN)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)

pixels.brightness = .2

playerstats = {'level': 1, 'hp': 100, 'atk': 25, 'exp': 0}
levelexpthresholds = {1: 100, 2: 225, 3: 350, 4: 475, 5: 600, 6: 725, 7: 850, 8: 975}
monsterstats = {'name': 'Goblin', 'hp': 50, 'atk': 10, 'exp_drop': 25}
monster_list = [{'name': 'Goblin', 'hp': 50, 'atk': 10, 'exp_drop': 25},{'name': 'Skeleton', 'hp': 75, 'atk': 15, 'exp_drop': 40},{'name': 'Slime', 'hp': 25, 'atk': 5, 'exp_drop': 10}, {'name': 'Minotaur', 'hp': 125, 'atk': 25, 'exp_drop': 100}, {'name': 'Werewolf', 'hp': 155, 'atk': 20, 'exp_drop': 150}]

def combat(php, monster):
    print(f'A {monster['name']} stands in your way!')
    global monsterstats
    global playerstats
    global pixels
    global button_a
    monsterstats.update(monster)

    monster_hp = monsterstats['hp']
    turn = 0

    while True:

        #YOUR TURN
        while turn == 0:
            #CHECK FOR DEATH
            if php <= 0:
                print('\nYOU DIED')
                turn = 3
                break

            print('\nIt is your turn. GET READY!!!')
            timeStart = time.time()

            while True:
                while((time.time()-timeStart) > 0) and ((time.time()-timeStart) < 6):
                    pixels.fill((100, 0, 0))
                    pixels.show()
                if((time.time()-timeStart) > 9):
                    print("\nYou missed!!!")
                    break
                elif((time.time()-timeStart) > 6):
                    pixels.fill((0, 0, 0))
                    pixels[2] = (0, 100, 0)
                    pixels.show()
                if((button_a.value)):
                    break

            #CHECK HIT LEVEL
            if time.time()-timeStart == 7:
                print("\nCritical Hit!")
                monster_hp -= playerstats['atk'] + 25
            elif time.time()-timeStart <= 9:
                print("\nNice! Reduced damage dealt.")
                monster_hp -= playerstats['atk']
            else:
                print("\nOh NO?!?!?!?!?! No damage dealt")

            #CHECK FOR VICTORY
            if monster_hp > 0:
                print(f'The monster has {monster_hp} HP')
                print(f'You have {php} HP')
                turn = 1
            else:
                print('you won!')
                turn = 2
                break

        # MONSTER'S TURN
        while turn == 1:
            print('\nIt is the monsters turn')
            time.sleep(1)
            php -= monsterstats['atk']
            print(f'\nThe monster deals {monsterstats["atk"]} damage to you')
            print(f'\nThe monster has {monster_hp} HP')
            print(f'You have {php} HP')
            time.sleep(2)
            turn = 0

        # VICTORY
        if turn == 2:
            global updated_hp
            updated_hp = {'hp': php}
            updated_exp = {'exp': monsterstats['exp_drop']}
            playerstats.update(updated_hp)
            playerstats.update(updated_exp)
            break

        # DEATH
        if turn == 3:
            break


combat(playerstats['hp'], random.choice(monster_list))
print('\nCombat is over')
print(f'You have {playerstats['hp']} HP after that battle')
print(f'You have {playerstats['exp']} EXP')



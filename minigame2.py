from adafruit_circuitplayground import cp
import time

cp.pixels.brightness = .2

playerstats = {'level': 1, 'hp': 100, 'atk': 25, 'exp': 0}
levelexpthresholds = {1: 100, 2: 225, 3: 350, 4: 475, 5: 600, 6: 725, 7: 850, 8: 975}
monsterstats = {'name': 'placeholder', 'hp': 100, 'atk': 25, 'exp_drop': 25}

def combat(php):
    global monsterstats
    global playerstats

    monster_hp = monsterstats['hp']
    turn = 0
    while True:

        #YOUR TURN
        while turn == 0:
            #CHECK FOR DEATH
            if php <= 0:
                print ('\nYOU DIED')
                turn = 3
                break

            print('\nIt is your turn. GET READY!!!')
            timeStart = time.time()

            while True:
                if ((time.time()-timeStart) > 0) and ((time.time()-timeStart) < 6):
                    cp.pixels.fill((100, 0, 0))
                elif((time.time()-timeStart) > 9):
                    print("\nYou missed!!!")
                    break
                elif((time.time()-timeStart) > 6):
                    cp.pixels.fill((0, 0, 0))
                    cp.pixels[2] = (0, 100, 0)
                if((cp.button_a)):
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
                print ('you won!')
                turn = 2
                break

        # MONSTER'S TURN
        while turn == 1:
            print('\nIt is the monsters turn')
            time.sleep(1)
            php -= monsterstats['atk']
            print('\nThe monster deals 5 damage to you')
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

        #DEATH
        if turn == 3:
            break


combat(playerstats['hp'])
print('\nCombat is over')
print(f'You have {playerstats['hp']} HP after that battle')
print(f'You have {playerstats['exp']} EXP')




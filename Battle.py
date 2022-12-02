import board
import digitalio
import time
import random

button_a = digitalio.DigitalInOut(board.BUTTON_A)
button_a.switch_to_input(pull=digitalio.Pull.DOWN)

levelexpthresholds = {1: 100, 2: 225, 3: 350, 4: 475, 5: 600, 6: 725}
levelstats = [{'level': 1, 'hp': 100, 'atk': 10},{'level': 2, 'hp': 110, 'atk': 15},{'level': 3, 'hp': 125, 'atk': 25},{'level': 4, 'hp': 140, 'atk': 30},{'level': 5, 'hp': 150, 'atk': 40},{'level': 6, 'hp': 170, 'atk': 45}]
monster_list = [{'name': 'Goblin', 'hp': 50, 'atk': 10, 'exp_drop': 25},{'name': 'Skeleton', 'hp': 75, 'atk': 15, 'exp_drop': 40},{'name': 'Slime', 'hp': 25, 'atk': 5, 'exp_drop': 10}, {'name': 'Minotaur', 'hp': 125, 'atk': 25, 'exp_drop': 100}, {'name': 'Werewolf', 'hp': 155, 'atk': 20, 'exp_drop': 120}]

class BattleHandler:
    def __init__(self, pixels, room):
        self.room = room
        self.pixels = pixels
        self.player = {'level': 1, 'hp': 100, 'atk': 25, 'exp': 0}
        self.enemy = {'name': 'Goblin', 'hp': 50, 'atk': 10, 'exp_drop': 25}
    def startBattle(self):
        global monster_list
        global button_a
        global levelexpthresholds
        global levelstats
        self.enemy.update(random.choice(monster_list))
        print(f'A {self.enemy['name']} stands in your way!')

        php = self.player['hp']
        monster_hp = self.enemy['hp']
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
                        self.pixels.fill((100, 0, 0))
                        self.pixels.show()
                    if((time.time()-timeStart) > 9):
                        print("\nYou missed!!!")
                        break
                    elif((time.time()-timeStart) > 6):
                        self.pixels.fill((0, 0, 0))
                        self.pixels[2] = (0, 100, 0)
                        self.pixels.show()
                    if((button_a.value)):
                        break

                #CHECK HIT LEVEL
                if time.time()-timeStart == 7:
                    print(f"\nCritical Hit! {self.player['atk']} damage dealt")
                    monster_hp -= self.player['atk'] + 25
                    time.sleep(2)
                elif time.time()-timeStart <= 9:
                    print(f"\nNice! {self.player['atk']} damage dealt")
                    monster_hp -= self.player['atk']
                    time.sleep(2)
                else:
                    print("\nOh NO?!?!?!?!?! No damage dealt")

                #CHECK FOR VICTORY
                if monster_hp > 0:
                    print(f'The monster has {monster_hp} HP')
                    print(f'You have {php} HP')
                    time.sleep(3)
                    turn = 1
                else:
                    print('you won!')
                    time.sleep(1)
                    turn = 2
                    break

            # MONSTER'S TURN
            while turn == 1:
                print('\nIt is the monsters turn')
                time.sleep(1)
                php -= self.enemy['atk']
                print(f'\nThe monster deals {self.enemy["atk"]} damage to you')
                print(f'\nThe monster has {monster_hp} HP')
                print(f'You have {php} HP')
                time.sleep(3.5)
                turn = 0

            # VICTORY
            if turn == 2:
                global updated_hp
                updated_hp = {'hp': php}
                updated_exp = {'exp': self.enemy['exp_drop']}
                self.player.update(updated_hp)
                self.player.update(updated_exp)
                print(f'You gained {self.enemy['exp_drop']} experience points.')
                time.sleep(2.5)
                if self.player['exp'] >= levelexpthresholds[self.player['level']]:
                    self.player.update(levelstats[self.player['level']])
                    print(('You leveled up! Your attack power and HP increased. HP fully healed.'))
                    time.sleep(4)
                print(f'You have {self.player['hp']} HP.')
                break

            # DEATH
            if turn == 3:
                break

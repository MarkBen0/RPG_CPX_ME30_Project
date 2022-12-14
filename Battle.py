import time
import random

levelexpthresholds = {1: 100, 2: 225, 3: 350,}
levelstats = [{'level': 1, 'hp': 100, 'atk': 15},{'level': 2, 'hp': 125, 'atk': 25},{'level': 3, 'hp': 150, 'atk': 30}]
monster_list = [{'name': 'goblin', 'hp': 50, 'atk': 10, 'exp_drop': 35}, {'name': 'skeleton', 'hp': 75, 'atk': 15, 'exp_drop': 45}, {'name': 'troll', 'hp': 100, 'atk': 20, 'exp_drop': 70}, {'name': 'Minotaur', 'hp': 125, 'atk': 25, 'exp_drop': 80},]

class BattleHandler:
    def __init__(self, pixels, room, button_a, gameState, AudioObj):
        self.room = room
        self.pixels = pixels
        self.player = {'level': 1, 'hp': 100, 'atk': 15, 'exp': 0}
        self.enemy = {}
        self.button_a = button_a
        self.gameState = gameState
        self.p = AudioObj
    def startBattle(self):
        global monster_list
        global button_a
        global levelexpthresholds
        global levelstats
        self.enemy.update(random.choice(monster_list))
        self.p.play_sound('alert.wav')
        print(f'A {self.enemy["name"]} stands in your way!')

        php = self.player['hp']
        monster_hp = self.enemy['hp']
        turn = 0

        while True:

            #YOUR TURN
            while turn == 0:
                #CHECK FOR DEATH
                if php <= 0:
                    print('\nYOU DIED! Game Over...')
                    turn = 3
                    break

                print('\nIt is your turn. GET READY!!!')
                timeStart = time.time()

                while True:
                    while((time.time()-timeStart) > 0) and ((time.time()-timeStart) < 6):
                        self.pixels.fill((100, 0, 0))
                        self.pixels.show()
                    if((time.time()-timeStart) > 7):
                        break
                    elif((time.time()-timeStart) > 6):
                        self.pixels.fill((100, 0, 0))
                        self.pixels[2] = (0, 100, 0)
                        self.pixels.show()
                    if((self.button_a.value)):
                        break

                #CHECK HIT LEVEL
                if time.time()-timeStart == 7:
                    self.p.play_sound('hit.wav')
                    print(f"\nCritical Hit! {self.player['atk']+20} damage dealt")
                    monster_hp -= self.player['atk'] + 20
                    time.sleep(2)
                elif time.time()-timeStart <= 7:
                    print(f"\nEarly! {self.player['atk']} damage dealt")
                    monster_hp -= self.player['atk']
                    time.sleep(2)
                else:
                    print("\nYou missed!! No damage dealt")

                #CHECK FOR VICTORY
                if monster_hp > 0:
                    print(f'The enemy has {monster_hp} HP')
                    print(f'You have {php} HP')
                    time.sleep(3)
                    turn = 1
                else:
                    print('\nYou won!')
                    time.sleep(1)
                    turn = 2
                    break

            # MONSTER'S TURN
            while turn == 1:
                print(f'\nIt is the {self.enemy["name"]}\'s turn')
                time.sleep(1)
                php -= self.enemy['atk']
                print(f'\nThe enemy deals {self.enemy["atk"]} damage to you')
                print(f'\nThe enemy has {monster_hp} HP')
                print(f'You have {php} HP')
                time.sleep(3.5)
                turn = 0

            # VICTORY
            if turn == 2:
                global updated_hp
                updated_hp = {'hp': php}
                updated_exp = {'exp': self.enemy['exp_drop'] + self.player["exp"]}
                self.player.update(updated_hp)
                self.player.update(updated_exp)
                print(f'You gained {self.enemy["exp_drop"]} experience points.')
                time.sleep(2.5)
                if self.player['exp'] >= levelexpthresholds[self.player['level']]:
                    self.player.update(levelstats[self.player['level']])
                    print(('You leveled up! Your attack power and HP increased. HP fully healed.'))
                    time.sleep(3)
                print(f'You have {self.player["hp"]} HP.')
                time.sleep(2)
                return

            # DEATH
            if turn == 3:
                self.gameState.losing()

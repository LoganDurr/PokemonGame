#Author Logan Durr
#Pokemon battle simulator that allows to players to select their own pokemon to battle against one another
#there are currently 22 pokemon in the game with the opportunity of added up to 152 all from the specific Kanto Region(Full list in Pokemon.txt)


from Pokemon import Pokemon
import Effectiveness
import random

class Battle():

    #constructor for battle class
    def __init__(self, pokemon, health, p_type, defense, attack, move1, move2, move3, move4, move_type1, move_type2, move_type3, move_type4):
        self.pokemon = pokemon
        self.health = health
        self.p_type = p_type
        self.defense = defense
        self.attack = attack
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4
        self.move_type1 = move_type1
        self.move_type2 = move_type2
        self.move_type3 = move_type3
        self.move_type4 = move_type4
    
    '''getters for battle class'''
    def getHealth(self):
        return self.health

    def getPokemonType(self):
        return self.p_type
    
    def getDefense(self):
        return self.defense

    def getAttack(self):
        return self.attack

    def getMove1(self):
        return self.move1

    def getMove2(self):
        return self.move2
    
    def getMove3(self):
        return self.move3

    def getMove4(self):
        return self.move4

    def getMoveType1(self):
        return self.move_type4

    '''Attack selection'''
    def playerAttack(self, choice):
        if choice == '1':
            return self.move1
        elif choice == '2':
            return self.move2
        elif choice == '3':
            return self.move3
        elif choice == '4':
            return self.move4

    '''Attack type'''
    def player_attackType(self, choice):
        if choice == '1':
            return self.move_type1
        elif choice == '2':
            return self.move_type2   
        elif choice == '3':
            return self.move_type3
        elif choice == '4':
            return self.move_type4

def calculateDamage(attacker_type, defender_type, attack, defense, power):
    critical = 20
    effectiveness = Effectiveness.effectivenessCalculator(attacker_type, defender_type)
    damage = (((22 * power * (attack / defense)) / 50) + 2) * effectiveness                #damage calculator
    rng = random.randint(0,45)                                                             #rng mechanic to determine if a hit was critical or not (1/45 chance)
    if rng == 1:
        damage += critical
    return damage
def healthAdjuster(damage, defender_health):
    #adjusts the health of the player that was just attacked
    defender_health -= damage
    if defender_health <= 0:
        return 0
    else:
        return defender_health       
    
'''Game'''
def main():
    '''Opening'''
    print('Welcome to the pokemon arena, here you will battle it out with another player.\nEach player chooses their own pokemon.')
    p1_name = input('Player 1, what is your name? ')
    p2_name = input('Player 2, what is your name? ')
    '''Type of pokemon'''
    p1_pokemon = input(p1_name + ' what pokemon will you choose? We are in the Kanto region. ').lower()
    p1 = Pokemon(p1_pokemon)
    exit = ''
    #tests to ensure the pokemon inputed is in the region
    while exit != 'y':
        if p1.pokemonChecker() == True:
            print(p1_pokemon, 'is a great choice! Best of luck!')
            exit = 'y'
        else:
            p1_pokemon = input('That pokemon is not from this region, select another and keep in mind we are in the Kanto region ').lower()
            p1 = Pokemon(p1_pokemon)
    p2_pokemon = input(p2_name + ' what pokemon will you choose? We are in the Kanto region. ').lower()
    p2 = Pokemon(p2_pokemon)
    exit2 = ''
    while exit2 != 'y':
        if p2.pokemonChecker() == True:
            print(p2_pokemon, 'is a great choice! Best of luck!')
            exit2 = 'y'
        else:
            p2_pokemon = input('That pokemon is not from this region, select another and keep in mind we are in the Kanto region ').lower()
            p2 = Pokemon(p2_pokemon)
    print('The stage is set, it is', p1_pokemon, 'vs', p2_pokemon + '.', 'Ready...Set...Fight!')
    #uses stack to transfer the data
    stats_list1 = []
    stats_list2 = []
    p1_stack = p1.getAttributes()
    p2_stack = p2.getAttributes()
    while p1_stack.is_empty() != True:
        stats_list1.append(p1_stack.pop())
    while p2_stack.is_empty() != True:
        stats_list2.append(p2_stack.pop())
    p1_B = Battle(p1_pokemon, stats_list1[11], stats_list1[10], stats_list1[9], stats_list1[8], stats_list1[7], stats_list1[6], stats_list1[5], stats_list1[4],  stats_list1[3], stats_list1[2], stats_list1[1], stats_list1[0])
    p2_B = Battle(p2_pokemon, stats_list2[11], stats_list2[10], stats_list2[9], stats_list2[8], stats_list2[7], stats_list2[6], stats_list2[5], stats_list2[4],  stats_list2[3], stats_list2[2], stats_list2[1], stats_list2[0])
    '''pokemon health'''
    p1_health = p1_B.getHealth()
    p2_health = p2_B.getHealth()
    '''pokemon type'''
    p1_type = p1_B.getPokemonType()
    p2_type = p2_B.getPokemonType()
    '''pokemon defense'''
    p1_defense = p1_B.getDefense()
    p2_defense = p2_B.getDefense()
    '''pokemon attack'''
    p1_base_attack = p1_B.getAttack()
    p2_base_attack = p2_B.getAttack()
    '''battle sequence'''
    while p1_health > 0 and p2_health > 0:
        #player 1 attacks
        if p1_health > 0:
            p1.movesDisplayer()
            p1_choice = input(p1_name + ' what move would you like to use? (1-4) ')
            while int(p1_choice) > 4 or int(p1_choice) < 1:
                p1.movesDispalyer()
                p1_choice = input('Whoops, looks like you pressed a key that is not between 1 and 4, try again. ')
            p1_attack = p1_B.playerAttack(p1_choice)
            p1_attack_type = p1_B.player_attackType(p1_choice)
            p1_damage = calculateDamage(p1_attack_type, p2_type, p1_base_attack, p2_defense, p1_attack)
            p2_health = round(healthAdjuster(p1_damage, p2_health))
            Effectiveness.effectivenessDisplayer(p1_attack_type, p2_type)
            print(p2_pokemon + '\'s health is now', p2_health)
        #player 2 attacks
        if p2_health > 0:
            p2.movesDisplayer()
            p2_choice = input(p2_name + ' what move would you like to use? (1-4) ')
            while int(p2_choice) > 4 or int(p2_choice) < 1:
                p2.movesDisplayer()
                p2_choice = input('Whoops, looks like you pressed a key that is not between 1 and 4, try again. ')
            p2_attack = p2_B.playerAttack(p2_choice)
            p2_attack_type = p2_B.player_attackType(p2_choice)
            p2_damage = calculateDamage(p2_attack_type, p1_type, p2_base_attack, p1_defense, p2_attack)
            p1_health = round(healthAdjuster(p2_damage, p1_health))
            Effectiveness.effectivenessDisplayer(p2_attack_type, p1_type)
            print(p1_pokemon + '\'s health is now', p1_health)


    #winner
    if p1_health > p2_health:
        print(p2_pokemon, 'has fainted.')
        print('Congratulations ' + p1_name +  ' you win!!')

    else:
        print(p1_pokemon, 'has fainted.')
        print('Congratulations ' + p2_name + ' you win!!')
    



main()
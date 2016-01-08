# Attack Simluator
#     Implemented:
#         basic formula for dealing damage
#         HP bars go down after Attacks
#         simple text display
#         testing for tackle
#     Pending
#         When is something supereffective????
#         crits?
#         rand factor?
#         testing of more attacks... more pokemon....

from pokemon import *

class Attack:
    def __init__(self, att_poke, def_poke, move):
        """the att_poke attacks def_poke, using move"""
        self.att_poke = att_poke
        self.def_poke = def_poke
        self.move = move

    def __str__(self):
        return self.att_poke.name + " used " + self.move.name + " on " + self.def_poke.name + "!"

    def find_effectiveness(self):
        """look up effectiveness in a large matrix
           each value in the matrix is stored as 0, 1/2, 1, or 2
           see http://pokemondb.net/type
         """
        typedict = {}
        typedict["Normal"] = 0
        typedict["Fire"] = 1
        typedict["Water"] = 2
        typedict["Electric"] = 3
        typedict["Grass"] = 4
        typedict["Ice"] = 5
        typedict["Fighting"] = 6
        typedict["Poison"] = 7
        typedict["Ground"] = 8
        typedict["Flying"] = 9 
        typedict["Physics"] = 10
        typedict["Bug"] = 11
        typedict["Rock"] = 12
        typedict["Ghost"] = 13
        typedict["Dragon"] = 14
        typedict["Dark"] = 15
        typedict["Steel"] = 16
        typedict["Fairy"] = 17
 
        effective = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, .5, 0, 1, 1, .5, 1],
        [1, .5, .5, 1, 2, 2, 1, 1, 1, 1, 1, 2, .5, 1, .5, 1, 2, 1] ,
        [1, 2, .5, 1, .5, 1, 1, 1, 2, 1, 1, 1, 2, 1, .5, 1, 1, 1] ,
        [1, 1, 2, .5, .5, 1, 1, 1, 0, 2, 1, 1, 1, 1, .5, 1, 1, 1] ,
        [1, .5, 2, 1, .5, 1, 1, .5, 2, .5, 1, .5, 1, 1, .5, 1, .5, 1] ,
        [1, .5, .5, 1, 2, .5, 1, 1, 2, 2, 1, 1, 1, 1, .5, 1, .5, 1] ,
        [2, 1, 1, 1, 1, 2, 1, .5, 1, .5, .5, .5, 2, 0, 1, 2, 2, 5] ,
        [1, 1, 1, 1, 1, 2, 1, .5, 1, .5, .5, .5, 2, 0, 1, 2, 2, 5] ,
        [1, 2, 1, 2, .5, 1, 1, 2, 1, 0, 1, .5, 2, 1, 1, 1, 2, 1] ,
        [1, 1, 1, .5, 2, 1, 2, 1, 1, 1, 1, 2, .5, 1, 1, 1, .5, 1] ,
        [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, .5, 1, 1, 1, 1, 0, .5, 1] ,
        [1, .5, 1, 1, 2, 1, .5, .5, 1, .5, 2, 1, 1, .5, 1, 2, .5, 5] ,
        [1, 2, 1, 1, 1, 2, .5, 1, .5, 2, 1, 2, 1, 1, 1, 1, .5, 1] ,
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, .5, 1, 1] ,
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, .5, 0] ,
        [1, 1, 1, 1, 1, 1, .5, 1, 1, 1, 2, 1, 1, 2, 1, .5, 1, 5] ,
        [1, .5, .5, .5, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, .5, 2], 
        [1, .5, 1, 1, 1, 1, 2, .5, 1, 1, 1, 1, 1, 1, 2, 2, .5, 1]] 


        if self.def_poke.pType != self.def_poke.sType:
            p_effective = effective[typedict[self.move.type]][typedict[self.def_poke.pType]]
            s_effective = effective[typedict[self.move.type]][typedict[self.def_poke.sType]]    
            return p_effective*s_effective


        return effective[typedict[self.move.type]][typedict[self.def_poke.pType]]

    def find_crit(self):
        """Crits double the damage - calculate this...
           Will implement crits phase 2 - note it changes based on basic / 1st stage etc """ # FIX
        return 1

    def find_stab(self):
        """Pokemon deals 1.5 times normal damage if same type as the move
           Return True if applicable"""
        if self.move.type == self.att_poke.pType or self.move.type == self.att_poke.sType:
            return 1.5
        return 1

    def find_other(self):
        """factor for other effects such as items, abilities, field advantages... etc
           will implement phase 2 """ # FIX
        return 1

    def find_rand(self):
        """Attacks deal anywhere between 85% and 100% of their theoretical damage
           Note: for E[X] calculations - set to average (uniform distribution)"""
        
        return (0.85+1.0)/2

    def find_damage(self):
        """Calculate the damage and subtract that amount from defender
           http://bulbapedia.bulbagarden.net/wiki/Damage#Damage_formula"""

        if self.move.cat == 'Physical':
            attack = self.att_poke.att
            defense = self.def_poke.dfn
        elif self.move.cat == 'Special':    
            attack = self.att_poke.spA
            defense = self.def_poke.spD
        else: # status moves deal no damage
            return 0
        base_damage = (((2.0*self.att_poke.lvl + 10) / 250) * attack / defense * self.move.pow) + 2
        modifier = (self.find_stab() * self.find_effectiveness() * self.find_crit() * 
                        self.find_other() * self.find_rand())
        # print(base_damage, modifier)
        damage = int(base_damage*modifier)
        self.def_poke.cHP -= damage
        return damage

    def report_results(self, damage):
        """inform user how much damage the attack would deal"""
        return "> " + self.att_poke.name + " dealt " + str(damage) + " damage to " + self.def_poke.name + '!'

    def check_fainted(self):
        if self.def_poke.cHP <= 0:
            return "...RIP The defending " + self.def_poke.name + " fainted"
        else:
            return "...The defending " + self.def_poke.name + " has " + str(self.def_poke.cHP) + " HP remaining" 

    def play(self):
        print(self.report_results(self.find_damage()))
        print(self.check_fainted())

def expected_damage_moves(attacker, defender):
    best_move, max_damage = DEFAULT_MOVE, 0

    for move in attacker.moves:
        attack_sim = Attack(attacker, defender, move)
        expected_damage = attack_sim.find_damage()
        if expected_damage > max_damage:
            best_move, max_damage = move, expected_damage
        # print(move.name + " is expected to deal " + str(attack_sim.find_damage()) + " damage.")
    print("Optimal move is to use " + best_move.name + " dealing " + str(max_damage) + " damage.")

    

expected_damage_moves(pikachu, squirtle)
expected_damage_moves(squirtle, squirtle)
expected_damage_moves(squirtle, pikachu)




# print(pikachu)
# print(squirtle)

# attack1 = Attack(pikachu, squirtle, tackle)
# attack1.play()
# attack1.play()
# attack1.play()
# attack1.play()
# attack1.play()
# attack1.play()

# print('\n<<<Squirtle fights back>>>\n')
# attack2 = Attack(squirtle, pikachu, tackle)
# attack2.play()
# attack2.play()
# attack2.play()

# print('\n<<<gg>>>\n')

# attack1.play() # rip

# print(pikachu)
# print(squirtle)



def test(a, b, c):
    """
    >>> test("Normal", "Normal", "Normal")
    1
    >>> test("Normal", "Fire", "Ground")
    1
    >>> test("Normal", "Normal", "Poison")
    1
    >>> test("Normal", "Ghost", "Normal")
    0
    >>> test("Fire", "Fire", "Normal")
    0.5
    >>> test("Fire", "Water", "Normal")
    0.5
    >>> test("Ground", "Flying", "Normal")
    0
    >>> test("Ground", "Flying", "Flying")
    0
    >>> test("Ground", "Fire", "Electric")
    4
    >>> test("Ground", "Ghost", "Normal")
    1
    >>> test("Steel", "Ice", "Rock")
    4
    >>> test("Fairy", "Fighting", "Dragon")
    4
    >>> test("Fairy", "Fire", "Poison")
    0.25


    """
    typedict = {}
    typedict["Normal"] = 0
    typedict["Fire"] = 1
    typedict["Water"] = 2
    typedict["Electric"] = 3
    typedict["Grass"] = 4
    typedict["Ice"] = 5
    typedict["Fighting"] = 6
    typedict["Poison"] = 7
    typedict["Ground"] = 8
    typedict["Flying"] = 9 
    typedict["Physics"] = 10
    typedict["Bug"] = 11
    typedict["Rock"] = 12
    typedict["Ghost"] = 13
    typedict["Dragon"] = 14
    typedict["Dark"] = 15
    typedict["Steel"] = 16
    typedict["Fairy"] = 17

    effective = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, .5, 0, 1, 1, .5, 1],
    [1, .5, .5, 1, 2, 2, 1, 1, 1, 1, 1, 2, .5, 1, .5, 1, 2, 1] ,
    [1, 2, .5, 1, .5, 1, 1, 1, 2, 1, 1, 1, 2, 1, .5, 1, 1, 1] ,
    [1, 1, 2, .5, .5, 1, 1, 1, 0, 2, 1, 1, 1, 1, .5, 1, 1, 1] ,
    [1, .5, 2, 1, .5, 1, 1, .5, 2, .5, 1, .5, 1, 1, .5, 1, .5, 1] ,
    [1, .5, .5, 1, 2, .5, 1, 1, 2, 2, 1, 1, 1, 1, .5, 1, .5, 1] ,
    [2, 1, 1, 1, 1, 2, 1, .5, 1, .5, .5, .5, 2, 0, 1, 2, 2, 5] ,
    [1, 1, 1, 1, 1, 2, 1, .5, 1, .5, .5, .5, 2, 0, 1, 2, 2, 5] ,
    [1, 2, 1, 2, .5, 1, 1, 2, 1, 0, 1, .5, 2, 1, 1, 1, 2, 1] ,
    [1, 1, 1, .5, 2, 1, 2, 1, 1, 1, 1, 2, .5, 1, 1, 1, .5, 1] ,
    [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, .5, 1, 1, 1, 1, 0, .5, 1] ,
    [1, .5, 1, 1, 2, 1, .5, .5, 1, .5, 2, 1, 1, .5, 1, 2, .5, 5] ,
    [1, 2, 1, 1, 1, 2, .5, 1, .5, 2, 1, 2, 1, 1, 1, 1, .5, 1] ,
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, .5, 1, 1] ,
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, .5, 0] ,
    [1, 1, 1, 1, 1, 1, .5, 1, 1, 1, 2, 1, 1, 2, 1, .5, 1, 5] ,
    [1, .5, .5, .5, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, .5, 2], 
    [1, .5, 1, 1, 1, 1, 2, .5, 1, 1, 1, 1, 1, 1, 2, 2, .5, 1]] 

    p_effective = effective[typedict[a]][typedict[b]]
    s_effective = effective[typedict[a]][typedict[c]]

    return p_effective*s_effective
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
           """ # FIX
        return 1

    def find_crit(self):
        """Crits double the damage - calculate this...""" # FIX
        return 1

    def find_stab(self):
        """Pokemon deals 1.5 times normal damage if same type as the move
           Return True if applicable"""
        if self.move.type == self.att_poke.pType or self.move.type == self.att_poke.sType:
            return 1.5
        return 1

    def find_other(self):
        """factor for other effects such as items, abilities, field advantages... etc""" # FIX
        return 1

    def find_rand(self):
        """Attacks deal anywhere between 85% and 100% of their theoretical damage""" # FIX
        return 1

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
            attack = 0
            defense = 9001 
        # print(attack,defense, self.move.pow, self.att_poke.lvl)
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

print(pikachu)
print(squirtle)

attack1 = Attack(pikachu, squirtle, tackle)
attack1.play()
attack1.play()
attack1.play()
attack1.play()
attack1.play()
attack1.play()

print('\n<<<Squirtle fights back>>>\n')
attack2 = Attack(squirtle, pikachu, tackle)
attack2.play()
attack2.play()
attack2.play()

print('\n<<<gg>>>\n')

attack1.play() # rip

print(pikachu)
print(squirtle)


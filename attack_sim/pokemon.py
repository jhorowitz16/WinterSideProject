# Basic Framework for pokemon and their moves

class Pokemon:
    def __init__(self, 
        name, lvl, mHP, cHP, att, dfn, spA, spD, spe, pType, sType, moves):
        """
            name: 'pikachu'
            level: 1 to 100
            mHP: Max Hit Points (ex: 55)
            cHP: Current Hit Points (ex: 40)
            att: Attack (ex: 55)
            dfn: Defense (ex: 40)
            spA: Special Attack (ex: 50)
            spD: Special Defense (ex: 50)
            spe: Speed (ex: 90)
            pType: Primary Type (Electric)
            sType: Secondary Type - same as primary type if no secondary type (Electric)
            moves: a list of 4 possible attacks this pokemon can have
                   (ex: [Tackle, Tail Whip, Thunderbolt, <blank>])
                   each of these are Move Objects
        """
        # assign instance variables for each of the traits
        self.name = name
        self.lvl = lvl
        self.mHP = mHP
        self.cHP = cHP
        self.att = att
        self.dfn = dfn
        self.spA = spA
        self.spD = spD
        self.spe = spe
        self.pType = pType
        self.sType = sType 
        self.moves = moves 

    def format_moves(self):
        """As moves is a list of move objects,
           use method for getting the names of each move"""
        moves_str = '[ '
        for move in self.moves[:len(self.moves)-1]:
            moves_str += move.name + ', '
        return moves_str + self.moves[len(self.moves)-1].name + ']'
    
    def __str__(self):
        """get a printout of all pokemon's info"""

        return '================' + '\n' + self.name.upper() + \
            '\n Level: ' + str(self.lvl) + \
            '\n Max HP: ' + str(self.mHP) + \
            '\n Current HP: ' + str(self.cHP) + \
            '\n Attack: ' + str(self.att) + \
            '\n Defense: ' + str(self.dfn) + \
            '\n Special Attack: ' + str(self.spA) + \
            '\n Special Defense: ' + str(self.spD) + \
            '\n Speed: ' + str(self.spe) + \
            '\n Primary Type: ' + self.pType + \
            '\n Secondary Type: ' + self.sType + \
            '\n Moves: ' + self.format_moves() + \
            '\n================'



class Move:
    def __init__(self, 
        name, type, cat, pow, acc, eff):
        """
            name: 'Tackle'
            type: 'Normal'
            cat: Category {Physical, Special, or Status(not damage dealing)} (ex: Physical)
            pow: Power (ex: 50)
            acc: Accuracy up to 100 (ex: 100)
            eff: Optional Effect Text to be implemented later (ex: <blank> b/c no text)
        """
        # assign instance variables for each of the traits
        self.name = name
        self.type = type
        self.cat = cat
        self.pow = pow
        self.acc = acc
        self.eff = eff

    def __str__(self):
        """get a printout of all move's info"""

        return '================' + '\n' + self.name.upper() + \
            '\n Type: ' + self.type + \
            '\n Category: ' + self.cat + \
            '\n Power: ' + str(self.pow) + \
            '\n Accuracy: ' + str(self.acc) + \
            '\n Effect: ' + self.eff + \
            '\n================'


# defaults
DEFAULT = '<blank>'
DEFAULT_MOVE = Move(DEFAULT, DEFAULT, DEFAULT, 0, 100, DEFAULT)
DEFAULT_POKEMON = Pokemon(DEFAULT, 0, 0, 0, 0, 0, 0, 0, 0, DEFAULT, DEFAULT, [DEFAULT_MOVE, DEFAULT_MOVE, DEFAULT_MOVE, DEFAULT_MOVE])

# moves 
tackle = Move('Tackle', 'Normal', 'Physical', 50, 100, DEFAULT)
tail_whip = Move('Tail Whip', 'Normal', 'Status', 0, 30, 'Lowers Opponent\'s Defense')
water_gun = Move('Water Gun', 'Water', 'Special', 40, 100, DEFAULT)
thunder_shock = Move('Thunder Shock', 'Electric', 'Special', 40, 100, 'May paralyze opponent')

# pokemon
pikachu = Pokemon('Pikachu', 10, 35, 35, 55, 40, 50, 50, 90, 'Electric', 'Electric', [tackle, tail_whip, thunder_shock, DEFAULT_MOVE])
squirtle = Pokemon('Squirtle', 10, 44, 44, 48, 65, 50, 64, 43, 'Water', 'Water', [tackle, tail_whip, water_gun, DEFAULT_MOVE] )



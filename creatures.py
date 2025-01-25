roll_table = ['1d4','1d6', '2d4', '2d6', '4d4', '4d6']

class Creature:

    def __init__(self, finesse, body, av, dodging, striking, name='Player'):
        self.finesse = finesse
        self.body = body
        self.av = av
        self.dodging = dodging
        self.striking = striking
        self.name = name

    def prefab(name):
        if name == 'skeleton':
            return Creature(3, 2, 5, 1, 1, name)
        if name == 'zombie':
            return Creature(1, 3, 2, 0, 1, name)
        if name == 'goblin':
            return Creature(2, 1, 2, 1, 1, name)
        
    def get_roll(self, skill, attribute, bonus = 0):
        roll = '0'
        if attribute == 'body':
            bonus = bonus + self.body
        if attribute == 'finesse':
            bonus = bonus + self.finesse
        if skill == 'striking':
            roll = roll_table[self.striking]
        if skill == 'dodging':
            roll = roll_table[self.dodging]
        return '%s + %s' % (roll, bonus)

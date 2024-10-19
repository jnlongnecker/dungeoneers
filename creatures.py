class Creature:
    def __init__(self, agility, strength, av, hit_die, pierce_die, dodging, striking, name='Player'):
        self.agility = agility
        self.strength = strength
        self.av = av
        self.hit_die = hit_die
        self.pierce_die = pierce_die
        self.dodging = dodging
        self.striking = striking
        self.name = name

    def prefab(name):
        if name == 'skeleton':
            return Creature(3, 2, 5, 'd4', 'd4', 'd8', 'd6', name)
        if name == 'zombie':
            return Creature(1, 3, 2, 'd4', 'd6', 'd4', 'd4', name)
        if name == 'goblin':
            return Creature(2, 1, 2, 'd4', 'd4', 'd6', 'd6', name)

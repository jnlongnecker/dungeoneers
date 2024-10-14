class Creature:
    def __init__(self, prowess, power, av, hit_die, pierce_die, dodge_die, name='Player'):
        self.prowess = prowess
        self.power = power
        self.av = av
        self.hit_die = hit_die
        self.pierce_die = pierce_die
        self.dodge_die = dodge_die
        self.name = name

    def prefab(name):
        if name == 'skeleton':
            return Creature(1, 2, 5, 'd8', 'd4', 'd4', name)
        if name == 'zombie':
            return Creature(1, 3, 2, 'd4', 'd6', 'd4', name)
        if name == 'goblin':
            return Creature(2, 1, 2, 'd8', 'd4', 'd6', name)

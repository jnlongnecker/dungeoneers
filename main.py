import rolls
import creatures

me = creatures.Creature(power=2, prowess=2, av=5, hit_die='d4', pierce_die='d8', dodge_die='d4')
targets = []
targets.append(creatures.Creature.prefab('goblin'))
targets.append(creatures.Creature.prefab('skeleton'))

for target in targets:
    print('\n== My Stats ==')
    chance = rolls.calculate_chance_to_wound(me, target)

    print('Chance to wound: %s' % rolls.perc_format(chance))

    print('\n== %s Stats ==' % (target.name))
    chance = rolls.calculate_chance_to_wound(target, me)

    print('Chance to wound: %s' % rolls.perc_format(chance))
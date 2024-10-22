import rolls
import creatures

result = rolls.calculate_chance_to_beat('4d6 + 7', '30', False)

print(result)

# me = creatures.Creature(strength=2, agility=4, av=5, dodging='d6', striking='d8', hit_die='d0', pierce_die='d8')
# targets = []
# targets.append(creatures.Creature.prefab('skeleton'))
# dodging = creatures.Creature.prefab('skeleton')
# dodging.agility = dodging.agility + 1
# targets.append(dodging)

# for target in targets:
#     print('\n== My Stats ==')
#     chance = rolls.calculate_chance_to_wound(me, target)

#     print('Chance to wound: %s' % rolls.perc_format(chance))

#     print('\n== %s Stats ==' % (target.name))
#     chance = rolls.calculate_chance_to_wound(target, me)

#     print('Chance to wound: %s' % rolls.perc_format(chance))
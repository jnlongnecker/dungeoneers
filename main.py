import rolls
import creatures

# rolls.print_chance_of('2d8', '=', 2)

# result = rolls.calculate_chance_to_beat('2d8', '2', False)

# print(result)

me = creatures.Creature(body=2, finesse=3, av=5, dodging=1, striking=1)
target = creatures.Creature.prefab('skeleton')

rolls.calculate_chance_to_wound(me, target, crit_threshold=5)

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
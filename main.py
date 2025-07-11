import rolls
import creatures
import graph

pool = rolls.DicePool(die='1d10', quantity=3, bonus=0, target=5)
pool2 = rolls.DicePool(die='1d10', quantity=3, bonus=0, target=3)
opposing_pool = rolls.DicePool(die='1d10', quantity=3, bonus=0, target=4)
opposing_pool2 = rolls.DicePool(die='1d10', quantity=3, bonus=0, target=5)

pool.print_expected_successes()
pool2.print_expected_successes()

damage = 2

# print(pool.average_damage(opposing_pool, damage + 1))
# print(pool.average_damage(opposing_pool2, damage))
# print(pool2.average_damage(opposing_pool, damage * 2))
# print(pool2.average_damage(opposing_pool2, damage - 1))

# graph.plot_success(pool, pool2, opposing_pool)


# quantity = 6
# for i in range(1, 10):
#     pool = rolls.DicePool(die='1d10', quantity=quantity, bonus=0, target=i)
#     print('Quantity: %s, Target: %s' % (quantity, i))
#     pool.print_expected_successes()


# pool = rolls.DicePool(die='1d10', quantity=3, bonus=0, target=1)
# opposing_pool = rolls.DicePool(die='1d10', quantity=3, bonus=0, target=4)
# pool.print_chances()
# pool.print_crit_chance()
# pool.print_expected_successes()

# rolls.print_chance_of('2d10+7', '>=', 12)

# die_roll = '4d6+1d4+2'
# target = '4d6+2'
# damage = 2
# body = 3
# result = rolls.calculate_chance_to_beat(die_roll, target, False)

# print('Chance of %s hit on %s: %s' % (die_roll, target, rolls.perc_format(result)))

# crit = 1
# crit_threshold = '+5'
# crit_chances = []
# crit_chances.append(result)
# while result > 0.0001:
#     target = target + crit_threshold
#     result = rolls.calculate_chance_to_crit(die_roll, target, False)
#     print('Chance of %s %s crit(s) %s' % (die_roll, crit, rolls.perc_format(result)))
#     crit = crit + 1
#     crit_chances.append(result)

# sum = body
# for i in range(0, len(crit_chances)):
#     item = crit_chances[i]
#     sum = sum + (damage * item)


# print('Expected damage: %s' % (sum))


# me = creatures.Creature(body=2, finesse=3, av=5, dodging=1, striking=1)
# target = creatures.Creature.prefab('skeleton')

# rolls.calculate_chance_to_wound(me, target, crit_threshold=5)

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
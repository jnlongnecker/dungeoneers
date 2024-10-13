import rolls
import creatures

me = creatures.Creature(power=2, prowess=2, av=7, hit_die='d6', pierce_die='d8', dodge_die='d4')
target = creatures.Creature(power=2, prowess=3, av=5, hit_die='d4', pierce_die='d4', dodge_die='d4')

print('== My Stats ==')
chance = rolls.calculate_chance_to_wound(me, target)

print('Chance to wound: %s' % rolls.perc_format(chance))

print('\n== Enemy Stats ==')
chance = rolls.calculate_chance_to_wound(target, me)

print('Chance to wound: %s' % rolls.perc_format(chance))
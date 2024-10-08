import math

class Roll:
    def __init__(self, roll_string):
        self.tokens = self.tokenize(roll_string)

    def tokenize(self, roll_string):
        tokens = []
        curr_token = ''
        for char in roll_string:
            if char == ' ':
                if curr_token != '':
                    tokens.push(curr_token)
                curr_token = ''
            elif char == '+' or char == '-':
                if curr_token != '':
                    tokens.push(curr_token)
                    curr_token = ''
                tokens.push(char)
            else:
                curr_token = curr_token + char
        return tokens
                

class DiceRoll:
    def __init__(self, die_string):
        parts = die_string.split('d')
        self.die_num = int(parts[1])
        self.die_count = max(1, int(parts[0]))

def fac(num):
    if num == 1: return 1
    if num == 2: return 3
    if num == 3: return 6
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact

def bin_coef(n, k):
    if n == k or k == 0: return 1
    return bin_coef(n - 1, k - 1) + bin_coef(n - 1, k)

def exact_sum(r, n, s):
    max = math.floor((r - n)/s)
    sum = 0
    a = 1/pow(s, n)
    for k in range(0, max + 1):
        sum = sum + pow(-1, k) * bin_coef(n, k) * bin_coef((r - s * k - 1), n - 1)
    return sum * a

def unique_rolls(list):
    num_unique = 0
    found = {}
    for i in list:
        if i not in found:
            found[i] = 0
            num_unique = num_unique + 1
    return num_unique

def get_chances(dice_roll):
    end_idx = dice_roll.die_num * dice_roll.die_count
    start_idx = dice_roll.die_count
    probabilities = [0] * (end_idx + 1)

    while end_idx >= start_idx:
        r = start_idx
        n = dice_roll.die_count
        s = dice_roll.die_num
        chance = exact_sum(r, n, s)

        probabilities[end_idx] = chance
        probabilities[start_idx] = chance
        start_idx = start_idx + 1
        end_idx = end_idx - 1
    return probabilities

def probability_at_least(probs, num):
    if num >= len(probs): return 0
    if num <= 0: return 1

    running_total = 0
    for i in range(0, num):
        running_total = running_total + probs[i]
    return 1 - running_total

def probability_at_most(probs, num):
    if num >= len(probs): return 1
    if num <= 0: return 0

    running_total = 0
    for i in range(0, num + 1):
        running_total = running_total + probs[i]
    return running_total

def print_probabilities(roll_string):
    roll = DiceRoll(roll_string)
    probabilities = get_chances(roll)
    for i in range(0, len(probabilities)):
        num = round(100 * probabilities[i], 1)
        print("Probability of %s: %s" % (i, num))

def print_chance_of(dice_string, operator, desired_num, modifier=0):
    dice_roll = DiceRoll(dice_string)
    probs = get_chances(dice_roll)
    real_num = desired_num - modifier
    chance = 0
    if operator == '<':
        chance = probability_at_most(probs, real_num - 1)
    elif operator == '<=':
        chance = probability_at_most(probs, real_num)
    elif operator == '>':
        chance = probability_at_least(probs, real_num + 1)
    elif operator == '>=':
        chance = probability_at_least(probs, real_num)


    pretty_chance = round(100 * chance, 2)
    print('Probability of rolling %s + %s %s %s: %s' % (dice_string, modifier, operator, desired_num, pretty_chance) + '%')

def calculate_improvement(before_string, after_string):
    before_probs = get_chances(DiceRoll(before_string))
    after_probs = get_chances(DiceRoll(after_string))
    end = min(len(before_probs), len(after_probs))
    longest = max(len(before_probs), len(after_probs))
    changes = [0] * longest
    for i in range(0, end):
        changes[i] = probability_at_least(after_probs, i) - probability_at_least(before_probs, i)
    for i in range(end, longest):
        changes[i] = 1
    return changes

def print_improvement(before_string, after_string):
    changes = calculate_improvement(before_string, after_string)
    for i in range(0, len(changes)):
        pretty_roll = '%s' % round(100 * changes[i], 2) + '%'
        print('Chance to roll %s changed by %s' % (i, pretty_roll))

def calculate_chance_to_beat(my_roll, their_roll, must_beat):
    my_probs = get_chances(DiceRoll(my_roll))
    their_probs = get_chances(DiceRoll(their_roll))
    meets = 1 if must_beat else 0

    chances_i_win = 0
    for i in range(0, len(my_probs)):
        chance_i_rolled = my_probs[i]
        chance_they_rolled = probability_at_most(their_probs, i - meets)
        chances_i_win = chances_i_win + (chance_i_rolled * chance_they_rolled)
    return chances_i_win

# print_improvement('2d4', '4d4')
# print(calculate_chance_to_beat('4d6', '6d4', must_beat=False))
print_chance_of('2d10', '>=', 15)
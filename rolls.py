import math

def fac(num):
    if num == 1: return 1
    if num == 2: return 3
    if num == 3: return 6
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact

# Combinatorics (n items, pick k without repetition or order)
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

def perc_format(percent):
    return '%s' % round(100 * percent, 2) + '%'

def subtract_chances(chance1, chance2):
    if len(chance1) == 0:
        return chance2
    if len(chance2) == 0:
        return chance1
    
    new_max = len(chance1) - 2
    result = [0] * (new_max + 1)
    for i in range(0, len(chance1)):
        if chance1[i] == 0:
            continue

        for j in range(0, len(chance2)):
            if chance2[j] == 0:
                continue
            idx = max(i - j, 0)
            result[idx] = result[idx] + (chance1[i] * chance2[j])

    return result

def add_chances(chance1, chance2):
    if len(chance1) == 0:
        return chance2
    if len(chance2) == 0:
        return chance1
    
    larger = []
    smaller = []
    if len(chance1) > len(chance2):
        larger = chance1
        smaller = chance2
    else:
        larger = chance2
        smaller = chance1
    
    new_max = len(chance1) - 1 + len(chance2) - 1
    result = [0] * (new_max + 1)
    for i in range(0, len(larger)):
        if larger[i] == 0:
            continue

        for j in range(0, len(smaller)):
            if smaller[j] == 0:
                continue
            result[i + j] = result[i + j] + (larger[i] * smaller[j])

    return result

def shift_chances(chances, amount):
    new_max = len(chances) - 1 + amount
    result = [0] * (new_max + 1)
    for i in range(0, len(chances)):
        idx = max(i + amount, 0)
        result[idx] = result[idx] + chances[i]
    return result

class DiceRoll:
    def __init__(self, die_string):
        parts = die_string.split('d')
        self.die_num = int(parts[1])
        self.die_count = max(1, int(parts[0]))
        self.chances = self.calculate_chances()

    def calculate_chances(self):
        end_idx = self.die_num * self.die_count
        start_idx = self.die_count
        probabilities = [0] * (end_idx + 1)

        while end_idx >= start_idx:
            r = start_idx
            n = self.die_count
            s = self.die_num
            chance = exact_sum(r, n, s)

            probabilities[end_idx] = chance
            probabilities[start_idx] = chance
            start_idx = start_idx + 1
            end_idx = end_idx - 1
        return probabilities

class Roll:
    def __init__(self, roll_string):
        self.tokenize(roll_string)
        self.chances = self.calculate_chances()

    def calculate_chances(self):
        running_chance = []
        operator = '+'
        for token in self.tokens:
            if type(token) is str:
                operator = token
                continue

            if operator == '+':
                if type(token) is DiceRoll:
                    running_chance = add_chances(running_chance, token.chances)
                if type(token) is int:
                    running_chance = shift_chances(running_chance, token)
            else:
                if type(token) is DiceRoll:
                    running_chance = subtract_chances(running_chance, token.chances)
                if type(token) is int:
                    running_chance = shift_chances(running_chance, -1 * token)

        return running_chance

    def tokenize(self, roll_string):
        self.tokens = []
        curr_token = ''
        for char in roll_string:
            if char == ' ':
                if curr_token != '':
                    self.add_token(curr_token)
                curr_token = ''
            elif char == '+' or char == '-':
                if curr_token != '':
                    self.add_token(curr_token)
                    curr_token = ''
                self.add_token(char)
            else:
                curr_token = curr_token + char
        self.add_token(curr_token)
    
    def add_token(self, token):
        is_dice = token.find('d') != -1
        is_modifier = token.isnumeric()
        if is_dice:
            self.tokens.append(DiceRoll(token))
        elif is_modifier:
            self.tokens.append(int(token))
        else:
            self.tokens.append(token)

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
    probabilities = roll.chances
    for i in range(0, len(probabilities)):
        num = round(100 * probabilities[i], 1)
        print("Probability of %s: %s" % (i, num))

def calculate_chance_of(dice_string, operator, desired_num):
    dice_roll = Roll(dice_string)
    probs = dice_roll.chances
    real_num = desired_num
    chance = 0
    if operator == '<':
        chance = probability_at_most(probs, real_num - 1)
    elif operator == '<=':
        chance = probability_at_most(probs, real_num)
    elif operator == '>':
        chance = probability_at_least(probs, real_num + 1)
    elif operator == '>=':
        chance = probability_at_least(probs, real_num)
    elif operator == '=':
        chance = probs[desired_num]
    return chance

def print_chance_of(dice_string, operator, desired_num):
    chance = calculate_chance_of(dice_string, operator, desired_num)

    pretty_chance = round(100 * chance, 2)
    print('Probability of rolling %s %s %s: %s' % (dice_string, operator, desired_num, pretty_chance) + '%')

def calculate_improvement(before_string, after_string):
    before_probs = Roll(before_string)
    after_probs = Roll(after_string)
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
    my_probs = Roll(my_roll).chances
    their_probs = Roll(their_roll).chances
    meets = 1 if must_beat else 0

    chances_i_win = 0
    for i in range(0, len(my_probs)):
        chance_i_rolled = my_probs[i]
        chance_they_rolled = probability_at_most(their_probs, i - meets)
        chances_i_win = chances_i_win + (chance_i_rolled * chance_they_rolled)
    return chances_i_win

def calculate_chance_to_crit(my_roll, their_roll, crit_threshold):
    my_probs = Roll(my_roll).chances
    their_probs = Roll(their_roll).chances

    chances_i_crit = 0
    for i in range(0, len(my_probs)):
        chance_i_rolled = my_probs[i]
        chance_they_rolled = probability_at_most(their_probs, i - crit_threshold)
        chances_i_crit = chances_i_crit + (chance_i_rolled * chance_they_rolled)
    return chances_i_crit

def calculate_chance_to_wound(me, target, crit_threshold = 5):
    my_hit = me.get_roll('striking', 'finesse')
    target_dodge = target.get_roll('dodging', 'finesse')

    hit_chance = calculate_chance_to_beat(my_hit, target_dodge, False)
    print('Hit chance of %s vs %s: %s' % (my_hit, target_dodge, perc_format(hit_chance)))

    crit_chance = 1
    crit_num = 1
    while crit_chance > 0:
        crit_chance = calculate_chance_to_crit(my_hit, target_dodge, crit_num * crit_threshold)
        print('Chance for %s crit: %s' % (crit_num, perc_format(crit_chance)))
        crit_num = crit_num + 1

    return hit_chance

### Dice Pool Statistics ###
class DicePool:

    def __init__(self, die, quantity, bonus, target):
        self.die = die
        self.quantity = quantity
        self.bonus = bonus
        self.target = target
        self.chances = self.calculate_chances()

    def calculate_chances(self):
        rolls = self.quantity
        bonus = self.bonus
        failure_chance = calculate_chance_to_beat(self.die, str(self.target), True)
        success_chance = 1 - failure_chance
        chance_for_x_success = []
        for successful_rolls in range(0, rolls + 1):
            base_chance = (success_chance ** successful_rolls) * (failure_chance ** (rolls - successful_rolls))
            combinations = float(bin_coef(rolls, successful_rolls))
            final_success_chance = base_chance * combinations
            chance_for_x_success.append(final_success_chance)
        ret = []
        index = 0
        for i in range(0, bonus):
            tup = (i, 0)
            ret.append(0)
        for i in range(bonus, rolls + bonus + 1):
            tup = (i, chance_for_x_success[index])
            ret.append(chance_for_x_success[index])
            index = index + 1
        return ret

    def chance_to_crit(self):
        parts = self.die.split('d')
        max_die = int(parts[1])
        max_chance = 1 / max_die
        normal_chance = 1 - max_chance
        if (self.quantity < 2):
            return 0
        base_chance = float((max_chance ** 2.0) * (normal_chance ** (self.quantity - 2.0)))
        combinations = float(bin_coef(self.quantity, 2))
        return base_chance * combinations
    
    def chance_to_beat(self, other, must_beat):
        my_probs = self.chances
        their_probs = other.chances
        meets = 1 if must_beat else 0

        chances_i_win = 0
        for i in range(0, len(my_probs)):
            chance_i_rolled = my_probs[i]
            chance_they_rolled = probability_at_most(their_probs, i - meets)
            chances_i_win = chances_i_win + (chance_i_rolled * chance_they_rolled)
        return chances_i_win
    
    def chances_of_success(self, other):
        my_probs = self.chances
        their_probs = other.chances
        success_probs = {}
        for i in range(0, len(my_probs)):
            for j in range (0, len(their_probs)):
                successes = i - j
                chance = my_probs[i] * their_probs[j]
                if successes in success_probs:
                    success_probs[successes] = success_probs[successes] + chance
                else:
                    success_probs[successes] = chance
        return success_probs
    
    def expected_successes(self):
        chances = self.chances
        expected_successes = 0
        success_count = 0
        for chance in chances:
            expected_successes = expected_successes + chance * success_count
            success_count = success_count + 1
        return expected_successes
    
    def print_expected_successes(self):
        expected = self.expected_successes()
        print('Expected successes: %s' % (expected))
    
    def print_chances_of_success(self, other):
        chances = self.chances_of_success(other)
        for success in sorted(chances):
            chance = chances[success]
            print('Chance of %s successes: %s' % (success, perc_format(chance)))
    
    def print_chance_to_beat(self, other, must_beat):
        chance = self.chance_to_beat(other, must_beat)
        print('Chance to win: %s' % (perc_format(chance)))

    def print_chances(self):
        for i in range(0, len(self.chances)):
            chance = self.chances[i]
            print('Chance of exactly %s successes: %s' % (i, perc_format(chance)))
    
    def print_crit_chance(self):
        chance = self.chance_to_crit()
        print('Crit chance: %s' % (perc_format(chance)))

def calculate_successes(rolls, bonus, proficiency):
    prof_string = str(proficiency)
    success_chance = 1 - calculate_chance_to_beat('1d6', prof_string, True)
    successes = bonus
    chance_for_x_success = []
    for successful_rolls in range(0, rolls + 1):
        failure_chance = 1 - success_chance ** successful_rolls
        combinations = float(bin_coef(rolls, successful_rolls))
        final_success_chance = 1.0 - (failure_chance ** combinations)
        chance_for_x_success.append(final_success_chance)
    return chance_for_x_success

def calculate_exact_successes(rolls, bonus, proficiency):
    successes = calculate_successes(rolls, bonus, proficiency)
    for i in range(0, len(successes) - 1):
        next = successes[i + 1]
        curr = successes[i]
        successes[i] = curr - next
    return successes
    ret = []
    for i in range(0, bonus + 1):
        ret.append(1)
    for chance in chance_for_x_success:
        ret.append(chance)
    return ret
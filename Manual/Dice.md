# Dice

In Dungeoneers, the number of dice rolled and the faces of said dice are subject to great change at any given time. If you're familiar with dice rolling systems, you'll find the nomenclature of Dungeoneers to be very similar and may not need most of this section (however, you'll probably still want to read up on `die sources`). If you're not, then no worries! This section will explain the terminology and what you'll need to know.

## Rolls

In Dungeoneers, the anatomy of a roll is the following:

`n`d`x` + `m`

This may seem scary, but it's a lot simpler than it looks! In our roll, `n` represents the number of dice to roll. The "d" just stands for "die". `x` stands for the number of sides the die has, and `m` are any add-ons to the roll (which can either be other rolls or straight numbers). For example, we may have the following roll:

2d6

This would be read in natural language as "2 die 6", which simply means that you roll 2 six-sided dice and add the result together. Let's say for this roll, you roll a 4 on your first die 6 and a 3 on your second die 6. You would add them together, which makes your result or "total" of the roll to be 7. A more complicated roll might be the following:

3d6 + 1d4 + 1

There are more parts, but by now we have enough of the nomenclature down to figure it out. We first get the total of 3d6, then we get the total of 1d4, and finally we add 1. Let's say we roll a 2, a 3, and a 6 on our 3d6 and a 3 on our 1d4. We do the following:

2 + 3 + 6 + 3 + 1 = 15

And find our total of the roll to be 15.

When a roll is made, there is some obstruction to the desired task being completed. After all, that's why we need the roll! This obstruction is represented by the `target` of the roll. In order for the roll to succeed, the total must either meet or exceed the `target`. Any `creature` is allowed to intentionally fail a roll that they are called to be a part of for any reason.

## Types of Rolls

There are 2 specific types of rolls: `checks` and `tests`. There's little difference between the two, but the distinction is made to make things a bit easier to understand while you're reading through the rules. A `check` is a roll made against a static number, while a `test` is a competition between two rolls.

In a `check`, the `target` is set by the static number. In a `test`, the `target` is set by the opponent's roll total; because of this a `test` is slightly more complicated. Remember, a roll is called for when there is some obstruction to the desired task being completed. In a `test`, this means that something (typically a `creature`) is skillfully opposing the `creature` attempting to perform the task. The `creature` that triggers the roll is called the `attacker` while the entity opposing the roll is called the `defender`. The `defender` sets the `target` of the roll that the `attacker` must meet or exceed for the roll to succeed.

> For example, when making a `strike`, a `test` is called between the `creature` who is `striking` and the `creature` being `struck`. The `creature` being `struck` is the opposition in this case, and their roll total determines the `target` that the `striking` `creature` must reach.

## Die Sources

Since the number of dice and the sides of those dice change often from roll to roll, we need a way to determine how many dice of what sides we need to roll. This is where `die sources` come into play. Whenever a roll is called for, the `die source` will be specified. Most often, the `proficiency` `die source` will be used. Don't worry about `proficiency` for right now; the important part to understand is that when a roll is called, you'll always know what dice to roll and how many. If there's ever a moment where you feel a roll is necessary but for whatever reason is not supported in the rules, look to your DM to decide what should be done.

The anatomy of a roll is the following:

roll type : [(`die source` | ... | `die source`)] + add-ons vs `target`

The "roll type" specifies what type of roll it is; either a `check` or a `test`. This lets you tell at a glance whether the roll is against a static number or another roll. Whenever you see square brackets `[]`, this indicates a roll of dice and inside we will have the options for the `die source`. If there are multiple options, they'll be contained within parenthesis `()` and separated with a pipe `|`. This means that the roller gets to choose which `die source` they want to use. The pattern here of containing options in parenthesis `()` separated by a pipe `|` is a general pattern used anywhere there are choices.

> Note the term "roller" was used, this does _not_ mean the `creature` that caused the roll! If the options are on the `defenders` side (after the vs), then the `defender` chooses for themselves. Similarly, if they're on the `attackers` side (before the vs), the `attacker` chooses for themselves.

Any add-ons to the roll (remember, these can include other rolls!) are noted after before a "vs" which denotes where the `target` begins. Depending on if the roll is a `check` or a `test`, this will either be another roll or a static number.

If this was confusing still, the best way to explain this is through an example:

_In order to see if a `grapple` succeeds, roll a_

_`test`: [`grappling`] + `body` vs [`dodging`] + (`finesse`|`body`)_

The `attacker` rolls dice determined by their `grappling` `proficiency` level (more on that in another section) and add their `body` score. This is compared against the `defenders` roll; they roll dice determined by their `dodging` `proficiency` and add their choice of their `finesse` or `body` score.

## Degrees of Success, Criticals and Compromises

If the die roll is meant to represent variability of the quality of the action, the outcome should have the quality of the total be represented as well. This is the purpose of degrees of success.

When a roll is made, compare the total to the `target`. If the the total is 5 or more below the `target`, the roll truly fails; whatever outcome was being tried simply does not work. If the total is above 5 less than the `target` but does not meet the `target`, the roll partially succeeds; whatever outcome was being tried has some undesired complication to the outcome or is of dubious quality. If the total meets or is less than 5 above the `target`, the roll succeeds; whatever outcome was being tried completes without complication and as intended.

For each multiple of 5 above the `target`, the roll `critically` succeeds. On a `critical`, the outcome is a success (or better) _and_ the player gains a point of `boon` for each `critical`.

> Example: on a roll with a `target` of 10, a total of 1-4 would be a failure, a total of 5-9 would be a partial success, and a total of 10-14 would be a success. A total of 15-19 would `critical` 1 time, a total of 20-24 would `critical` 2 times, and so on. The roll succeeds and for each `critical`, another point of `boon` is gained.

When a roll does not succeed, a player may ask for a `compromise`. When a `compromise` occurs, the degree of success of the roll becomes 1 greater (i.e., a total failure becomes a partial success and a partial success becomes a success). In return, the GM gains a point of `villainy`. It is up to the GM whether to accept the `compromise` or not.

# Dice

In Dungeoneers, the number of dice rolled and the faces of said dice are subject to great change at any given time. Many systems choose to revolve around a twenty-sided die, but Dungeoneers prefers the math that is yielded from rolling multiple dice at once and adding them up (for you stats nerds, this is the normal distribution). If you're familiar with dice rolling systems, you'll find the nomenclature of Dungeoneers to be very similar and may not need this section. If you're not, then no worries! This section will explain the terminology and what you'll need to know.

## Rolls

In Dungeoneers, the anatomy of a roll is the following:

`n`d`x` + `m`

This looks scary, but it's a lot simpler than it looks! In our roll, `n` represents the number of dice to roll. The "d" just stands for "die". `x` stands for the number of sides the die has, and `m` are any add-ons to the roll (which can either be other rolls or straight numbers). For example, we may have the following roll:

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

Since the number of dice and the sides of those dice change often from roll to roll, we need a way to determine how many dice of what sides we need to roll. This is where `die sources` come into play. Whenever a roll is called for, the `die sources` will be specified. Most often, the number of dice rolled is determined by an `attribute score` `die source` and the number of sides of the dice are determined by the `proficiency` `die source`. Don't worry about these for right now; the important part to understand is that when a roll is called, you'll always know what dice to roll and how many. If there's ever a moment where you feel a roll is necessary but for whatever reason is not supported in the rules, look to your DM to decide what should be done.

The anatomy of a roll is the following:

roll type : (side `die source` option | ... | side `die source` option) [(die size `die source` | ... | die size `die source`)] + add-ons vs `target`

The "roll type" specifies what type of roll it is; either a `check` or a `test`. This lets you tell at a glance whether the roll is against a static number or another roll. Next, we have the options for die sides. If there are multiple options, they'll be contained within parenthesis `()` and separated with a pipe `|`. This means that the roller gets to choose which `die source` they want to use.

> Note the term "roller" was used, this does _not_ mean the `creature` that caused the roll! If the options are on the `defenders` side (after the vs), then the `defender` chooses for themselves. Similarly, if they're on the `attackers` side (before the vs), the `attacker` chooses for themselves.

Inside square brackets `[]` is the `die source` for the size of the dice. Again, if multiple `die sources` can be chosen from, they'll be contained within parenthesis `()` and separated with a pipe `|`. Any add-ons to the roll (remember, these can include other rolls!) are noted after before a "vs" which denotes where the `target` begins. Depending on if the roll is a `check` or a `test`, this will either be another roll or a static number.

If this was confusing still, the best way to explain this is through an example:

_In order to see if a `grapple` succeeds, roll a_

_`test`: `power` [`grappling`] vs (`prowess`|`power`) [`dodging`]_

The `attacker` rolls a number of dice equal to their `power` score, the size of which is determined by their `grappling` `proficiency` level (more on that in another section). This is compared against the `defenders` roll; they roll a number of dice equal to their choice of their `prowess` or `power` score, the size of which is determined by their `dodging` `proficiency`.

## Additional Dice

Certain `modifications` will cause a `creature` to gain or lose dice to certain rolls. When speaking about the modifications to the dice to roll, the which dice roll is specified by the `modification`. For example, let's take a look at the `stress`:

_While making a `strike`, a `creature` can elect to gain any number of `stress` in order to roll extra `striking` dice to `hit`._

In order to fully understand, we'll take a look at the `test` this refers to:

_`test`: `agility`[`striking`] + 1[`hit die`] vs `agility`[`dodging`]_

Since the excerpt about `stress` specifies you roll extra `striking` dice, this means that your `agility` score sets the base amount of `striking` dice you roll and you gain `stress` to increase that amount by the `stress` you gain. Since the `1[hit die]` component is _not_ referenced, we still only roll 1[`hit die`]. If our `agility` is 2 and we use 1 `stress` for the `strike`, we would roll a total of 3 `striking` dice.

There can also be dice rolls that don't modify the amount or size of dice rolled at base, but instead _add on_ to the dice already being rolled. Again, taking `stress` as an example:

_While a `creature` has accumulated `stress` past their capacity, they roll an extra 1d4 to their `check` to `pierce`._

And again, the `check` in reference:

_`check`: `strength`[`pierce die`] vs `armor value`_

If we are past our `stress` capacity, this means we roll 1d4 _in addition to_ the standard `strength`[`pierce die`], making our end `check` being the following:

_`check`: `strength`[`pierce die`] + 1d4 vs `armor value`_

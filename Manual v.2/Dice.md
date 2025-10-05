# Dice

In Dungeoneers, most the rolling happens at the beginning of `player phase`. Every dungeoneer has a pool of 6-sided dice called their `dice pool`. You start off with 5 dice in your `dice pool` and gain more periodically as you `level up` or use special `abilities`. Whenever an `action` specifies a `roll`, you utilize your `dice pool` to complete the task.

At the start of `player phase`, all `exhausted` dice are re-rolled, as well as any other dice in the `dice pool` the player wishes. For example, if Freya exhausts 3 of her 5 dice at the start of `player phase` she re-rolls her 3 `exhausted` dice. If she wishes to, she may also re-roll her 2 unused dice or hang on to them to use their side.

## Action Roll

An `action roll` is called for during an `action`. Each `action roll` will have a `stat` associated with it and a `difficulty`. In order to succeed on the `action roll`, you must be able to spend dice in your `dice pool` to overcome the `difficulty` after adding your `stat`.

Let's look at an example:

> Ulfarmi takes the `fight` `action` to attack a `skeleton`. He has his full `dice pool` available to him and he's rolled the following numbers: 4, 3, 4, 1, 2. In order to succeed on the `fight` `action`, Ulfarmi needs a 5 or greater. Since Ulfarmi is using an `arcana`-based `weapon`, he gets to add his `arcana` `stat` (4) to his total. This means that Ulfarmi only needs to use up the die that he rolled a 1 on in order to succeed!

Once a die from the `dice pool` is used for an `action roll`, it is `exhausted` and cannot be used again. In order to regain lost dice, the `rest` `action` must be used.

### Running out of Dice

If at any point you use your final die in your `dice pool` and then are subjected to another `roll`, you gain 1 `stress`. You may gain another `stress` to reroll and immediately use 1 die in your `dice pool`.

## Group Roll

A `group roll` is called for when multiple dungeoneers attempt to do the exact same thing with the exact same `action`, and that `action` calls for a `roll`. For example, if 2 dungeoneers both take the `fight` `action` to fight the same `creature`, or if 3 dungeoneers attempt to kick open a door.

During a `group roll`, the `difficulty` is increased by the number of dungeoneers that participate. Each dungeoneer may contribute their `stat` to the total, but they may only contribute 1 die from their `dice pool`.

If the `roll` has varying outcomes based on an equipped `weapon` or `stat`, the involved dungeoneers choose which outcome they wish. For example, if 2 dungeoneers `fight` a skeleton and one outcome would deal 2 damage and the other would deal 4 damage, the dungeoneers may opt for the 4 damage outcome.

## Degrees of Success

Whenever an `action roll` occurs (outside of the `fight` `action`, which is a special case) there are 4 possible outcomes, called `degrees of success`. These will be listed whenever the `roll` is called for. When a Game Master is calling for a `roll` outside of when it is explicitly lain out by the rules, they should also adhere to allowing different `degrees of success`. This will look something like the following:

`<stat> roll`

-   Failure: _Description of outcome_
-   Partial success (-3): _Description of outcome_
-   Success (0): _Description of outcome_
-   Greater success (3): _Description of outcome_

Something to immediately note is the numbers that sit beside the `partial success`, `success` and `greater success` outcomes. What this means is that if your total is 2 or less below the `difficulty`, you get a `partial success`. If your total is 2 or more _above_ the `difficulty`, it's a `greater success`. It's easiest to understand by applying some numbers, so let's do that.

Let's imagine our `difficulty` is 10. This means a total of 1-6 is a `failure`, 7-9 is a `partial success`, 10-12 is a `success` and 13 or more as a `greater success`.

## Criticals

Whenever you apply 2 or more dice to a `roll` and 2 sides are the same, it is treated as a `critical`. A `critical` increases the `degree of success` by 1 degree.

## Cooldowns and Durations

The other kinds of rolling that will be done are for `cooldowns` and `durations`. Whenever an `ability` is used, it goes on `cooldown` which is a number of `rounds` before it can be used again. Often times, `abilities` will last for a period of time called the `duration`.

In both cases, they are accompanied by a die size. When an `ability` is used, both the `cooldown` and the `duration` (if applicable) are rolled. Place these dice on the `ability` description and decrement their side by 1 at the start of every `round`. Once the `cooldown` die reaches 0, the `ability` can be used again. Once the `duration` die reaches 0, the effect no longer applies.

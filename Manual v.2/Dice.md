# Dice

In Dungeoneers, most the rolling happens at the beginning of `player phase`. Every dungeoneer has a pool of 6-sided dice called their `dice pool`. You start off with 6 dice in your `dice pool` and gain more periodically as you `level up` or use special `abilities`. Whenever an `action` specifies a `roll`, you utilize your `dice pool` to complete the task.

## Action Roll

An `action roll` is called for during an `action`. Each `action roll` will have a `stat` associated with it and a `difficulty`. In order to succeed on the `action roll`, you must be able to spend dice in your `dice pool` to overcome the `difficulty` after adding your `stat`.

Let's look at an example:

> Ulfarmi takes the `fight` `action` to attack a `skeleton`. He has his full `dice pool` available to him and he's rolled the following numbers: 4, 3, 4, 5, 1, 2. In order to succeed on the `fight` `action`, Ulfarmi needs a 5 or greater. Since Ulfarmi is using an `arcana`-based `weapon`, he gets to add his `arcana` `stat` (4) to his total. This means that Ulfarmi only needs to use up the die that he rolled a 1 on in order to succeed!

Once a die from the `dice pool` is used for an `action roll`, it is exhausted and cannot be used again. In order to regain lost dice, the `rest` `action` must be used.

## Cooldowns and Durations

The other kinds of rolling that will be done are for `cooldowns` and `durations`. Whenever an `ability` is used, it goes on `cooldown` which is a number of `rounds` before it can be used again. Often times, `abilities` will last for a period of time called the `duration`.

In both cases, they are accompanied by a die size. When an `ability` is used, both the `cooldown` and the `duration` (if applicable) are rolled. Place these dice on the `ability` description and decrement their side by 1 at the start of every `round`. Once the `cooldown` die reaches 0, the `ability` can be used again. Once the `duration` die reaches 0, the effect no longer applies.

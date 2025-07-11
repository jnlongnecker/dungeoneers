# Dice

In Dungeoneers, when there uncertainty in an outcome or an evaluation of ability of a `creature` that can have multiple outcomes, dice are used to determine what happens.

## Rolls

For any roll, the base is always built out of a roll of 3d10, or 3 ten-sided dice. This pool of dice will be accompanied by numbers to determine bonus dice to roll as well as the `target number` (`TN`) of your rolls, typically a `skill` and an `attribute`. Let's dive into both of those mechanics.

When you make a roll, you are trying to rack up successful rolls, called `successes`. A `success` is when you roll a number _less than or equal to_ your `TN`. If you roll a number _above_ your `TN`, that is called a `loss`.

### Core Rolls

For a `core roll` (`CR`), your `target number` is determined by your `attribute score` associated with the roll. You get additional dice to roll based on your `skill proficiency` associated with the `skill` called for.

In addition to these, each `CR` is evaluated against a `difficulty`. Each `difficulty` is associated with a number called the `DN`. This is the number that determines the degrees of success of the `CR` and is compared against the number of `successes` that were rolled. A `difficulty` has a natural language name and corresponds to the following `DN`:

| Difficulty   | Difficulty Number (`DN`) |
| ------------ | ------------------------ |
| Trivial      | 0                        |
| Easy         | 1                        |
| Average      | 2                        |
| Hard         | 3                        |
| Insane       | 4                        |
| Absurd       | 5                        |
| Unfathomable | 6                        |

Because it's hard to remember how the numbers line up with the natural language name of a `difficulty`, both are used in the rules. Your GM might decide to only say the number or only say the name of the `difficulty`; it's up to them. The aforementioned degrees of success are determined by how many `successes` that are rolled compared against the `DN`:

-   2 or more under the `DN`: Failure
-   1 under the `DN`: Lesser success
-   Meets `DN`: Success
-   1 or more over the `DN`: Greater success

This was a lot of precise language, so let's go through an example. When you see a `CR` called for in the rules, you'll see it in the following format:

**`Core` (`finesse`, `striking`) - Average (2)**

-   Lesser success (-1): _Description of what occurs_
-   Success (0): _Description of what occurs_
-   Greater success (1): _Description of what occurs_

Notice that what happens on a `failure` wasn't described, since whatever you were trying to do simply doesn't work on a `failure`. However, the other degrees of success are noted. Also notice that first listed in the parenthesis is the `attribute` and second listed is the `skill` being called for. If something specific _does_ happen on a `failure`, it will be noted.

Occasionally, the roller is able to pick between multiple options for their `attribute`. When this is the case, the two options are separated by a pipe (|), and looks like this:

**`Core` (`finesse`|`body`, `striking`) - Average (2)**

In this example, the roller can choose between using their `finesse` or their `body` score to determine their `TN`.

Let's apply some numbers with the earlier example with a `creature` that has 5 `finesse` and is `trained` in `striking`, giving them an additional die to roll. Imagine our `creature` rolled a 5, a 4, a 7, and a 1 on their 4d10. Since the `target number` is 5 (coming from the 5 `finesse`), this means that 3 `successes` were rolled, meaning the result of this `CR` is a greater success.

In Dungeoneers, only the players make `CRs`. Other `creatures` instead have `difficulties` that need to be met for a `CR` for the players. For example, instead of adversaries rolling to `strike` the players, they have a `strike difficulty` that the player must roll to `dodge`.

### Standard Roll

For a `standard roll` (`SR`), typically only a `target number` is specified, again often with an `attribute`. In these types of rolls, no additional dice are used so they are always of average `difficulty`; 2 `successes` are required. Here's an example:

**`Standard` (`finesse`) - Average (2)**

-   Lesser success (-1): _Description of what occurs_
-   Success (0): _Description of what occurs_
-   Greater success (1): _Description of what occurs_

### Group Rolls

Sometimes, circumstance calls for multiple `creatures` in a group to participate in a roll; these instances are `group rolls` (`GR`). The way the `GR` is handled is the following.

First, a leader is designated to lead the roll. Their `skill proficiency` sets the baseline dice to be rolled (minimum of 1d10), and their `attribute` sets the `target number` if one is not specified. For each additional `creature` that is part of the `GR`, an additional die is rolled. For each `loss`, the leader gains 1 `stress`.

### Tests

A `test` is a competition of two actively opposing skilled forces. In a `test`, two `core rolls` are competing against one another. However, instead of the `success` count being evaluated at a `difficulty`, they're instead evaluated against the `success` count of the _other_ `core roll`. Here's an example:

**`Test`: (`finesse`, `striking`) vs (`finesse`, `dodging`)**

-   Lesser success (-1): _Description of what occurs_
-   Success (0): _Description of what occurs_
-   Greater success (1): _Description of what occurs_

Something to notice is that in the event of a tie between the two, the initiator of the `test` (the one on the left) is the winner.

`Tests` are rarely used in Dungeoneers and are only for competition between player characters.

## Success Control

Whenever you make any kind of roll, there may be circumstances where you wish the outcome to be _less_ successful than how you rolled. For example, if an ally is trying to `push` you out of the way, you may want to decide to have fewer `successes` in order for their `push` to be more effective. Similarly, if you are the `push`-er, you may want your `push` to not be _that_ effective if you roll well.

In these circumstances, you can decide the number of `successes` you wish to use for the roll, as long as that number is equal to or less than the actual `successes` you rolled.

## Bane & Boon

In certain circumstances, a `creature` may be unusually hindered or aided in completing the task at hand. In these situations, they are awarded points of `bane` and `boon` to help or hinder their roll.

These points are two sides of the same coin and cancel each other out. For every point of `boon` a `creature` has, they add 1 to their `TN`. For every point of `bane` a `creature` has on a roll, they must _subtract_ 1 from their `TN`.

### Bane & Boon on Adversaries

Since only the players roll, how does `bane` and `boon` affect other `creatures`? `Bane` and `boon` will cancel one another out and the GM will roll 1d3, with the `TN` being the remaining points of `bane` or `boon`. Rolling a `success` raises (`boon`) or lowers (`bane`) the `DN`, while rolling a `loss` yields no result.

> You likely don't have a 3-sided die, as those don't exist! If you're using a physical dice, you roll 1d3 by rolling 1d6 and treating 1-2 as a 1, 3-4 as a 2 and 5-6 as a 3. If remembering this is undesired, you can instead roll 1d4. Be warned that doing so will make `bane` and `boon` less statistically impactful to non-players!

## Criticals & Compromises

In the circumstance that 2 dice roll a 1, this is a `critical`. When a `critical` occurs, 1 additional `success` is gained.

In the event that a player rolls a failure or lesser success, the player can opt for a `compromise` with the GM. In exchange for 1 additional `success`, the GM gains 1 `dread`. It is up to the GM whether to accept the `compromise` or not.

# Dungeoneering

The core of _Dungeoneers_ is divided into `rounds` which take two `phases`:

-   Player phase
-   World phase

During `player phase`, the first thing that occurs is a re-roll of each players' `dice pool`. They must re-roll all `exhausted` dice and may choose whether or not to re-roll their non-`exhausted` dice. The players then decide in which order to resolve each of their `turns`.

During a player `turn`, they may take up to 3 `actions`. The core 4 `actions` all use up a single `action`, but the `abilities` `action` that activates an `ability` may take more than 1 `action`. Any activation that does not require an `action` may be done so for free. The `actions` section has more information about the general `actions` available to players.

Once a player has used up all their `actions` or willingly relinquishes their `turn` before all `actions` are used, their `turn` ends. Players need not take their `turns` in the same order every `round`, nor do they need to take all their `actions` before another player can take any `actions`. However, no two players should take an `action` at the same time, and players who have just taken an `action` should be given priority to take another if they wish until they use up all their `actions`.

Once all players have taken their `turn`, the `player phase` ends and the `world phase` begins. During the `world phase`, the Game Master decides what `actions` are taken by the `environment`, other `creatures`, and any random events. Once the world has resolved, the `round` ends and a new `round` begins with the `player phase`.

## The Map

_Dungeoneers_ focuses heavily on the visual representation of the world, the map. The map has 2 levels of detail:

1. The `dungeon map`
2. The `wilderness map`

An important note on these names; they are merely titles and not always descriptive of what the maps actually represent. For example, you may have a `wilderness map` that represents a city, or a `dungeon map` that represents a forest tangle. They simply describe the level of detail they portray.

A `dungeon map` is a detailed representation of the world at the lowest (relevant) level. The `dungeon map` is divided into `tiles` that represent the space a single `medium` sized `creature` occupies. At this level, individual interactable objects are lain out as well as obstacles, hazards, and `creatures`. This is the level of detail that the majority of the game occurs in and is the level of detail referenced by all `actions` except for the `explore` `action`.

A `wilderness map` is a less detailed representation of the world that covers a larger space than a `dungeon map`. The `wilderness map` is divided into `tiles` that represent the space that can be traveled in about 30 minutes by a regular person. At this level, the minute details are not captured; instead only noting `notable features` (such as a distinct landmark like a hill or an telltale sign of a `creature`) or a `point of interest` (such as a shrine, statue, or old battle site). A `point of interest` is discovered immediately upon revealing a `wilderness map` `tile`, while a `notable feature` must be `investigated` for.

### Revealing the Map

For each level of detail, there are different ways in which more of the map is revealed. A `dungeon map` is revealed room-by-room; or by line of sight (whichever makes more sense in the moment). This means that large swathes of `tiles` are revealed all at once. A `wilderness map` is revealed tile-by-tile.

## Combat & Exploration

Fighting `creatures` and exploring the world are two sides of the same coin and happen together. Dungeoneers take `turns` moving themselves through the map in any manner they choose. Often times, they will encounter `creatures` and must decide what they wish to do with them. Some `creatures` will be hostile and immediately attack. Some may not notice the party right away and a strategy can be formulated. Some may be friendly and wish to trade or even team up with the party.

At the same time, the environment can be interacted with. Perhaps there are curious statues to decipher, or ancient puzzles to solve for riches. These interactions could potentially be happening at the same time as combat is happening down the hall. It is up to the party to determine how to handle their time.

### Conditions

Most effects in the game take place in the form of `conditions`. Most `conditions` are specific to the `technique` that applies it, but there are a few generic `conditions` that can get applied from a multitude of sources. Those `conditions` and what they do are detailed here.

> Intention note: `Conditions` have some sort of effect, whether positive or negative. Whenever the `condition` ends, the effect also ends immediately. If this effect `exhausts` dice, those dice are no longer `exhausted`.

#### Weakened

A `creature` who is `weakened` has all their `difficulties` reduced by 2. A dungeoneer who is `weakened` must exhaust 1 die of their choice at the start of every `round`.

#### Empowered

A `creature` who is `empowered` has all their `difficulties` increased by 2. A dungeoneer who is `empowered` gets to roll 1 additional die at the start of every `round`.

#### Incapacitated

A `creature` who is `incapacitated` has all their `difficulties` set to 0 and cannot take `actions`. A dungeoneer who is `incapacitated` has all their dice `exhausted` at the start of every `round` and cannot take `actions`.

#### Suffocating

A `creature` who is `suffocating` is `weakened` and a `countdown` begins. The `countdown` starts at the `power` of the `creature`, up to a maximum of 10 (use 1d10 to represent this `countdown`). Taking damage reduces the `countdown` by 1. When the `countdown` ends, the `creature` takes 1 `true` damage at the start of every `round`.

#### Burned

A `creature` who is `burned` takes 1 additional damage every time it takes damage.

#### Poisoned

A `creature` who is `poisoned` takes 1 `true` damage at the start of every `round`.

#### Freezing

A `creature` who is `freezing` has their `speed` `score` reduced by 2.

#### Wet

A `creature` who is `wet` cannot be `burned`. If a `creature` is `wet` and `freezing`, the `freezing` `duration` does not tick until the `wet` `duration` is complete.

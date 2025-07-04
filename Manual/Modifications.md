# Modifications

The baseline kit of all `creatures` is interesting enough, but doesn't quite capture the vast array of capabilities that make each `creature` unique. Instead, there are a number of `modifications` that apply to each `creature` that give them their uniqueness. Additionally, some `modifications` are temporary and potentially even negative. These `modifications` come in several categories:

-   `Abilities`
-   `Traits`
-   `Conditions`
-   `Properties`
-   `Effects`

## Abilities

An `ability` is a special capability that changes the basic kit of a `creature`. An `ability` can give new `actions`, apply `conditions`, and provide passive benefits amongst other things. For the most part, any `creature` can gain any `ability`, but some `abilities` have prerequisites. There are two categories of `ability`: `class abilities` and `generic abilities`. As you might imagine, `class abilities` are `abilities` granted by a `creature's` `class`. `Generic abilities` can be granted to any `creature`, as long as they meet any `prerequisites` that `ability` might have. `Generic abilities` are further categorized into 2 categories: `skill abilities` and `combat abilities`. `Abilities` will have its own dedicated section later on.

## Traits

A `trait` is an intrinsic property of a `creature`, and can be beneficial or handicapping. Typically, a `trait` is tied to the `creature` itself and cannot be permanently gained or lost otherwise.

### Vulnerability

`Vulnerability` is a `trait` that causes a `creature` to sustain more `wounds` than normal whenever a `wound` is sustained of a certain damage type. There are 3 levels of `vulnerability` (`vulnerability(1)`, `vulnerability(2)`, and `vulnerability(3)`) and a variant of `vulnerability` for every damage type. Each level of `vulnerability` causes the `creature` to sustain that number of extra `wounds`.

> For example, a skeleton has the `trait` `vulnerability(B1)`. This means that whenever a skeleton sustains 1 `bludgeoning` `wound`, they instead sustain 2.

### Resistance

`Resistance` is a `trait` that causes a `creature` to sustain _less_ `wounds` than normal whenever a `wound` is sustained of a certain damage type. There are 3 levels of `resistance` (`resistance(1)`, `resistance(2)`, and `resistance(3)`) and a variant of `resistance` for every damage type. Each level of `resistance` causes the `creature` to sustain that number fewer `wounds`.

> For example, a skeleton has the `trait` `resistance(P3)`. This means that whenever a skeleton sustains 3 or fewer `piercing` `wounds`, they instead sustain 0.

### Hyperarcanum

`Hyperarcanum` is a `trait` that describes a `creature` with sensitivity towards arca. A `creature` with `hyperarcanum` has 1 extra point of `arca` than normal and regains 1 more point of `arca` from any source that would do so. However, any source that would drain `arca` will drain 1 _extra_ `arca`.

> Note that _spending_ `arca` is different than _draining_ `arca`. Normal use of `arca` is not increased by `creatures` with `hyperarcanum`.

### Senses

There are multiple types of senses that a `creature` may have, and corresponding sense `traits` to describe them.

| Trait Name    | Trait Description                                            |
| ------------- | ------------------------------------------------------------ |
| Darkvision    | Vision that can see in complete, non-arcane darkness         |
| Truevision    | Vision that can see in arcane darkness and through illusions |
| Blindsense\*  | Ability to sense `creatures` without needing to use vision   |
| Tremorsense\* | Ability to sense `creatures` that are touching the ground    |
| Blind         | Does not have any visual sense                               |
| Deaf          | Cannot hear                                                  |

> \* These senses are not blocked by visual limiters like darkness or walls.

Each sense `trait` comes with a range. If a range is not specified, the range is unlimited. Unless a `creature` has the `blind` or `deaf` `traits`, they can see or hear at a level equal to a typical, healthy real-world human being.

### Speed

There are several different kinds of `speeds` a `creature` can use to travel. Each one has a name and number. The name denotes what kind of travel the `creature` may take, while the number denotes how many tiles that `creature` may traverse when they travel.

| Travel Speed | Description                                                                                 |
| ------------ | ------------------------------------------------------------------------------------------- |
| Ground       | The `creature` may traverse along the surface of a solid, horizontal plane.                 |
| Burrow       | The `creature` may traverse through solid dirt or stone.                                    |
| Fly          | The `creature` may traverse through the air.                                                |
| Swim         | The `creature` may traverse through water.                                                  |
| Climb        | The `creature` may traverse along the surface of a solid, vertical/vertically angled plane. |
| Cling        | The `creature` may traverse along the surface of a solid, horizontal plane against gravity. |

#### Movement

In order to distinguish between a `move` and physical movement through the world, the term "travel" is used instead of "move" to describe movement. Whenever a creature travels, they may use any of their `speeds` to do so. If you use multiple `speeds` to travel, subtract the number of tiles you have already covered from the new `speed` you wish to use to determine how many remaining tiles you can travel with the new `speed`.

> Example: Alberich has two `speeds`; `Ground(2)` and `Fly(3)`. If Alberich travels 1 tile using his `Fly` `speed`, he may only travel 1 tile with his `Ground` `speed` in the current travel. If he travels 2 tiles using his `Ground` `speed`, he may travel 1 tile using his `Fly` `speed` after.

### Language

A `creature` can utilize a number of languages in accordance to the below table. A `creature` with the `literate` `trait` can read and write with the `languages` they know. A `creature` with the `speech` `trait` may speak the `languages` they know. Unless a `creature` has the `deaf` `trait`, they can understand spoken words in any of the `languages` they know provided they can hear them.

| Language | Common Users                         |
| -------- | ------------------------------------ |
| Adish    | Most `creatures` capable of language |
| Mensish  | Mensa                                |
| Elvish   | Elves                                |
| Dwarvish | Dwarves                              |
| Gnomish  | Gnomes                               |

## Conditions

A `condition` is a temporary `modification` that is applied usually by some `move`.

### Grappled

`Creatures` who are `grappled` have their `travel` speeds forced to be 0 and gains 2 points of `bane` to all `dodging` rolls. When a `grappling` `creature` `travels`, the `creature` they are `grappling` is `forced` the same distance using the same `travel` speed as the `grappler`.

### Grappling

`Creatures` who are `grappling` have their `travel` speeds halved and gain 1 point of `bane` to all `dodging` rolls. If this `creature` is `forced`, the `grappling` and `grappled` `condition` are removed from their respective `creatures`.

### Defensive

`Creatures` who are `defensive` gain a point of `boon` to their `dodging` rolls.

### Blocking

`Creatures` who are `blocking` gain a point of `boon` to their `dodging` rolls and a point of `bane` to their `striking` rolls.

### Berserk

`Creatures` who are `berserk` gain a point of `boon` to their `striking` rolls, a point of `bane` on their `dodging` rolls, and deal 1 additional `wound` with `strikes`.

### Taunted

`Creatures` who are `taunted` only focus on the `creature` who applied this `condition` on them.

### Prone

`Creatures` who are `prone` gain 3 points of `bane` to their `dodging` rolls while they are `prone`. `Creatures` who make a `strike` against a `prone` `creature` who is outside of their `reach` also gains 3 points of `bane` to their `striking` roll.

### Frightened

`Creatures` who are `frightened` gain 1 point of `boon` to their `dodging` rolls, but all `speeds` become 0.

### Weakened

`Creatures` who are `weakened` deal 1 fewer `wounds` whenever they would deal a `wound`.

### Dazed

`Creatures` who are `dazed` gain two points of `bane` to their `dodging` rolls.

### Blinded

`Creatures` who are `blinded` cannot add their `proficiency` to `striking` or `dodging` rolls.

### Freezing

`Creatures` who are `freezing` gain a point of `bane` to their `dodging` and `striking` rolls.

### Burning

`Creatures` who are `burning` cannot recover `stress` or use `moves` that cause `stress`.

### Shocked

`Creatures` who are `shocked` cannot recover `arca`.

### Plagued

`Creatures` who are `plagued` have their `speeds` reduced by 1.

## Falling

A `creature` with the `falling` `condition` is `forced` towards the ground 15 tiles. This movement is applied the moment the `falling` `condition` is applied and at the start of every `round` thereafter. When the `creature` impacts a surface solid enough to stop them, the `falling` `condition` is removed and sustains 1 `bludgeoning` `direct wound` plus an additional `bludgeoning` `direct wound` per 5 tiles they fall. A `creature` may reduce the effective number of tiles they fall by making a

`check`: [1d4] + `body` vs number of tiles fallen.

If the `check` succeeds, the `creature` sustains no `wounds`. If they fail, the difference between the roll and the number of tiles fallen is the effective number of tiles they have fallen.

## Properties

`Properties` are `modifications` where the source is an `item`. Often times, the `modification` applies to the _`item`_ and not the `creature` using the `item`, but can also enforce requirements for using the `item`. More information about `properties` is covered in the `equipment` section.

## Effects

An `effect` is a `modification` that is applied when specific criteria is met. These `modifications` are usually the application of other `modifications` and are described elsewhere.

The only exception is the `forced` `effect` which will be explained here.

### Forced

When an entity is `forced`, it is moved via a `travel` speed against its will, ending up the number of tiles specified by the `travel` speed. This happens instantaneously.

> Example: the `push` `move` on a success causes the target to be `forced` Ground(1). This means that the target must move across the ground 1 tile against its will.

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

### Senses

There are multiple types of senses that a `creature` may have, and corresponding sense `traits` to describe them.

| Trait Name    | Trait Description                                             |
| ------------- | ------------------------------------------------------------- |
| Darkvision    | Vision that can see in complete, non-magical darkness         |
| Truevision    | Vision that can see in magical darkness and through illusions |
| Blindsense\*  | Ability to sense `creatures` without needing to use vision    |
| Tremorsense\* | Ability to sense `creatures` that are touching the ground     |
| Blind         | Does not have any visual sense                                |
| Deaf          | Cannot hear                                                   |

> \* These senses are not blocked by visual limiters like darkness or walls.

Each sense `trait` comes with a range. If a range is not specified, the range is unlimited. Unless a `creature` has the `blind` or `deaf` `traits`, they can see or hear at a level equal to a typical, healthy real-world human being.

### Travel Speed

There are several different kinds of `travel` speeds. Each one has a name and number. The name denotes what kind of `travel` the `creature` may take, while the number denotes how many tiles that `creature` may traverse when they take the `move` `action`.

| Travel Speed | Description                                                                                                                            |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| Ground       | The `creature` may traverse along the surface of a solid, horizontal plane.                                                            |
| Burrow       | The `creature` may traverse through solid dirt or stone.                                                                               |
| Fly          | The `creature` may traverse through the air. The `creature` is `falling` if they spend 1 `turn` not `moving` with this `travel` speed. |
| Swim         | The `creature` may traverse through water.                                                                                             |
| Climb        | The `creature` may traverse along the surface of a solid, vertical/vertically angled plane.                                            |
| Cling        | The `creature` may traverse along the surface of a solid, horizontal plane against gravity.                                            |

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

A `condition` is a temporary `modification` that is applied usually by some `ability`, `spell` or `action`.

### Threatened

A `creature` within the `threat range` of another `creature` that is hostile to them is `threatened`. By itself, `threatened` does not do anything but there are `abilities` that can only take effect on a `creature` who is `threatened`.

### Grappled

`Creatures` who are `grappled` have their `travel` speeds forced to be no greater than 0 and gain a point of `bane` to all `dodging` rolls. When a `grappling` `creature` uses the `move` `action`, the `creature` they are `grappling` is `forced` the same distance using the same `travel` speed as the `grappler`.

### Grappling

`Creatures` who are `grappling` have their `travel` speed halved. If this `creature` is `forced`, the `grappling` and `grappled` `condition` are removed from their respective `creatures`.

### Defensive

`Creatures` who are `defensive` gain a point of `boon` to their `dodging` rolls.

### Prone

`Creatures` who are `prone` gain 3 points of `bane` to their `dodging` rolls while they are `prone`. `Creatures` who make a ranged `strike` against a `prone` `creature` also gain the 3 points of `bane` to their `striking` roll.

## Falling

A `creature` with the `falling` `condition` is `forced` towards the ground 15 tiles. This movement is applied the moment the `falling` `condition` is applied and at the start of every `round` thereafter. When the `creature` impacts a surface solid enough to stop them, the `falling` `condition` is removed and sustains 1 `bludgeoning` `wound` plus an additional `bludgeoning` `wound` per 5 tiles they fall. A `creature` may reduce the effective number of tiles they fall by making a

`check`: [1d4] + `dexterity` vs number of tiles fallen.

If the `check` succeeds, the `creature` sustains no `wounds`. If they fail, the difference between the roll and the number of tiles fallen is the effective number of tiles they have fallen.

The `wounds` sustained by `falling` are unique. They are subject to `resistance` and `vulnerability`, but otherwise cannot be affected (including from `physical defense`). These `wounds` cannot be absorbed by `stress`.

## Properties

`Properties` are `modifications` where the source is an `item`. Often times, the `modification` applies to the _`item`_ and not the `creature` using the `item`, but can also enforce requirements for using the `item`. More information about `properties` is covered in the `equipment` section.

## Effects

An `effect` is a `modification` that is applied when specific criteria is met. These `modifications` are usually the application of other `modifications` and are described elsewhere.

The only exception is the `forced` `effect` which will be explained here.

### Forced

When an entity is `forced`, it is moved via a `travel` speed against its will, ending up the number of tiles specified by the `travel` speed. This happens instantaneously.

> For example, the `push` `action` on a success causes the target to be `forced` Ground(1). This means that the target must move across the ground 1 tile against its will.

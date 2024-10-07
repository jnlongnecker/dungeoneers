# Modifications

The baseline kit of all `creatures` is interesting enough, but doesn't quite capture the vast array of capabilities that make each `creature` unique. Instead, there are a number of `modifications` that apply to each `creature` that give them their uniqueness. Additionally, some `modifications` are temporary and potentially even negative. These `modifications` come in several categories:

-   `Abilities`
-   `Traits`
-   `Conditions`
-   `Effects`

## Abilities

An `ability` is a special capability that changes the basic kit of a `creature`. An `ability` can give new `actions`, apply `conditions`, and provide passive benefits amongst other things. For the most part, any `creature` can gain any `ability`, but some `abilities` have prerequisites. There are two categories of `ability`: `class abilities` and `generic abilities`. As you might imagine, `class abilities` are `abilities` granted by a `creature's` `class`, while `generic abilities` can be attained by any `creature` as long as they meet any other prerequisites the `ability` might have. `Class abilities` won't be covered here, but `generic abilities` will be covered.

## Traits

A `trait` is an intrinsic property of a `creature`, and can be beneficial or handicapping. Typically, a `trait` is tied to the `creature` itself and cannot be permanently gained or lost otherwise.

### Vulnerability

`Vulnerability` is a `trait` that causes a `creature` to sustain more `wounds` than normal whenever a `wound` is sustained of a certain damage type. There are 3 levels of `vulnerability` (`vulnerability 1`, `vulnerability 2`, and `vulnerability 3`) and a variant of `vulnerability` for every damage type. Each level of `vulnerability` causes the `creature` to sustain that number of extra `wounds`.

> For example, a skeleton has the `trait` `vulnerability 1: bludgeoning`. This means that whenever a skeleton sustains 1 `bludgeoning` `wound`, they instead sustain 2.

### Resistance

`Resistance` is a `trait` that causes a `creature` to sustain _less_ `wounds` than normal whenever a `wound` is sustained of a certain damage type. There are 3 levels of `resistance` (`resistance 1`, `resistance 2`, and `resistance 3`) and a variant of `resistance` for every damage type. Each level of `resistance` causes the `creature` to sustain that number fewer `wounds`.

> For example, a skeleton has the `trait` `resistance 3: piercing`. This means that whenever a skeleton sustains 3 or fewer `piercing` `wounds`, they instead sustain 0.

### Senses

There are multiple types of senses that a `creature` may have, and corresponding sense `traits` to describe them.

| Trait Name    | Trait Description                                             |
| ------------- | ------------------------------------------------------------- |
| Vision        | Typical vision good enough to see what is being fought        |
| Darkvision    | Vision that can see in complete, non-magical darkness         |
| Truevision    | Vision that can see in magical darkness and through illusions |
| Hearing       | Basic hearing capabilities                                    |
| Blindsense\*  | Ability to sense `creatures` without needing to use vision    |
| Tremorsense\* | Ability to sense `creatures` that are touching the ground     |
| Blind         | Does not have any visual sense                                |
| Deaf          | Cannot hear                                                   |

> \* These senses are not blocked by visual limiters like darkness or walls.

Each sense `trait` comes with a range. If a range is not specified, the range is unlimited.

## Conditions

A `condition` is a temporary `modification` that is applied usually by some `ability`, `spell` or `action`.

### Threatened

`Creatures` who are `threatened` are subject to `opportune strikes` when they move out of the `threat range` of the `creature` they are `threatened` by or if they used a ranged `spellcast`/`attack`.

### Grappled

`Creatures` who are `grappled` have 0 `movement points` and cannot gain any `movement points`. When the `entity` that is `grappling` them uses a `movement action`, this `creature` immediately takes that same `movement action`.

### Grappling

`Creatures` who are `grappling` have half (rounded down) their normal `movement points` and gain half (rounded down) `movement points` from any `effect` that would grant them. If this `creature` takes a `movement action` while on _another_ `creatures` `turn`, the `grappling` and `grappled` `condition` are removed from their respective `creatures`.

### Sprinting

`Creatures` who are `sprinting` gain 2 base `movement points`.

### Defensive

`Creatures` who are `defensive` may roll 1 additional `dodge die` when they are `defenders`.

### Prone

`Creatures` who are `prone` can only roll a maximum of 1 `dodge die` when they are `defenders`. If a `prone` `creature` is a `defender` against a `spell save` that uses `prowess`, they may roll a maximum of 1 `spell save die`. `Creatures` who are ranged `attackers` against a `prone` `defender` may only roll a maximum of 1 `hit die` or `spell hit die`.

## Effects

An `effect` is a `modification` that is applied when specific criteria is met. It's not really a _different_ concept from other `modifications`, it's merely the _application_ of the `modification`.

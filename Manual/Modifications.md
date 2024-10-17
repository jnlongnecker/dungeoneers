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

A `creature` within the `threat range` of another `creature` that is hostile to them is `threatened`. By itself, `threatened` does not do anything but there are `abilities` that can only take effect on a `creature` who is `threatened`.

### Grappled

`Creatures` who are `grappled` have their `travel` speeds forced to be no greater than 0. When a `grappling` `creature` uses the `move` `action`, the `creature` they are `grappling` is `forced` the same distance using the same `travel` speed as the `grappler`.

### Grappling

`Creatures` who are `grappling` have their `travel` speed halved. If this `creature` is `forced`, the `grappling` and `grappled` `condition` are removed from their respective `creatures`.

### Defensive

`Creatures` who are `defensive` can roll an extra 2d4 as `defenders` to `tests` made to `hit`.

### Prone

`Creatures` who are `prone` gain the `agilitybane(4)` `condition`, but only to `tests` made to `hit`. `Creatures` who make a `test` to `hit` a `creature` who is `prone` and outside of their `threat range` also gain the `agilitybane(4)` `condition` for that `test`.

> For example, if a goblin is `prone` and Suori makes a `strike` at it with a warhammer, the goblin can only roll 1d6 despite having 2 `agility`. If Suori was instead making a ranged `strike` with a short bow at that goblin,

## Properties

`Properties` are `modifications` where the source is an `item`. Often times, the `modification` applies to the _`item`_ and not the `creature` using the `item`, but can also enforce requirements for using the `item`. More information about `properties` is covered in the `equipment` section.

## Effects

An `effect` is a `modification` that is applied when specific criteria is met. It's not really a _different_ concept from other `modifications`, it's merely the _application_ of the `modification`.

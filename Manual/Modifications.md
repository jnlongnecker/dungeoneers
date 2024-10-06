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

## Effects

An `effect` is a `modification` that is applied when specific criteria is met. It's not really a _different_ concept from other `modifications` as when the above take place conditionally, the result is called an `effect`. It's meant as a catch-all to refer to these conditional `modifications`.

> For example, the \_\_\_ `ability` applies the `prone` `condition` on a `hit`. This would be categorized as an on `hit` `effect`, because it conditionally takes place when a `hit` occurs.

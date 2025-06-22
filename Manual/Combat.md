# Combat in Dungeoneers

As a Dungeoneer, you will encounter many foes that stand in your way to your inevitable goal. Some may be able to be avoided, but you will ultimately come to blows with many `creatures`. You should become familiar with combat mechanics in order to overcome these obstacles and complete your mission. When `creatures` come to blows, not all interactions between the combatants influence the results of the combat. These interactions still _happen_, but they are not the "spotlight". In Dungeoneers, combat only focuses on the spotlight.

Combat is a `scene` like any other `scene` and is handled via the same flow of play. However, GM `moves` are much more common during combat.

## Damage Types

Whenever a `wound` is sustained, there is a `damage type` associated with it. This is important as some `damage types` are more or less effective on certain `creatures`.

> For example, a skeleton won't be phased by a dagger because its `damage type` is piercing. However, a big maul smashes it to pieces with its bludgeoning `damage type`!

Each `damage type` is part of a category, and all types exist under the "damage" category. The following is a list of all `damage types` and the categories they fall under:

-   Damage
    -   Physical
        -   Bludgeoning (B)
        -   Piercing (P)
        -   Slashing (S)
    -   Energy
        -   Heat (H)
        -   Cold (C)
        -   Toxic (T)
        -   Disintegrate (D)
    -   Precision

## Combat Moves

The `moves` found here are ones that are most applicable during combat. As a reminder, any `move` can be taken at any time, as long as it applies.

### Sprint

Tags: Movement
Range: Self

---

You may use the `sprint` `move` to travel additional tiles. Roll a

`total`: [`finesse`]d4.

The total is the number of additional tiles you may travel.

> Example: Alberich takes the `sprint` `move` and gets a total of 3, Alberich may travel 3 tiles using his travel `speeds`, plus the distance he could normally cover while traveling. If Alberich only has a `speed` of `Ground(6)` for example, he could travel `Ground(9)` with this roll.

### Grapple

Tags: Attack
Range: Reach

---

You must have a hand free in order to take this `move`. In order to see if a `grapple` succeeds, roll a

`test`: [`striking`] + `body` vs [`dodging`] + (`finesse`|`body`).

If the `grapple` succeeds, you are `grappling` and the `defender` is `grappled`.

### Push

Tags: Attack
Range: Reach

---

In order to see if a `push` succeeds, roll a

`test`: [`striking`] + `body` vs [`dodging`] + (`finesse`|`body`).

If the `push` succeeds, the `defender` is `forced` in a direction of your choosing or knocked `prone`.

### Strike

Tags: Attack, Critical
Range: Weapon Range

---

A `strike` is a `move` that constitutes attacking a `creature` with some sort of weapon. This weapon could be a club, a dagger, an enchanted staff, or even a bare fist! During a `strike`, the `attacker` is the `creature` making the `strike` and the `defender` is the `creature` subject to the `strike`.

> In other systems, there is often a distinction between attacks with a weapon and attacks without a weapon, or with an object not typically used as a weapon. In Dungeoneers, all strikes with physical objects are `strikes`; there is no difference. Attacks with arcana are treated differently, and we'll talk about that when we get to `performing arcana`.

There are 2 steps to the process of making a `strike`:

-   Determine if the `strike` `hits`
-   Determine the number of `wounds` inflicted

To determine a `hit`, roll a

`test`: [`striking`] + `finesse` vs [`dodging`] + `finesse`.

On a failure, the `strike` `misses`. On a partial success, the `defender` accumulates an amount of `stress` equal to the number of `wounds` marked on the `attackers` weapon, plus the `attackers` `body` score. On a success, the `strike` `hits` and the `defender` then sustains the number of `wounds` marked on the `attackers` weapon, plus the `attackers` `body` score.

### Perform Arcana

Tags: Arcana, Critical
Range: Varies

---

In the middle of combat, there simply isn't enough time to cast `arcana` in the traditional way. In order to cast `arcana` quickly, a `creature` must either use a tome, invoke a miracle/curse or use a `cantrip`. Regardless of which they choose, in order to cast the `arcana` a `creature` must take the `perform arcana` `move`.

> Keep in mind that not all `cantrips` are treated the same! Some `cantrips` are extremely weak, and some are more powerful than many spell tomes. The determining factor of what is and is not a `cantrip` is the location of the spell inscription.

All `arcana` consumes `arca` in order to be cast. A `creature` has an amount of `arca` equal to their `level`. Each `arcana` has a baseline amount of `arca` that must be spent in order to cast and/or maintain the `arcana`.

Every `arcana` has a range on it. The range can be self meaning the `arcana` can only be applied to the caster, reach meaning the `arcana` can be cast within the `reach` of the caster, or denoted in a distance of tiles.

> Note: you cannot target a `creature` outside the range of the particular `arcana`!

The details of what happens when you cast `arcana` depends on the `arcana`, and is found in the `arcana` detail section.

### Leap

Tags: Movement
Range: Self

---

You may jump a number of tiles equal to your `body` score. Alternatively, you may gain 1 `stress` and elect to jump a greater distance by succeeding on a:

`check`: 1d4 + `body` vs (number of tiles you want to jump)

On a success, you make the jump. On a failure, you overstrain yourself and only jump half the distance.

## Combat Free Moves

The `free moves` found here are ones that are most applicable during combat.

### Reposition

Tags: Movement
Range: Self

---

A `creature` may travel using their `speeds`.

### Interact

Tags: Interaction
Range: Reach

---

You may `interact` to manipulate your environment. Opening doors, pulling levers, drawing or stowing a weapon, equipping a shield, drinking a potion, picking up an object, and similar such tasks can all be accomplished.

### Drop Prone

Tags: Movement
Range: Self

---

You immediately fall `prone`.

### Hop

Tags: Movement
Range: Self

---

You may jump a number of tiles equal to your `Ground` `speed`.

### Mount

Tags: Movement
Range: Reach

---

You may climb onto a willing `creature` at least one `size` larger than you.

### Channel

Tags: Arcana
Range: Self

---

You recover `arca` equal to your `spirit` score.

## Critical Hits

When a roll is made that would cause a `wound` from a success, the normal rules around `criticals` apply. Additionally, for each `critical`, the `wounds` from the roll are applied again. These additional `wounds` are calculated before any other `modifications`, like adding or subtracting a `creature's` `body` score.

> Example: if a roll `criticals` twice and would deal 2 `wounds`, it instead deals 6 `wounds`. If the roll was done by a `creature` and their `body` score was 3, that same roll would instead deal 9 `wounds`.

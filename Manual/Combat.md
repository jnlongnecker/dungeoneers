# Combat in Dungeoneers

As a Dungeoneer, you will encounter many foes that stand in your way to your inevitable goal. Some may be able to be avoided, but you will ultimately come to blows with many `creatures`. You should become familiar with combat mechanics in order to overcome these obstacles and complete your mission. When `creatures` come to blows, not all interactions between the combatants influence the results of the combat. These interactions still _happen_, but they are not the "spotlight". In Dungeoneers, combat only focuses on the spotlight.

Combat is a `scene` like any other `scene` and is handled via the same flow of play. However, GM `actions` are much more common during combat.

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

## Combat Actions

The `actions` found here are ones that are most applicable during combat. As a reminder, any `action` can be taken at any time, as long as it applies.

### Sprint

Tags: Movement, Momentum
Range: Self

---

You may use the `sprint` `action` to `move` additional times.

`Standard` (`body`) - Average (2)

-   Lesser success (-1): You may `move` using 1x your `speeds`
-   Success (0): You may `move` using 2x your `speeds`
-   Greater success (1): You may `move` using 3x your `speeds`

### Grapple

Tags: Attack
Range: Reach

---

You must have a hand free in order to take this `action`.

`Core`: (`body`, `striking`) - `Dodging difficulty`

-   Lesser success (-1): Your target is `grappled` and you are `grappling`, `Countdown`: `RC`(1)
-   Success (0): Your target is `grappled` and you are `grappling`
-   Greater success (1): Your target is `grappled` and you are `grappling`, your target also gains 1 `stress`

### Push

Tags: Attack, Forces
Range: Reach

---

You may use the `push` `action` to reposition another `creature` or an object.

`Core`: (`body`, `striking`) - `Dodging difficulty`

-   Lesser success (-1): Your target is `forced` 1 tile
-   Success (0): Your target is `forced` 2 tiles or knocked `prone`
-   Greater success (1): Your target is `forced` 2 tiles and knocked `prone`

If the target is an object, the `DN` is the `size number` of the object.

### Strike

Tags: Attack, Deadly
Range: Weapon Range

---

A `strike` is an `action` that constitutes attacking a `creature` with some sort of weapon. This weapon could be a club, a dagger, an enchanted staff, or even a bare fist! During a `strike`, the `attacker` is the `creature` making the `strike` and the `defender` is the `creature` subject to the `strike`.

`Core`: (`finesse`, `striking`) - `Dodging difficulty`

-   Lesser success (-1): Your target gains a number of `stress` equal to the `wounds` from your weapon
-   Success (0): Your target takes a number of `wounds` equal to the `wounds` from your weapon
-   Greater success (1): Your target takes a number of `wounds` equal to _twice_ the `wounds` from your weapon

A `hit` occurs on a result of a success or better.

### Perform Arcana

Tags: Arcana, Deadly
Range: Varies

---

In the middle of combat, there simply isn't enough time to cast `arcana` in the traditional way. In order to cast `arcana` quickly, a `creature` must either use a tome, invoke a miracle/curse or use a `cantrip`. Regardless of which they choose, in order to cast the `arcana` a `creature` must take the `perform arcana` `action`.

> Keep in mind that not all `cantrips` are treated the same! Some `cantrips` are extremely weak, and some are more powerful than many spell tomes. The determining factor of what is and is not a `cantrip` is the location of the spell inscription.

All `arcana` consumes `arca` in order to be cast. A `creature` has an amount of `arca` equal to their `level`. Each `arcana` has a baseline amount of `arca` that must be spent in order to cast and/or maintain the `arcana`.

Every `arcana` has a range on it. The range can be self meaning the `arcana` can only be applied to the caster, reach meaning the `arcana` can be cast within the `reach` of the caster, or denoted in a distance of tiles.

> Note: you cannot target a `creature` outside the range of the particular `arcana`!

The details of what happens when you cast `arcana` depends on the `arcana`, and is found in the `arcana` detail section.

### End Condition

Tags: Restoration, Momentum
Range: Reach

---

You attempt to end a `condition` that is ailing another `creature` within your `reach`.

`Standard`: (`mind`) - Average (2)

-   Lesser Success (-1): You end 1 `condition` of your choice, but you and the target gain 1 `stress`
-   Success (0): You end 1 `condition` of your choice
-   Greater Success (1): You end 1 `condition` of your choice and the target loses 1 `stress`

## Combat Free Actions

The `free actions` found here are ones that are most applicable during combat.

### Reposition

Tags: Movement
Range: Self

---

A `creature` may use the `reposition` `free action` to `move` or stand up.

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

### Mount

Tags: Movement
Range: Reach

---

You may climb onto a willing `creature` at least one `size` larger than you.

### Channel

Tags: Arcana
Range: Self

---

You recover 1 `arca`.

## Deadly Hits

For `actions` with the `deadly` `tag`, for each `success` above a greater success, the `wounds` from the `action` are applied again.

> Example: a `strike` that deals 4 `wounds` on a success and 8 `wounds` on a greater success would deal 12 `wounds` at +2 `successes`, 16 wounds at +3 `successes` and so on.

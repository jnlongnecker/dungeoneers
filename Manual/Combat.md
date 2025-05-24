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

## Combat Moves

The `moves` found here are ones that are most applicable during combat. As a reminder, any `move` can be taken at any time, as long as it applies.

### Interact

Tags: Interaction

---

A `creature` may use the `interact` `move` to manipulate its environment. Opening doors, pulling levers, drawing or stowing a weapon, equipping a shield, drinking a potion, picking up an object, and similar such tasks can all be accomplished using the `interact` `move`.

### Sprint

Tags: Movement

---

A `creature` may use the `sprint` `move` to `travel` _twice_.

### Grapple

Tags: Attack

---

A `grapple` `move` may only be used on a `creature` they `threaten`, and a `creature` must have a hand free in order to take this `move`. In order to see if a `grapple` succeeds, roll a

`test`: [`grappling`] + `body` vs [`dodging`] + (`finesse`|`body`).

If the `grapple` succeeds, the `attacker` is `grappling` and the `defender` is `grappled`.

### Push

Tags: Attack

---

A `push` `move` may only be used on a `creature` they `threaten`. In order to see if a `push` succeeds, roll a

`test`: [`grappling`] + `body` vs [`dodging`] + (`finesse`|`body`).

If the `push` succeeds, the `defender` is `forced` in a direction of the `attackers` choosing or knocked `prone`.

### Strike

Tags: Attack, Critical
Cost: 3 action points

---

A `strike` is an `action` that constitutes attacking a `creature` with some sort of `weapon`. This `weapon` could be a club, a dagger, an enchanted staff, or even a bare fist! During a `strike`, the `attacker` is the `creature` making the `strike` and the `defender` is the `creature` subject to the `strike`.

> In other systems, there is often a distinction between attacks with a weapon and attacks without a weapon, or with an object not typically used as a weapon. In Dungeoneers, all strikes with physical objects are `strikes`; there is no difference. Attacks with arcana are treated differently, and we'll talk about that when we get to `spellcasts`.

Every `strike` is either melee or ranged. If the distance to the `defender` is greater than the `threat range` of the `attacker`, the `strike` is ranged. Unless a `weapon` has the `range` or `toss` `properties`, you cannot make a `strike` against a `creature` outside your `threat range`.

There are 3 steps to the process of making a `strike`:

-   Determine if the `strike` `hits`
-   Determine the number of `wounds` inflicted

To determine a `hit`, roll a

`test`: [`striking`] + `finesse` vs [`dodging`] + `finesse`.

On a failure, the `strike` `misses`. On a success, the `strike` `hits` and the `defender` then sustains the number of `wounds` marked on the `attackers` `weapon`, plus their `body` score.

#### A Sample Scenario

> For example, Suori makes a `strike` on a skeleton. The skeleton is `trained` in `dodging`, and has an `finesse` score of 1. Suori is making this attack with a warhammer, which gives her a `pierce die` of a d6. Suori is `trained` in `striking` and has an `finesse` score of 2. This means that Suori rolls 2d6, and the skeleton rolls 1d6. If the `test` succeeds, Suori `hits`!
>
> If Suori `hits`, we then roll the `check` to `pierce`. The skeleton has an `armor value` of 5 and Suori has 2 `body`, so Suori rolls 2d6 and compares her total against 5. If Suori `pierces`, she then causes the skeleton to sustain 1 `bludgeoning wound` as marked on the warhammer, + 2 for her `body` score. We definitely recommend writing down these numbers for your character so you don't have to look them up in the moment!

### Power Strike

Tags: Attack, Critical
Cost: 4 action points

---

A `creature` that takes the `power strike` `action` can make 1 `strike`. This `strike` deals 1 extra `wound` and has 1 point of `boon` on the `striking` roll.

### Spellcast

Tags: Arcana, Critical
Cost: Varies

---

In the middle of combat, there simply isn't enough time to cast a `spell` in the traditional way. In order to cast a `spell` quickly, a `creature` must either cast out of a tome or use a `cantrip`. Regardless of which they choose, in order to cast the `spell` a `creature` must take the `spellcast` `action`.

> Keep in mind that not all `cantrips` are treated the same! Some `cantrips` are extremely weak, and some are more powerful than many spell tomes. The determining factor of what is and is not a `cantrip` is the location of the spell inscription.

A `spell` consumes `arca` in order to be cast. A `creature` has an amount of `arca` equal to twice their `wisdom` score. Each `spell` has a baseline amount of `arca` that must be spent in order to cast the `spell`, and extra `arca` must be spent to overcome the `defender`. Ambient `arca` is available to spend on the baseline cost of the `spell`.

Every `spell` has a range on it. The range can be self meaning the `spell` can only be applied to the caster, reach meaning the spell can be cast within the `reach` of the caster, or denoted in a distance of tiles.

> Note that you cannot target a `creature` outside the range of the particular `spell`!

There are 3 steps to the process of making a `spellcast`:

-   Determine if the `spellcast` `hits`
-   Determine the the `spells` effect

The `attacker` must decide how much extra `arca` is used before seeing if the `spell` `hits`, and that `arca` is expended whether the `spell` `hits` or not.

#### Resolving a Spell Attack

If a `spell` calls for a `spell attack`, roll a

`test`: [`spellcraft`] + `mind` vs [`target skill`] + `spirit`.

If the `test` succeeds, the `spellcast` `hits`.

> Note that each `spell` that requires a `spell attack` will target a specific `skill` in its description. This is what `proficiency` is used for the `defender's` roll. Sometimes, a `spell attack` may be requested at a later point than during the `spellcast` `action`, make sure you read the `spell`!

#### On Hit

If the `spell` `hits`, the next step is to apply the `spell` `effect`. Read the `spell` to determine the impact of the extra `arca` spent and what occurs when the `spell` `hits`.

## Reactions

Some tasks happen practically automatically in response to certain stimuli. A `reaction` represents an instantaneous twitch of muscle memory; practically involuntarily. All `reactions` cost `action points`, and a `reaction` can only be used if that `creature` still has `action points` to spare.

### Grab a Ledge

Tags: Reaction
Cost: 1 action point

---

A `creature` may instinctively reach out for a ledge if they find themselves being knocked off. If a `creature` is `forced` to a point where they pass over a ledge within their `threat range`, they may use the `grab a ledge` `reaction` to stop themselves at the ledge. In order to do so, roll a

`check`: [1d4] + `dexterity` vs 5 + the number of tiles `forced`.

On a success, the `creature` stops at a point where they are hanging on the ledge.

## Critical Hits

When a roll is made that would cause a `wound` from a success, the normal rules around `criticals` apply. Additionally, for each `critical`, the `wounds` from the roll are applied.

> Example: if a roll `criticals` twice and would deal 2 `wounds`, it instead deals 6 `wounds`.

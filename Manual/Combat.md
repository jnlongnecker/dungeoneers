# Combat in Dungeoneers

As a Dungeoneer, you will encounter many foes that stand in your way to your inevitable goal. Some may be able to be avoided, but you will ultimately come to blows with many `creatures`. You should become familiar with combat mechanics in order to overcome these obstacles and complete your mission. When `creatures` come to blows, the passage of time becomes more strictly represented. All of time is represented in the following way, but it is typically only important to track this during time-sensitive moments like combat.

A time span of 6 seconds is represented by a `round`. During a `round`, each `creature` has 6 `action points` representing their ability to affect their world each second. During the course of a single `round`, a `creature` will have one or more `turns` in order to spend their allotted `action points`, but the way this works may be different than what you're used to if you've played a turn-based game before. Instead of a `creature` using up all of their `action points` at once, they instead use 1 `action` that costs 1-6 `action points`. Once they do so, their `turn` is over and the `creature` with the next highest `action point` total takes their `turn`. In the event of a tie, the two `creatures` act simultaneously if they are in the same `creature group` (described below). If two `creatures` from different `creature groups` have the same number of `action points`, the `creature` from the `group` with the higher `body` total goes first.

> It is useful to precalculate the `body` total of each group ahead of time to keep the flow of combat going! Make sure it's clear and easy to find out how to break ties, as it's pretty common.

Certain `actions` can be taken in response to something occurring in the world. These `actions` are called `reactions`. They still use `action points`, so a `creature` _must have_ `action points` still in order to use them. A `reaction` interrupts anything that is currently happening until the completion of the `reaction`, then the interrupted `action` continues if possible. Once all `creatures` are at 0 `action points`, this marks the end of the `round` and a new `round` begins with every `creature` at 6 `action points` again.

Let's walk through an example to see how this works in action with 3 `creatures`; 2 player characters (Freya and Alberich) and 1 skeleton:

-   At the start of the `round`, each `creature` has 6 `action points`
-   The player group has a higher body total than the skeleton, so the player characters go first
-   Alberich spends 3 `action points`, so now his `turn` is over and Freya goes
-   Freya spends 2 `action points`, so now her `turn` is over and the skeleton goes
-   The skeleton spends 4 `action points`, so now it is Freya's turn since she has the most `action points`
-   Freya spends 1 `action points`, which brings her total to the same as Alberich
-   Freya spends 1 `action point` again
    -   Note that Alberich is going at the same time here, we've just chosen to put Freya first
-   Alberich spends 2 `action points`
-   Now Freya and the skeleton have the same `action point` total, so Freya goes first due to her being in the higher `body` total group
-   Freya spends her remaining 2 `action points`
-   The skeleton also spends 2 `action points`
    -   This causes Alberich to use a `reaction` that costs 1 `action points`.
    -   Freya _could not_ react because she had 0 `action points` remaining
-   Now all `creatures` have 0 `action points`, and a new `round` begins with all `creatures` at 6 `action points`

## Creature Groups

`Creatures` who are allied with one another should be part of the same group, unless it makes sense for them not to (for example, reinforcements arriving in the middle of combat). The `players` are always part of the same group, unless for whatever reason they are not allied with one another. Any `NPC` allies of the `players` should be part of their own group.

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

## Actions

There are many things that use up `action points`, and the specific cases are covered by the specific abilities that give the `action`. Some `actions` may take up multiple `action points`, many only use 1. Many `actions` are given to `creatures` through various `abilities`. However, there are some basic `actions` that are able to be taken by any `creature` unless otherwise specified which we will cover here.

Every `action` has one or more `tags` that is used to categorize that `action`. For simplicity, `tags` are used to refer to groups of `actions` instead of having to list off each and every `action` that the rule affects.

### Deep Breath

Tags: Restoration
Cost: 2 action points

---

A `creature` may use the `deep breath` `action` to relieve 2 points of `stress`. This `action` may only be used if the `creature` has _more_ `stress` than their capacity.

> For example, Freya has 4 `endurance`, meaning her `stress` capacity is 4. If she has fewer than 4 `stress` accumulated, she cannot use the `deep breath` `action`. However, if she has 5 or more `stress` accumulated, the `deep breath` `action` relieves 2 points of `stress`. This _does_ mean if she has exactly 5 `stress`, it will reduce her `stress` to 3; below her capacity!

### Focus

Tags: Restoration
Cost: 2 action points

---

A `creature` may use the `focus` `action` to regain 2 points of `arca`.

### Interact

Tags: Interaction
Cost: 1 action point

---

A `creature` may use the `interact` `action` to manipulate its environment. Opening doors, pulling levers, drawing or stowing a weapon, equipping a shield, drinking a potion, picking up an object, and similar such tasks can all be accomplished using the `interact` `action`.

### Move

Tags: Movement
Cost: 1 action point

---

A `creature` may use 1 `action point` to use the `move` `action` to choose a `travel` speed and move up to a number of tiles equal to that `travel` speed.

> For example, a `creature` may have 2 `travel` speeds: Ground (1) and Fly (2). That `creature` may take the `move` `action` and choose one of their `travel` speeds, either Ground (1) or Fly (2). If they choose Fly(2), they may fly up to 2 tiles. If they choose Ground (1), they may move along the ground 1 tile.

### Sprint

Tags: Movement
Cost: 1 action point

---

A `creature` may use the `sprint` `action` to choose a `travel` speed and move _twice_ the number of tiles equal to that `travel` speed. In doing so, the `creature` gains 1 points of `stress`.

### Defend

Tags: Defensive
Cost: 2 action point

---

A `creature` may use 1 `action point` to use the `defend` `action` to give themselves the `defensive` `condition` until the start of their next `turn`.

### Ready

Tags: Untagged
Cost: 1 action point

---

A `creature` may make the `ready` `action` on their turn to delay the start of an `action` they can use. The chosen `action` is called the `readied` `action`. The `creature` may then take the `readied action` as a `reaction` at any time during the current `round`.

> Note that the `ready` `action` itself costs 1 `action point`. This is **in addition** to the cost of the `readied action`, but the `action points` for the `readied action` are only spent when it is used as a `reaction`. If this never occurs, only the `action point` for the `ready` `action` is spent.
>
> Also keep in mind that you do not _have_ to use your `readied action`. This `action` merely gives you the ability to do so as a `reaction` for the current `round`.

### Grapple

Tags: Attack
Cost: 2 action points

---

A `creature` may use 2 `action points` to use the `grapple` `action`. A `grapple` may only be used on a `creature` they `threaten`, and a `creature` must have a hand free in order to take this `action`. In order to see if a `grapple` succeeds, roll a

`test`: [`grappling`] + `body` vs [`dodging`] + (`finesse`|`body`).

If the `grapple` succeeds, the `attacker` gains the `grappling` `condition` and the `defender` gains the `grappled` `condition`. If the `grappling` `creature` is `forced`, the `grapple` immediately ends and the `grappling` and `grappled` `conditions` are removed from their respective `creatures`.

### Push

Tags: Attack
Cost: 2 action points

---

A `creature` may use 2 `action points` to use the `push` `action`. A `push` may only be used on a `creature` they `threaten`. In order to see if a `push` succeeds, roll a

`test`: [`grappling`] + `body` vs [`dodging`] + (`finesse`|`body`).

If the `push` succeeds, the `defender` is `forced` Ground(1) in a direction of the `attackers` choosing.

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

Critical hits occur when an `attacker` roll greatly exceeds a `defender` roll on an `action` with the `critical` tag. Each `creature` has a number called a `critical threshold`. For each multiple of the `critical threshold` that the `attacker` roll exceeds the `defender` roll by, a critical hit occurs. The `wounds` dealt again for each critical hit that occurs, plus the original `wounds`. The default `critical threshold` of all `creatures` is 5. A critical hit reapplies _all_ `wounds` that would be dealt by the `action`.

> For example, let us consider the following `test` for a `strike`: 1d6 + 3 vs 1d6 + 3. For a critical hit to occur, the `striking` roll must exceed the `dodging` roll by 5. Therefore, 6 + 3 vs 1 + 3 = 9 vs 4 results in a 1x critical hit, and the `wounds` are dealt a total of 2 times (once for the normal `wounds` done, and another for the 1x critical hit).
>
> Let us consider a second example with a point of boon: 1d6 + 4 + 1d4 vs 1d6 + 3. Imagine that the result is 6 + 4 + 4 vs 1 + 3 = 14 vs 4. Since the `striking` roll exceeds the `dodging` roll by 2 multiples of the `critical threshold`, this results in a 2x critical hit and the `wounds` are dealt a total of 3 times.
>
> Imagine in our first case, the weapon deals 1 `wound` and the `attacker` has a `body` score of 3. The normal `wounds` dealt from the `strike` would be 4, but since it's a 1x critical hit it will deal a total of 8 `wounds`. For the 2x critical hit, it would do 12 `wounds`. If the `defender` had vulnerability(1) to the `damage type`, the normal hit would deal 5 `wounds`, the 1x critical hit would do 10 `wounds` and the 2x critical hit would do 15 `wounds`.

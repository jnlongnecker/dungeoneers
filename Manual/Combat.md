# Combat in Dungeoneers

As a Dungeoneer, you will encounter many foes that stand in your way to your inevitable goal. Some may be able to be avoided, but you will ultimately come to blows with many `creatures`. You should become familiar with combat mechanics in order to overcome these obstacles and complete your mission. When `creatures` come to blows, the passage of time becomes more strictly represented. All of time is represented in the following way, but it is typically only important to track this during time-sensitive moments like combat.

A time span of 6 seconds is represented by a `round`. During a `round`, each `creature` has a `turn` where they are allowed to use certain resources in order to interact with the world. The order of each `creature's` `turn` is decided at the start of a `round` using the `creature's` `initiative`. For each group of `creatures`, find the one with the highest `initiative`: this is the `initiative` of the group. Each `creature` in that group then takes their `turn` one after the other in whichever order they please. The group with the highest `initiative` acts first, then the next highest and so on. In the event of a tie, roll 1d10 for each tied group. The highest roll wins the tie (repeat this process as many times as necessary).

> Re-rolling `initiative` every `round` can be cumbersome. Feel free to only roll `initiative` once if you have ties and stick to that number until it's no longer necessary to strictly track time in `rounds`.

During a `turn`, the `creature` that owns the `turn` has 3 `action points` that they can use to perform tasks called `actions`, which are the vast majority of all interactions with the world. `Creatures` also have 1 `reaction point` that they can use to perform tasks called `reactions`, which are special, quick motions done in response to some trigger. A `creature` can use `reaction points`, during any `turn` (not just the one the `creature` owns), and regains their `reaction points` at the start of each `round`.

Once a `creature` has completed its `turn`, the next `creature` in the group takes their `turn`. Once all `creatures` in the group have acted, the next group goes in the same manner. Once all `creatures` in each group have acted, the `round` ends and starts again with the group with the highest `initiative`.

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
        -   Melt (M)
        -   Erase (E)

## Actions

There are many things that use up `action points`, and the specific cases are covered by the specific abilities that give the `action`. Some `actions` may take up multiple `action points`, many only use 1. Many `actions` are given to `creatures` through various `abilities`. However, there are some basic `actions` that are able to be taken by any `creature` unless otherwise specified which we will cover here.

Every `action` has one or more `tags` that is used to categorize that `action`. For simplicity, `tags` are used to refer to groups of `actions` instead of having to list off each and every `action` that the rule affects.

### Deep Breath

Tags: Restoration
Cost: 1 action point

---

A `creature` may use the `deep breath` `action` to relieve 2 points of `stress`. This `action` may only be used if the `creature` has _more_ `stress` than their capacity.

> For example, Freya has 4 `endurance`, meaning her `stress` capacity is 4. If she has fewer than 4 `stress` accumulated, she cannot use the `deep breath` `action`. However, if she has 5 or more `stress` accumulated, the `deep breath` `action` relieves 2 points of `stress`. This _does_ mean if she has exactly 5 `stress`, it will reduce her `stress` to 3; below her capacity!

### Focus

Tags: Restoration
Cost: 1 action point

---

A `creature` may use the `focus` `action` to regain 2 points of `magica`.

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

> For example, a `creature` may have 2 `travel` speeds: Ground (3) and Fly (4). That `creature` may take the `move` `action` and choose one of their `travel` speeds, either Ground (3) or Fly (4). If they choose Fly(4), they may fly up to 4 tiles. If they choose Ground (3), they may move along the ground 3 tiles.

### Defend

Tags: Defensive
Cost: 1 action point

---

A `creature` may use 1 `action point` to use the `defend` `action` to give themselves the `defensive` `condition` until the start of their next `turn`.

### Ready

Tags: Untagged
Cost: 1 action point

---

A `creature` may make the `ready` `action` on their turn to delay the start of an `action` they can use. The chosen `action` is called the `readied` `action`. A `creature` must spend an equal amount of `action points` to `ready` an `action` as they would to take that `action` normally, but they must also use a `reaction point` to begin taking that `action`. When the `ready` `action` is taken, the `creature` must specify which `turn` they trigger their `readied` `action` and if it occurs just before that `turn` begins or just after that `turn` ends.

> For example, Suori is next to Ulfarmi and they are in combat with a skeleton. Suori goes first, the skeleton second and Ulfarmi last, and Suori knows that Ulfarmi will want to move outside of the skeleton's `threat range`. However, she cannot prevent the skeleton from closing that distance since her `turn` comes before the skeleton's. Suori takes the `ready` `action` and `readies` the `push` `action`, spending 1 `action point` and specifying that it will take place before the start of Ulfarmi's `turn`. Suori's `turn` ends and the skeleton `moves` towards Ulfarmi and deals a mighty blow! The skeleton's `turn` ends, and before Ulfarmi's `turn` begins, Suori spends a `reaction point` to trigger her `readied` `action` and `pushes` the skelton away. This now gives Ulfarmi the space he needs to run away!

### Grapple

Tags: Attack
Cost: 1 action point

---

A `creature` may use 1 `action point` to use the `grapple` `action`. A `grapple` may only be used on a `creature` they `threaten`, and a `creature` must have a hand free in order to take this `action`. In order to see if a `grapple` succeeds, roll a

`test`: [`grappling`] + `body` vs [`dodging`] + (`finesse`|`body`).

If the `grapple` succeeds, the `attacker` gains the `grappling` `condition` and the `defender` gains the `grappled` `condition`. If the `grappling` `creature` is `forced`, the `grapple` immediately ends and the `grappling` and `grappled` `conditions` are removed from their respective `creatures`.

### Push

Tags: Attack
Cost: 1 action point

---

A `creature` may use 1 `action point` to use the `push` `action`. A `push` may only be used on a `creature` they `threaten`. In order to see if a `push` succeeds, roll a

`test`: [`grappling`] + `body` vs [`dodging`] + (`finesse`|`body`).

If the `push` succeeds, the `defender` is `forced` Ground(1) in a direction of the `attackers` choosing.

### Strike

Tags: Attack
Cost: 2 action points

---

A `strike` is an `action` that constitutes attacking a `creature` with some sort of `weapon`. This `weapon` could be a club, a dagger, a magical staff, or even a bare fist! During a `strike`, the `attacker` is the `creature` making the `strike` and the `defender` is the `creature` subject to the `strike`.

> In other systems, there is often a distinction between attacks with a weapon and attacks without a weapon, or with an object not typically used as a weapon. In Dungeoneers, all strikes with physical objects are `strikes`; there is no difference. Attacks with magic are treated differently, and we'll talk about that when we get to `spellcasts`.

Every `strike` is either melee or ranged. If the distance to the `defender` is greater than the `threat range` of the `attacker`, the `strike` is ranged. Unless a `weapon` has the `range` or `toss` `properties`, you cannot make a `strike` against a `creature` outside your `threat range`.

There are 3 steps to the process of making a `strike`:

-   Determine if the `strike` `hits`
-   Determine the number of `wounds` inflicted

To determine a `hit`, roll a

`test`: [`striking`] + `finesse` vs [`dodging`] + `finesse`.

On a failure, the `strike` `misses`. On a success, the `strike` `hits` and the `defender` then sustains the number of `wounds` marked on the `attackers` `weapon`.

#### A Sample Scenario

> For example, Suori makes a `strike` on a skeleton. The skeleton is `trained` in `dodging`, and has an `finesse` score of 1. Suori is making this attack with a warhammer, which gives her a `pierce die` of a d6. Suori is `trained` in `striking` and has an `finesse` score of 2. This means that Suori rolls 2d6, and the skeleton rolls 1d6. If the `test` succeeds, Suori `hits`!
>
> If Suori `hits`, we then roll the `check` to `pierce`. The skeleton has an `armor value` of 5 and Suori has 2 `body`, so Suori rolls 2d6 and compares her total against 5. If Suori `pierces`, she then causes the skeleton to sustain 1 `bludgeoning wound` as marked on the warhammer. We definitely recommend writing down these numbers for your character so you don't have to look them up in the moment!

### Power Strike

Tags: Attack
Cost: 3 action points

---

A `creature` that takes the `power strike` `action` can make 1 `strike`. This `strike` deals 1 extra `wound` and has 1 point of `boon` on the `striking` roll.

### Spellcast

Tags: Magic
Cost: Varies

---

In the middle of combat, there simply isn't enough time to cast a `spell` in the traditional way. In order to cast a `spell` quickly, a `creature` must either cast out of a tome or use a `cantrip`. Regardless of which they choose, in order to cast the `spell` a `creature` must take the `spellcast` `action`.

> Keep in mind that not all `cantrips` are treated the same! Some `cantrips` are extremely weak, and some are more powerful than many spell tomes. The determining factor of what is and is not a `cantrip` is the location of the spell inscription.

A `spell` consumes `magica` in order to be cast. A `creature` has an amount of `magica` equal to twice their `wisdom` score. Each `spell` has a baseline amount of `magica` that must be spent in order to cast the `spell`, and extra `magica` must be spent to overcome the `defender`. Ambient `magica` is available to spend on the baseline cost of the `spell`.

Every `spell` is either melee or ranged, which is determined by the distance to the `defender`. If the distance to the `defender` is greater than the `threat range` of the `creature`, the `spell` is ranged.

> Note that each `spell` has a range that it can extend. You cannot target a `creature` outside the range of the particular `spell`!

There are 3 steps to the process of making a `spellcast`:

-   Determine if the `spellcast` `hits`
-   Determine the the `spells` effect

The `attacker` must decide how much extra `magica` is used before seeing if the `spell` `hits`, and that `magica` is expended whether the `spell` `hits` or not.

#### Resolving a Spell Attack

If a `spell` calls for a `spell attack`, roll a

`test`: [`spellcraft`] + `mind` vs [`target skill`] + `spirit`.

If the `test` succeeds, the `spellcast` `hits`.

> Note that each `spell` that requires a `spell attack` will target a specific `skill` in its description. This is what `proficiency` is used for the `defender's` roll. Sometimes, a `spell attack` may be requested at a later point than during the `spellcast` `action`, make sure you read the `spell`!

#### On Hit

If the `spell` `hits`, the next step is to apply the `spell` `effect`. Read the `spell` to determine the impact of the extra `magica` spent and what occurs when the `spell` `hits`.

## Reactions

Some tasks happen practically automatically in response to certain stimuli. A `reaction` represents an instantaneous twitch of muscle memory; practically involuntarily. Most `creatures` only have 1 `reaction point` to spend on `reactions`. Like `actions`, not every `reaction` will be listed here as some may be given by other features and `abilities`, but there are some general `reactions` that any `creature` can take.

A `reaction` can be taken at any point during any `turn` as long as a `creature` has a `reaction point` to spend on it.

### Grab a Ledge

A `creature` may instinctively reach out for a ledge if they find themselves being knocked off. If a `creature` is `forced` to a point where they pass over a ledge within their `threat range`, they may use the `grab a ledge` `reaction` to stop themselves at the ledge. In order to do so, roll a

`check`: [1d4] + `dexterity` vs 5 + the number of tiles `forced`.

On a success, the `creature` stops at a point where they are hanging on the ledge.

## Critical Hits

There are two variations for `critical hits`: a general rule and a specific rule. The general rule for `critical hits` is a rule that is _always_ in play, while the specific rule only applies for specific contexts such as using a particular weapon in a certain way. Whenever a `critical hit` is determined to have occurred, the number of `wounds` listed on the `spell` or weapon being used to deliver the `critical hit` is doubled. For `spells` that do not deal `wounds`, there is no benefit.

> Note the specific wording! Only the raw number listed is doubled, so this takes place before any `modifications` to the number of `wounds` sustained.

If a `critical hit` is determined by any of the rules that apply to the circumstance, there is no need to determine if any of the other applicable rules would also give a `critical hit`. In other words, `critical hits` are binary: it either is or is not a `critical hit`. There is no "stacking" of `critical hits`.

If an `attack` or a `spellcast` is a `critical hit`, it automatically `hits` and `pierces` (or if the `spell` requires a `spell save`, the `spell save` is automatically failed).

### General Rule

For `attacks`, if the `pierce dice` total rolled is equal to or greater than _twice_ the `defenders` `armor value`, a `critical hit` occurs. For `spellcasts`, if the `spell pierce dice` total rolled is equal to or greater than _twice_ the `defenders` `spell resistance`, a `critical hit` occurs.

### Specific Rule - Blades & Bows

An `attack` with a blade or bow type weapon becomes a `critical hit` if the `hit dice` total rolled is equal to or greater than the _maximum possible_ `dodge dice` total than can be rolled by the `defender`.

> For example, a `creature` has a `dodge die` of d4 and a `prowess` of 1. Their maximum possible `dodge die` total is 4. If Suori rolls an 4 or above on her `hit dice` total with her shortsword, her `attack` is a `critical hit`.

### Specific Rule - Cudgels & Axes

An `attack` with a cudgel or axe type weapon becomes a `critical hit` if the `attackers` `body` score is greater than or equal to the `dodge die` total rolled by the `defender`.

> For example let's imagine a skeleton is being `attacked` by Suori, who is wielding a warhammer. Suori has a `body` score of 3, and the skeleton's `dodge die` total is a 2. In this instance, Suori's `attack` is a `critical hit`!

### Specific Rule - Lances

An `attack` with a lance type weapon becomes a `critical hit` if at least 2 of the `hit dice` rolled their maximum number.

> For example, if Freya `attacks` with a spear, the spear has a `hit die` of d6. If Freya rolls at least two 6's for her `hit dice` total, her `attack` is a `critical hit`. This means that lances with _lower_ `hit dice` are actually more likely to get a `critical hit`! Which do you go for, better chances to `hit` but you must `pierce` OR try for a `critical hit` and automatically `pierce`?

### Specific Rule - Spells

A `critical hit` with any kind of `spell` can be achieved if the `spell save dice` or `spell attack dice` rolled total of the `attacker` is greater than the maximum possible `spell save dice` or `dodge dice` total of the `defender`.

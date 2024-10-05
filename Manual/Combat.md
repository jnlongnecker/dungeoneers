## Wounds

A `creature` is only able to sustain a certain amount of damage before succumbing to death. This is represented by `wounds`. A `creature` can sustain a number of `wounds` determined by their `size`:

-   `Tiny`: 0
-   `Small`: 1
-   `Medium`: 2
-   `Large`: 3
-   `Huge`: 4
-   `Massive`: 5

If a `creature` takes a `wound` past their maximum number of `wounds` they can sustain, that `creature` is now `dead`.

> For example, Alberich the dwarf is a `medium` `creature`, so he can sustain a maximum of 2 `wounds`. If Alberich is `hit` by an `attack` and is dealt 2 `wounds`, he won't die just yet. If Alberich is `hit` by another `attack` and that deals at least 1 `wound`, Alberich is `dead`.

Taking a `wound` past a `creatures` maximum does not immediately kill that `creature`; a `creature` cannot sustain more `wounds` than their capacity. However, if a `creature` sustains a number of `wounds` above their maximum in a single `attack`, that `creature` is `dead`.

> For example, if Alberich in our above scenario had already sustained 1 `wound`, taking 2 `wounds` would _not_ kill Alberich; he would still have to be `hit` by the second `attack`. However, if Alberich sustains 3 `wounds` at any time in a single `attack`, he will `die` instantly.

Once a `wound` has been sustained, the only way to recover it is through magic or time. Certain `spells`and potions are capable of restoring `wounds`, and you recover all `wounds` at the end of a `full rest`.

## Stress

A `creature` accumulates `stress` over the course of a battle, and this `stress` can make them a better combatant but at a cost. A `creature` can handle an amount of `stress` equal to their `endurance`.

> For example, if Freya has 3 `endurance`, she can handle up to 3 `stress`.

A `creature` can gain `stress` in a number of ways. Firstly, if a `creature` would sustain a `wound` while they can handle more `stress`, instead of sustaining the `wound(s)` they instead accumulate the number of `wounds` as `stress`. If this would exceed the maximum `stress` a `creature` can handle, any excess `wounds` are sustained as normal.

> For example, if Freya can handle 3 `stress` but has already accumulated 2 `stress`, sustaining 2 `wounds` would accumulate 1 `wound` as `stress` and Freya would sustain the remaining 1 `wound` as a `wound`. This would leave Freya at 3 `stress` and 1 `wound`.

While making an `attack`, a `creature` can elect to gain any number of `stress` in order to roll extra dice to `hit`. They must declare that they are doing this before any `hit dice` are rolled for the `attack`.

Gaining `stress` in any way other than sustaining `wounds` will still accumulate that `stress` past the `creatures` capacity. If a `creature` accumulates `stress` past their maximum, there are some consequences for doing so. If you sustain a `wound` while you have more `stress` than you can handle, you take _twice as many `wounds`_. This takes place before any `wound` reduction effects a `creature` may have. Additionally, whenever you accumulate `stress`, you accumulate _twice as much `stress`_. Again, this takes place before any `stress` reduction effects a `creature` may have. If you accumulate `stress` past 3 times your maximum, you sustain 1 `wound` every time you sustain `stress` past this maximum.

> For example, Freya can handle up to 3 `stress`. Let us fast-forward to a point where Freya has accumulated 9 `stress`. Freya elects to gain 2 `stress` to roll and extra `2d4` to `hit`. Because Freya has exceeded her `stress` maximum, she accumulates twice as much `stress`, so she now has accumulated 13 `stress`. Again, because Freya has accumulated `stress` once she has reached 3 times her capacity, she sustains 1 `wound`. Since she is past her `stress` capacity, Freya sustains 2 `wounds`! If Freya doesn't have any `wound` reduction effects, the next `wound` she sustains will kill her!

Going past a `creatures` `stress` capacity isn't purely negative, however. While a `creature` has accumulated `stress` past their capacity, they roll an extra `1d4` to their `pierce` rolls.

Once `stress` has been accumulated, there are a few ways to relieve it. Certain `spells`, `potions` and other `items` are capable of relieving `stress`, as well as certain `creature` `abilities`. A `creature` may relieve a number of `stress` equal to their `endurance` at the end of a `short rest` and they relieve all of their accumulated `stress` at the end of a `long rest` or `full rest`.

# Combat in Dungeoneers

As a Dungeoneer, you will encounter many foes that stand in your way to your inevitable goal. Some may be able to be avoided, but you will ultimately come to blows with many `creatures`. You should become familiar with combat mechanics in order to overcome these obstacles and complete your mission. When `creatures` come to blows, the passage of time becomes more strictly represented. All of time is represented in the following way, but it is typically only important to track this during time-sensitive moments like combat.

A time span of 5 seconds is represented by a `round`. During a `round`, each `creature` has a `turn` where they are allowed to use certain resources in order to interact with the world. The order of each `creature's` `turn` is decided at the start of a `round` using the `creature's` `initiative`. If two or more `creatures` have the same `initiative`, roll a d10 to break the tie, re-rolling if necessary.

> Re-rolling `initiative` every `round` can be cumbersome. Feel free to only roll `initiative` once if you have ties and stick to that number until it's no longer necessary to strictly track time in `rounds`.

During a `turn`, the `creature` that owns the `turn` has 2 resources they are able to use:

-   `Action Points`
-   `Movement Points`

Any `creature` is able to use a third resource, `reaction points`, during any `turn` (not just the one the `creature` owns). `Action points` are used to take `actions`, which are the vast majority of all interactions with the world. A `creature` will use their `action points` to perform the bulk of their impact during their `turn`. A `creature` may also use `movement points` to perform basic position transformations, like standing up or moving in a direction. `Reaction points` are used to take `reactions`, which are special, quick motions done in response to some trigger.

During a `round`, the `creature` with the highest `initiative` takes their `turn` first. Once they are finished with their `turn`, the `creature` with the next-highest `initiative` takes their `turn`, and so on until the `creature` with the lowest `initiative` completes their `turn`. The `round` then completes and the next `round` begins, starting with the `creature` with the highest `initiative` taking their `turn` again.

## Actions

There are many things that use up `action points`, and the specific cases are covered by the specific abilities that give the `action`. Some `actions` may take up multiple `action points`, many only use 1. However, there are some basic `actions` that are able to be taken by any `creature` unless otherwise specified:

-   Disengage
-   Defend
-   Sprint
-   Grapple
-   Push
-   Attack
-   Spellcast

### Disengage

A `creature` that `moves` outside of the `threat range` of another `creature` can be subject to an `opportune strike`. If a `creature` wishes to avoid this, that `creature` must use 1 `action point` to use the `disengage` `action`. The `disengage` `action` removes the `threatened` `condition` from themselves.

> Keep in mind that the `threatened` `condition` is recalculated after every `move`. It's possible to `disengage` then `move` and be `threatened` again! If that `creature` has multiple `movement points` and they use another `movement point` to move outside of the `threat range` of the second `creature`, they can still be subject to an `opportune strike`.

If a `creature` has the `grappled` `condition`, the `disengage` `action` instead attempts to break the `grapple`. The `defender` rolls `dodge dice` equal to their choice of their `power` or `prowess` score and the `attacker` rolls `hit dice` equal to their `power` score. If the `defender's` total is greater than or equal to the `attacker's` total, the `grappled` `condition` is removed from the `defender` and the `grappling` `condition` is removed from the `attacker`.

> Note this is one of the rare instances where the `defender's` total must be equal to or greater than the `attacker's` total; this gives the edge to the `defender` to break the `grapple`!

### Defend

A `creature` may use 1 `action point` to use the `defend` `action` to give themselves the `defensive` `condition` until the start of their next `turn`. A `creature` with the `defending` `condition` can roll 1 extra `dodge die` when `defending`.

### Sprint

A `creature` may use 1 `action point` to use the `sprint` `action` to give themselves the `sprinting` `condition` until the start of their next `turn`. A `creature` with the `sprinting` `condition` has 2 extra `movement points`.

### Grapple

A `creature` may use 1 `action point` to use the `grapple` `action`. A `grapple` may only be used on a `creature` they `threaten`. In order to see if a `grapple` succeeds, the `attacker` must roll `hit dice` and the `defender` must roll `dodge dice`. The `defender` may use either their `prowess` score or their `power` score to determine the number of `dodge dice` they roll while the `attacker` must use their `power` score. The total of the `attacker` must be greater than or equal to the total of the `defender` in order for the `grapple` to succeed. If the `grapple` succeeds, the `attacker` gains the `grappling` `condition` and the `defender` gains the `grappled` `condition`.

The `grappled` `condition` sets a `creature's` `movement points` to 0, and they can no longer gain any `movement points`. The `grappling` condition halves the amount of `movement points` the `creature` has and halves the amount of `movement points` that `creature` gains. When a `grappling` `creature` uses a `movement action`, the `creature` they are `grappling` immediately performs the same `movement action`.

### Push

A `creature` may use 1 `action point` to use the `push` `action`. A `push` may only be used on a `creature` they `threaten`. In order to see if a `push` succeeds, the `attacker` must roll `hit dice` and the `defender` must roll `dodge dice`. The `defender` may use either their `prowess` score or their `power` score to determine the number of `dodge dice` they roll while the `attacker` must use their `power` score. The total of the `attacker` must be greater than or equal to the total of the `defender` in order for the `push` to succeed.

If the `push` succeeds, the `defender` is moved 1 tile in the direction of the `facing` direction of the `attacker`.

### Attack

An `attack` is an `action` that constitutes striking at a `creature` with some sort of traditional `weapon`. This `weapon` could be a club, a dagger, a magical staff, or even a bare fist! During an `attack`, the `attacker` is the `creature` making the `attack` and the `defender` is the `creature` subject to the `attack`. An `attack` `action` costs 1 `action point`. A `creature` may only use the `attack` `action` on a `creature` they `threaten`.

> In other systems, there is often a distinction between attacks with a weapon and attacks without a weapon, or with an object not typically used as a weapon. In Dungeoneers, all strikes with conventional objects are `attacks`; there is no difference. Strikes with magic are treated differently, and we'll talk about that when we get to `spellcasting`.

#### Making an Attack

When a `creature` decides to use an `action point` to make an `attack`, there are 3 steps to the process:

-   Determine if the `attack` `hits`
-   Determine if the `attack` `pierces`
-   Determine the number of `wounds` inflicted

#### Determining if an Attack Hits

To determine a `hit`, the `attacker` and `defender` make competing dice rolls. The `attacker` rolls a number of `hit dice` equal to their `prowess` score (plus any modifiers they may have) and the `defender` rolls a number of `dodge dice` equal to their `prowess` score (plus any modifiers they may have). The two rolls are compared: if the `attacker's` total is equal to or greater than the `defender's` total, the `attack` `hits` and any `effects` that take place on `hit` are immediately applied. If the `defender's` total exceeds the `attacker's`, the attack `misses` and any `effects` that take place on a `miss` are immediately applied. Finally, if the `attack` `hits`, the `attack` moves on to the next step to determine if the `attack` `pierces`.

> For example, Suori makes an `attack` on a skeleton. The skeleton has no `abilities` improving its `dodge dice`, and has a `prowess` score of 1. Suori is making this attack with a warhammer, which gives her a `hit dice` of a d4. Suori has a `prowess` score of 2. This means that Suori rolls 2d4, and the skeleton rolls 1d4. Imagine that Suori rolls a 1 and a 3 and the skeleton rolls a 4; this would mean that Suori's total is 4 and the skeleton's total is also 4. Since Suori's total is not exceeded by the skeleton's, this means her `attack` `hits`!
>
> Now imagine that Suori rolls a 1 and a 2, and the skeleton rolls a 4. Since the skeleton's roll exceeds Suori's roll, her `attack` `misses`.

#### Determining if an Attack Pierces

Remember, you only check if an `attack` `pierces` if the `attack` has already `hit`!

To determine a `pierce`, the `attacker` makes a dice roll and compares their total against the `armor value` of the `defender`. The `attacker` rolls a number of `pierce dice` equal to their `power` score. If this total is equal to or greater than the `defender's` `armor value`, the `attack` `pierces` and any `effects` that take place on a `pierce` are immediately applied. If the `defender's` `armor value` exceeds the `attacker's` total, the `attack` `deflects` and any `effects` that take place on a `deflection` are immediately applied. Finally, if the `attack` `pierces`, the `attack` moves on to the next step to determine the number of `wounds` the `defender` will sustain.

#### Determining the Number of Wounds Inflicted

When an `attack` `pierces`, the last step in the `attack` is to determine the number of `wounds` the `defender` will sustain. The `attacker` can inflict a number of `wounds` as marked with their `weapon`, plus any modifiers they might have. The `defender` then sustains that number of `wounds`, and all calculations for determining `wounds` sustained then apply.

Once this step has been completed, the `attack` `action` concludes.

#### Hit Dice

`Hit dice` are used to determine if an `attack` `hits` or not. An `attacker's` `hit dice` are determined by their `weapon`.

#### Dodge Dice

`Dodge dice` are used to determine if an `attack` `hits` or not; but on the `defender's` side. A `defender's` `dodge dice` is a d4, unless that `creature` has an `ability`/`effect` to change this.

#### Pierce Dice

When an `attacker` `hits` with an `attack`, in order to see if that `attack` `pierces` the `defenders` `armor`, `pierce dice` are used. When rolling for a `pierce`, an `attacker` rolls a number of `pierce dice` equal to their `power` score. The total rolled is then compared to the `defenders` `armor value`; if this is at or above the `defenders` `armor value`, then the `attack` `pierces` and the `defender` sustains a number of `wounds` as marked on the `attackers` `weapon`. If there are any `wound` bonuses or penalties, the `attackers` modifiers are applied first, then the `defenders`.

> For example, lets say Freya is `attacking` a skeleton with a mace. Freya has 2 `power`, the mace has a `pierce die` of `1d6`, and the skeleton has an `armor value` of 4. Freya rolls `2d6`, and her total is a 4. Since this meets or exceeds the skeletons 4 `armor value`, Freya's `attack` `pierces`. The mace deals 1 `wound` on a `pierce`, so the skeleton sustains 1 `bludgeoning` `wound`. However, since the skeleton is `weak` to `bludgeoning`, the skeleton instead sustains 2 `wounds`!
>
> Now imagine that same `skeleton` had exceeded its `stress` capacity. This causes the `skeleton` to sustain twice the number of `wounds`, but this effect occurs before any modifiers. The 1 `bludgeoning` `wound` becomes 2 `bludgeoning` `wounds` due to `stress`, and then the skeletons `weak` modifier increases that to 3 `bludgeoning` `wounds`!

#### Armor Value

When a `creature` is `hit` by an `attack`, they do not immediately sustain any `wounds`. Instead, a roll must be made to determine if the `attack` `pierces`. Based on various natural resistances, `abilities`, `spells`, items and `armor`, a `creature` will have an `armor value` equal to the sum of all of these factors. The `attacker` must roll a `pierce dice` total that meets or exceeds the `defenders` `armor value`.

> For example, Ulfarmi has 0 `armor value` naturally. He has the `spell` mage armor cast on him, which gives him 3 `armor value`. If Ulfarmi equips leather armor, this gives him 1 `armor value`. In total, he would then have 4 `armor value`.

### Spellcast

In the middle of combat, there simply isn't enough time to cast a `spell` in the traditional way. In order to cast a `spell` quickly, a `creature` must either cast out of a tome or use a `cantrip`. Regardless of which they choose, in order to cast the `spell` a `creature` must take the `spellcast` `action`.

> Keep in mind that not all `cantrips` are treated the same! Some `cantrips` are extremely weak, and some are more powerful than many spell tomes. The determining factor of what is and is not a `cantrip` is the location of the spell inscription.

A `spell` consumes `magica` in order to be cast. A `creature` has an amount of `magica` equal to their `mind` score and regains 1 `magica` at the start of their `turn`. Each `spell` has a baseline amount of `magica` that must be spent in order to cast the `spell`, and extra `magica` must be spent to overcome the `resistance` of the `defender`. Ambient `magica` is available to spend on the baseline cost of the `spell` and any leftover can be used to roll more `spell pierce` dice before tapping into the `creatures` `magica` reserves.

The general process for resolving a `spellcast` `action` differs only in the first step amongst `spells`. A `spell` can either require a `spell attack` or a `spell save`.

#### Resolving a Spell Attack

In order to see if a `spell attack` hits, the `attacker` must roll `spell attack dice` equal to their `spell` score and the `defender` must roll `dodge dice` equal to their `prowess` score. If the `attacker's` total is equal to or greater than the `defender's` total, the `spell attack` `hits` and the process moves to the next step.

#### Resolving a Spell Save

In order to see if a `spell save` is failed, the `attacker` must roll `spell save dice` equal to their `mind` score and the `defender` must roll `spell save dice` equal to the score specified by the `spell`. Unless otherwise specified by the `spell`, this score is `resistance`. If the `attacker's` total is equal to or greater than the `defender's` total, the `spell save` is failed and the process moves to the next step.

A `defender` may elect to intentionally fail their `spell save` if they so choose.

#### Overcoming Spell Resistance

Each `creature` has a `spell resistance` score that the `attacker` must overcome for the `spell` to take `effect`. The `attacker` rolls `spell pierce` dice equal to the _extra_ `magica` they choose to spend on the `spell` + 1. The size of the `spell pierce` dice begins at a d4, but can change based on the `spell` and other `abilities`. If the total rolled by the `attacker` is greater than or equal to the `defender's` `spell resistance`, the `spell` takes `effect`.

If the `spell` inflicts an `effect`, that `effect` takes place. If the `spell` inflicts `wounds`, that number of `wounds` are inflicted. A `creature` may elect to allow the `spell` through their `spell resistance` if they choose.

## Movement

Unless otherwise specified, all `creatures` have 1 `movement point`. There are a number of modifiers that can be attained to increase or reduce this number, but a `creature` having less than 0 `movement points` does not functionally do anything except make it more difficult for that `creature` to gain positive amounts of `movement points` to do anything with.

A `creatures` `movement points` are able to spent on `movement actions`. The primary `movement action` is simply `movement`. A `creature` can spend 1 `movement point` to `move` 1 tile in any cardinal or orthogonal direction. While this is the most _common_ way a `creature` spends their `movement points`, it's not the _only_ way. While the following is not a comprehensive list, the following are ways for every `creature` to use their `movement points`. Just keep in mind that there are `abilities` and `effects` that allows a `creature` to use their `movement points` in other ways.

-   Stand up from `prone`
-   Change `facing` direction

### Prone

A `creature` can drop `prone` at any moment on their `turn`, no resources needed. There are advantages and disadvantages to being `prone` that will be covered in the `conditions` section, but if a `creature` does not want to be `prone` anymore, they must spend 1 `movement point` to stand up and remove the `prone` condition.

### Facing Direction

A `creature` is always `facing` a particular direction. Whenever `moving`, `attacking`, `grappling`, `pushing` or `spellcasting`, a `creature` may automatically changes their `facing` direction towards their target before the `action` begins. If a `creature` wants to change their `facing` direction in isolation of these other options, they must spend 1 `movement point`.

While a `creature` is a `defender` and their `attacker` is positioned opposite of their `facing` direction, they have a penalty to their `dodge dice` equal to 1d8.

> Note the wording here! A `creature` can be a `defender` in multiple scenarios, like `attacks` and `spellcasts`!

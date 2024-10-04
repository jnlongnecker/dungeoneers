# Combat in Dungeoneers

As a Dungeoneer, you will encounter many foes that stand in your way to your inevitable goal. Some may be able to be avoided, but you will ultimately come to blows with many creatures. You should become familiar with combat mechanics in order to overcome these obstacles and complete your mission.

In order to understand how combat works in Dungeoneers, we first need to understand the values that are used in combat. There are 6 important combat values:

-   Wounds
-   Stress
-   Hit Dice
-   Dodge Dice
-   Pierce Dice
-   Armor Value (AV)

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

## Hit Dice

`Hit dice` are used to determine if an `attack` `hits` or not. An `attacker's` `hit dice` are determined by their `weapon`.

## Dodge Dice

`Dodge dice` are used to determine if an `attack` `hits` or not; but on the `defender's` side. A `defender's` `dodge dice` is a d4, unless that `creature` has an `ability`/`effect` to change this.

## Pierce Dice

When an `attacker` `hits` with an `attack`, in order to see if that `attack` `pierces` the `defenders` `armor`, `pierce dice` are used. When rolling for a `pierce`, an `attacker` rolls a number of `pierce dice` equal to their `power` score. The total rolled is then compared to the `defenders` `armor value`; if this is at or above the `defenders` `armor value`, then the `attack` `pierces` and the `defender` sustains a number of `wounds` as marked on the `attackers` `weapon`. If there are any `wound` bonuses or penalties, the `attackers` modifiers are applied first, then the `defenders`.

> For example, lets say Freya is `attacking` a skeleton with a mace. Freya has 2 `power`, the mace has a `pierce die` of `1d6`, and the skeleton has an `armor value` of 4. Freya rolls `2d6`, and her total is a 4. Since this meets or exceeds the skeletons 4 `armor value`, Freya's `attack` `pierces`. The mace deals 1 `wound` on a `pierce`, so the skeleton sustains 1 `bludgeoning` `wound`. However, since the skeleton is `weak` to `bludgeoning`, the skeleton instead sustains 2 `wounds`!
>
> Now imagine that same `skeleton` had exceeded its `stress` capacity. This causes the `skeleton` to sustain twice the number of `wounds`, but this effect occurs before any modifiers. The 1 `bludgeoning` `wound` becomes 2 `bludgeoning` `wounds` due to `stress`, and then the skeletons `weak` modifier increases that to 3 `bludgeoning` `wounds`!

## Armor Value

When a `creature` is `hit` by an `attack`, they do not immediately sustain any `wounds`. Instead, a roll must be made to determine if the `attack` `pierces`. Based on various natural resistances, `abilities`, `spells`, items and `armor`, a `creature` will have an `armor value` equal to the sum of all of these factors. The `attacker` must roll a `pierce dice` total that meets or exceeds the `defenders` `armor value`.

> For example, Ulfarmi has 0 `armor value` naturally. He has the `spell` mage armor cast on him, which gives him 3 `armor value`. If Ulfarmi equips leather armor, this gives him 1 `armor value`. In total, he would then have 4 `armor value`.

---

Now that we are familiar with the basic numbers involved in basic `attacks`, let's look at the rules for making an `attack` and even what constitutes an `attack` in the first place.

## What is an Attack?

An `attack` is an `action` that constitutes striking at a `creature` with some sort of traditional `weapon`. This `weapon` could be a club, a dagger, a magical staff, or even a bare fist! During an `attack`, the `attacker` is the `creature` making the `attack` and the `defender` is the `creature` subject to the `attack`.

> In other systems, there is often a distinction between attacks with a weapon and attacks without a weapon, or with an object not typically used as a weapon. In Dungeoneers, all strikes with conventional objects are `attacks`; there is no difference. Strikes with magic are treated differently, and we'll talk about that when we get to `spellcasting`.

## Making an Attack

When a `creature` decides to use an `action point` to make an `attack`, there are 3 steps to the process:

-   Determine if the `attack` `hits`
-   Determine if the `attack` `pierces`
-   Determine the number of `wounds` inflicted

Lets look at each part individually.

### Determining if an Attack Hits

To determine a `hit`, the `attacker` and `defender` make competing dice rolls. The `attacker` rolls a number of `hit dice` equal to their `prowess` score (plus any modifiers they may have) and the `defender` rolls a number of `dodge dice` equal to their `prowess` score (plus any modifiers they may have). The two rolls are compared: if the `attacker's` total is equal to or greater than the `defender's` total, the `attack` `hits` and any `effects` that take place on `hit` are immediately applied. If the `defender's` total exceeds the `attacker's`, the attack `misses` and any `effects` that take place on a `miss` are immediately applied. Finally, if the `attack` `hits`, the `attack` moves on to the next step to determine if the `attack` `pierces`.

> For example, Suori makes an `attack` on a skeleton. The skeleton has no `abilities` improving its `dodge dice`, and has a `prowess` score of 1. Suori is making this attack with a warhammer, which gives her a `hit dice` of a d4. Suori has a `prowess` score of 2. This means that Suori rolls 2d4, and the skeleton rolls 1d4. Imagine that Suori rolls a 1 and a 3 and the skeleton rolls a 4; this would mean that Suori's total is 4 and the skeleton's total is also 4. Since Suori's total is not exceeded by the skeleton's, this means her `attack` `hits`!
>
> Now imagine that Suori rolls a 1 and a 2, and the skeleton rolls a 4. Since the skeleton's roll exceeds Suori's roll, her `attack` `misses`.

### Determining if an Attack Pierces

Remember, you only check if an `attack` `pierces` if the `attack` has already `hit`!

To determine a `pierce`, the `attacker` makes a dice roll and compares their total against the `armor value` of the `defender`. The `attacker` rolls a number of `pierce dice` equal to their `power` score. If this total is equal to or greater than the `defender's` `armor value`, the `attack` `pierces` and any `effects` that take place on a `pierce` are immediately applied. If the `defender's` `armor value` exceeds the `attacker's` total, the `attack` `deflects` and any `effects` that take place on a `deflection` are immediately applied. Finally, if the `attack` `pierces`, the `attack` moves on to the next step to determine the number of `wounds` the `defender` will sustain.

### Determining the Number of Wounds Inflicted

When an `attack` `pierces`, the last step in the `attack` is to determine the number of `wounds` the `defender` will sustain. The `attacker` can inflict a number of `wounds` as marked with their `weapon`, plus any modifiers they might have. The `defender` then sustains that number of `wounds`, and all calculations for determining `wounds` sustained then apply.

Once this step has been completed, the `attack` `action` concludes.

## Casting a Spell

In the middle of combat, there simply isn't enough time to cast a `spell` in the traditional way. In order to cast a `spell` quickly, a `creature` must either cast out of a tome or use a `cantrip`. Regardless of which they choose, in order to cast the `spell` a `creature` must take the `spellcasting` `action`.

> Keep in mind that not all `cantrips` are treated the same! Some `cantrips` are extremely weak, and some are more powerful than many spell tomes. The determining factor of what is and is not a `cantrip` is the location of the spell inscription.

A `spell` consumes `magica` in order to be cast. A `creature` has an amount of `magica` equal to their `mind` score and regains 1 `magica` at the start of their `turn`. Each `spell` has a baseline amount of `magica` that must be spent in order to cast the `spell`, and extra `magica` must be spent to overcome the `resistance` of the `defender`. Ambient `magica` is available to spend on the baseline cost of the `spell` and any leftover can be used to roll more `spell pierce` dice before tapping into the `creatures` `magica` reserves.

The general process for resolving a `spellcasting` `action` differs only in the first step amongst `spells`. A `spell` can either require a `spell attack` or a `spell save`.

### Resolving a Spell Attack

In order to see if a `spell attack` hits, the `attacker` must roll `spell attack dice` equal to their `spell` score and the `defender` must roll `dodge dice` equal to their `prowess` score. If the `attacker's` total is equal to or greater than the `defender's` total, the `spell attack` `hits` and the process moves to the next step.

### Resolving a Spell Save

In order to see if a `spell save` is failed, the `attacker` must roll `spell save dice` equal to their `mind` score and the `defender` must roll `spell save dice` equal to the score specified by the `spell`. Unless otherwise specified by the `spell`, this score is `resistance`. If the `attacker's` total is equal to or greater than the `defender's` total, the `spell save` is failed and the process moves to the next step.

A `defender` may elect to intentionally fail their `spell save` if they so choose.

### Overcoming Spell Resistance

Each `creature` has a `spell resistance` score that the `attacker` must overcome for the `spell` to take `effect`. The `attacker` rolls `spell pierce` dice equal to the _extra_ `magica` they choose to spend on the `spell` + 1. The size of the `spell pierce` dice begins at a d4, but can change based on the `spell` and other `abilities`. If the total rolled by the `attacker` is greater than or equal to the `defender's` `spell resistance`, the `spell` takes `effect`.

If the `spell` inflicts an `effect`, that `effect` takes place. If the `spell` inflicts `wounds`, that number of `wounds` are inflicted. A `creature` may elect to allow the `spell` through their `spell resistance` if they choose.

# Creatures

In Dungeoneers, a `creature` is any living entity in the world. Often times, systems might refer to all hostile entities as "monsters". This feels like a less-inclusive phrase and morally loaded; after all, not all "enemies" are "monstrous", and some truly "monstrous" entities may not be "enemies". A `creature` has a few properties universal to all `creatures` that will be covered in this section.

## Attribute Scores

Every `creature` has 6 `attribute scores` that are used in a variety of scenarios. The specific scenarios are covered in their respective sections, but we'll talk a bit about each here. Every `creature` is also made up of a body, mind and spirit (represented by their respective scores). The body of a `creature` is their physical body, their mind is the processing and mental facilities, and their spirit the `arca` that makes up their otherwordly presence.

A typical human will have at least 2 in each `attribute score`. A general feel of the power tied to an `attribute score` can be determined by the following table:

| Score Value | Name         | Description                                                                                                       |
| ----------- | ------------ | ----------------------------------------------------------------------------------------------------------------- |
| 0           | Crippled     | This attribute has been significantly crippled compared to an average person                                      |
| 1           | Weak         | This attribute is deficient compared to even an average person                                                    |
| 2           | Average      | This attribute is typical of the average person                                                                   |
| 3           | Trained      | This attribute score is found only amongst people that actively train it                                          |
| 4           | Experienced  | This attribute score is found only amongst genetic anomalies dedicated to training it                             |
| 5           | Master       | This attribute score is found only amongst genetic anomalies with arcane enhancement                              |
| 6           | Legendary    | This attribute score is found only amongst genetic anomalies with supreme arcane enhancement                      |
| 7           | Mythical     | This attribute score is found only amongst genetic anomalies with arcane enhancement from other genetic anomalies |
| 8           | Unbelievable | This attribute score is found only amongst supreme arcane beings gifted in the attribute                          |
| 9           | Demigodly    | This attribute score can only be found amongst demigods gifted in the attribute                                   |
| 10          | Godly        | This attribute score can only be found amongst gods                                                               |

### Body

The `body` score represents the physicality of the `creature`. It is used to determine things like `wounds` inflicted and `stress` capacity.

### Spirit

The `spirit` score represents the force of personality and otherworldly presence of the `creature`. It is used to determine things like `arca` capacity and arcane resistance.

### Mind

The `mind` score represents the mental practice and recall of a `creature`. It is used to determine things like `spell` control and skill.

### Finesse

The `finesse` score represents the precision and flexibility of a `creature`. It is used to determine things like `strike` accuracy and `dodging` efficacy.

## Threat Range & Reach

Every `creature` has a baseline `threat range` called their `reach`. This is a distance in tiles that denotes how far the `creature` can interact with using a prehensile limb. The `threat range` of a `creature` may be expanded by various `effects`, but their `reach` is determined by the `creatures` `size`. A `creature` that is within the `threat range` of a `hostile` `creature` gains the `threatened` `condition`. This is checked after every `move`.

> For example, Suori the dwarf has a `reach` of 1 since she is a `medium` `creature`. Let's say Suori is 2 tiles away from a skeleton, another `medium` `creature`. Neither Suori nor the skeleton are `threatened`, because both are outside of each other's `threat range`. Now let's say Suori `moves` 1 tile towards the skeleton. The skeleton is now within Suori's `threat range`, so it is `threatened` by Suori. However, we re-calculate _all_ `threat ranges` after a `move`, so Suori is _also_ `threatened` by the skeleton since she is within _its_ `threat range`!

## Size

A `creature` has a `size` that represents the amount of physical space that they occupy. Something to note is that not all `creatures` in the same `size` category are the exact same physical size, only that they are able to control the specified number of tiles with the physical space they take up.

The `size` categories, tiles that `creatures` of that `size` occupy and `threat range` can be identified in the following table:

|                    | Tiny | Small | Medium | Large | Huge | Massive | Gargantuan |
| ------------------ | ---- | ----- | ------ | ----- | ---- | ------- | ---------- |
| **Tiles Occupied** | 1/4  | 1/2   | 1      | 2     | 3    | 4       | 5+         |
| **Threat Range**   | 1    | 1     | 1      | 1     | 2    | 2       | 3          |
| **Size Value**     | 0    | 1     | 2      | 3     | 4    | 5       | 6          |

Unless a `creature` occupies less than 1 tile, 2 `creatures` are not allowed to occupy the same tile. A tile that is fully occupied cannot be moved into or past, unless the occupying `creatures` allow it.

## Wounds

A `creature` is only able to sustain a certain amount of damage before succumbing to death. This is represented by `wounds`. A `creature` can sustain a number of `wounds` determined by their `size`:

-   `Tiny`: 0
-   `Small`: 1
-   `Medium`: 2
-   `Large`: 3
-   `Huge`: 4
-   `Massive`: 5
-   `Gargantuan`: 6+

If a `creature` takes a `wound` while they are at their maximum number of `wounds` they can sustain, that `creature` is now `dead`.

> For example, Alberich the dwarf is a `medium` `creature`, so he can sustain a maximum of 2 `wounds`. If Alberich is `hit` by a `strike` and is dealt 2 `wounds`, he won't die just yet. If Alberich is `hit` by another `strike` and that deals at least 1 `wound`, Alberich is `dead`.

Taking a `wound` past a `creatures` maximum does not immediately kill that `creature`; a `creature` cannot sustain more `wounds` than their capacity. However, if a `creature` sustains a number of `wounds` above their maximum in at once, that `creature` is `dead`.

> For example, if Alberich in our above scenario had already sustained 1 `wound`, taking 2 `wounds` would _not_ kill Alberich; he would still have to be `hit` by the second `strike`. However, if Alberich sustains 3 `wounds` at any time in a single `strike`, he will `die` instantly. Note that this only applies if the `creature` sustains that many actual `wounds`; if some are absorbed by `stress` they may not be outright killed. If Alberich can accumulate 1 `stress` when he sustains those 3 `wounds`, he only functionally sustains 2 `wounds` and wouldn't `die` instantly.

Once a `wound` has been sustained, the only way to recover it is through arcana or time. Certain `spells`and potions are capable of restoring `wounds`, and you recover all `wounds` at the end of a `full rest`.

When a `wound` is sustained, it often has a `damage type` associated with it. This becomes relevant `wound` `modifications` as most only apply to certain `damage types`. You cannot sustain a negative amount of `wounds`, the minimum is 0. If a `wound` is sustained without a `damage type`, this means it is unaffected by any `wound` `modifications` that apply to certain `damage types`.

> For example, a mace is a weapon that inflicts 1 `bludgeoning wound`, so `creatures` with the `vulnerability(B)` `trait` sustain more `wounds` from this weapon.

## Stress

A `creature` accumulates `stress` over the course of a battle, and this `stress` can make them a better combatant but at a cost. A `creature` can handle an amount of `stress` equal to their `body` score.

> For example, if Freya has 3 `body`, she can handle up to 3 `stress`.

A `creature` can gain `stress` in a number of ways. Firstly, if a `creature` would sustain a `wound` while they can handle more `stress`, instead of sustaining the `wound(s)` they instead accumulate the number of `wounds` as `stress`. If this would exceed the maximum `stress` a `creature` can handle, any excess `wounds` are sustained as normal.

> For example, if Freya can handle 3 `stress` but has already accumulated 2 `stress`, sustaining 2 `wounds` would accumulate 1 `wound` as `stress` and Freya would sustain the remaining 1 `wound` as a `wound`. This would leave Freya at 3 `stress` and 1 `wound`.

While making a `strike`, a `creature` can elect to gain any number of `stress` in order to gain a point of `boon` for each `stress` gained in this way. The `creature` must make this choice _before_ any roll is made.

Gaining `stress` in any way other than sustaining `wounds` will still accumulate that `stress` past the `creatures` capacity. If a `creature` accumulates `stress` past their maximum, there are some consequences for doing so. If you sustain a `wound` while you have more `stress` than you can handle, you take _twice as many `wounds`_. This takes place before any `wound` reduction `effects` a `creature` may have. Additionally, whenever you accumulate `stress`, you accumulate _twice as much `stress`_. Again, this takes place before any `stress` reduction `effects` a `creature` may have. If you accumulate `stress` past 3 times your maximum, you sustain 1 `wound` every time you sustain `stress` past this maximum.

> For example, Freya can handle up to 3 `stress`. Let us fast-forward to a point where Freya has accumulated 9 `stress`. Freya elects to gain 2 `stress` to gain an extra 2 points of `boon` to `hit`. Because Freya has exceeded her `stress` maximum, she accumulates twice as much `stress`, so she now has accumulated 13 `stress`. Again, because Freya has accumulated `stress` once she has reached 3 times her capacity, she sustains 1 `wound`. Since she is past her `stress` capacity, Freya sustains 2 `wounds`!

Going past a `creatures` `stress` capacity isn't purely negative, however. While a `creature` has accumulated `stress` past their capacity, they gain a point of `boon` all `striking` and `dodging` rolls.

Once `stress` has been accumulated, there are a few ways to relieve it. Certain `spells` and `items` are capable of relieving `stress`, as well as certain `creature` `abilities`. A `creature` may relieve a number of `stress` equal to their `endurance` at the end of a `short rest` and they relieve all of their accumulated `stress` at the end of a `long rest` or `full rest`.

## Equipment Slots

Each `creature` has a number of `equipment slots` based off of their anatomy. These are places on their body that they are able to `equip` `equipment`. The following are possible `equipment slots`:

-   Head
-   Body
-   Feet
-   Hands
-   Back
-   Wield
-   Ring
-   Hang
-   Belt

Every piece of `equipment` has an `equipment slot` that it occupies when it is `equipped`. While the anatomy of every `creature` will not be listed here, the most common player `creature` anatomy Humanoid will be listed:

-   1 head
-   1 body
-   1 feet
-   1 hands
-   1 back
-   2 wield
-   1 hang
-   2 ring
-   1 belt

As a rule of thumb, you can use the below guidelines to determine the `equipment slots` any `creature` may have, but note that `creatures` will either have their anatomy listed and use the `equipment slots` tied to that anatomy or will explicitly list their `equipment slots`.

-   A `creature` only ever has 1 `body` slot
-   A `creature` only ever has 1 `back` slot
-   A `creature` has 1 `belt` slot per waist they have
-   A `creature` has 1 `head` slot per head they have
-   A `creature` has 1 `hang` slot per neck they have
-   A `creature` has 1 `ring` slot per hand with fingers they have
-   A `creature` has 1 `wield` slot per prehensile limb they have
-   A `creature` has 1 `feet` slot every 2 feet they have
-   A `creature` has 1 `hands` slot every 2 hands they have

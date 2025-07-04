# Creatures

In Dungeoneers, a `creature` is any living entity in the world. Often times, systems might refer to all hostile entities as "monsters". This feels like a less-inclusive phrase and morally loaded; after all, not all "enemies" are "monstrous", and some truly "monstrous" entities may not be "enemies". A `creature` has a few properties universal to all `creatures` that will be covered in this section.

## Attribute Scores

Every `creature` has 4 `attribute scores` that are used in a variety of scenarios. The specific scenarios are covered in their respective sections, but we'll talk a bit about each here. Every `creature` is also made up of a body, mind and spirit (represented by their respective scores). The body of a `creature` is their physical body, their mind is the processing and mental facilities, and their spirit the `arca` that makes up their otherwordly presence. `Creatures` additionally wield themselves with a certain level of finesse; representative of their general precision of action.

A typical human will have at least 4 in each `attribute score`. A general feel of the power tied to an `attribute score` can be determined by the following table:

| Score Value | Name         | Description                                                                                            |
| ----------- | ------------ | ------------------------------------------------------------------------------------------------------ |
| 0           | Incapable    | This attribute is found on creatures virtually or completely incapable of exhibiting the attribute     |
| 1           | Crippled     | This attribute is found on creatures far more deficient in the attribute than the most deficient human |
| 2           | Deficient    | This attribute score is found on humans extremely deficient in the attribute                           |
| 3           | Weak         | This attribute is below the average for a human                                                        |
| 4           | Average      | This attribute is at the level of an average human                                                     |
| 5           | High         | This attribute score is found on highly trained humans                                                 |
| 6           | Legendary    | This attribute score is found on highly trained humans with arcane enhancement                         |
| 7           | Mythical     | This attribute score is found on highly trained humans with powerful arcane enhancement                |
| 8           | Unbelievable | This attribute score is found only amongst supreme arcane beings gifted in the attribute               |
| 9           | Demigodly    | This attribute score can only be found amongst demigods gifted in the attribute                        |
| 10          | Godly        | This attribute score can only be found amongst gods                                                    |

### Body

The `body` score represents the physicality of the `creature`. It is used to determine things like additional `wounds` they can take and physical power.

### Spirit

The `spirit` score represents the force of personality and otherworldly presence of the `creature`. It is used to determine things like `stress` capacity.

### Mind

The `mind` score represents the mental practice and recall of a `creature`. It is used to determine things like `spell` control and skill.

### Finesse

The `finesse` score represents the precision and flexibility of a `creature`. It is used to determine things like `strike` accuracy and `dodging` efficacy.

## Reach

Every `creature` has a baseline range of interaction called their `reach`. This is a distance in tiles that denotes how far the `creature` can interact with using a prehensile limb. A `creature's` `reach` is determined by its `size`, but may be increased for certain kinds of long limbs.

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

A `creature` is only able to take a certain amount of damage before succumbing to death. This is represented by `wounds`. A `creature` can take a number of `wounds` determined by their `size`, plus their `body` score:

-   `Tiny`: 2
-   `Small`: 3
-   `Medium`: 4
-   `Large`: 5
-   `Huge`: 6
-   `Massive`: 7
-   `Gargantuan`: 8+

If a `creature` takes a `wound` while they are at their maximum number of `wounds`, that `creature` is now `dead`.

> Example: Alberich the dwarf is a `medium` `creature` with 4 `body`, so he can take a maximum of 8 `wounds`. If Alberich takes 8 `wounds`, he won't die just yet. If Alberich takes at least 1 `wound` before clearing any `wounds`, Alberich is `dead`.

Taking a `wound` past a `creatures` maximum does not immediately kill that `creature`; a `creature` cannot take more `wounds` than their capacity. However, if a `creature` takes a number of `wounds` above their maximum in at once, that `creature` is `dead`.

> Example: if Alberich in our above scenario had already taken 1 `wound`, taking 8 `wounds` would _not_ kill Alberich. However, if Alberich takes 9 `wounds` at any time at once, he will `die` instantly. Note that this only applies if the `creature` takes that many actual `wounds`; if some are absorbed by `armor points` they may not be outright killed.

Once a `wound` has been taken, the only way to clear it is through arcana or time. Certain `spells` and potions are capable of clearing `wounds`, and you clear all `wounds` as a `downtime move` during a `vacation`.

When a `wound` is taken, it has a `damage type` associated with it. This becomes relevant for `wound` `modifications` as most only apply to certain `damage types`. You cannot take a negative amount of `wounds`, the minimum is 0.

## Stress

A `creature` gains `stress` over the course of a battle, and this `stress` can make them a better combatant but at a cost. A `creature` can handle an amount of `stress` equal to 2 + their `spirit` score.

> Example: if Freya has 5 `spirit`, she can handle up to 7 `stress`.

A `creature` can gain `stress` in a number of ways. Firstly, if a `creature` rolls a lesser success on their `striking` roll, the `wounds` of the `attacker's` weapon are instead gained as `stress`.

> Example: if Freya rolls a lesser success to `strike` a skeleton, instead of her weapon dealing 1 `wound` it will instead deal 1 `stress` to the skeleton.

If a `creature` gains `stress` past their maximum, there are some consequences for doing so. While a `creature` has `stress` past their capacity, they are `broken` meaning they take _twice_ the normal number of `wounds`. If a `creature` gains `stress` past 2 times their maximum, they die.

Going past a `creatures` `stress` capacity isn't purely negative, however. While a `creature` has gained `stress` past their capacity, whenever they would inflict a `wound`, they inflict 1 extra `wound`.

Once `stress` has been gained, there are a few ways to relieve it. Certain `spells` and `items` are capable of relieving `stress`, as well as certain `creature` `abilities`. A `creature` may relieve a number of `stress` equal to their `spirit` score at the end of a `short rest` and they relieve all of their gained `stress` at the end of a `long rest`.

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

# Creatures

In Dungeoneers, a `creature` is any living entity in the world. Often times, systems might refer to all hostile entities as "monsters". This feels like a less-inclusive phrase and morally loaded; after all, not all "enemies" are "monstrous", and some truly "monstrous" entities may not be "enemies". A `creature` has a few properties universal to all `creatures` that will be covered in this section.

## Attribute Scores

Every `creature` has 6 `attribute scores` that are used in a variety of scenarios. The specific scenarios are covered in their respective sections, but we'll talk a bit about each here.

### Power

The `power` score represents the physical strength and force output of a `creature`. The `power` score is used to determine things like `push` and `pierce` success.

### Prowess

The `prowess` score represents combat skill/capability. The `prowess` score is used to determine things like `hitting` and `dodging`.

### Endurance

The `endurance` score represents the physical and mental resilience of a `creature`. The `endurance` score is used to determine things like `stress` capacity.

### Resistance

The `resistance` score represents the magical defense of a `creature`. The `resistance` score is used to determine things like `magical armor` and `spell saves`.

### Spell

The `spell` score represents the talent with magic a `creature` has. The `spell` score is used to determine things like accuracy with `spell attacks` and `spell pierce`.

### Mind

The `mind` score represents the magical capacity of a `creature`. The `mind` score is used to determine things like `spell save` difficulty and `magica` capacity.

## Size

A `creature` has a `size` that represents the amount of physical space that they occupy. Something to note is that not all `creatures` in the same `size` category are the exact same physical size, only that they are able to control the specified number of tiles with the physical space they take up.

The `size` categories and tiles that `creatures` of that `size` occupy can be identified in the following table:

| Tiny | Small | Medium | Large | Huge | Massive |
| ---- | ----- | ------ | ----- | ---- | ------- |
| 1/4  | 1/2   | 1      | 2     | 3    | 4       |

Unless a `creature` occupies less than 1 tile, 2 `creatures` are not allowed to occupy the same tile. A tile that is fully occupied cannot be moved into or past, unless the occupying `creatures` allow it.

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

A `creature` accumulates `stress` over the course of a battle, and this `stress` can make them a better combatant but at a cost. A `creature` can handle an amount of `stress` equal to their `endurance` score.

> For example, if Freya has 3 `endurance`, she can handle up to 3 `stress`.

A `creature` can gain `stress` in a number of ways. Firstly, if a `creature` would sustain a `wound` while they can handle more `stress`, instead of sustaining the `wound(s)` they instead accumulate the number of `wounds` as `stress`. If this would exceed the maximum `stress` a `creature` can handle, any excess `wounds` are sustained as normal.

> For example, if Freya can handle 3 `stress` but has already accumulated 2 `stress`, sustaining 2 `wounds` would accumulate 1 `wound` as `stress` and Freya would sustain the remaining 1 `wound` as a `wound`. This would leave Freya at 3 `stress` and 1 `wound`.

While making an `attack`, a `creature` can elect to gain any number of `stress` in order to roll extra dice to `hit`. They must declare that they are doing this before any `hit dice` are rolled for the `attack`.

Gaining `stress` in any way other than sustaining `wounds` will still accumulate that `stress` past the `creatures` capacity. If a `creature` accumulates `stress` past their maximum, there are some consequences for doing so. If you sustain a `wound` while you have more `stress` than you can handle, you take _twice as many `wounds`_. This takes place before any `wound` reduction effects a `creature` may have. Additionally, whenever you accumulate `stress`, you accumulate _twice as much `stress`_. Again, this takes place before any `stress` reduction effects a `creature` may have. If you accumulate `stress` past 3 times your maximum, you sustain 1 `wound` every time you sustain `stress` past this maximum.

> For example, Freya can handle up to 3 `stress`. Let us fast-forward to a point where Freya has accumulated 9 `stress`. Freya elects to gain 2 `stress` to roll and extra `2d4` to `hit`. Because Freya has exceeded her `stress` maximum, she accumulates twice as much `stress`, so she now has accumulated 13 `stress`. Again, because Freya has accumulated `stress` once she has reached 3 times her capacity, she sustains 1 `wound`. Since she is past her `stress` capacity, Freya sustains 2 `wounds`! If Freya doesn't have any `wound` reduction effects, the next `wound` she sustains will kill her!

Going past a `creatures` `stress` capacity isn't purely negative, however. While a `creature` has accumulated `stress` past their capacity, they roll an extra `1d4` to their `pierce` rolls.

Once `stress` has been accumulated, there are a few ways to relieve it. Certain `spells`, `potions` and other `items` are capable of relieving `stress`, as well as certain `creature` `abilities`. A `creature` may relieve a number of `stress` equal to their `endurance` at the end of a `short rest` and they relieve all of their accumulated `stress` at the end of a `long rest` or `full rest`.
# Techniques

There are a multitude of `techniques` that a dungeoneer can learn and benefit from. These are selected largely when `leveling up` and are divided into 3 categories:

-   `Active Techniques`
-   `Passive Techniques`
-   `Exploration Techniques`

## Active Techniques

An `active technique` is a `technique` that must be activated as an `action` using `action points`. You can know any number of `active techniques` that you desire, but in order to activate an `active technique` as an `action`, it must be in your `loadout`.

Your `loadout` is the set of `active techniques` that you have ready to use at any given time. At level 1, all dungoneers have a `loadout` size of 6, which can be increased through `leveling up`. During `downtime`, you are free to swap out your `loadout` as you see fit, but if you want to swap your `loadout` on the fly you must pay the `stress` penalty marked on the `active technique`.

Below is the list of `active techniques`.

### General Techniques

#### Conduit

⚛️ | 🧠<br>
Cooldown: 1d6<br>
Tags: `Maneuver`

---

You regain `arca`.

`arcana roll` (`difficulty` 10)

-   Failure: You regain 1 `arca` and gain 2 `stress`
-   Partial success (-3): You regain 1 `arca` and gain 1 `stress`
-   Success (0): You regain 1 `arca`
-   Greater success (3): You regain 2 `arca`

#### Swap

⚛️ | 🧠<br>
Cooldown: 1d4<br>
Tags: `Maneuver`

---

Choose an adjacent `creature`. If that `creature` is willing, you may swap places with them. If the `creature` is unwilling, you may make a `roll`:

`speed roll` (`health` `difficulty`)

-   Failure: You fail to swap positions
-   Partial success (-3): You swap positions, but your target may `counterattack`
-   Success (0): You swap positions
-   Greater success (3): You swap positions and may `counterattack` your target

### Warrior Techniques

#### Sweeping Strikes

⚛️ | 🧠🧠<br>
Cooldown: 1d10<br>
Tags: `Fight`, `Weapon`

---

Pick a `tile` occupied by a `creature` and 2 `tiles` adjacent; all of which are in range of your `weapon`. You `fight` the `creature` in the first `tile` and the damage dealt is dealt to any `creature` occupying the other 2 `tiles`. A `creature` can be dealt damage multiple times in this way.

#### Charge

⚛️⚛️ | 🧠🧠🧠🧠<br>
Cooldown: 1d10<br>
Tags: `Fight`, `Weapon`, `Movement`

---

You immediately `move` a number of `tiles` up to your `speed` in a straight line, then `fight` an adjacent `creature`. For each `tile` you `move`, your weapon deals 1 additional `physical` damage.

#### Disarm

⚛️ | 🧠🧠<br>
Cooldown: 1d10<br>
Tags: `Maneuver`, `Weapon`

---

Pick a `creature` in range of your `weapon` and make a `roll`.

`skill roll` (`hit` `difficulty`)

-   Failure: You miss; nothing happens
-   Partial success (-3): Your target takes half the damage from your `weapon` (rounded down), but they hold on to their items
-   Success (0): You force your target to drop 1 item of your choice in their `wield` slots
-   Greater success (3): You force your target to drop 2 items of your choice in their `wield` slots

#### Hobble

⚛️ | 🧠🧠<br>
Cooldown: 1d6 | Duration: 1d6<br>
Tags: `Fight`, `Weapon`

---

You `fight` a `creature` and attempt to reduce their `speed`.

`<weapon stat> roll` (`hit` `difficulty`)

-   Failure: You miss your target and they take no damage
-   Partial success (-3): Your target takes half the damage from your `weapon` (rounded down)
-   Success (0): Your target takes the damage from your `weapon` and their `speed` is reduced by that damage
-   Greater success (3): Your target takes double the damage from your `weapon` and their `speed` is reduced by that damage

#### Marked Shot

⚛️⚛️ | 🧠🧠<br>
Cooldown: 1d10 | Duration: 1d8<br>
Tags: `Maneuver`, `Weapon`

---

You `mark` a `creature` within range of your `weapon`. While `marked`, whenever you deal damage to this `creature`, you deal an additional amount of `damage` equal to your `skill`.

#### Called Shot

⚛️ | 🧠🧠🧠<br>
Cooldown: 1d12<br>
Tags: `Fight`, `Weapon`

---

You attempt to bypass the `resistances` of your target.

`skill roll` (`hit` `difficulty`)

-   Failure: You miss your target and they take no damage
-   Partial success (-3): Your target takes the damage from your `weapon` as `stress`
-   Success (0): Your target takes the damage from your `weapon` and you ignore their `resistances`
-   Greater success (3): Your target takes double the damage from your `weapon` and you ignore their `resistances`

#### Entrench

⚛️⚛️ | 🧠🧠<br>
Cooldown: 1d10 | Duration: 1d8<br>
Tags: `Maneuver`, `Weapon`

---

You `entrench` yourself. While `entrenched`, when you `fight` you may target an additional `creature` within range, but your `speed` `stat` temporarily becomes 0. Using any `action` with the `movement` `tag` ends this `condition` early.

> Intention note: Using an `action` with the `movement` `tag` ends the `condition` before the `action` is resolved, meaning you'll be able to utilize your `speed` `stat` like normal.

#### Block

⚛️ | 🧠🧠<br>
Cooldown: 1d6 | Duration: 1d6<br>
Tags: `Maneuver`

---

You begin `blocking`. While `blocking`, you gain 1 `physical resistance`. If you have a `shield` equipped, you gain the `physical resistance` and `arcane resistance` of the `shield` instead.

> Intention note: While you have a `shield` equipped, you are already gaining the benefit of its `resistances`. This `ability` is intended to give those `resistances` _again_!

#### Redirect

⚛️⚛️ | 🧠🧠🧠🧠<br>
Cooldown: 1d12 | Duration: 1d8<br>
Tags: `Maneuver`

---

You begin to `redirect` nearby attacks. While `redirecting`, when a `creature` attempts to `fight` another `creature` while you are in their range, you may gain 1 `stress` to force yourself to be `fought` instead.

#### Deflection

⚛️ | 🧠🧠🧠🧠<br>
Cooldown: 1d12 | Duration: 1d8<br>
Tags: `Maneuver`

---

You start `deflecting` attacks from missiles. While `deflecting`, when a `creature` attempts to `fight` you with a `missile` `weapon`, any dice you use to avoid their attack are not `exhausted`.

#### Heavy Blows

⚛️⚛️ | 🧠🧠🧠🧠<br>
Cooldown: 1d12<br>
Tags: `Fight`, `Weapon`

---

You `fight` a `creature` within range. For this `action`, your damage with your `weapon` is doubled.

#### Disorient

⚛️⚛️⚛️ | 🧠🧠🧠🧠<br>
Cooldown: 1d12 | Duration: 1d4<br>
Tags: `Maneuver`, `Weapon`

---

You attempt to to de-stabilize a `creature`.

`<weapon stat> roll` (`health` `difficulty`)

-   Failure: You fail to meaningfully impact your target
-   Partial success (-3): Your target is `weakened`; but this `condition` is removed early after a roll is made against it
-   Success (0): Your target is `weakened` for the duration
-   Greater success (3): Your target is `weakened` for the duration, and you may roll 2 duration dice and take the higher

### Arcanist Techniques

#### Focus

⚛️ | 🧠🧠<br>
Cooldown: 1d8<br>
Tags: `Maneuver`

---

You may spend 1 `arca` per die you wish to add to your `dice pool` for this `round`.

#### Efficient Casting

⚛️ | 🧠🧠<br>
Cooldown: 1d8 | Duration: 1d8<br>
Tags: `Maneuver`

---

You utilize the `ambient arca` in order to bolster the `arca` available for your next `arcana`. The next `arcana` you use within the duration does not cost any `arca` until you spend past the `ambient arca`. This effect then ends.

#### Arcana Shield

⚛️⚛️ | 🧠🧠🧠<br>
Cooldown: 1d8 | Duration: 1d8<br>
Tags: `Maneuver`

---

You utilize `arca` to bolster your defenses. Until the duration ends, you have additional `physical resistance` and `arcana resistance` equal to the `arca` you spend on this `technique`.

> Intention note: This effect _does_ stack with `resistance` from other sources such as `armor` or `shields`!

#### Explosive Force

⚛️ | 🧠🧠🧠<br>
Cooldown: 1d6<br>
Tags: `Fight`

---

You `fight` a `creature`. You may spend `arca` in order to improve your damage by 1 `arcane` damage per `arca` spent.

#### Teleswap

⚛️⚛️ | 🧠🧠🧠🧠<br>
Cooldown: 1d12<br>
Tags: `Maneuver`
Range: Aura (3)

---

You may spend 1 `arca` to swap places with a willing `creature` within range, plus 1 tile for each additional `arca` you spend.

#### Detect Arcana

⚛️ | 🧠<br>
Cooldown: 1d6<br>
Tags: `Maneuver`, `Area`
Range: Aura (`arcana`)

---

You attempt to detect the presence of `arcana` in your vicinity.

`arcana roll` (`difficulty` 10)

-   Failure: You are unable to focus yourself to detect any form of `arcana`
-   Partial success (-3): You detect the presence of a major source of `arcana` within range
-   Success (0): You detect the presence of all but intentionally hidden sources of `arcana` and the nature of one of your choice within range
-   Greater success (3): You detect the presence of all sources of `arcana` and the nature of one of your choice within range

### Technician Techniques

#### Elusive Strike

⚛️ | 🧠🧠🧠<br>
Cooldown: 1d12<br>
Tags: `Fight`, `Weapon`

---

You `fight` a `creature` in range. Your `weapon` deals 1 less damage, but your target cannot counterattack.

#### Rally

⚛️⚛️ | 🧠🧠🧠<br>
Cooldown: 1d10<br>
Tags: `Maneuver`, `Area`
Range: Aura (5)

---

You attempt to invigorate your allies.

`skill roll` (`difficulty` 10)

-   Failure: You fail to inspire your allies
-   Partial success (-3): All allies in range (except you) lose 1 `stress`, and you gain 1 `stress`
-   Success (0): All allies in range (except you) lose 1 `stress`
-   Greater success (3): All allies in range (except you) lose 2 `stress`, and you lose 1 `stress`

#### Taunt

⚛️ | 🧠🧠🧠<br>
Cooldown: 1d10 | Duration: 1d8<br>
Tags: `Maneuver`, `Area`
Range: Aura (5)

---

You attempt to become the biggest threat to a `creature`.

`skill roll` (`morale` `difficulty`)

-   Failure: Your target does not see you as more or less threatening
-   Partial success (-3): Your target sees you as the biggest threat for 1 `round`
-   Success: Your target sees you as the biggest threat for the `duration`
-   Greater success: Your target sees you as the biggest threat for the `duration` and has its `hit` `difficulty` reduced by 1

#### Diminish

⚛️ | 🧠🧠🧠<br>
Cooldown: 1d10 | Duration: 1d8<br>
Tags: `Maneuver`, `Area`
Range: Aura (5)

---

You attempt to become the smallest threat to a `creature`.

`skill roll` (`morale` `difficulty`)

-   Failure: Your target does not see you as more or less threatening
-   Partial success (-3): Your target sees you as the smallest threat for 1 `round`
-   Success: Your target sees you as the smallest threat for the `duration`
-   Greater success: Your target sees you as a smallest threat for the `duration`. If you `fight` it, it cannot `counterattack`; after you do so the `duration` ends early

#### Recall Lore

⚛️ | 🧠<br>
Cooldown: 1d4<br>
Tags: `Maneuver`

---

You attempt to recall information about something you can sense or are being told about/reading about.

`skill roll` (`obscurity` `difficulty`)

-   Failure: You are unable to recall information in the moment
-   Partial success (-3): You recall a somewhat relevant or relatively obvious piece of information
-   Success: Your recall an important piece of information
-   Greater success: You recall several important pieces of information

> Intention note: the outcome from this `technique` is purposefully vague. There's a good amount of GM discretion as to what you are able to recall. For locations, it may be a piece of lore relevant to your objective. For `creatures`, it may be tactics, abilities, or weaknesses. Vague information is often not super enlightening. Here's an example:
>
> For a skeleton, a `partial success` would explain that it was a rather weak undead and that it was a skeleton. A `success` would be the above, as well as that it is weak to `arcane` damage. A `greater success` would be the above, as well as that it becomes `weakened` when it is `burned`.

#### Selfless

⚛️ | 🧠<br>
Cooldown: 1d4 | Duration: 1d6<br>
Tags: `Maneuver`
Range: Aura(2)

---

Target 1 `creature` within range; you may give them one of your un-`exhausted` `dice pool` dice. They may re-roll it and use it as if it were one of their own for the `duration`, but you do not gain that die back until the `duration` ends or you end it early.

#### Dirty Trick

⚛️ | 🧠<br>
Cooldown: 1d6 | Duration: 1d6<br>
Tags: `Maneuver`
Range: Aura(3)

---

You attempt to weaken a `creature` with an underhanded technique.

`skill roll` (`health` `difficulty`)

-   Failure: You fail to weaken your target
-   Partial success (-3): You lower 1 `difficulty` of your choice by 1 until the next `round`
-   Success (0): You lower 1 `difficulty` of your choice by 1 for the `duration`
-   Greater success (3): You lower 2 `difficulties` of your choice by 1 for the `duration`

#### Cover Me

⚛️⚛️ | 🧠<br>
Cooldown: 1d10 <br>
Tags: `Maneuver`, `Movement`
Range: Aura(4)

---

You attempt to support a `creature's` movement.

`skill roll` (`difficulty` 10)

-   Failure: You are unable to meaningfully cover your target
-   Partial success (-3): Your target may immediately move a number of `tiles` equal to their `speed`, but you gain 1 `stress`
-   Success (0): Your target may immediately move a number of `tiles` equal to their `speed`
-   Greater success (3): Your target may immediate move a number of `tiles` equal to their `speed` or your `skill`; whichever is higher

#### Demoralize

⚛️ | 🧠🧠🧠<br>
Cooldown: 1d10 | Duration: 1d8<br>
Tags: `Maneuver`, `Area`
Range: Aura (5)

---

You attempt to instill despair in a `creature`.

`power roll` (`morale` `difficulty`)

-   Failure: Your target is unaffected
-   Partial success (-3): Your target is `afraid` for the remainder of the `round`
-   Success: Your target is `afraid` for the `duration`
-   Greater success: Your target is `afraid` for the `duration` and gives up fighting if they are alone and are not a `solo` `creature`

While `afraid`, a `creature` attempts to flee the source of their fear. If they are unable to or believe it to be futile, they will put everything into killing the source of their fear.

## Passive Techniques

A `passive technique` is a `technique` which does not need to be activated in order to apply. You can know a number of `passive techniques` equal to your `level`. Even though `passive techniques` do not need to be activated, some have a `cooldown` for how often they can be applied.

Below is the list of `passive techniques`.

### General Techniques

### Warrior Techniques

#### Dual Wielder

Tags: `Talent`

---

When you have 2 `weapons` equipped, you may choose to `fight` with either `weapon` or both `weapons`. If you choose to `fight` with both `weapons`, you may forfeit adding your `stat` to the `roll` in order to deal the damage of both `weapons`.

#### Leverage

Tags: `Talent`

---

Your damage with `control` `weapons` increases by your `skill` when you hit a `creature` at your maximum range.

#### Armor Pierce

Tags: `Talent`

---

When you hit a `creature` and get a `greater success` with a `light` `weapon`, you may choose to gain 1 `stress` in order to ignore all `resistances`.

#### Consistency

Tags: `Talent`

---

When you are making a `roll` to hit a `creature` during a `fight` with a `standard` `weapon`, you may gain 1 `stress` to add a `dice pool` die without `exhausting` it.

#### Follow Through

Tags: `Talent`

---

When you miss a `creature` while `fighting` it with a `heavy` `weapon`, you can gain 1 `stress` in order to make a separate `roll` against another `creature` that is also in your range. This second `creature` cannot counterattack.

#### Sharpshooter

Tags: `Talent`

---

When you miss while `fighting` with a `missile` `weapon`, you can gain 2 `stress` in order to turn the `roll` into a `success`.

#### Parry

Tags: `Talent`

---

When making a `roll` to avoid damage from a `weapon`, you may gain 1 `stress` to add an `exhausted` die to your `roll`.

#### Pivot

Tags: `Talent`

---

After making a `roll`, you may `exhaust` a die to immediately `move` that number of `tiles`.

#### Quick Step

Tags: `Talent`

---

Before initiating a `fight` or just before making a `counterattack`, you may use a die to `move` that number of `tiles`. You _must_ use that die in the `roll`.

#### Run Interference

Tags: `Talent`

---

When a `creature` a number of `tiles` equal or less than your `speed` is forced to make a `roll` to avoid damage, you may give them one of your dice to use in the roll. When you do so, you immediately `move` to an adjacent `tile` to that `creature` within your `speed`.

#### Lethal Body

Tags: `Talent`

---

You may treat your body (elbows, headbutt, kick, etc) as `standard weapons` that are always `equipped`. This counts as dual wielding.

#### Shield Wall

Cooldown: 1d10
Tags: `Talent`

---

Whenever you are making a `roll` to avoid `weapon` damage with a `shield` `equipped`, you may un-`exhaust` a die and immediately use it in your `roll`.

#### Bulwark

Tags: `Talent`

---

While you have `heavy armor` `equipped`, your `armor die` is now 2d6 instead of 1d6.

#### Practiced Distribution

Tags: `Talent`

---

While you have `medium armor` `equipped`, when you roll a 1 on your `armor die` you may re-roll it once. You must keep the new result.

#### Free Motion

Tags: `Talent`

---

While you have `light armor` `equipped`, you can `break` your `armor` in order to automatically roll a `greater success` on any roll to avoid damage without having to expend any dice. You cannot do this if your `armor` is already `broken`.

### Arcanist Techniques

#### Danger Close

Tags: `Talent`

---

When casting `arcana` with the `area` `tag`, you can gain 1 `stress` per `creature` you wish to exclude from the effects of the `arcana`.

#### Intense Focus

Duration: 1d12
Tags: `Talent`

---

When casting `arcana` with the `concentration` `tag`, you may `exhaust` 1 `dice pool` die. Any damage taken less than or equal to that die total does not break your `concentration`. You may maintain this for the duration, but you may not un-`exhaust` or re-roll the die you choose until it ends or you choose to end it early.

### Technician Techniques

#### Lead by Example

Tags: `Talent`

---

When you partake in a `group roll`, you may re-roll the die you pick for the `roll` one time if you wish.

#### Trap Sniffer

Tags: `Talent`, `Search`

---

When you try and `search` for traps, you may use 1 die without `exhausting` it as long as you choose to give up your chance to find anything hidden that isn't a trap.

## Exploration Techniques

An `exploration techniques` are similar to `active` and `passive techniques`, but `exploration techniques` are to be used in the `wilderness map`. You can know any number of `exploration techniques`.

Below is the list of `exploration techniques`.

### Exploration Techniques List

#### Quick Backtrack

Tags: `Exploration`, `Passive`

---

When you take the `travel` `action`, you may move 2 `tiles` instead of 1 if they are both `tiles` you have been in before.

#### Secret Connoisseur

Tags: `Exploration`, `Passive`

---

You may use 1 die without `exhausting` it when you make a `roll` attempting to discover hidden paths or objects. Additionally, you automatically recall connections between locks and keys (such as identifying a key goes to a door found earlier, or that a door is opened by a lever you saw earlier).

#### Move Defensively

⚛️<br>
Tags: `Exploration`

---

You move carefully in the attempt to protect yourself from a sudden attack. If you need to make a `roll` this `round` to avoid damage, you may re-roll one die you choose to contribute to the `roll`.

#### Eye for Shelter

⚛️⚛️<br>
Tags: `Exploration`

---

You are able to discern if/how you are likely to be attacked during `downtime` in a certain location.

#### Gift of Direction

⚛️⚛️<br>
Tags: `Exploration`

---

Name a location/point of interest that you are searching for and attempt to sense if you have moved closer to it or farther from it.

`skill roll` (`environment` `difficulty`)

-   Failure: You're unable to tell if you've gotten farther or closer
-   Partial success (-3): You can tell if you've gotten closer, but you're unable to tell if you've gotten farther or stayed just as far
-   Success (0): You can tell if you've gotten closer or farther
-   Greater success (3): You can tell if you've gotten closer or farther _and_ you can tell if your target is moving

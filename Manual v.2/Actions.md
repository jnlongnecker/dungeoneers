# Actions

Every `player phase`, each dungeoneer has 3 `action points` to spend on `actions`. There are 4 generally available `actions`:

-   Fight
-   Movement
-   Interact
-   Rest

Each `action` uses up a different number of `action points`, represented by a ⚛️.

## Fight

⚛️<br>
Tags: `Fight`

---

The `fight` `action` allows you to enter combat with another `creature`. The way the `fight` `action` works depends largely on the `weapon` you have equipped.

First, you can only take the `fight` `action` on a `creature` that's in range of your `weapon`. This is distance is listed in `tiles`; if your target is within this distance then you're able to `fight` it.

There are 2 parts to a `fight` `action`. The first part is the attack from a `roll`:

`<weapon stat> roll` (`hit` `difficulty`)

-   Failure: You miss your target and they take no damage
-   Partial success (-3): You barely miss your target, and they take half the damage from your `weapon` (rounded down)
-   Success (0): You hit your target, and they take the damage from your `weapon`
-   Greater success (3): You soundly hit your target, and they take double the damage from your `weapon`

The `stat` you add to your `roll` depends on the `stat` used by your `weapon`. If your target survives your strike and you are in range of their `weapon`, the second part occurs and they will `counterattack` and a second `roll` is needed:

`speed roll` (`dodge` `difficulty`)

-   Failure: You are soundly hit, and you take double the damage from their `weapon`
-   Partial success (-3): You are hit and take the damage from their `weapon`
-   Success (0): You barely dodge out of the way and take half the damage from their `weapon` as `stress`
-   Greater success (3): You completely avoid all damage

It is important to note that the second part of a `fight` `action` applies to _any_ `action` with the `fight` `tag`. Also note that when another `creature` `fights` you, this order is reversed; first you must make the `dodge` `roll`, and then you may `counterattack` them.

## Movement

⚛️<br>
Tags: `Movement`

---

The `movement` `action` allows you to move a number of `tiles` up to your `speed`. You must spend a die in your `dice pool` in order to take this `action`. You can break this movement up over your other `actions`, but once you end your `turn` any remaining potential movement is lost.

### Movement on Difficult Terrain

Certain types of terrain is more difficult to move in than normal land. For these scenarios, a `roll` is necessary (the die used to take the `action` _can_ be used in this `roll`). Consult the chart below to determine the `difficulty` of various types of terrain:

| Terrain Type             | Difficulty |
| ------------------------ | ---------- |
| Muck/Debris/Foliage/Etc. | 5          |
| Water                    | 7          |
| Gap                      | 10         |
| Wall                     | 15         |

## Interact

⚛️<br>
Tags: `Interact`

---

The `interact` `action` allows you to manipulate an object in the environment. This varies wildly and can be anything from opening a door or chest to pulling a lever to drawing a note for yourself on the wall.

## Rest

⚛️<br>
Tags: `Rest`

---

The `rest` `action` allows you to take a breather. You may use this to do one of the following:

-   Change out 1 `active technique`, paying its `stress` cost
-   Re-roll or regain 3 dice for your `dice pool`
-   Advance a `cooldown` by 1

## Search

⚛️<br>
Tags: `Search`, `Area`
Range: Sight

---

The `search` `action` allows you to investigate your surroundings. You can use this to try and find anything from secrets to hidden items to traps. Regardless of what you're looking for, make a `roll`:

`skill roll` (`locate` `difficulty`)

-   Failure: You are unable to find anything of note
-   Partial success (-3): You are able to tell something is nearby, but not its nature or location
-   Success (0): You are able to tell where something hidden is
-   Greater success (3): You are able to tell where something hidden is and its nature

> Intention note: It's likely that there will be occasions where there are multiple hidden things that can be `searched` for in one area. Each one will potentially have separate `locate` `difficulties`. When a `roll` is made, consider it to be made against everything in range. This is what the `area` `tag` means, but we wanted to specify that directly here!

## Explore

⚛️⚛️⚛️<br>
Tags: `Explore`

---

When taken while on a `dungeon map`, the `creature` flees the area in an attempt to move on. Players are free to take this `action` should they wish to preserve their dungeoneer should the dungeon prove too lethal, but Game Masters should be careful about communicating the consequences of such a choice.

## Travel

⚛️<br>
Tags: `Exploration`

---

On the `wilderness map`, you move 1 `tile`.

## Track

⚛️⚛️️️️<br>
Tags: `Exploration`

---

You may attempt to follow a trail left behind by a `creature`.

`skill roll` (`locate` `difficulty`)

-   Failure: You fail to find the proper path
-   Partial success (-3): You learn the next `tile` to go to in order to follow the trail
-   Success (0): You learn the next `tile` to go to in order to follow the trail and may move 1 `tile`
-   Greater success (3): You learn the next 2 `tiles` to go to in order to follow the trail and may move 1 `tile`

## Hide

⚛️⚛️️️️<br>
Tags: `Exploration`

---

You attempt to hide your party.

`skill roll` (`local` `difficulty` + number of `creatures` impacted)

-   Failure: Your party is as noticeable as normal
-   Partial success (-3): All `creatures` you come across do not notice you this `round`
-   Success (0): All `creatures` your party comes across do not notice any of your party this `round`
-   Greater success (3): All `creatures` your party comes across do not notice any of your party this `round` or the next

## Scout

⚛️⚛️️️️<br>
Tags: `Exploration`

---

You attempt to gain a preview of your surroundings.

`speed roll` (`local` `difficulty`)

-   Failure: You are unable to accurately and safely understand your surroundings
-   Partial success (-3): You uncover 1 adjacent `tile` of your choice
-   Success (0): You uncover 2 adjacent `tiles` of your choice
-   Greater success (3): You uncover 3 adjacent `tiles` of your choice

## Investigate

⚛️️️️⚛️️️️<br>
Tags: `Exploration`

---

You attempt to uncover `notable features` in your `tile`.

`skill roll` (`local` `difficulty`)

-   Failure: You are unable to discover any `notable features`
-   Partial success (-3): You discover one `notable feature` (if any), but `creatures` at it may notice you
-   Success (0): You discover all `notable features` (if any), but `creatures` at them may notice you
-   Greater success (3): You discover all `notable features` (if any), and any `creatures` at them do not notice you

> Intention note: The outcomes reference that `creatures` may or may not notice you at the `notable features` you uncover. The only reason they would _not_ notice you on a `partial success` or a `success` is if a feature keeps you hidden. On a `greater success`, regardless if you have such a feature or not you are not noticed.

## Group Actions

Whenever a player takes an `action`, another player within range and with the ability to take the same `action` may offer to make it a `group action`. This is only mechanically meaningful when there is a `roll` involved, but you may desire to do so for a narrative reason.

When a `group action` is made, the `difficulty` becomes multiplied by the number of players involved in the `group action`. Each involved player must contribute dice towards the `difficulty`, each adding their applicable `stat`. If the `roll` fails, all players involved gain 1 `stress`. If the `roll` is successful, all players involved gain the benefit of the outcome.

For example, if 2 players make a `fight` `group action` and the `difficulty` is a 5, the new `difficulty` that both players must work together to beat is 10. If they fail, they both gain 1 `stress`. If they succeed, their opponent takes the damage from _both_ of their `weapons`.

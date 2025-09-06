# Actions

Every `player phase`, each dungeoneer has 3 `action points` to spend on `actions`. There are 6 `actions`:

-   Fight
-   Movement
-   Interact
-   Rest
-   Explore
-   Ability

Each `action` uses up a different number of `action points`, represented by a ⚛️.

## Fight

⚛️

---

The `fight` `action` allows you to enter combat with another `creature`. The way the `fight` `action` works depends largely on the `weapon` you have equipped.

First, you can only take the `fight` `action` on a `creature` that's in range of your `weapon`. This is distance is listed in `tiles`; if your target is within this distance then you're able to `fight` it.

Once you've started the `fight`, you'll spend your `dice pool` towards the `hit difficulty` of your opponent. For each multiple of your opponent's `difficulty`, you deal your `weapon's` damage. However, if your opponent lives once you've finished spending your `dice pool`, they will counterattack as long as you are in range of them.

You will need to spend your `dice pool` towards the `dodge difficulty` of your opponent, using your `speed` as the bonus. If you cannot meet or surpass your opponent's `dodge difficulty`, you will take the damage of their `weapon`.

## Movement

⚛️

---

The `movement` `action` allows you to move a number of `tiles` up to your `speed`. You must spend a die in your `dice pool` in order to take this `action`. You can break this movement up over your other `actions`, but once you end your `turn` any remaining potential movement is lost.

### Movement on Difficult Terrain

Certain types of terrain is more difficult to move in than normal land. For these scenarios, a `roll` is necessary (the die used to take the `action` _can_ be used in this `roll`). Consult the chart below to determine the `difficulty` of various types of terrain:

| Terrain Type | Difficulty |
| ------------ | ---------- |
| Muck/Debris  | 5          |
| Water        | 7          |
| Gap          | 10         |
| Wall         | 15         |

## Interact

⚛️

---

The `interact` `action` allows you to manipulate an object in the environment. This varies wildly and can be anything from opening a door or chest to pulling a lever to drawing a note for yourself on the wall.

## Rest

⚛️

---

The `rest` `action` allows you to take a breather. You may use this to do one of the following:

-   Change out 1 `ability`
-   Re-roll or regain 3 dice for your `dice pool`
-   Advance a `cooldown` by 1

## Ability

Varies

---

This `action` allows you to utilize one of the `abilities` in your `loadout`. You'll have to refer to the `ability` description in order to know what it will do and how many `action points` it requires.

## Explore

⚛️⚛️⚛️

---

This `action` functions differently depending on the type of `map` in use. If taken while on a `dungeon map`, the `creature` flees the area in an attempt to move on. Players are free to take this `action` should they wish to preserve their dungeoneer should the dungeon prove too lethal, but Game Masters should be careful about communicating the consequences of such a choice.

In a `wilderness map`, the `explore` `action` allows the player to use an `exploration technique` they know or do one of the following listed in this section.

### Travel

On the `wilderness map`, you move up to 2 `tiles`.

### Track

You may attempt to follow a trail left behind by a `creature`.

`skill roll`

-   Failure: You fail to find the proper path
-   Partial success (-3): You learn the next `tile` to go to in order to follow the trail
-   Success (0): You learn the next `tile` to go to in order to follow the trail and may move 1 `tile`
-   Greater success (3): You learn the next 2 `tiles` to go to in order to follow the trail and may move 1 `tile`

### Hide

You attempt to hide your party.

`skill roll` (`difficulty` + number of `creatures` impacted)

-   Failure: Your party is as noticeable as normal
-   Partial success (-3): All `creatures` you come across do not notice you this `round`
-   Success (0): All `creatures` your party comes across do not notice any of your party this `round`
-   Greater success (3): All `creatures` your party comes across do not notice any of your party this `round` or the next

### Scout

You attempt to gain a preview of your surroundings.

`speed roll`

-   Failure: You are unable to accurately and safely understand your surroundings
-   Partial success (-3): You uncover 1 adjacent `tile` of your choice
-   Success (0): You uncover 2 adjacent `tiles` of your choice
-   Greater success (3): You uncover 3 adjacent `tiles` of your choice

### Investigate

You attempt to uncover `notable features` in your `tile`.

`skill roll`

-   Failure: You are unable to discover any `notable features`
-   Partial success (-3): You discover one `notable feature` (if any), but `creatures` at it may notice you
-   Success (0): You discover all `notable features` (if any), but `creatures` at them may notice you
-   Greater success (3): You discover all `notable features` (if any), and any `creatures` at them do not notice you

> Intention note: The outcomes reference that `creatures` may or may not notice you at the `notable features` you uncover. The only reason they would _not_ notice you on a `partial success` or a `success` is if a feature keeps you hidden. On a `greater success`, regardless if you have such a feature or not you are not noticed.

## Group Actions

Whenever a player takes an `action`, another player within range and with the ability to take the same `action` may offer to make it a `group action`. This is only mechanically meaningful when there is a `roll` involved, but you may desire to do so for a narrative reason.

When a `group action` is made, the `difficulty` becomes multiplied by the number of players involved in the `group action`. Each involved player must contribute dice towards the `difficulty`, each adding their applicable `stat`. If the `roll` fails, all players involved gain 1 `stress`. If the `roll` is successful, all players involved gain the benefit of the outcome.

For example, if 2 players make a `fight` `group action` and the `difficulty` is a 5, the new `difficulty` that both players must work together to beat is 10. If they fail, they both gain 1 `stress`. If they succeed, their opponent takes the damage from _both_ of their `weapons`.

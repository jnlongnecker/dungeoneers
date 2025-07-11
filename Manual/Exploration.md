# Exploration

Exploration is the pillar of play that connects together combat and socialization, and is quite a broad category. Exploration handles everything from macro travel over miles of expanse to micro investigation of individual rooms. If there is terrain to be dissected, it is covered by exploration.

## Environments

Exploration is done within `environments`. Each `environment` is home to a number of `creatures`; some passive, some helpful, and some hostile. These `environments` are also home to any number of natural hazards, such as ravines, tar pits, rockfalls, and cliffs. Further still, these `environments` have points of interest for the players to more fully interact with in comparison to large swathes of homogenous terrain.

Each `environment` is difficult to travel in for various reasons. The baseline difficulty of an `environment` is called the `environmental difficulty`. Many rolls that challenge the `environment` will require the `environmental difficulty` in order to determine the outcome of the roll. Additionally, depending on a variety of criteria the length of an `exploration round` will differ. The `exploration speed` represents the number of 1 mile tiles traveled during the `exploration round`.

| Danger Level | Environmental Difficulty | Exploration Round Time | Base Exploration Speed | Tier |
| ------------ | ------------------------ | ---------------------- | ---------------------- | ---- |
| Peaceful     | 0                        | 8 hours                | 16                     | All  |
| Low          | 1                        | 1 hour                 | 2                      | 1    |
| Medium       | 2                        | 1 hour                 | 2                      | 2    |
| High         | 3                        | 1 hour                 | 2                      | 3    |
| Extreme      | 4                        | 1 hour                 | 2                      | 4    |

In a typical `environment`, every `exploration round` of travel the players should potentially come across an `encounter`. In particularly barren or crowded `environments`, this will be more or less likely to be something other than the `free encounter`. The `encounter table` of these unique `environments` should be adjusted to ensure `encounters` are more or less likely.

The relative danger level and population level of the `environment` isn't the only factor to consider; the complexity level of the `environment` also influences how fast a party can move through it and find their way.

| Complexity Level | Navigation Difficulty | Base Exploration Speed |
| ---------------- | --------------------- | ---------------------- |
| Trivial          | -1                    | +1                     |
| Simple           | +0                    | +1                     |
| Average          | +0                    | +0                     |
| Complex          | +0                    | -1                     |
| Labyrinthian     | +1                    | -1                     |

During exploration, GM moves are primarily just rolling on the `encounter table`. In a dungeon, the rules for exploration are the same, except the unit for `exploration speed` is 1 room and the `exploration round` time is 5 minutes.

In any `environment`, the world is divided into tiles called `locations` that represent the distance traveled per unit of `exploration speed`. These tiles may or may not have points of interest to explore. GMs should have a rough map of `locations`, and when players travel they should be aware of where they are on the map and pick a tile within their `exploration speed` to travel to.

### Encounter Tables

Exploration and player `moves` are balanced around certain `encounters` being more or less likely in a particular environment. There are 7 types of `encounters` that can appear on an `encounter table`:

| Encounter Type        | Description                                                                                             |
| --------------------- | ------------------------------------------------------------------------------------------------------- |
| Hostile `creature(s)` | One or more `creatures` cross paths with the party and attack                                           |
| Neutral `creature(s)` | One or more `creatures` cross paths with the party and interact                                         |
| Point of Interest     | An interesting feature appears, such as a waterfall, lake, oasis, ruined structure, etc.                |
| Hazard                | A dangerous hazard strikes the party, such as an unseen tar pit, bottomless pit, or a trap              |
| Curiosity             | An unnatural occurrence appears, such as glowing flora, a stretch of reversed gravity, or recent battle |
| Lost                  | The party loses their way and makes no progress                                                         |
| Free                  | Nothing happens                                                                                         |

Each encounter table should be made up of the above `encounters`, but the actual contents of the table are determined by the GM.

## Exploration Moves

The `moves` found here are most applicable for exploration contexts.

### Push Forward

Tags: Long-acting

---

You and your group travel to a new location in the `environment`, but you and your group cannot take `free moves` with the _stationary_ `tag`.

### Hold Position

Tags: Long-acting

---

You and your group stay in your current location and are able to take `free moves` that have the _stationary_ `tag`. You have a point of `boon` to your roll if you make the `lookout` `free move`.

### Backtrack

Tags: Long-acting

---

You and your group move to a location in the `environment` you have already been before. You cannot get a `lost encounter`, but you and your group cannot take `free moves` with the _stationary_ `tag`.

## Exploration Free Moves

The `free moves` found here are most applicable for exploration contexts.

### Navigate

Tags: Long-acting, Concentrate

---

You navigate your group through the `environment`.

`Group` (`mind`, `knowledge`) - Environmental Difficulty

-   Lesser success (-1): Replace 1 lost `encounter` with 1 hazard `encounter`
-   Success (0): Replace 1 lost `encounter` with 1 free `encounter`
-   Greater success (1): Replace 2 lost `encounters` with 2 free `encounters`

### Head the March

Tags: Long-acting, Movement

---

You lead the charge for your group to improve the efficiency that you move through the `environment`.

`Group` (`spirit`, `influence`) - Environmental Difficulty

-   Lesser success (-1): Your maximum `exploration speed` improves by 1
-   Success (0): Your maximum `exploration speed` improves by 2
-   Greater success (1): Your maximum `exploration speed` improves by 2, and you relieve a `stress`

### Track

Tags: Long-acting, Concentrate, Procurement

---

You follow the leftover context clues a `creature` has made by moving through the `environment`.

`Core` (`mind`, `hunting`) - Environmental Difficulty

-   Lesser success (-1): You follow the trail of a `creature` at a maximum `exploration speed` of 1
-   Success (0): You follow the trail of a `creature` at a maximum `exploration speed` of 2
-   Greater success (1): You follow the trail of a `creature` at a maximum `exploration speed` of 3

### Detect Arcana

Tags: Long-acting, Concentrate, Arcana

---

When taking this `free move`, your party can move at a maximum `exploration speed` of 1.

`Core` (`mind`, `arcana`) - Environmental Difficulty

-   Lesser success (-1): You detect the presence of arcana within a tile radius of 5
-   Success (0): You detect the presence of arcana within a tile radius of 10
-   Greater success (1): You detect the presence of arcana within a tile radius of 15

### Muffle

Tags: Long-acting, Stealth

---

When taking this `free move`, your party can move at a maximum `exploration speed` of 1.

`Group` (`finesse`, `stealth`) - Environmental Difficulty

-   Lesser success (-1): 1 hostile `creature` `encounter` is replaced with a neutral `creature` `encounter`
-   Success (0): 1 hostile `creature` `encounter` is replaced with a free `encounter`
-   Greater success (1): 1 hostile `creature` `encounter` and 1 neutral `creature` `encounter` are replaced with 2 free `encounters`

### Boost Morale

Tags: Long-acting, Concentrate, Influence

---

`Core` (`spirit`, `influence`) - Environmental Difficulty

-   Lesser success (-1): You may relieve 1 `stress`
-   Success (0): You and all of your party may relieve 1 `stress`
-   Greater success (1): All your party may relieve 1 `stress` and you may relieve 2 `stress`

### Lookout

Tags: Long-acting, Concentrate, Observe

---

You may attempt to `notice` as you travel. The party can move at a maximum of `exploration speed` of 1.

### Cloak

Tags: Long-acting, Movement

---

When taking this `free move`, your party can move at a maximum `exploration speed` of 1.

`Core` (`finesse`, `stealth`) - Environmental Difficulty

-   Lesser success (-1): You are `cloaked` for 1 `combat round`, should an `encounter` arise
-   Success (0): You are `cloaked` for 2 `combat rounds`, should an `encounter` arise
-   Greater success (1): You are `cloaked` for the remainder of this `exploration round`; until broken or searched for

### Investigate

Tags: Long-acting, Concentrate, Stationary

---

You may attempt to `examine`.

### Scrounge

Tags: Long-acting, Concentrate, Procurement, Stationary

---

You may attempt to `harvest`.

### Scout

Tags: Long-acting, Concentrate, Stationary

---

You move ahead of the group in order to prepare them for what is to come.

`Core` (`finesse`, `examination`) - Environmental Difficulty

-   Lesser success (-1): You reveal an adjacent location, but a non-`free encounter` occurs this turn
-   Success (0): You reveal an adjacent location
-   Greater success (1): You reveal an adjacent location and guarantee a `free encounter` occurs this turn

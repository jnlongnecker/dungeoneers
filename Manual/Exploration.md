# Exploration

Exploration is the pillar of play that connects together combat and socialization, and is quite a broad category. Exploration handles everything from macro travel over miles of expanse to micro investigation of individual rooms. If there is terrain to be dissected, it is covered by exploration.

## Environments

Exploration is done within `environments`. Each `environment` is home to a number of `creatures`; some passive, some helpful, and some hostile. These `environments` are also home to any number of natural hazards, such as ravines, tar pits, rockfalls, and cliffs. Further still, these `environments` have points of interest for the players to more fully interact with in comparison to large swathes of homogenous terrain.

Each `environment` is difficult to travel in for various reasons. The baseline difficulty of an `environment` is called the `environmental difficulty`. Many rolls that challenge the `environment` will require the `environmental difficulty` in order to determine the outcome of the roll. Additionally, depending on a variety of criteria the length of an `exploration round` will differ. The `exploration speed` represents the number of 1 mile tiles traveled during the `exploration round`.

| Danger Level | Environmental Difficulty | Exploration Round Time | Exploration Speed | Tier |
| ------------ | ------------------------ | ---------------------- | ----------------- | ---- |
| Peaceful     | 1                        | 8 hours                | 32                | All  |
| Low          | 5                        | 1 hour                 | 3                 | 1    |
| Medium       | 8                        | 1 hour                 | 3                 | 2    |
| High         | 10                       | 1 hour                 | 3                 | 3    |
| Extreme      | 13                       | 1 hour                 | 3                 | 4    |

In a typical `environment`, every hour of travel the players should potentially come across an `encounter`. In particularly barren or crowded `environments`, this frequency will change. The `encounter table` of these unique `environments` should be adjusted to ensure `encounters` are more or less likely.

The relative danger level and population level of the `environment` isn't the only factor to consider; the complexity level of the `environment` also influences how fast a party can move through it and find their way.

| Complexity Level | Navigation Difficulty | Exploration Speed |
| ---------------- | --------------------- | ----------------- |
| Trivial          | -5                    | +1                |
| Simple           | -2                    | +1                |
| Average          | 0                     | +0                |
| Complex          | +2                    | -1                |
| Labyrinthian     | +5                    | -1                |

During exploration, GM moves are primarily just rolling on the `encounter table`. In a dungeon, the rules for exploration are the same, except the unit for `exploration speed` is 1 room and the `exploration round` time is 5 minutes.

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
| Free                  | Nothing occurs                                                                                          |

Each encounter table should be made up of the above `encounters`, but the actual contents of the table are determined by the GM.

## Exploration Moves

The `moves` found here are most applicable for exploration contexts.

### Navigate

Tags: Long-acting, Concentrate

---

You may make a `group roll`:

`check`: [`knowledge`] + `mind` vs [environmental difficulty]

On a success, replace 2 lost `encounters` with 2 free `encounters`. On a partial success, replace 1 lost `encounter` with 1 free `encounter`.

### Head the March

Tags: Long-acting, Movement

---

You may make a `group roll`:

`check`: [`influence`] + `spirit` vs [environmental difficulty]

On a success, you may improve `exploration speed` to 3, or 2 on a partial success.

### Track

Tags: Long-acting, Concentrate, Procurement

---

You may make a `group roll`:

`check`: [`hunting`] + `mind` vs [environmental difficulty]

On a success, you follow the trail of a `creature` at a maximum `exploration speed` of 4. On a partial success, you follow the trail of a `creature` at a maximum of `exploration speed` of 3.

## Exploration Free Moves

The `free moves` found here are most applicable for exploration contexts.

### Detect Arcana

Tags: Long-acting, Concentrate, Arcana

---

You may make a roll:

`total`: [`arcana`] + `mind`

You detect the presence of arcana within a tile radius determined by your roll. The party can move at a maximum of `exploration speed` of 2.

### Step Softly

Tags: Long-acting, Movement, Assist

---

You may make a `group roll`:

`check`: [`stealth`] + `finesse` vs [environmental difficulty]

On a success, 1 hostile `creature` `encounter` and 1 neutral `creature` `encounter` are replaced with 2 free `encounters`. On a partial success, 1 neutral `creature` `encounter` is replaced with a free `encounter`. The party can move at a maximum of `exploration speed` of 2.

### Scout

Tags: Long-acting, Concentrate

---

You may make a roll:

`check`: [`examination`] + `finesse` vs [environmental difficulty]

On a success, you learn what the next `encounter` is going to be. On a partial success, nothing happens. On a failure, the next `encounter` happens to you 5 `combat rounds` early.

### Boost Morale

Tags: Long-acting, Concentrate, Influence

---

You may make a roll:

`check`: [`influence`] + `spirit` vs [environmental difficulty]

On a success, you and all of your party may clear 1 `stress`. On a partial success, all of your party except you may clear 1 `stress`.

### Scrounge

Tags: Long-acting, Concentrate, Procurement

---

You may attempt to `harvest` as you travel. The party can move at a maximum of `exploration speed` of 2.

### Lookout

Tags: Long-acting, Concentrate, Observe

---

You may attempt to `notice` as you travel. The party can move at a maximum of `exploration speed` of 2.

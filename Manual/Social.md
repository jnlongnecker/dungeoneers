# Socialization

Interactions with `creatures` who aren't in the middle of trying to fight you are handled as socialization. In many instances, these scenarios are simple exchanges of information between characters. The mechanics found here are to track and identify `attitudes` of `creatures` to each other and to the players, as well as give mechanics for players who wish to negotiate and talk down intelligent `creatures`.

> Some tables prefer to handle socialization without any rules. Defining mechanics for how these scenarios unfold allows players to specialize their characters to handle socialization with bespoke `abilities`. Leaving socialization out of the realm of mechanics doesn't fit well with the rest of the game, but if that is the preference of the table be sure to communicate this with your table so that players can pick `abilities` that align more with how the game is going to be played.

## Attitude

Every `creature` in the game will have an `attitude` about the players as well as other `creatures`. The `attitude` will influence the decisions of the `creature` when they are asked for something from the players. Importantly though, is that `attitude` is not mind control! Unreasonable requests may simply be denied no matter what. You can find a list of `attitudes` and their meaning below:

| Attitude     | Description                                                                   |
| ------------ | ----------------------------------------------------------------------------- |
| Servant      | Will follow any requests to the best of their ability                         |
| Trusted Ally | Will follow reasonable requests without convincing                            |
| Ally         | Will follow most requests with minimal convincing                             |
| Friendly     | Will follow some requests with convincing                                     |
| Neutral      | Will make equivalent exchanges if prompted                                    |
| Unfriendly   | Will be reluctant to make even equivalent exchanges                           |
| Disgust      | Will refuse equivalent exchanges and will openly attack in the right scenario |
| Hostile      | Will openly attack, but can be pacified through great effort                  |
| Nemesis      | Will openly attack and obsessively scheme downfall at all opportunities       |

These are the `attitudes` of intelligent `creatures`. This then begs the question of what defines an "intelligent" `creature`. This is any `creature` with a `mind` score of 3 or above. `Creatures` with a `mind` score of 1 or 2 instead are simplified into the hostile, neutral and trusted ally `attitudes`.

Below you can find a table detailing common requests in socialization and the `difficulty` of doing so depending on the `attitude` of the `creature`.

| Request                                   | Servant | Trusted Ally | Ally | Friendly | Neutral | Unfriendly | Disgust | Hostile | Nemesis |
| ----------------------------------------- | ------- | ------------ | ---- | -------- | ------- | ---------- | ------- | ------- | ------- |
| End combat                                | 0       | 0            | 0    | 1        | 2       | 3          | 4       | 5       | 7       |
| End combat after killing/injuring an ally | 0       | 1            | 2    | 3        | 4       | 5          | 6       | 7       | 8       |
| Low-effort request                        | 0       | 0            | 1    | 2        | 3       | 4          | 5       | 7       | 8       |
| High-effort/Dangerous request             | 0       | 1            | 2    | 3        | 5       | 6          | 7       | 8       | 8       |
| Accept a gift                             | 0       | 0            | 0    | 0        | 0       | 1          | 3       | 4       | 6       |
| Equivalent trade                          | 0       | 0            | 0    | 0        | 0       | 2          | 4       | 6       | 8       |
| Unfavorable trade                         | 0       | 0            | 1    | 2        | 3       | 4          | 5       | 7       | 8       |
| Favorable trade                           | 0       | 0            | 0    | 0        | 0       | 0          | 1       | 5       | 7       |
| Share a secret                            | 0       | 0            | 1    | 2        | 4       | 5          | 6       | 7       | 8       |

Despite the above table, interactions between intelligent `creatures` rarely devolve down to single rolls. Instead, they are more akin to `combat` scenarios where players need to work together and present arguments in order to get the outcome that is most desirable. In these situations, a `negotiation` is held.

## Negotiations

If a `creature` cannot be convinced with a single request, back and forth `negotiation` begins. `Negotiation` begins when the request is initially made, and the `difficulty` starts at the value it would normally be set at for the request. For example, if the party attempts to sway a group of bandits to end combat, they may stop momentarily to hear out the party and begin a `negotiation`, with the `difficulty number` starting at 5.

When a `negotiation` begins, `social actions` are taken in order to influence `morale` and `compassion`, which then subsequently lower or raise the `difficulty`.

> When multiple `creatures` are on the opposing side, they may either defer to a leader and use their `morale` and `compassion`, or the group will have a single `moral` and `compassion` number that is targeted. In the latter case, the highest `morale` and the lowest `compassion` amongst the group is used. At the GMs discretion, individuals can have their own `morale` and `compassion` separate from the group. When the rules make mention of the "opposition", it is referencing to the entire opposing group, whether that is 1 `creature` or many.

`Morale` is the desire of a `creature` to continue to do what they are currently doing. In other words, to double-down on the choice they have already made. If a `creature` has high `morale`, it will be difficult to convince them to change course. However, if their `morale` is broken, they will likely dislike the other after the `negotiation`.

`Compassion` is the sympathy for the plight of others. `Creatures` with high `compassion` are more likely to change their minds to benefit that who they are `compassionate` for. If a `creature` has high `compassion`, they are more likely to like the other after the `negotiation`.

`Actions` during social scenarios affect `morale` and `compassion`. These will have starting values, 1-5. Increasing or decreasing past that range will alter the `difficulty number` and then wrap back around. For example, lowering from 1 wraps to 5 and increasing from 5 wraps to 1. Lowering past 1 is called a `break` and increasing past 5 is called an `overflow`. When `morale` `overflows`, the `difficulty` increases by 1. When `morale` `breaks`, the `difficulty` decreases by 1. The opposite of both is true for `compassion`.

## Social Actions

The `actions` found here are ones that are most applicable during socialization. As a reminder, any `action` can be taken at any time, as long as it applies.

### Appeal to Logic

Tags: Influence

---

You make a logical argument for your position.

`Core`: (`mind`, `knowledge`) - `Mind Difficulty`

-   Lesser Success (-1): `Morale` _and_ `compassion` are reduced by 1
-   Success (0): `Morale` is reduced by 1
-   Greater Success: (1): `Morale` is reduced by 2

### Appeal to Emotion

Tags: Influence

---

You make an emotional plea in support of your position.

`Core`: (`spirit`, `influence`) - `Spirit Difficulty`

-   Lesser Success (-1): `Morale` _and_ `compassion` are increased by 1
-   Success (0): `Compassion` is increased by 1
-   Greater Success: (1): `Compassion` is increased by 2

### Intimidation

Tags: Influence

---

You attempt to strike fear in the opposition.

`Core`: (`body`|`spirit`, `influence`|`knowledge`) - `Morale Difficulty`

-   Lesser Success (-1): `Morale` is reduced by 1, and `compassion` is reduced by 3
-   Success (0): `Morale `is reduced by 2, and `compassion` is reduced by 3
-   Greater Success: (1): `Morale` and `compassion` are reduced by 2, and the opposition gains 1 `stress`

### Active Listening

Tags: Notice

---

You earnestly listen to the plight of the opposition.

`Core`: (`mind`, `notice`) - `Mind Difficulty`

-   Lesser Success (-1): `Compassion` is increased by 1
-   Success (0): `Compassion` is increased by 1, and you gain a point of `boon` on your next `influence` roll against the opposition
-   Greater Success: (1): `Compassion` is increased by 1, and you gain a point of `boon` on your next roll against the opposition

### Offer Gift

Tags: Knowledge

---

You offer something of value (not necessarily monetary) to the opposition.

`Core`: (`mind`|`spirit`, `examination`|`knowledge`) - `Spirit Difficulty`

-   Lesser Success (-1): `Morale` is reduced by 1
-   Success (0): `Compassion` is increased by 1, and `morale` is reduced by 1
-   Greater Success: (1): `Compassion` is increased by 1, and `morale` is reduced by 2

### Observe Custom

Tags: Knowledge

---

You perform a respectful custom for the opposition.

`Core`: (`finesse`, `knowledge`|`examination`) - `Spirit Difficulty`

-   Lesser Success (-1): `Morale` is reduced by 1
-   Success (0): `Morale` is reduced by 1, and you gain a point of `boon` on your next `influence` roll against the opposition
-   Greater Success: (1): `Morale` is reduced by 1, and you gain a point of `boon` on your next roll against the opposition

### Add Context

Tags: Knowledge, Unique

---

You give additional context to an `appeal to logic` `action`, giving the roller a point of `boon`.

### Look Tough

Tags: Influence, Unique

---

You make a show of force or power for an `intimidate` `action`, giving the roller a point of `boon`.

### Grovel

Tags: Influence, Unique

---

You act pathetic and harmless, reducing the efficacy of 1 `compassion` reducing `action` by 1.

### Complement

Tags: Influence, Unique

---

You speak a genuine compliment to the opposition during an `appeal to emotion` `action`, giving the roller a point of `boon`.

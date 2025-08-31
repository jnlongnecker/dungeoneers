# Core Mechanics

## Gameplay Loop

In Dungeoneers, the core gameplay loop remains the same at all times. This ensures that no matter what kind of activities are happening (social intrigue, combat, exploration, etc.), all players know what they can do and how they can interact with each other and the game world. The gameplay loop is simple:

-   Set the `scene`
-   Resolve uncertainties
-   Advance the `scene`
-   Repeat

In more details, the nuance of this loop can be described below:

-   The GM describes the `scene`
-   The players ask any questions they have about the details of the `scene`
-   If other `creature` actors are a part of the scene, they declare their intent
-   The players each make 1 `action`
-   The declared intent resolves
-   Repeat as necessary
-   The `scene` ends

Let's explore the key terminology to gain a fuller understanding of the mechanics.

### Scenes

Think of a `scene` as you would a `scene` in a play. In a `scene`, something is happening for the characters to interact with. The role of the GM is to explain the setup necessary for the `scene` to take place, and the role of the players is to listen to this exposition in order to properly react to it.

> For example, a GM might narrate the passage of several days where certain world events take place, and then explain that the players find themselves in a tavern in a city. The GM may describe the ambiance of the tavern; the gentle firelight tickling their periphery and the scent of booze in the air and on the lips of their companions. This is the GM describing the `scene`.

Not every `scene` is long, and the GM may set a `scene` where nothing ends up happening. When one `scene` ends, the GM sets up another `scene`. The point is for the players to interact and take `actions` (as this is where the game is had!). Once everyone is clear on what the `scene` is like, the GM will then declare the intent of other `creatures` or actors in the `scene`.

### Intent

The "other `creatures` in the `scene`" need a name; they are referred to as non-player characters or NPCs. These can be friends, enemies, neutral parties or otherwise and are simply beings who are not in control by the players.

Before the players make their decisions on which `actions` they would like to take, the intent of the NPCs is declared. This means that the players know what the NPCs are about to do or are planning on doing in advance of taking their turn. In order to determine intent, the GM will either decide on an `action` for the NPC or determine it by rolling.

This looks different depending on what kind of scenario is being played out: `combat`, `social`, or `exploration`. For example, in a `combat` scenario the opposing forces will declare what `action` they are about to take, giving the opportunity for the players to counter. In a `social` scenario, the NPC will make their case or starting position known, and the players can offer a rebuttal or counter argument. In an `exploration` scenario, the "actor" will be the `environment` and any environmental hazards or effects will be sprung, allowing the players to act before resolving. As mentioned, the mechanism by which they do this are `actions`.

### Actions

An `action` is an interaction with the world that moves the `scene` forwards in some way. Some `actions` only make sense for certain situations, such as combat. It is up to the player to determine which `action` is most appropriate for where they are in the `scene`.

The specifics of what `actions` a player can take are covered in the sections where the `action` most applies (e.g., `actions` that harm other `creatures` are covered in the Combat section). Each `action` has `tags` which help identify it in more general categories.

When both the player and the GM have each taken 1 `action`, a `round` has occurred. The amount of time that occurs during a `round` depends on the type of `round` that it was:

-   `combat round`: 6 seconds
-   `exploration round`: Varies; 8 hours - 2 minutes
-   `social round`: Varies; 1 minute - 10 minutes

Once the intent is known, all players may simultaneously take their `action`. They may pass up their `action` (especially during a more casual `scene` where the flow is more freeform) and may choose amongst themselves in what order to go.

## Countdowns

A `countdown` is a ticking clock to represent a duration. There are different `countdowns` to describe different lengths of time:

-   `Rapid countdown` (`RC`): Ticks at the end of a `combat round` or `social round`
-   `Short countdown` (`SC`): Ticks at the end of an `exploration round`
-   `Day countdown` (`DC`): Ticks at the end of a day

Each `countdown` lasts for a specific number of `rounds`, and depending on the `countdown` they will decrement their counter on different types of `round`. When a longer-lasting `countdown` ticks, all shorter-lasting `countdowns` end. A "tick" is simply the decrement of the counter. Each `countdown` will either have a set number of `rounds` _or_ they will have their duration marked by a die number, like 1d6. If the duration is marked by a die number, the duration is determined by rolling the die. Whatever the die lands on is the duration.

> Tip: when representing a `countdown`, it's best to represent it with a physical die. When the `countdown` ticks, simply flip the die to the next number.

A `countdown` will be described in the rules in the following way: _`Countdown`: `SC`(4)_. Let's take a look at an example of `countdown` mechanics in action.

We'll start with `Countdown`: `SC`(1d8). Since it's a die number, we need to roll a d8, or an eight-sided die. Let's say we get a 6 on our roll. This means that our `countdown` is effectively the same as `Countdown`: `SC`(6). Whenever a `combat round` or `social round` completes, the `countdown` ticks. Let's tick our `countdown` first to 5 and then to 4 to represent 2 `rounds` completing. Now imagine our `countdown` is still in effect, but an `exploration round` occurs. This means that even though we had 4 `rounds` left on our `countdown`, the `countdown` immediately completes when the `exploration round` finishes since it's a longer-lasting time frame.

In addition to the three temporal `countdowns`, there is also the `generic countdown:

-   `Generic countdown` (`GC`): Ticks only when specified

All `countdowns` can be additionally ticked when specified; for example the `countdown` associated with the `suffocating` `condition`:

> A `creature` who is `suffocating` starts a `Countdown`: `RC`(`body`). Taking a `wound` or taking an `action` ticks the `countdown` by 1. When the `countdown` ends, the `creature` takes 1 `precision wound` whenever the `countdown` would tick.

Here, a `rapid countdown` is set like most `conditions`, however the `condition` specifies additional criteria that tick the `countdown`. `Generic countdowns` can only be ticked by such "additional criteria".

### Failure Countdowns

In some scenarios (such as crafting items, chases, and skill challenges), a `failure countdown` is used to track failure of subtasks that eventually lead to the failure of the larger task being attempted. `Failure countdowns` are always accompanied by a regular `countdown`, and `failure countdowns` are of the same type of the regular `countdown` (such as `rapid`, `general`, `short`, or `day`). Success on a subtask decrements the regular `countdown`, while failure of a subtask decrements the `failure countdown`.

Scenarios with a `failure countdown` follow the same general outcome rule for any rolls:

-   Failure (-2): The `failure countdown` ticks once, and something bad happens (default is the `failure countdown` ticks again)
-   Partial Success (-1): The `failure countdown` and `countdown` both tick once
-   Success: (0): The `countdown` ticks once
-   Greater Success: (1): The `countdown` ticks once, and something else good happens (default is the `countdown` ticks again)

## Dread

`Dread` is a metacurrency that is gained by the GM to mechanize consequences for player actions. The GM spends `dread` to enhance the abilities of `creatures` that they control in opposition of the players. The GM will gain `dread` from making GM `actions` during `rests`, but they also gain `dread` during `compromises`.

**Why Metacurrency?**

> No other feature in Dungeoneers extends past the "meta" of the game world but `dread`. `Dread` is the solution to two different common issues that are found in these types of games: rolling just under what you needed and the "10 minute adventuring day". Rolling just under your target is handled with the `compromise` mechanic. This is a "meta" choice by the player for a "meta" result, but it's an interesting choice to be made by the player. At the end of the day, Dungeoneers is a game and these kinds of decisions make for an interesting game. It also empowers the GM to make consequences for an earlier decision while still allowing the player to make that roll that they _really_ wanted to.
>
> The second issue of the "10 minute adventuring day" is an issue that arises when the GM isn't running the system in a time-sensitive environment. If there is nothing stopping the party from setting up camp and fully resting between each encounter, it makes for a rather boring game. With `dread`, it ensures that no matter the circumstance around the adventure, there is always a cost to resting.

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
-   If a `spotlight` is necessary, the players collaborate on who will take the `spotlight`
    -   The `spotlit` player makes a `move`
-   The players make 1 `free move`
-   The GM makes a `move`, if applicable
-   Repeat as necessary
-   The `scene` ends

Let's explore the key terminology to gain a fuller understanding of the mechanics.

### Scenes

Think of a `scene` as you would a `scene` in a play. In a `scene`, something is happening for the characters to interact with. The role of the GM is to explain the setup necessary for the `scene` to take place, and the role of the players is to listen to this exposition in order to properly react to it.

> For example, a GM might narrate the passage of several days where certain world events take place, and then explain that the players find themselves in a tavern in a city. The GM may describe the ambiance of the tavern; the gentle firelight tickling their periphery and the scent of booze in the air and on the lips of their companions. This is the GM describing the `scene`.

Not every `scene` is long, and the GM may set a `scene` where nothing ends up happening. When one `scene` ends, the GM sets up another `scene`. The point is for the players to interact and take `moves` (as this is where the game is had!), and in order for a player to make a `move` they must have the `spotlight`.

### Spotlight

The `spotlight` is the focus of attention in a `scene`. This is not to say that other events are not taking place outside of the `spotlight`, but these events are considered inconsequential to the story (e.g. casual eating, restroom breaks, sneezes, coughing). In order for a player to gain the `spotlight`, the following must occur:

-   The players must agree on who gets the `spotlight` (majority consensus, ties/disputes broken by the GM)
-   The player with the `spotlight` must have a `spotlight token`

At the start of the game, each player has 3 `spotlight tokens` to represent the number of times they can take the `spotlight` before needing to take a backseat to allow other players to have the `spotlight`. Every time a player has the `spotlight`, they must use one of their `spotlight tokens`. Players are able to freely exchange `spotlight tokens` amongst each other if they desire. Once all `spotlight tokens` are spent, each player regains their 3 `spotlight tokens`.

> Some tables have no issues with hogging the `spotlight`. If this is your group, feel free to discard the concept of `spotlight tokens`.

The party typically comes to a general consensus on who will take the `spotlight`. Often times, this comes in the form of general agreement on who should take the lead for the task demanded of the `scene`.

> Example: a party with a charismatic talker may opt to give them the `spotlight` for an important political debate.

Once one player has the `spotlight`, they may make their `move`.

### Moves

A `move` is an interaction with the world that moves the `scene` forwards in some way. Some `moves` only make sense for certain situations, such as combat. It is up to the player with the `spotlight` to determine which `move` is most appropriate for where they are in the `scene`.

The specifics of what `moves` a player can take are covered in the sections where the `move` most applies (e.g., `moves` that harm other `creatures` are covered in the Combat section). Each `move` has `tags` which help identify it in more general categories.

When both the player and the GM have each taken 1 `move`, a `round` has occurred. The amount of time that occurs during a `round` depends on the type of `round` that it was:

-   `combat round`: 6 seconds
-   `exploration round`: Varies; 8 hours - 2 minutes
-   `social round`: Varies; 1 minute - 10 minutes

Once a player has determined their `move`, other players may have something they can do to either aid the player with the `spotlight` or set up for their turn in the `spotlight`: a `free move`.

### Free Moves

Some interactions with the world don't necessarily move the `scene` forward, but are important as they set up proper context for a future `move`. These are captured with `free moves`. A player can make a single `free move` before, after, or in tandem with the player with the `spotlight` and their `move`. `Creatures` under the GMs control may also make `free moves` after the GM completes their `move`.

## Countdowns

A `countdown` is a ticking clock to represent a duration. There are different `countdowns` to describe different lengths of time:

-   `Rapid countdown` (`RC`): Ticks at the end of a `combat round` or `social round`
-   `Short countdown` (`SC`): Ticks at the end of an `exploration round`
-   `Day countdown` (`DC`): Ticks at the end of a day

Each `countdown` lasts for a specific number of `rounds`, and depending on the `countdown` they will decrement their counter on different types of `round`. When a longer-lasting `countdown` ticks, all shorter-lasting `countdowns` end. A "tick" is simply the decrement of the counter. Each `countdown` will either have a set number of `rounds` _or_ they will have their duration marked by a die number, like 1d6. If the duration is marked by a die number, the duration is determined by rolling the die. Whatever the die lands on is the duration.

> Tip: when representing a `countdown`, it's best to represent it with a physical die. When the `countdown` ticks, simply flip the die to the next number.

A `countdown` will be described in the rules in the following way: _`Countdown`: `SC`(4)_. Let's take a look at an example of `countdown` mechanics in action.

We'll start with `Countdown`: `SC`(1d8). Since it's a die number, we need to roll a d8, or an eight-sided die. Let's say we get a 6 on our roll. This means that our `countdown` is effectively the same as `Countdown`: `SC`(6). Whenever a `combat round` or `social round` completes, the `countdown` ticks. Let's tick our `countdown` first to 5 and then to 4 to represent 2 `rounds` completing. Now imagine our `countdown` is still in effect, but an `exploration round` occurs. This means that even though we had 4 `rounds` left on our `countdown`, the `countdown` immediately completes when the `exploration round` finishes since it's a longer-lasting time frame.

## Dread

`Dread` is a metacurrency that is gained by the GM to mechanize consequences for player actions. The GM spends `dread` to enhance the abilities of `creatures` that they control in opposition of the players. The GM will gain `dread` from making GM `moves` during `rests`, but they also gain `dread` during `compromises`.

**Why Metacurrency?**

> No other feature in Dungeoneers extends past the "meta" of the game world but `dread`. `Dread` is the solution to two different common issues that are found in these types of games: rolling just under what you needed and the "10 minute adventuring day". Rolling just under your target is handled with the `compromise` mechanic. This is a "meta" choice by the player for a "meta" result, but it's an interesting choice to be made by the player. At the end of the day, Dungeoneers is a game and these kinds of decisions make for an interesting game. It also empowers the GM to make consequences for an earlier decision while still allowing the player to make that roll that they _really_ wanted to.
>
> The second issue of the "10 minute adventuring day" is an issue that arises when the GM isn't running the system in a time-sensitive environment. If there is nothing stopping the party from setting up camp and fully resting between each encounter, it makes for a rather boring game. With `dread`, it ensures that no matter the circumstance around the adventure, there is always a cost to resting.

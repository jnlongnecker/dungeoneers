# Dungeoneers

On this repository you can find the manual and supplemental tools for Dungeoneers. In this document, we'll talk about what Dungeoneers is and the philosophy behind its creation.

## What is Dungeoneers?

Dungeoneers is two things: a TableTop Role Playing Game (TTRPG) and a video game. In this repository, you won't find the source code to the video game, only the rules for the TTRPG. The central design philosophy behind the rules you'll find here are that they (in general) need to work in both a video game context _and_ a TTRPG context. A central allure of TTRPG games is the freedom that you have in them, so hearing this may initially seem like a debilitating restriction. However, we believe that restrictions make for _better_ and _more_ interesting games due to the creativity that they force; as long as the restrictions are reasonable.

A lot of TTRPGs/TTRPG systems try to be or do too much. Infinite possibilities, infinite customization, any setting, any genre... if you try and do it all, you stretch yourself too thin. We all know the best restaurants tend to have smaller menus. If you want the best of the best, you go to a specialist. This is the philosophy Dungeoneers takes on; Dungeoneers is a game about exploring dungeons. More aptly, it's about the _people_ that find themselves exploring dungeons; these people being named the titular "dungeoneers".

## Balancing and Tools

When designing rules for Dungeoneers, the dual context for the game introduces both challenges and insights. In most RPG video games, the computer does all of the heavy lifting in terms of calculations. The player simply presses the button and the consequences are calculated with perfect precision in the blink of an eye. While this is very convenient, this convenience can itself be a source of pain in terms of design. Let's take a real-life example of an RPG video game: Fire Emblem. In particular, we can look at Fire Emblem 8: Sacred Stones (FE8).

FE8 is on the more conservative end of calculation for an RPG video game. Damage is a simple formula: `strength + weapon might + weapon triangle - enemy defense` for physical weapons and `magic + tome might + weapon triangle - enemy resistance` for magical weapons. This is not very challenging to calculate and allows the player to make well-informed decisions on the impact of the `strength`, `magic`, `resistance`, and `defense` stats as well as if combat were to be held between two combatants. However, if we take a look at the accompanying system to damage in FE8, hit rate, then we run into a bit of an issue.

In FE8, a unit's chance to hit is given by the following formula: `weapon hit + 2 * skill + 0.5 * luck + weapon triangle + S rank bonus`. From this number, the defending unit's dodge rate (another similarly complex formula) is subtracted for a percentage. The game then rolls 2 random numbers, takes the average and compares the result to the result of the hit rate - dodge rate. Whew! Imagine trying to simulate such a complicated formula in a tabletop setting; it'll never happen. There are a few problems with this design:

1. The impact of stats is not as apparent
2. There are many factors at play
3. It is difficult to understand (mostly because of #2)
4. The "true" result is obfuscated by the 2 random number (2RN) system

Now, the 2RN system typically works in the benefit of the player and better aligns with how humans perceive probability as it gives percentages above 50% a higher chance of success than listed and percentages below 50% a lower chance of success than listed. Typically, enemies will have below 50% hit and players will have above 50% hit. Players also expect a better than 50% chance to work all the time and below 50% to never work. These terms (all the time, never) are a bit hyperbole, but humans expect these results to skew more than they realistically do and aren't really capable of observing these percentages in the bigger picture. Usually, only the last 5 or so results are in mind, so if a player misses two 80% chances back-to-back, they'll feel cheated even if the last 20 80% chances all hit.

As mentioned, Fire Emblem is one of the least sinful implementations of calculation in RPGs. We could spend weeks going over all the silly, overly complex systems of video games that lean far too heavily into the power of computers to come up with complicated formulas for basic functions the player will be doing over and over again. If the game doesn't really have any strategy in the numbers except for big number = good, then these complex formulas can be excused as it doesn't really benefit the player to understand the complexity. There are some lessons to be learned though, and they're put in place in Dungeoneers.

The first lesson is that humans are very bad at intuiting statistics. In virtually every RPG video game, there are percentages galore (especially Strategy RPGs). However, somehow TTRPGs work without using a single percent sign! Well, not quite "somehow"; they work by using the inherent probability in dice. Even though statistics are still in play with dice, there are a couple advantages:

-   "Success" exists in a variety of ranges, and these ranges can be felt
    -   Getting above the necessary threshold feels good
    -   Just barely making the threshold exciting in its own, different way
-   Rolling dice makes it feel like the player owns the action and has agency
-   The true statistics are obfuscated, but in a positive way
    -   Dice chance is better "felt"

Players are much more content with chances with dice rather than rolling a random number 0-100 because they don't _see_ the underlying 80% chance or the underlying 20% chance, despite it still being there.

In the section where FE8 hit chance was analyzed, it may seem like it was being disparaged as poorly designed or "bad". However, the real problem is the lack of connection between the mechanics at play/the result and the player. It's well-designed because when the player sees their 80% hit, the results more or less fall in line with what they expect. The problem is how the 80% is calculated and, more importantly, the fact that they player sees the 80% _at all_. The problems with statistics all begin when the player can see their chance out of 100 since that's when the human brain starts misinterpreting what that means.

The second lesson is that complex formulas, curves or distributions are not actually the problem, the problem is when they cannot be intuited from the mechanics at play. This math is actually a very powerful balancing tool: by tweaking the formulas underneath various mechanics you can better balance your game. The trick is hiding the math from the player but also exposing enough of it for them to be able to understand how mechanics benefit them.

We can take a simple example: Let's say you want your game to have 5 battles before the players heal back to full. You need to balance things so that the player can achieve this. If we use a typical system with hitpoints, we can calculate the average damage a player deals and takes to certain enemies. Let's say our player has 50 hitpoints and fights skeletons only. Skeletons have 10 hitpoints and can do 5 damage per turn on average to our player. Our player can do 10 damage per turn on average. If we have battles with 2 skeletons each, we can reasonably expect our player to be able to take on 5-10 battles before needing to heal to full. We can tweak the underlying math here to reach our target and adjust the enemies in our battles.

Dice help greatly to this end. The mathematics behind dice statistics can get pretty tricky, but the nice thing is that the intuition humans have about statistics line up pretty well with dice statistics. The simplicity of throwing dice obscures all the nasty percentages at the heart of the act. Comparing dice totals against each other gives you different math than comparing a dice total at a static number, and these values all change again when you add up dice with different sides. Despite all this, it follows the simple pattern of big number = good: 2d6 rolls better than 2d4 because bigger number. 3d6 rolls better than 2d6 because bigger number. Here's a tricky one: what's the chance 2d6 rolls better than or meets 3d4? Our rule of bigger number = win doesn't quite work, because each side has a bigger number in some respect. The answer may be surprising: a perfect 50%. Of course, not all relationships between each side having a slightly bigger number on both sides end up like this, but the uncertainty in the prediction reveals the truth of the underlying math.

The third lesson is that while complex formulas are great for balance, they don't work in TTRPGs because the math is done by the player. Not only is it just not feasible for players to be capable of calculating some of the more complicated formulas you can find in video games in their heads (or even by hand with pen and paper), but it's also not much fun for the general public. As you increase complexity and math necessary to play, you start to restrict your audience and general appeal.

The solution once again is to reach for dice. If all the math works by adding up dice faces and comparing results to other dice face additions (or better yet, static numbers) then this is easy enough for people to be expected to do on the fly and in their heads. Better yet, people _love_ rolling big numbers, and more dice give more opportunities for big numbers to occur. Lets imagine our 2d6 vs 3d4 example from before; each side has a 50% chance of success. However, for both rollers it doesn't _feel_ like they are flipping a coin. Both side feels in control of their result and there is triumph in rolling 12 vs 9 _and_ triumph in rolling 4 vs 3 but both successes feel wildly different. Best of all, each side only had to add up 2-3 numbers between 1-6!

## Rules Philosophy

In many TTRPGs, there are 3 core components or "scenes" to the game, most commonly referred to as pillars of gameplay. These 3 pillars are usually the following; in some variation and no particular order:

-   Combat
-   Exploration
-   Socialization

Additionally, many TTRPG systems can be categorized based on the amount of rules they have; systems can be rules-light or rules-heavy (also referred to as "crunchy"). Dungeoneers is a rules-heavy system that follows the typical 3 pillars of gameplay.

Some may have an intrinsic "weight" attached to not only a certain amount of rules but also systems that favor (or _don't_ favor) a particular pillar of gameplay. Just because Dungeoneers has chosen to be a rules-heavy system does _not_ mean it's because we believe rules-heavy systems are superior; in fact these systems can absolutely benefit from taking inspiration from rules-light systems. We believe it's important to identify what kind of system that is attempting to be made as not to create a rules-heavy system that attempts to masquerade as a rules-light system and wear the label proudly. This lets players make better-informed decisions about whether or not they will like the game before committing to reading the words necessary to understand the game.

Of the 3 pillars, Dungeoneers focuses on the combat pillar. As a rules-heavy system, however, we believe that it is important to still have rules for the other 2 pillars. The intention here is not to require DMs and players to have to learn more rules and "complicate" these parts of the game. Instead, it is there to give guidance, structure, and (most importantly) _power_ in the hands of the players to say that there are certain things they absolutely can do.

If a game table feels that these rules get in the way of role play or "bogs down" the game, then these rules by all means should be ignored. These rules have a secondary purpose, however, and this secondary purpose is married to the reason Dungeoneers chooses to be a rules-heavy system that focuses on combat: Dungeoneers is also a video game.

Unfortunately (or fortunately, depending on who you ask), computers can not yet perform tasks of imagination and improvise to the same degree as a human can. In the context of a video game, everything that the player _can_ do has to be well-defined or else the player simply cannot do it.

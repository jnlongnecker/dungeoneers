# Dungeoneering

The rules covered elsewhere are most of everything one will need in order to play Dungeoneers. The rules found here cover some edge cases about moving through and interacting with the world in various ways, as well as giving some perspective of play.

## Space and Travel

When measuring out space, Dungeoneers is less concerned with specific measurements like meters and feet. These terms give a visualization, but the preferred way to play is with a map at all times. This is not to say that everything will be visualized with precision down to the inch, only that space is abstracted via the concept of tiles at various levels of detail.

### Levels of Detail

There are 3 levels of detail that maps in Dungeoneers observe:

1. Battle Map (Combat, Social)
2. Room Map (Social, Exploration)
3. Environment Map (Exploration)

In each level of detail, the map will be divided into "tiles", which are the singular unit of space for that level of detail. Various `actions` and `free actions` will make reference to tiles; the size of the tile corresponding to the type of `action` that it is. For example, `combat actions` referencing tiles mean the ones used in the Battle Map level of detail, while `exploration actions` referencing tiles mean either a tile of the Room Map size or the Environment Map size (whichever is currently in use).

### Tiles

Tiles are not meant to represent strict distances, they're meant to break up a space into tactically meaningful divisions. It's therefore not advised to break out a tile into feet or meters or kilometers or miles or any other unit of measure you decide on. After all, the goal is not to do trigonometry in order to figure out if you're in range of something. As such, when calling out movement along a number of tiles an ordinal direction (diagonal) is equally valid as a cardinal direction for a single tile.

This gets a little tricky when you involve the vertical axis. Such times should only be meaningful in combat situations or in exploration at the Room Map level, so the distances should not be that great. Here's the rule: if you are above your target, the range in tiles increases by the number of tiles you are above your target. If you are below your target, your range in tiles decreases by the number of tiles you are below your target. From there, you simply ignore the verticality.

> Example: Freya is on an elevated cliff overlooking the battlefield that is 2 tiles in height. If she makes a `strike` using a missile weapon at something below her, her range increases by 2 tiles. A skeleton on the battlefield trying to shoot back at with a missile weapon of its own has its range _decreased_ by 2 tiles. If the skeleton and Freya both have a range of 10 tiles with their missile weapons and they're both 10 tiles away, Freya can hit the skeleton but it can't hit her back!

### Line of Sight

There are times when the ability to see a `creature` comes into question due to angles of the terrain and obstacles. In order to determine what you do or don't have line of sight to, draw a line from the center of your tile to the center of the tile you're trying to see, as well as each tile adjacent. If every line intersects an obstacle, you do not have line of sight to the tile at all. If the line between yourself and the tile you're trying to see does not intersect an obstacle, you have complete line of sight to the target. If neither of the above are true, then you have partial line of sight to the target.

When you have no line of sight to the target tile, any `creature` there is `hidden` from you. When you have partial line of sight to the target, any `creature` there is `shrouded` to you. When performing this line of sight check, you can alternatively use a tile adjacent to yourself as the tile "you" are in. This is useful in situations where you are, for example, taking cover behind a wall and "peeking out" to do something in order to keep yourself out of line of sight from your target while keeping them within line of sight of you.

## Inventory

In Dungeoneers, carrying things is more abstract than manually tracking the individual weight and size of everything you are carrying. Instead, a dungeoneer has a baseline set of 20 inventory slots in which items can be carried. Items that can fit within a closed fist can be stored with similar items in the same slot (called a "stack"), and items that are too large to fit in a bag cannot be carried in a dungeoneers' inventory.

For example, a potion is too large to stack since it can't fit entirely within a closed fist. However, a gold piece _is_ small enough to fit in a closed fist so it can be stacked.

Some equipment exists which is used to increase available inventory slots; 20 is simply the baseline. Additionally, anything you currently have equipped does not take up room in your inventory. As long as you do not exceed the inventory slots available, there is no limit to the weight that can be carried. However, equipment that is able to contain other items must be empty if you wish to store it in an inventory slot.

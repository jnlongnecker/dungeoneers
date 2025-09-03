# Equipment

There are a variety of `items` that can be worn on your person; these `items` are called `equipment`. For a piece of `equipment` to serve proper benefit, it must be properly equipped. As a dungeoneer, you have the following `equipment slots` to wear `equipment`:

- Head
- Neck
- Body
- Back
- Hands
- Ring
- Ring
- Wield
- Wield
- Belt
- Feet

Every piece of `equipment` specifies which `equipment slot` it occupies and how many. If you do not have an unoccupied `equipment slot` for a piece of `equipment`, you cannot properly equip it and gain its benefits.

## Weapons

`Weapons` are tools to deal physical trauma to something. These are swords, maces, axes, hammers, spears, bows, and the like. `Weapons` are divided into categories that determine their strength, `equipment slots` and more. Use your imagination to fill out the details of your `weapon` and customize its appearance as you see fit.

| Weapon Type | Damage | Stat  | Equipment Slots | Range | Examples                                           |
| ----------- | ------ | ----- | --------------- | ----- | -------------------------------------------------- |
| Light       | 2      | Skill | 1x wield        | 1     | a dagger, a handaxe, a light hammer, a javelin     |
| Standard    | 3      | Power | 1x wield        | 1     | a broadsword, a battleaxe, a maul, a spear         |
| Control     | 3      | Power | 2x wield        | 2     | a zweihander, a bardiche, a polehammer, a partisan |
| Heavy       | 4      | Power | 2x wield        | 1     | a longsword, a broadaxe, a lever mace, a glaive    |
| Missile     | 2      | Skill | 2x wield        | 4     | a sling, a crossbow, a longbow                     |

## Armor

`Armor` is clothing built to protect the wearer from harm. `Armor` is divided into categories in a similar way as `weapons`; again, use your imagination to fill out the details of your `armor` and customize its appearance as you see fit.

| Armor Type | Physical Resistance | Arcane Resistance | Equipment Slots | Examples                                    |
| ---------- | ------------------- | ----------------- | --------------- | ------------------------------------------- |
| Light      | 0                   | 2                 | Body            | studded leather armor, boiled leather armor |
| Medium     | 1                   | 1                 | Body            | brigandine armor, chain armor               |
| Heavy      | 2                   | 0                 | Body            | plate mail, heavy chain armor               |
| Shield     | 1                   | 1                 | 1x wield        | kite shield, round shield                   |

### Physical and Arcane Resistance

Whenever a `creature` is struck by damage, `physical resistance` or `arcane resistance` will lessen the impact. First, reduce the damage by the corresponding resistance (`physical damage` is reduced by `physical resistance`, and `arcane damage` is reduced by `arcane resistance`). For the leftover damage, this is taken as normal. Additionally, roll 1d6: if the result is less than the leftover damage, the corresponding resistance is `broken` and must be repaired. While `broken`, treat that resistance as if it were 0.

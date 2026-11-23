# West of Loathing

West of Loathing Archipelago (WOLAP) integrates West of Loathing with the Archipelago multiworld randomizer.
Players can find items belonging to other players while receiving their own items from locations throughout the
multiworld.

## Where is the options page?

The [player options page for this game](../player-options) contains all the options you need to configure and export a
config file.

Players using a locally installed APWorld can also generate a YAML template through the Archipelago Launcher.

## What does randomization do to this game?

WOLAP randomizes the majority of unique items and rewards throughout West of Loathing.

Items normally obtained through exploration, quests, shops, and other activities are replaced by Archipelago
location checks. Completing a location check sends its assigned item to the appropriate player in the multiworld.

Progression items from West of Loathing can appear in other players' games, while items belonging to other players
can be found throughout the West.

The *Reckonin' at Gun Manor* DLC is also supported as an optional part of the randomization.

## What is considered a location check in West of Loathing?

Location checks include:

- Unique item pickups throughout the world
- Quest rewards and objectives
- Shop purchases
- Certain combat encounters and enemy drops
- Crafting and exploration rewards
- Interactions with objects throughout the game

Several optional YAML settings add or remove categories of location checks.

## What items can appear in other players' worlds?

Most randomized items can be placed in another player's world.

These include:

- Weapons, hats, boots, pants, and accessories
- Quest items and progression items
- Skillbooks and abilities
- Tools and crafting-related items
- Consumables and other useful equipment

Certain items unlock new regions, activities, or quest progression. Players may need to receive these items
before continuing parts of their adventure.

Not all vanilla items are randomized. Most repeatable loot, unlimited shop inventory, and Foragin' plants
remain outside the randomization.

## When the player receives an item, what happens?

When the player recieves an item from the server, if the game is in a grantable state it will pop a notification in the
top left corner of the screen. This notification will show a picture of the item recieved and the name of the item.

## What is different from the vanilla game?

WOLAP changes several mechanics to make West of Loathing compatible with randomized progression.

Some notable changes include:

- The Boring Springs tutorial is skipped through an adjusted starting sequence.
- Many class-specific restrictions have been removed or modified.
- Skillbooks and abilities can be obtained independently of the player's starting class.
- Several quests have adjusted requirements to support randomized item acquisition.
- Certain normally missable checks have alternate methods of completion.
- Missed checks can be recovered through Lloyd at The Jewel Saloon.
- Some progression items appearing in randomized shops can generate Archipelago hints.

For more information, see the
[WOLAP mechanical and logic changes](https://github.com/TylerJG92/WOLAP/blob/main/docs/changelist.md).

## Where can I find more information?

Visit the [WOLAP GitHub repository](https://github.com/TylerJG92/WOLAP) for releases, installation instructions,
troubleshooting, and bug reporting.

Players can also discuss WOLAP in the West of Loathing thread of the Archipelago Discord.
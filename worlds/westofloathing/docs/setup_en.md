# West of Loathing Randomizer Setup Guide

This guide explains how to install West of Loathing Archipelago (WOLAP), configure a multiworld, and connect to an
Archipelago server.

## Required software

To play West of Loathing with Archipelago, you need:

- [West of Loathing](https://store.steampowered.com/app/597220/West_of_Loathing/)
- [WOLAP Client Mod](https://github.com/TylerJG92/WOLAP/releases)
- The required WOLAP dependencies, including BepInEx

The *Reckonin' at Gun Manor* DLC is required only when enabling its associated randomization option.

## Optional Software
- Archipelago from the [Archipelago Releases Page](https://github.com/ArchipelagoMW/Archipelago/releases)
    * This provides access to various built-in tools, text client, and local generation and hosting
- [Universal Tracker](https://github.com/FarisTheAncient/Archipelago/releases?q=Tracker)
    * If you installed Archipelago, you can use the Universal Tracker to see what you checks you still have!

## Installing the Archipelago mod

WOLAP can be installed through a mod manager or manually, depending on your operating system.

### Windows installation

Supported installation methods include:

- Thunderstore Mod Manager
- r2modman
- Manual installation

For instructions, see the
[WOLAP Windows installation guide](https://github.com/TylerJG92/WOLAP/blob/main/docs/installation-windows.md).

### Linux installation

WOLAP can be installed using r2modman with the Windows version of West of Loathing running through Steam Proton.

Manual installation with the native Linux version is also documented, but has not been fully verified.

For details, see the
[WOLAP Linux installation guide](https://github.com/TylerJG92/WOLAP/blob/main/docs/installation-linux.md).

### macOS installation

WOLAP supports a manual installation procedure using BepInEx. Some aspects of this installation are still
undergoing verification.

For instructions, see the
[WOLAP macOS installation guide](https://github.com/TylerJG92/WOLAP/blob/main/docs/installation-macos.md).

After completing installation, launch West of Loathing and confirm that WOLAP loads successfully.

## Configuring your YAML file

### What is a YAML and why do I need one?

A YAML file defines the settings for your player slot in an Archipelago multiworld.

It controls which randomization features are enabled and other options affecting your game.

For more information, see Archipelago's
[Basic Multiworld Setup Guide](/tutorial/Archipelago/setup/en).

### Where do I get a YAML?

If the West of Loathing options page is available on your Archipelago host, you can configure and export a
YAML file there.

Alternatively, you can generate a YAML template locally:

1. Install a compatible West of Loathing APWorld.
2. Open the Archipelago Launcher.
3. Select **Generate Template Options**.
4. Find the West of Loathing YAML template in `Players/Templates`.
5. Customize the options as desired.

If another player is hosting your multiworld, send them your completed YAML before generation.

## Installing the West of Loathing APWorld

The APWorld is used by Archipelago to generate West of Loathing's randomized items, locations, and
progression logic.

If you are generating a seed locally:

1. Download a compatible `westofloathing.apworld` from the
   [WOLAP releases page](https://github.com/TylerJG92/WOLAP/releases).
2. Open the Archipelago Launcher.
3. Select **Install APWorld**.
4. Select the downloaded file.
5. Generate your seed using your configured YAML.

The APWorld and WOLAP client versions should be compatible. Check the release notes before mixing versions.

**Note:** Players joining an already-generated multiworld generally do not need the APWorld installed to run
the WOLAP client.

## Joining a multiworld game

Once the multiworld has been generated and the Archipelago server is running:

1. Launch West of Loathing with WOLAP enabled.
2. Open WOLAP's Archipelago connection interface.
3. Enter the server address and port.
4. Enter your player slot name exactly as it appears in the multiworld.
5. Enter the password if the server requires one.
6. Connect to the server and begin your game.

Your server address, port, and slot name must match the information provided by the host.

**Important:** When switching between different multiworlds, verify your connection details before loading
your game. Connecting to the wrong server or slot can cause unexpected progression behavior.

## Playing West of Loathing with Archipelago

WOLAP modifies the opening sequence to skip the Boring Springs tutorial.

As you progress, completing location checks sends items through the Archipelago server.

You may receive your own items or items belonging to other players. Some regions and quests may require
progression items that have been placed elsewhere in the multiworld.

Certain missed checks can be recovered from Lloyd at The Jewel Saloon.

## Updating WOLAP

The WOLAP client and West of Loathing APWorld are separate components and may be updated independently.

Some updates are compatible with existing games, while others require generating a new seed.

Before updating, consult the release notes and the
[WOLAP updating guide](https://github.com/TylerJG92/WOLAP/blob/main/docs/updating.md).

## Troubleshooting

If WOLAP fails to load or connect, first verify:

- The mod and its dependencies are correctly installed.
- The Archipelago server is available.
- Your server address and port are correct.
- Your slot name matches the generated multiworld.
- Your installed versions are compatible.

For further assistance, see the
[WOLAP troubleshooting guide](https://github.com/TylerJG92/WOLAP/blob/main/docs/troubleshooting.md).

Bugs and other issues can be reported through the
[WOLAP GitHub Issues page](https://github.com/TylerJG92/WOLAP/issues) or discussed in the Archipelago Discord.
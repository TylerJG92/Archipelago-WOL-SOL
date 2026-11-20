from dataclasses import dataclass
from typing import Dict, Any
from Options import (DefaultOnToggle, Toggle, StartInventoryPool, Choice, Range, TextChoice, PlandoConnections,
                     PerGameCommonOptions, OptionGroup, Visibility)

class EnableDLC(Toggle):
    """
    To use this option, you must own the "Reckonin' at Gun Manor" DLC.
    """
    internal_name = "dlc_enabled"
    display_name = "Gun Manor DLC Enabled"

class RandomizeGunManorCoach(Toggle):
    """
    Randomize the coach to access Gun Manor into the item pool.
    This has no effect if the Gun Manor DLC is disabled.
    """
    internal_name = "randomize_ghost_coach"
    display_name = "Randomize Gun Manor Coach"

class RandomizeGoblintongue(DefaultOnToggle):
    """
    Randomize the ability to speak Goblintongue into the item pool.
    If this is disabled, you will always be able to speak Goblintongue from the start.
    """
    internal_name = "randomize_goblintongue"
    display_name = "Randomize Goblintongue"

class WanderSanity(DefaultOnToggle):
    """
    Originally called "Random Event"
    Enables single event Random Encounters, in each region, while wandering to contain Check Locations.
    If disabled these events will contain their normal items instead of them being randomized into the pool.
    Note: Some items need to remain in the randomizer, If disabled the items that remain will be replaced with Meat instead.
    """
    internal_name = "wander_sanity"
    display_name = "Wander Sanity"

class CrateSanity(DefaultOnToggle):
    """
    Originally called "Progressive Loot"
    Enables checks to be located in a variety of crates located throught the game.
    Crates include: Ranch crates, Grave crates, Medical crates and El Vibrato Crates.
    If disabled these crates will contain their original or adjacent items to the vanilla game. Special items only will be excluded from the randomize pool.
    Note: Some items need to remain in the randomizer, If disabled the items that remain will be replaced with Meat instead.
    """
    internal_name = "crate_sanity"
    display_name = "Crate Sanity"

class HaystackSanity(DefaultOnToggle):
    """
    Enables check locations to be placed inside each haystack within the game.
    If disabled, the check location will be turned off only.
    """
    internal_name = "haystack_sanity"
    display_name = "Haystack Sanity"

class UnbreakableTools(Toggle):
    """
    Makes it impossible for shovels and pickaxes to break in certain circumstances.
    If this is disabled, additional tools will be available for purchase if yours breaks.
    """
    internal_name = "unbreakable_tools"
    display_name = "Unbreakable Tools"

class Deathlink(Toggle):
    """
    Allows for the sending and recieving of Deathlink packets:
    Recieving: The players character gains the Angry effect.
    Sending: Whenever the player fails a combat, gives up in combat and certain special death events will send a deathlink.

    Note: Can be toggled on or off within the Escape menu in game at any time.
    """
    internal_name = "deathlink_enabled"
    display_name = "Deathlink"

@dataclass
class WOLOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool

    dlc_enabled: EnableDLC
    randomize_ghost_coach: RandomizeGunManorCoach
    randomize_goblintongue: RandomizeGoblintongue
    wander_sanity: WanderSanity
    crate_sanity: CrateSanity
    haystack_sanity: HaystackSanity
    unbreakable_tools: UnbreakableTools
    deathlink_enabled: Deathlink

wol_option_groups = [
    OptionGroup("Sanity Options", [
        WanderSanity,
        CrateSanity,
        HaystackSanity
    ]),

    OptionGroup("DLC Options", [
            EnableDLC,
            RandomizeGunManorCoach
        ], True),
]

wol_option_presets: Dict[str, Dict[str, Any]] = {
    
}
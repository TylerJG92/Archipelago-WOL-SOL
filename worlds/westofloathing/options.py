from dataclasses import dataclass
from typing import Dict, Any
from Options import (DefaultOnToggle, Toggle, StartInventoryPool, Choice, Range, TextChoice, PlandoConnections,
                     PerGameCommonOptions, OptionGroup, Visibility)

class EnableDLC(Toggle):
    """
    To use this option, you MUST own the "Reckonin' at Gun Manor" DLC.
    Disabling this option does disable the DLC even if you have it 
    installed.
    """
    internal_name = "dlc_enabled"
    display_name = "Gun Manor DLC Randomization Enabled"

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

class Horse(Choice):
    """
    Choice of horse effects the game in interesting ways, please select your horse here.
    Normal Horse: Dosent change the game in any way.
    Pale Horse: Adds random Undead and Nex-Mex Book encounters (Good for Vanilla completion on NexMex Bridge Option.)
    Dark Horse: Adds options to run from most random encounters without consequences.
    Crazy Horse: More likely to trigger Random Events and locate locations faster while "Wanderin"
    """
    internal_name = "horse_selection"
    display_name = "Yer Horse"
    option_normal_horse = 1
    option_pale_horse = 2
    option_dark_horse = 3
    option_crazy_horse = 4
    default = option_normal_horse

class BridgeMethodElVibrato(DefaultOnToggle):
    """
    This option if enabled will allow the "El Vibrato Model Bridge" to remain in the item randomized pool.
    If dissabled the item will be removed from the pool and thus you cannot use this option to progress to Frisco with.

    Note: At least 1 Bridge Method option must be selected.
    """
    internal_name = "el_vib_bridge_enabled"
    display_name = "Bridge Method: El Vibrato Model Bridge"

class BridgeMethodNecro(DefaultOnToggle):
    """
    This option if enabled will allow the collection of 4 NexMex books and being able to get the Unlimited Bones perk from
    the Buffalo Bone Pile to be used to create the bridge to Frisco.
    Disabling this option will not remove the NexMex books from randomization, only the ability to build the bridge with
    them. It will also turn the items from Progressive to Useful in the randomzed pool.

    Note: At least 1 Bridge Method option must be selected.
    """
    internal_name = "necro_bridge_enabled"
    display_name = "Bridge Method: NexMex Bone Bridge"

class BridgeMethodBreadwood(DefaultOnToggle):
    """
    This option if enabled will allow the completion of 5 quests for Breadwood to be able to have them build the bridge
    to Frisco.
    Disabling this option will not remove the items or quests from the game, just the ability to build the bridge.

    Note: At least 1 Bridge Method option must be selected.
    """
    internal_name = "breadwood_bridge_enabled"
    display_name = "Bridge Method: Breadwood Lumber Bridge"

class BridgeMethodQuest(Toggle):
    """
    If enabled this option augments the Bridge Method(s) to require the player to also reach their normal vanilla completion
    places.

    Bridge Method: El Vibrato Model Bridge will require the player be able to reach the check location 
    "El Vibrato Construction Facility (Curious Copse) - HOSOM NOAN NOFU" to be able to also build the bridge

    Bridge Method: NexMex Bone Bridge will require the player to be able to reach the bone pile and at least 4 locations
    where they could have gotten NexMex books.

    Bridge Method: Breadwood Lumber Bridge will require the player to be able to reach the end of 5 questlines for breadwood 
    to consider the bridge buildable 
    """
    internal_name = "bridge_quest_enabled"
    display_name = "Require Vanilla Completions to build Bridge?"

class AllBreadwoodQuests(Toggle):
    """
    If enabled this option augments "Bridge Method: Breadwood Lumber Bridge" further to include all 7 Breadwood Quests
    to build the Lumber Bridge

    This requires both "Bridge Method: Breadwood Lumber Bridge" and "Bridge Method: Breadwood Lumber Bridge" options
    enabled to have any effect.
    """
    internal_name = "all_breadwood_quests"
    display_name = "(Breadwood Lumber Bridge Vanilla) Increase number of Breadwood quests?"

class NortonMethodCElVib(DefaultOnToggle):
    """
    If enabled this option allows the item "El Vibrato Crown" to be added to the loot needed to complete the game.

    If disabled, the Crown will not be removed from the Randomized pool, but will change from Progressive to Useful
    and no longer be usable to give to Norton.

    Note: At least 1 option must be selected.
    """
    internal_name = "el_crown_enabled"
    display_name = "Norton Method: El Vibrato Crown"

class NortonMethodCNecro(DefaultOnToggle):
    """
    If enabled this option allows the item "The Necromancer's Crown" to be added to the loot needed to complete the game.

    If disabled, the Crown will be removed from the Randomized pool and will not be useable to give to Norton for game
    completion.

    Note: At least 1 option must be selected.
    """
    internal_name = "necro_crown_enabled"
    display_name = "Norton Method: The Necromancer's Crown"

class NortonMethodCGoldTooth(DefaultOnToggle):
    """
    If enabled this option allows the item "Gold Tooth Crown" to be added to the loot needed to complete the game.

    If disabled, the Crown will not be removed from the Randomized pool, but will change from Progressive to Useful
    and no longer be usable to give to Norton.

    Note: At least 1 option must be selected.
    """
    internal_name = "gold_crown_enabled"
    display_name = "Norton Method: Gold Tooth Crown"

class NortonMethodCTurnip(DefaultOnToggle):
    """
    If enabled this option allows the item "Turnip Crown" to be added to the loot needed to complete the game. 

    If disabled, the Crown will not be removed from the Randomized pool, but will change from Progressive to Useful
    and no longer be usable to give to Norton.

    Note: At least 1 option must be selected.
    """
    internal_name = "turnip_crown_enabled"
    display_name = "Norton Method: Turnip Crown"

class NortonMethodHoneyBean(DefaultOnToggle):
    """
    If enabled this option allows the item "Honey Jelly Bean" to be added to the loot needed to complete the game. 
    Additionally the player will need to be aware they will have to complete the Train Heist quest before completion.

    If disabled, the Honey Jelly Bean will be removed from the Randomized pool and the Train Heist quest will not be
    an option for the end of the game.

    Note: At least 1 option must be selected.
    """
    internal_name = "honey_jellybean_enabled"
    display_name = "Norton Method: Honey Jelly Bean"

class NortonMethodQuest(Toggle):
    """
    If enabled this option will augment the selected Norton Method(s) to require the vanilla method of getting the
    item as well as getting the item from the randomized pool for game completion.

    Norton Method: El Vibrato Crown will require the player be able to reach the check location "El Vibrato Control
    Center (Deepest Delve Mine) - El Vibrato Quest Completion" to be able to give the El Vibrato Crown to Norton. 

    Norton Method: The Necromancer's Crown will require the player be able to reach the check location 
    "Necromancer's Tower - Necromancer Defeated" to be able to give the Necromancers Crown to Norton.

    Norton Method: Gold Tooth Crown will require the player to be able to reach the check location "Fort of Darkness
    (Second Tent) - Bone Trader (23 Gold Teeth)" to be able to give the Gold Tooth Crown to Norton.

    Norton Method: Turnip Crown will require the player to be able to reach the check location "The Silver Plater
    - Plated the Turnip" to be able to give the Turnip Crown to Norton. Additionally the ability to eat the
    Turnip will be turned off if this option is selected with the listed Norton Method.

    Norton Method: Honey Jelly Bean will require the player be able reach the check location "Roy Bean's House - 
    Honey Bean" to be able to use enter the Train Heist quest.
    """
    internal_name = "norton_quest_enabled"
    display_name = "Require Vanilla Completions for Norton?"

@dataclass
class WOLOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool

    horse_selection: Horse
    dlc_enabled: EnableDLC
    randomize_ghost_coach: RandomizeGunManorCoach
    randomize_goblintongue: RandomizeGoblintongue
    wander_sanity: WanderSanity
    crate_sanity: CrateSanity
    haystack_sanity: HaystackSanity
    unbreakable_tools: UnbreakableTools
    deathlink_enabled: Deathlink
    el_vib_bridge_enabled: BridgeMethodElVibrato
    necro_bridge_enabled: BridgeMethodNecro
    breadwood_bridge_enabled: BridgeMethodBreadwood
    bridge_quest_enabled: BridgeMethodQuest
    all_breadwood_quests: AllBreadwoodQuests
    el_crown_enabled: NortonMethodCElVib
    necro_crown_enabled: NortonMethodCNecro
    gold_crown_enabled: NortonMethodCGoldTooth
    turnip_crown_enabled: NortonMethodCTurnip
    honey_jellybean_enabled: NortonMethodHoneyBean
    norton_quest_enabled: NortonMethodQuest


wol_option_groups = [
    OptionGroup("WOLAP World Options", [
        Horse,
        UnbreakableTools,
        RandomizeGoblintongue
    ], True),

    OptionGroup("Mid Game Bridge Options", [
        BridgeMethodElVibrato,
        BridgeMethodNecro,
        BridgeMethodBreadwood,
        BridgeMethodQuest,
        AllBreadwoodQuests
    ], True),

    OptionGroup("End Game Norton Options", [
        NortonMethodCTurnip,
        NortonMethodCGoldTooth,
        NortonMethodCNecro,
        NortonMethodCElVib,
        NortonMethodHoneyBean,
        NortonMethodQuest
    ], True),

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
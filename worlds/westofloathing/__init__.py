import settings
from typing import List, Dict, Any
from BaseClasses import Item, Location, Tutorial, ItemClassification, Region
from worlds.AutoWorld import WebWorld, World
from Options import OptionError
from .options import wol_option_groups, wol_option_presets, WOLOptions
from .items import item_table, item_name_groups, item_name_to_id, starting_gear_list, extra_filler_list
from .locations import location_table, location_name_groups, location_name_to_id
from .regions import basegame_region_table, combined_dlc_region_table
from .rules import set_location_rules, set_region_rules

class WOLLocation(Location):
    game: str = "West of Loathing"

class WOLItem(Item):
    game: str = "West of Loathing"

class WOLWeb(WebWorld):
    tutorials = [
        Tutorial(
            tutorial_name="Multiworld Setup Guide",
            description="A guide to setting up the West of Loathing AP mod for Archipelago multiworld games.",
            language="English",
            file_name="setup_en.md",
            link="setup/en",
            authors=["Xylen, TylerJG92"]
        )
    ]
    theme = "dirt"
    game = "West of Loathing"
    option_groups = wol_option_groups
    options_presets = wol_option_presets

#class WOLSettings(settings.Group):
    #"""May not need this at all, not sure yet"""

class WOLWorld(World):
    """
    Say howdy to West of Loathing -- a single-player slapstick comedy adventure role-playing game set in the wild west 
    of the Kingdom of Loathing universe. Traverse snake-infested gulches, punch skeletons wearing cowboy hats, grapple 
    with demon cows, and investigate a wide variety of disgusting spittoons. Explore a vast open world and encounter a 
    colorful cast of characters, some of whom are good, many of whom are bad, and a few of whom are ugly.
    """
    game = "West of Loathing"
    web = WOLWeb()

    options: WOLOptions
    options_dataclass = WOLOptions
    #settings: typing.ClassVar[WOLSettings]
    item_name_groups = item_name_groups
    location_name_groups = location_name_groups

    item_name_to_id = item_name_to_id
    location_name_to_id = location_name_to_id

    #This should pass the slot data to UT
    @staticmethod
    def interpret_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
        return slot_data
    #This should allow UT to generate without a yaml
    ut_can_gen_without_yaml = True
    explicit_indirect_conditions = False

    def generate_early(self):
        if (not self.options.el_vib_bridge_enabled and
            not self.options.necro_bridge_enabled and
            not self.options.breadwood_bridge_enabled):
            raise OptionError("West of Loathing's yaml requires at least one Bridge Method enabled.")

        if (not self.options.el_crown_enabled and
            not self.options.necro_crown_enabled and
            not self.options.gold_crown_enabled and
            not self.options.turnip_crown_enabled and
            not self.options.honey_jellybean_enabled):
            raise OptionError("West of Loathing's yaml requires at least one Norton Method enabled.")

        if hasattr(self.multiworld, "generation_is_fake"):
            if hasattr(self.multiworld, "re_gen_passthrough"):
                if "West of Loathing" in self.multiworld.re_gen_passthrough:
                    slot_data = self.multiworld.re_gen_passthrough["West of Loathing"]
                    self.options.dlc_enabled.value = slot_data["dlc_enabled"]
                    self.options.randomize_ghost_coach.value = slot_data["randomize_ghost_coach"]
                    self.options.randomize_goblintongue.value = slot_data["randomize_goblintongue"]
                    self.options.wander_sanity.value = slot_data["wander_sanity"]
                    self.options.crate_sanity.value = slot_data["crate_sanity"]
                    self.options.haystack_sanity.value = slot_data["haystack_sanity"]
                    self.options.unbreakable_tools.value = slot_data["unbreakable_tools"]
                    self.options.deathlink_enabled.value = slot_data["deathlink_enabled"]
                    self.options.el_vib_bridge_enabled.value = slot_data["el_vib_bridge_enabled"]
                    self.options.necro_bridge_enabled.value = slot_data["necro_bridge_enabled"]
                    self.options.breadwood_bridge_enabled.value = slot_data["breadwood_bridge_enabled"]
                    self.options.bridge_quest_enabled.value = slot_data["bridge_quest_enabled"]
                    self.options.all_breadwood_quests.value = slot_data["all_breadwood_quests"]
                    self.options.el_crown_enabled.value = slot_data["el_crown_enabled"]
                    self.options.necro_crown_enabled.value = slot_data["necro_crown_enabled"]
                    self.options.gold_crown_enabled.value = slot_data["gold_crown_enabled"]
                    self.options.turnip_crown_enabled.value = slot_data["turnip_crown_enabled"]
                    self.options.honey_jellybean_enabled.value = slot_data["honey_jellybean_enabled"]
                    self.options.norton_quest_enabled.value = slot_data["norton_quest_enabled"]
                    self.options.horse_selection.value = slot_data["horse_selection"]
        return

    def get_filler_item_name(self) -> str:
        return self.random.choice(extra_filler_list)

    def create_item(self, name: str, classification: ItemClassification = None) -> WOLItem:
        item_data = item_table[name]

        if not self.options.wander_sanity and name == "Bottle Of Ghost Whiskey":
            classification = ItemClassification.useful
        if not self.options.necro_bridge_enabled and name == "Progressive Nex-Mex Skillbook":
            classification = ItemClassification.useful
        if not self.options.el_crown_enabled and name == "El Vibrato Crown":
            classification = ItemClassification.useful
        if not self.options.gold_crown_enabled and name == "Gold Tooth Crown":
            classification = ItemClassification.useful
        if not self.options.turnip_crown_enabled and name == "Turnip Crown":
            classification = ItemClassification.useful
        
        if classification is None:
            classification = item_data.classification
        return WOLItem(name, classification, self.item_name_to_id[name], self.player)

    def create_items(self) -> None:
        wol_items: List[WOLItem] = []
        items_to_create: Dict[str, int] = {item: data.copies_in_pool for item, data in item_table.items()}

        #Logic for modifying the item pool contents based on options and such will go here

        if not self.options.start_inventory_from_pool:
            for item in starting_gear_list:
                items_to_create[item] -= 1

        if not self.options.randomize_ghost_coach:
            items_to_create["Ghost Coach To Gun Manor"] = 0

        if not self.options.randomize_goblintongue:
            items_to_create["English-Goblintongue Dictionary"] = 0

        if not self.options.el_vib_bridge_enabled:
            items_to_create["El Vibrato Model Bridge"] = 0

        if not self.options.necro_crown_enabled:
            items_to_create["The Necromancer's Crown"] = 0

        if not self.options.honey_jellybean_enabled:
            items_to_create["Honey Jelly Bean"] = 0

        if not self.options.dlc_enabled:
            for item, data in item_table.items():
                if data.is_dlc:
                    items_to_create[item] = 0

        if not self.options.wander_sanity:
            for item, data in item_table.items():
                if data.is_wandersanity:
                    items_to_create[item] = 0

        if not self.options.crate_sanity:
            for item, data in item_table.items():
                if data.is_cratesanity:
                    items_to_create[item] = 0

        for item, quantity in items_to_create.items():
            for _ in range(quantity):
                wol_items.append(self.create_item(item))

        for _ in range(len(self.multiworld.get_unfilled_locations(self.player)) - len(wol_items)):
            wol_items.append(self.create_item(self.get_filler_item_name()))

        self.multiworld.itempool += wol_items

    def create_regions(self) -> None:
        if self.options.dlc_enabled:
            region_table = combined_dlc_region_table
        else:
            region_table = basegame_region_table

        for region_name in region_table:
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        for region_name, exits in region_table.items():
            region = self.get_region(region_name)
            region.add_exits(exits)

        for location_name, location_id in self.location_name_to_id.items():
            if ((not self.options.dlc_enabled and location_table[location_name].is_dlc) or
                (not self.options.wander_sanity and location_table[location_name].is_wandersanity) or
                (not self.options.crate_sanity and location_table[location_name].is_cratesanity) or
                (not self.options.haystack_sanity and location_table[location_name].is_haystacksanity)):
                continue
            
            region = self.get_region(location_table[location_name].region)
            location = WOLLocation(self.player, location_name, location_id, region)
            region.locations.append(location)

        victory_region = self.get_region("End Credits")
        victory_location = WOLLocation(self.player, "Temp Victory Location", None, victory_region)
        victory_location.place_locked_item(WOLItem("Temp Victory Item", ItemClassification.progression, None, self.player))
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Temp Victory Item", self.player)
        victory_region.locations.append(victory_location)

    def set_rules(self) -> None:
        set_region_rules(self)
        set_location_rules(self)

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data: Dict[str, Any] = {
            "dlc_enabled": self.options.dlc_enabled.value,
            "randomize_ghost_coach": self.options.randomize_ghost_coach.value,
            "randomize_goblintongue": self.options.randomize_goblintongue.value,
            "wander_sanity": self.options.wander_sanity.value,
            "crate_sanity": self.options.crate_sanity.value,
            "haystack_sanity": self.options.haystack_sanity.value,
            "unbreakable_tools": self.options.unbreakable_tools.value,
            "deathlink_enabled": self.options.deathlink_enabled.value,
            "el_vib_bridge_enabled": self.options.el_vib_bridge_enabled.value,
            "necro_bridge_enabled": self.options.necro_bridge_enabled.value,
            "breadwood_bridge_enabled": self.options.breadwood_bridge_enabled.value,
            "bridge_quest_enabled": self.options.bridge_quest_enabled.value,
            "all_breadwood_quests": self.options.all_breadwood_quests.value,
            "el_crown_enabled": self.options.el_crown_enabled.value,
            "necro_crown_enabled": self.options.necro_crown_enabled.value,
            "gold_crown_enabled": self.options.gold_crown_enabled.value,
            "turnip_crown_enabled": self.options.turnip_crown_enabled.value,
            "honey_jellybean_enabled": self.options.honey_jellybean_enabled.value,
            "norton_quest_enabled": self.options.norton_quest_enabled.value,
            "horse_selection": self.options.horse_selection.value
        }

        return slot_data
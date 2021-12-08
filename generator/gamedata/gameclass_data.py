import generator.stats


GAMECLASSDATA = {
    # To be Expanded Upon
    # "classname" : {
    #     "hit_dice" : "d12",
    #     "saving_throws" : generator.stats.Stats(CON = True),
    #     "skills" : [],
    #     "preferred_stats" : generator.stats.Stats(DEX = True),
    #     "subclasses" : []
    # },
    "Barbarian": {
        "hit_dice": "d12",
        "saving_throws": generator.stats.Stats(STR=True, CON=True),
        "skills": [
            "Animal Handling",
            "Athletics",
            "Intimidation",
            "Nature",
            "Perception",
            "Survival",
        ],
        "preferred_stats": generator.stats.Stats(STR=True, CON=True),
        "subclasses": ["Path of the Berserker", "Path of the Totem Warrior"],
    },
    "Rogue": {
        "hit_dice": "d8",
        "saving_throws": generator.stats.Stats(DEX=True, INT=True),
        "skills": [
            "Acrobatics",
            "Athletics",
            "Deception",
            "Insight",
            "Intimidation",
            "Investigation",
            "Perception",
            "Performance",
            "Persuasion",
            "Sleight of Hand",
            "Stealth",
        ],
        "preferred_stats": generator.stats.Stats(DEX=True, CHA=True),
        "subclasses": ["Thief", "Assassin", "Arcane Trickster"],
    },
    "Wizard": {
        "hit_dice": "d6",
        "saving_throws": generator.stats.Stats(INT=True, WIS=True),
        "skills": [
            "Arcana",
            "History",
            "Insight",
            "Investigation",
            "Medicine",
            "Religion",
        ],
        "preferred_stats": generator.stats.Stats(INT=True, CON=True),
        "subclasses": [
            "School of Abjuration",
            "School of Conjuration",
            "School of Divination",
            "School of Enchantment",
            "School of Evocation",
            "School of Illusion",
            "School of Necromancy",
            "School of Transmutation",
        ],
    },
    "Ranger": {
        "hit_dice": "d10",
        "saving_throws": generator.stats.Stats(STR=True, DEX=True),
        "skills": [
            "Animal Handling",
            "Athletics",
            "Insight",
            "Investigation",
            "Nature",
            "Perception",
            "Stealth",
            "and Survival",
        ],
        "preferred_stats": generator.stats.Stats(WIS=True, DEX=True),
        "subclasses": ["Hunter", "Beast Master"],
    },
}

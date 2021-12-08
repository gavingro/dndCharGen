from character.character import Character
from character.character_idea import display as ci_display
from character.character_sheet import display as cs_display
from character.character_sheet import save_to_pdf
from generator.background import Background
from generator.gameclass import GameClass
from generator.race import Race
from generator.stats import Stats


def main():
    # Generate and display a random character
    mychar = Character()
    ci_display(mychar)
    print("-----------------------------------------------------------")
    cs_display(mychar)

    # Generate a custom character
    base_stats = Stats(STR=15, DEX=3, CON=20, INT=10, WIS=8, CHA=7)
    game_class = GameClass("Barbarian", auto_generate=True)
    race = Race("Dwarf", auto_generate=True)
    background = Background("Acolyte", auto_generate=True)

    mychar = Character(base_stats, game_class, race, background, auto_generate=False)
    save_to_pdf(mychar, flatten=True)


if __name__ == "__main__":
    main()

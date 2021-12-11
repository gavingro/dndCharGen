import unittest

from dndcharactergenerator.generator.test_background import TestBackground
from dndcharactergenerator.generator.test_race import TestRace
from dndcharactergenerator.generator.test_stats import TestStats
from dndcharactergenerator.generator.test_rpggenerator import TestRpgGenerator
from dndcharactergenerator.generator.test_gameclass import TestGameClass
from dndcharactergenerator.character.test_character import TestCharacter
from dndcharactergenerator.character.test_character_idea import TestCharacterIdea
from dndcharactergenerator.character.test_character_sheet import TestCharacterSheet


def full_test_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult

    ####### Character Tests
    suite.addTest(unittest.makeSuite(TestCharacter))
    suite.addTest(unittest.makeSuite(TestCharacterIdea))
    suite.addTest(unittest.makeSuite(TestCharacterSheet))

    ####### Generator Tests
    suite.addTest(unittest.makeSuite(TestRpgGenerator))
    suite.addTest(unittest.makeSuite(TestStats))
    suite.addTest(unittest.makeSuite(TestGameClass))
    suite.addTest(unittest.makeSuite(TestRace))
    suite.addTest(unittest.makeSuite(TestBackground))

    runner = unittest.TextTestRunner()
    print(runner.run(suite))


if __name__ == "__main__":
    full_test_suite()

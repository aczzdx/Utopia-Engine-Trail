import unittest

from player import Player


class MyTestCase(unittest.TestCase):
    def test_player_hit_point(self):
        p = Player()
        self.assertEqual(p.hit_point, 7)
        with self.assertRaises(ValueError):
            p.hit_point = -1
        with self.assertRaises(ValueError):
            p.hit_point = "foo"

        p.hit_point = 4
        self.assertEqual(p.hit_point, 4)

    def test_player_turn_count(self):
        p = Player()
        self.assertEqual(p.turn_count, 0)
        with self.assertRaises(ValueError):
            p.turn_count = "foo"
        with self.assertRaises(ValueError):
            p.turn_count = -1

        p.turn_count = 3
        self.assertEqual(p.turn_count, 3)

        p.next_turn()
        self.assertEqual(p.turn_count, 4)

    def test_player_is_game_over(self):
        p = Player()
        self.assertFalse(p.is_game_over(),
                         "The player are DEAD at its initial time.")

        p.hit_point = 0
        self.assertTrue(p.is_game_over(),
                        "The player are NOT dead when its HP is 0.")

        p.hit_point = 7
        p.turn_count = 15
        self.assertTrue(p.is_game_over(),
                        "The player are NOT dead when at the turn 15")


if __name__ == '__main__':
    unittest.main()

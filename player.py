###############
# player.py
#
# This file define the properties of player
#
#

import constant


class Player:
    def __init__(self):
        """Initialization of player.

        """
        self.__hp = constant.HIT_POINT_INITIAL
        self.__turns = 0

    @property
    def hit_point(self):
        return self.__hp

    @hit_point.setter
    def hit_point(self, value):
        if not isinstance(value, int):
            raise ValueError("The value of hit point should be integer")
        if value < constant.HIT_POINT_MINIMUM or value > constant.HIT_POINT_MAXIMUM:
            raise ValueError("The value of hit point should be within [" +
                             str(constant.HIT_POINT_MINIMUM) + "," +
                             str(constant.HIT_POINT_MAXIMUM) + "]")
        self.__hp = value

    @property
    def turn_count(self):
        return self.__turns

    @turn_count.setter
    def turn_count(self, value):
        if not isinstance(value, int):
            raise ValueError("The value of turn_count should be integer.")
        if value < 0:
            raise ValueError("The value of turn_count should not be negative.")

        self.__turns = value

    def next_turn(self):
        self.__turns += 1

    def is_game_over(self):
        """
        Check whether the game is over with the status of player.
        :return: true if the game is over, otherwise false.
        """
        return (self.hit_point <= 0)

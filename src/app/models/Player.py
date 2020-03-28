from src.app.models.Board import Board


class Player(object):

    def __init__(self, name, pion):
        board = Board()
        self._name = name
        self._pion = pion
        self._money = 1500
        self._position = board.cases[0]
        self._propriete_cards = []
        self._special_cards = []

    # GETTER
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def pion(self):
        return self._pion

    @pion.setter
    def pion(self, pion):
        self._pion = pion

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, money):
        self._money = money

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

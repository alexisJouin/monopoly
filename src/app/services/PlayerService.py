from src.app.models.Player import Player


def add_proriete_card(player: [Player], propriete_card):
    player.append(propriete_card)


def remove_proriete_card(player: Player, propriete_card):
    player.propriete_cards.remove(propriete_card)


def add_spectial_card(player: Player, special_card):
    player.special_cards.append(special_card)


def remove_spectial_card(player: Player, special_card):
    player.special_cards.remove(special_card)


def create_player(name, pion):
    return Player(name, pion)

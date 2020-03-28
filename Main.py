# coding: utf-8
# from unidecode import unidecode

from src.app.models.Board import Board
from src.app.models.Player import Player
from random import randrange


# Fonctions
from src.app.services.PlayerService import create_player


def jeter_des():
    a = randrange(1, 6)
    b = randrange(1, 6)
    return a + b


board = Board()

print("************************************")
print("Monopoly CORONAVIRUS")
print("By Alexis JOUIN et Marianne SEIGNEUR")
print("************************************")

error = 1
while error == 1:
    # nbPlayers = int(input("Combien de joueurs ? "))
    nbPlayers = 2
    if nbPlayers <= 1 or nbPlayers > 6:
        print("ERROR min:2  max:6")
        error = 1
    else:
        error = 0

players: [Player] = []
print(nbPlayers)
for i in range(0, nbPlayers):
    print(i)
    # print(create_player('test','test'))
    name = "Joueur " + str(i + 1)
    print("Nom du joueur ", i + 1, " : ", name)
    # name = input()
    pion = "Pion J" + str(i + 1)
    print("Pion du joueur ", i + 1, " : ", pion)
    # pion = input()
    players.append(create_player(name, pion))

# print("************************************")
# print("************************************")

for player in players:
    print("Bienvenue ", player.name)
    print("Position : ", player.position)

endGame = False
turn = 1
# while not endGame:
#     print("************************************")
#     print("Tour n°", turn)
#     for player in players:
#         print(player.name, " à toi de jouer. Press d pour jeter les dés")
#         input()
#         scoreDes = jeter_des()
#         print("Score : ", scoreDes)
#         tempPosition = player.position["position"] + scoreDes
#         position = tempPosition if tempPosition >= 40 else tempPosition - 40
#         player.position(board.cases[position])
#         print(player.position)
#         print(player.position["type"])
#         # Menu choix pendant un tour
#         print("Acheter ")
#     turn = turn + 1
#     print("************************************")

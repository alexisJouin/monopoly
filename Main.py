# coding: utf-8
#from unidecode import unidecode

from Board import Board;
from Player import Player;
from random import randrange


######## Fonctions ########
def jeterDes():
    a = randrange(1,6) 
    b = randrange(1,6)
    return a + b



board = Board()

print("************************************")
print("Monopoly CORONAVIRUS")
print("By Alexis JOUIN et Marianne SEIGNEUR")
print("************************************")

error = 1
while(error == 1):
    #nbPlayers = int(input("Combien de joueurs ? "))
    nbPlayers = 2
    if(nbPlayers<=1 or nbPlayers >6):
        print("ERROR min:2  max:6")
        error = 1
    else:
        error = 0

players = []
for i in range(nbPlayers):
    print("Nom du joueur ", i+1, " : ")
    #name = input()
    name = "Joueur " , i+1
    print("Pion du joueur ", i+1, " : ")
    #pion = input()
    pion = "Pion J", i+1
    players.append(Player(name, pion))
    

print("************************************")
print("************************************")

for player in players:
    print("Bienvenue ", player.name)   
    print("Position : ", player.position)
    
endGame = False
turn = 1
while endGame==False:
    print("************************************")
    print("Tour n°",turn)
    for player in players:
        print(player.name, " à toi de jouer. Press d pour jeter les dés")
        input()
        scoreDes = jeterDes()
        print("Score : ", scoreDes )
        position = player.position["position"] + scoreDes
        #Gestion du tour complet du plateau
        if(position >= 40):
            position = position - 40
        player._setPosition(board.cases[position])
        print(player.position)
        print(player.position["type"])
        #Menu choix pendant un tour
        print("Acheter ")
    turn = turn + 1
    print("************************************")
        
        
    




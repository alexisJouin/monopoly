from Board import Board;

class Player(object):
  
    def __init__(self, name, pion):
        board = Board()
        self.name= name
        self.pion= pion
        self.money= 1500
        self.position = board.cases[0]
        self.proprieteCards=[]
        self.specialCards=[]
   
    def addProrieteCard(self, proprieteCard):
        self.proprieteCards.append(proprieteCard)
    
    def removeProrieteCard(self, proprieteCard):
        self.proprieteCards.remove(proprieteCard)
    
    def addSpectialCard(self, specialCard):
        self.specialCards.append(specialCard)
    
    def removeSpectialCard(self, specialCard):
        self.specialCards.remove(specialCard)
        
        
        
    #SETTER    
    def _setName(self, name):
        self.name = name
        
    def _setPion(self, pion):
        self.pion = pion
        
    def _setMoney(self, money):
        self.money = money
        
    def _setPosition(self, position):
        self.position = position
        
    #GETTER  
    def _getName(self):
        return self.name
        
    def _getPion(self):
        return self.pion
        
    def _getMoney(self):
        return self.money
        
    def _getPosition(self):
        return self.position
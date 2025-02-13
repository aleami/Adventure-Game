from dictionary import *
#en klass 
class player:
  def __init__(self,attack, weapon_1, weapon_2, weapon_3, health):
    #olika funktioner för karaktärer
    self.attack = attack
    self.weapon1 = weapon_1
    self.weapon2 = weapon_2
    self.weapon3 = weapon_3
    self.health = health

    attacked = 1
    self.health -= attacked

pirat = player('jump and hit', 'knife','sword', 'chillipowder', 3)

blackbeard = player('Magic spell', 'wind power','fire', 'rope', 5)
    
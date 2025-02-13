#Importerar olika moduler
import time 
from os import system, name
from dictionary import *
from chapter2 import *
from chapter1 import *

def starttext():
  """Text vid uppstart """
  text = 'The mysterious sea advanture'
  mitten = text.center(65)
  rad = '--------------------------------'
  mitten2 = rad.center(70)
  print(' ')
  print(mitten, mitten2)
  
def clear():
  """Tar bort spelets historik"""
  if name == 'nt':
    _ = system('cls')
   #för mac and linux operativsystem
  else:
    _ = system('clear')
  return clear

def klar(valisland, avatar):
  klar = input('Do you want to play chapter 2, play again or end the game?(play/again/end) ')
  if klar in play:
    countdown(3)
    time.sleep(2)
    clear()
  #Om svaret på variabeln klar är play så hamnar man här och går vidare till kapitel 2.
    kap2(valisland, avatar)
  elif klar in again:
    clear()
    
  elif klar in end:
    clear()
    print('Well played😊!')

#Rekursiv funktion som rknar ned till nästa kapitel
def countdown(n):
  """Nedrkning till nästa kapitel"""
  import time
  if n == 0:
    print('Let´s play!!!')
  else:
    time.sleep(1)
    print(n) # funkar ej helt den printar none
    countdown(n - 1)
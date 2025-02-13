from dictionary import * 
from chapter1 import * 
from chapter2 import* 
from tabulate import tabulate
from klaser import *
from funktioner import *

def island3(avatar):
  """Spelets slut"""
  print('You have arrived at your final destination!')
  print('')
  print('You have come to Blackbeards island where the treasure is hidden!')
  print('')
  print('You have come very close to the tressure!')
  print('')
  print('In order to achive your prise you need to defeat Blackbeard and win the game!')
  print('')
  battle(avatar)
def knife(avatar, move1):
  print('Blackbeard barbosa attacked you while you chose your weapon so slowly!')
  print('He used his best method of attacking:', blackbeard.weapon1)
  print('\nYou now only have', pirat.health,'❤️',' left!')
  print ('◦',pirat.weapon3)
  move_next = input('Anwser -> ')
  if move_next == 'chillipowder':
    chillipowder(avatar, move1)

def sword():
  print('\nYou quikly realise that it wont help you unless he gets weak of course')

def chillipowder(avatar, move1):
  print('\nOH wow! You are a very clever pirate!')
  print('You throw the chillipowder on Blackbeard, and now he has very difficulty to see for some time!')
  print('Now you can attack him in order to defeat him!')
  print('\nYess you finally got the chance attacking him!')
  print('But dont be so happy, he still has', blackbeard.health, '❤️',' left!' )
  if move1 == 'knife':
    data = [[characters[avatar],age[avatar],pirat.health], 
          ['Blackbeard',41,blackbeard.health]]
    col_names = ["Avatar", "Age","Lifes",]
    print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))

  if move1 == 'chillipowder':
    print('The scoreboard is now:')
    data = [[characters[avatar],age[avatar],3], 
          ['Blackbeard',41,blackbeard.health]]
    col_names = ["Avatar", "Age","Lifes",]
    print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))

  
def battle(avatar):
  battle_start = input('Do you want to start this battle?(y/n) ')
  while battle_start not in yes and battle_start not in no:
    battle_start = input('Do you want to start this battle?(y/n) ')
    
  if battle_start in yes:
    print('')
    info = input('Before we start the battle do you want to know some information about yourself and your oponent Blackbeard!(y/n) ')
    
    if info in yes:
      print('')
      data = [[characters[avatar],age[avatar],'❤ 3st', pirat.weapon1], 
      ['Blackbeard',41,'❤ 5st',blackbeard.weapon2]]
      col_names = ["Avatar", "Age","Lifes", "Best Weapons"]
      print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))
      
    if battle_start in no and info in no:
      time.sleep(1)
      print('You have 3 hearts, if you lose all the game ends!')
      print('The game will start in: ')
      countdown(3)
      
    while info not in yes and info not in no:
      info = input('Before we start the battle do you want to know some information about yourself and your oponent Blackbeard!(y/n) ')
  
  print('\nYou are starting the battle!')
  print('Which weapon are you using to attack?')
  print ('\n◦',pirat.weapon1)
  print ('◦',pirat.weapon2)
  print ('◦',pirat.weapon3)
  
  move1 = input('Anwser -> ')
  if move1 == 'sword':
    sword()
  if move1 == 'knife':
    knife(avatar, move1)
  if move1 == 'chillipowder':
    chillipowder(avatar, move1)

  last_move = input('Blackbeard seems very tired. Do you want to attack him, If you attack him now you will win the game!(y/n)')
  while last_move not in yes and last_move not in no:
    last_move = input('Blackbeard seems very tired. Do you want to attack him, If you attack him now you will win the game!(y/n)')
    
  if last_move in yes:
    print('You', pirat.attack, 'him!')
    print('Congratulations you defeated him!')
    print('You now have found the hidden treasure!')
    time.sleep(2)
    clear()
    print('Congratulations!!!!!!!!!')
  if last_move in no:
    print('OH NO!!! You should have attacked him!!')
    print('He now attacked you!')
    clear()
    print('Game Over😅')
  return move1
    
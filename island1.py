from funktioner import *
from dictionary import characters, money, gadgets
from chapter2 import * 
from chapter1 import *
import random

def island1(avatar):
  """Första ön"""
  #slumpar tal mellan 1-100
  slumpad(avatar)
  print('\n\nYou have now arrived to your destination! You now leave the ship to find the hidden tressure which might be on this island.')
  time.sleep(1)
  print('You walk around the island and suddenly see two small houses not so far ahead!')
  time.sleep(1)
  print('You deside to walk further and get closer to those small houses until you deside to go inside one of the houses. Which house do you want to go inside in?')
  time.sleep(1)
  select = select_house()
  if select in svara:
    anwser_a(select)
  if select in svarb:
    anwser_b(select)
  while select not in svara and select not in svarb:
    select = select_house()
    if select in svara:
      anwser_a(select)
    if select in svarb:
      anwser_b(select)

def select_house():
  """Väg val av hus"""
  print("""  A. The yellow house
  B. The red house""")
  select = input(">>> ")
  return select
  
def slumpad(avatar):
  lista = []
  for i in range (1):
    while True:
      slumppris = random.randrange(1,100)
      if slumppris not in lista:
        lista.append(slumppris)
        i+=1
        break
    time.sleep(1)
    print('\nCongratulations! You found',*lista,'kr on the ship!', sep = " ") 
    money[avatar] += slumppris 
    print('You now have',money[avatar],'kr in balance!')
    time.sleep(1)
        
def anwser_b(select):
  """Text vid svar b"""
  print('\nYou went inside the red house.')
  time.sleep(1)
  print('But you didn´t find anything')
  time.sleep(2)
  print('So you go to the Yellow house.')
  anwser_a(select)
        
def anwser_a(select):
  """Text och svar vid svar a"""
  time.sleep(1)
  print('\nYou went inside the yellow house which was almost emty except for a table which had a mysterius box on top of it.')
  time.sleep(1)
  print('\nYou deside to pick it up and try to open the box but it seems that it is closed.')
  time.sleep(1)
  print('\nIn order to open the box you look around trying to find somthing you could open the box whith, but don´t find anything.....')
  time.sleep(1)
#En input som frågar om man vill leta efter något
  hitta()
#Här får användaren lite uppgifter
  prova()

def hitta():
  """frågeställning"""
  hitta = input('\nDo you want to go to the red house and find somthing to open the box whith?(y/n) ')
  while hitta not in yes and hitta not in no:
    hitta = input('\nDo you want to go to the red house and find somthing to open the box whith?(y/n) ')
  if hitta in no:
    time.sleep(1)
    print('\nAre you sure🤨???')
    time.sleep(1)
    hitta = input('\nDo you want to go to the red house and find somthing to open the box whith?(y/n) ') 
  if hitta in yes:
    time.sleep(1)
    print('\nYou go to the red house and see somthing yellow sparkling in the corner, you deside to pick it up and you see that it is a {}'.format(gadgets['tool']))
    time.sleep(1)


def prova():
  """testa alterantiven"""
  prova = input('\nDo you want to run back to the yellow house to try the {} (yes/no)? '.format(gadgets['tool']))
  print(prova)
  if prova not in yes and prova not in no:
    print('Not allowed!')
    prova = input('\nDo you want to run back to the yellow house to try the {} (yes/no)? '.format(gadgets['tool']))
    
  if prova in no:
    print('\nAre you sure???')
    time.sleep(1)
    prova()  
  if prova in yes:
    time.sleep(1)
    print('\nYou went inside the yellow house again to see if you could open the mysterius box.')
    time.sleep(1)
    print('\nYou try to twist the {} left to right you heard a klicking nois....'.format(gadgets['tool']))
    time.sleep(1)
    print('You succesfully opend the box!!!!!!')
    time.sleep(1)
    print('\nSlowly openning the box you see one piece of a torn map inside the box.')
    time.sleep(1)
    print('\nCongratulations! You found the other half of the torn map!!!!!')
    time.sleep(1)
    print('You can now succesfully find the hidden tressure!')
    time.sleep(1)
    print('\nGood luck:):):)')
 
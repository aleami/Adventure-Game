from dictionary import * 
from chapter1 import *
from island1 import *
from island2 import *
from island3 import *

#I kapitel 2 kommer rubriken kapitel 2 upp samt frågar om de resterande öarna som finns kvar.
def kap2(valisland, avatar):
  """Andra kapitlet""" 
  text2 = 'Kapitel 2'
  rubrik2 = text2.center(65)
  rad = '----------------------'
  rad2 = rad.center(60)
  print(rubrik2, rad2)
  
  if valisland == 1:
    island2_3(valisland)
  if valisland == 2:
    island1_3(valisland, avatar)
  if valisland == 3:
    print('You are done with the game!')
    time.sleep(2)
    clear()
    print('Well played!!')

def island2_3(valisland):
  """Val av island"""
  print('You have found the missing piece of the torn map and now yu just need to follow the path and find the lost tressure!')
  print("""
  2. ISLAND OF FLAME
  3. PARADISE ISLAND""")
  valisland = input(">>> ")
  while valisland != '2' and valisland != '3':
    island2_3(valisland)
  chosenisland = 'You chose {}!'.format(island[int(valisland)])
  mitten = chosenisland.center(65)
  print(mitten)
  if island[int(valisland)] in island[2]:
    island2()
    island3(avatar)
  if island[int(valisland)] in island[3]:
    island3(avatar)
  
  
def island1_3(valisland, avatar):
  """Val av island"""
  print('To find the missing pice of the map chose a island and find the tressure')
  print ("""  1. NEVERLAND ISLAND
  3. PARADISE ISLAND""")
  valisland = input(">>> ")
  while valisland != '1' and valisland != '3':
    island2_3(valisland)
  chosenisland = 'You chose {}!'.format(island[int(valisland)])
  mitten = chosenisland.center(65)
  print(mitten)
  if island[int(valisland)] in island[1]:
    island1(avatar)
    island3(avatar)
  if island[int(valisland)] in island[3]:
    island3(avatar)

  
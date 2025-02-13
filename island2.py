from funktioner import *
from dictionary import * 
from chapter2 import* 
from chapter1 import* 

def island2():
  """Sortering av input"""
  print('You have arrived at a very dangerouse island!')
  print('What do you want to do?')
  print ("""  a) Pick & plant flowers!
  b) Find the missing tressure!""")
  chose_direction = input('>>> ')
  if chose_direction in svara:
    clear()
    garden(chose_direction)
  if chose_direction in svarb:
    escape(chose_direction)
  while chose_direction not in svara and chose_direction not in svarb:
    island2()
  return chose_direction

def garden(chose_direction):
  """Sorterings start av spel"""
  text = '🌻🌷🌼Will Turners garden🌻🌷🌼' 
  rubrik = text.center(60)
  rad = '----------------------------'
  rad2 = rad.center(60)
  print(rubrik, rad2)
  print('Welcome to the garden!')
  print('Oh no!! Wil´s plants have been withered from the heat🥀.')
  print('Please help him re plant his flowers!')
  #merge sort vid val av blommor
  lista = merge_output()
  flowers(lista)
  print('\nThank you for helping me save my garden!')
  print('Here is a gift from Will Turner!')
  print('You got a magic potion!')
  escape(chose_direction)


def merge_sort(lista):
  if len(lista) <= 1:
    return lista
  middle = len(lista) // 2
  left_list = lista[:middle]
  right_list = lista[middle:]

  left_list = merge_sort(left_list)
  right_list = merge_sort(right_list)
  return list(merge(left_list, right_list))

def merge(left_half,right_half):
   res = []
   while len(left_half) != 0 and len(right_half) != 0:
      if left_half[0] < right_half[0]:
         res.append(left_half[0])
         left_half.remove(left_half[0])
      else:
         res.append(right_half[0])
         right_half.remove(right_half[0])
   if len(left_half) == 0:
      res = res + right_half
   else:
      res = res + left_half
   return res
  
def merge_output():
  lista = []
  max_antal = 5
  while len(lista) < max_antal:
    while True:
      try:
        item = int(input("\nPick a number between (1-10): ")) 
        if item > 10:
          print('Try again')
          item = int(input("\nPick a number between (1-10): "))
        seen = set(lista)
        if item not in seen:
          seen.add(item)
          lista.append(item)
          break
      except:
        print('Try again')
  print('')
  print(merge_sort(lista))
  return lista


def flowers(lista):
  print('\nSiffrorna du valde motsvarar dessa blommor: ')
  if 1 in lista:
    print('◦', växt[1])
  if 2 in lista:
    print('◦', växt[2])
  if 3 in lista:
    print('◦', växt[3])
  if 4 in lista:
    print('◦', växt[4])
  if 5 in lista:
    print('◦', växt[5])
  if 6 in lista:
    print('◦', växt[6])
  if 7 in lista:
    print('◦', växt[7])
  if 8 in lista:
    print('◦', växt[8])
  if 9 in lista:
    print('◦', växt[9])
  if 10 in lista:
    print('◦', växt[10])
  search()

def search():
  """sökning på en lista"""
  wonder = input('Do you want to know how many flowers Will Turner has? ')
  while wonder not in no and wonder not in yes:
    print('Try again!!!!!!😐')
    wonder = input('Do you want to know how many flowers Will Turner has? ')
  if wonder in yes:
    print("Will has", len(options_flowers),'flowers in his collection')
    find = False
    sok = input('Which flower do you want? ')
    x = 0
    while x < len(options_flowers):
      if options_flowers[x] == sok:
        print("The flower you chose is at number", x, "in Will´s favorite list!!!")
        break
      else:
        x += 1
        if x == len(options_flowers):
          print("Sorry but that flower does not exist!!")
  if wonder in no:
    print('That´s sad😐')
  
def escape(chose_direction):
  """Spelets action"""
  print('\nOh no you someone is following you!')
  print('What are you going to do?')
  print ("""  a) Run!
  b) pretend to be dead!
  c)Use the magic potion!""")
  svar = input('>>> ')
  while svar not in svara and svar not in svarb and svar not in svarc:
    print('\nOh no you someone is following you!')
    print('What are you going to do?')
    print ("""  a) Run!
  b) pretend to be dead!
  c)Use the magic potion!""")
    svar = input('>>> ')
    
  if svar in svara:
    print('\nYou are runnng as fast as you can but he is catching up with you')
    print('What are you going to do next?')
    print ("""  a) pretend to be dead!
  b)Use the magic potion!""")
    svar2 = input('>>> ')
    
    while svar2 not in svara and svar2 not in svarb:
      print ("""  a) pretend to be dead!
  b)Use the magic potion!""")
      svar2 = input('>>> ')
      
    if svar2 in svara:
      killed()
    if svar2 in svarb:
      if chose_direction in svara:
        have_magicpotion()
      if chose_direction in svarb:
        not_have_magicpotion()
        killed()
        
  if svar in svarb:
    killed()
    
  if svar in svarc:
    if chose_direction in svara:
      have_magicpotion()
    if chose_direction in svarb:
      not_have_magicpotion()
      killed()
    
def have_magicpotion():
  """Rädda från att förlora"""
  print('\nYou use the magic potion Will gave you and defeat the scary creature that was following you!')
  time.sleep(1)
  print('Good job!!')

def not_have_magicpotion():
  """Spel text"""
  print('\nOh no you don´t have any magic potion!')
  time.sleep(1)
  print('He heads toward you and attacks you!!')

def killed():
  """Spelet avslutar"""
  while True:
    print('Oh no you died!')
    time.sleep(2)
    clear()
    print("""  ________                                                 ._.
 /  _____/_____    _____   ____     _______  __ ___________| |
/   \  ___\__  \  /     \_/ __ \   /  _ \  \/ // __ \_  __ \ |
\    \_\  \/ __ \|  Y Y  \  ___/  (  <_> )   /\  ___/|  | \/\|
 \______  (____  /__|_|  /\___  >  \____/ \_/  \___  >__|   __
        \/     \/      \/     \/                   \/       \/""")
    break

def clear():
  """Tar bort spelets historik"""
  if name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')
  return clear

#Importerar andra filer hit
from funktioner import *
from dictionary import * 
from chapter2 import * 

def kap1_text():
  text1 = 'Chapter 1'
  rubrik1 = text1.center(70)
  rad = '-------------------'
  rad1 = rad.center(60)
  print(rubrik1, rad1)

def handling1():
  import time
  '''
    Returnerar en sträng text samt argumentet i dictionary när man kallar på nyckel värdet. 
            Returnerar:
                  characters[avatar]:  När man kallar på nyckelvärdet så returneras karaktärens namn samt en anpassad sträng för den karaktren.
  '''
  print("You have arived to a mystarius island and don´t know how to escape. You walk around the whole island and suddenly find a torn map whit a x on it, you found out that it´s a tressure map and get curious and want to find the tressure instead of going home.")
  print('Write with a lower case letters (type ex: jack )')
  time.sleep(1)
  print('\nTo start the game chose a caracter:')
  print ("""  --> Jack Sparrow
  --> Elisabeth Swann
  --> Hector Barbossa """)
  avatar = input(">>> ")
  if avatar in characters:
    characters[avatar] = selectedcharacter(avatar)
  else:
   avatar = handling1()
  return avatar
  
def selectedcharacter(avatar): 
  '''
    Returnerar avataren man har valt samt pengarna den avataren har när man anger key value. 
  
            Parameter:
                    avatar (str) : En input sträng

            Returnerar:
                    characters[avatar]:  När man kallar på nyckelvärdet genom "avatar" så returneras karaktärens namn samt en sträng för den karaktren.
                    money[avatar]: När man kallar på nyckelvärdet genom "avatar" så returneras karaktärens pengar.
  '''
  print('\nHello {}! Welcome to the mysterious island!'.format(characters[avatar]))
  print('I´m Captain Will Turner and I will guide you trough this game!')
  print('In the begining of the game you start with', money[avatar],'kr') 
  print('To find the tressure you need to chose your transport method!')
  time.sleep(1)


def travel():
  """Val av båt"""
  print('Which boat do you want to travel in?(type ex: ship4) ')
  print ("""  --> Take ship 1
  --> Take ship 2
  --> Take ship 3 """)
  alternatives = input("Anwser: ")
  if alternatives in ships:
    print('\nYour chosen ship is {}! '.format(ships[alternatives]))
  else:
    alternatives = travel()
  return alternatives

def selectboat(avatar,alternatives):
  """Insreuktion vid val av båt"""
  if alternatives == 'ship1' or alternatives == 'ship2':
    time.sleep(1)
    print('Wow, you chose the best ship, you are very lucky!')
    time.sleep(1) 
    message = 'Lets start the journey!'
    messagecenter = message.center(67)
    print(messagecenter)

  if alternatives == 'ship3':
    time.sleep(1)
    print('Oh no! the boat is a bit old, but don´t worry!, you have some options!')
    time.sleep(1)
    print("""  A. Repair your boat?
  B. Select another boat?""")
    alternatives = str(input(">>> "))
    while alternatives not in svara and alternatives not in svarb:
      print("""  A. Repair your boat?
  B. Select another boat?""")
      alternatives = str(input(">>> "))
    
    if alternatives in svara:
      time.sleep(1)
      print('\nIn order to repair your boat you need to pay 10kr')
      print('Your current money balance is {} kr! '.format(money[avatar]))
      
      option2 = input('Do you want to pay or change boat?(pay/change)')
      while option2 not in pay and option2 not in change:
        print('Try again😒')
        option2 = input('Do you want to pay or change boat?(pay/change)')
        
      if option2 in pay: 
        time.sleep(1)
        print('Your purchase was successful💰!')
        time.sleep(1)
        money[avatar] -= 10
        print('You now have {} kr left!'.format(money[avatar]))
        message = 'Lets start the journey!'
        messagecenter = message.center(67)
        print(messagecenter)
        
      if option2 in change:
        time.sleep(1)
        alternatives = travel() 
        selectboat(avatar,alternatives)
        
    if alternatives in svarb:
      alternatives = travel()
      selectboat(avatar,alternatives) 
      
def textislands():
  """Text vid val av Island"""
  print('As the jorney begins, you are sailing across the sea over the pasific ocean and over the atlantic ocean')
  time.sleep(1)
  print('\nNow the time has come to chose which island you want to go to and find the hidden tressure!')
  time.sleep(1)
  print('\nTo chose your path you need to select a island!')

def val_options():
  """Val av slumpad eller själv vald island"""
  options = input('\nDo you want to pick a island or do you want a end the game?(end/pick)')
  if options not in pick and options not in end:
    options = input('\nDo you want to pick a island or do you want a end the game?(end/pick)')
  return options

def islands(avatar, options):
  if options in pick:
    while True:
      print('\nPick a island by typing a number!')
      print ("""  1. NEVERLAND ISLAND
  2. ISLAND OF FLAME
  3. PARADISE ISLAND""")
      try:
        valisland = int(input(">>> "))
        if island[int(valisland)] in island[1]:
          text_val(valisland)
          island1(avatar)
        if island[int(valisland)] in island[2]:
          text_val(valisland)
          island2()
        if island[int(valisland)] in island[3]:
          text_val(valisland)
          island3(avatar)
        return valisland
      except:
        print('Invalid!')
    if options in end:
      clear()
      print('chapter 1 ended😊!')

    
def text_val(valisland):
    chosenisland = 'You chose {}!'.format(island[int(valisland)])
    mitten = chosenisland.center(65)
    print(mitten)

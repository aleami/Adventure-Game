#Importerar kapitel 1 filen hit
from chapter1 import *
from time import sleep
from chapter2 import *
from funktioner import *

island2()

#Denna anrop definerar och sätter en rubrik.
#Skriver ut en text mitten på sidan
starttext() 

#rubrik för kapitel 1
kap1_text()

#Inom handling1() funktionen får man välja en avatar via inputen avatar, samt returnerar variabeln avatar
avatar = handling1()

#Här får man välja färdmedel detta är kopplat med en dictionary med inputen alternatives, samt returnerar variabeln alternatives.
alternatives = travel() 

#Här får man en text beroende på vilken båt man väljer. Om man väljer båt 3 så får man reperera den genom att betala vilket görs med en dictionary.
selectboat(avatar,alternatives)

#Printar ut olika texter för spelets början
textislands()

#I variabeln options får man välja om man själv vill vlja en island eller få en slumpad island av se 3 island som finns.
options = val_options()

#Beroende på input man gör i options så hamnar man på olika ö:ar
valisland = islands(avatar, options)

#Avslutar spelet, eller startar om spelet, eller så kan man spela vidare på kapitel 2.
klar(valisland, avatar)
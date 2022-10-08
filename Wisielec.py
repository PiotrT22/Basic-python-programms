from ast import keyword
from operator import index
from itertools import groupby
from os import remove
import getpass

print("Witaj w wisielcu! Poniżej podaj swoje hasło - wpisując je, nie będzie go widać by przeciwnicy nie podglądali: ")
used_letters_set = set()
answer = getpass.getpass("Podaj hasło: ").upper()
letters_remaining = [*answer]
letters_in_answer = [*answer]
health_points = 10
value1 = 0
player_view = []


### functions ###
def print_player_view(value1):    
    print("\n ")

    for _ in letters_in_answer:

        player_view.append("_")
        value1 += 1
        if value1 == len(letters_in_answer):
            return player_view
            



def correct_letter(player_view):
    while True:
        try:
            index_litery = letters_in_answer.index(litera)
            letters_in_answer.remove(litera)
            letters_in_answer.insert(index_litery, 0)
           


            player_view.pop(index_litery)
            player_view.insert(index_litery, litera)
            #print(widok_gracza)

            letters_remaining.remove(litera)
            
        except:
            break
    
   
### main loop ###


print_player_view(value1)

while True:
    print("\n")
    litera = input("Podaj Literę: ").upper()
    if litera in letters_in_answer:
        value2 = 0
        correct_letter(player_view)
        

        if len(letters_remaining) == 0:
            print ("Gratulacje, wygrałeś! Hasło to: " + (answer))
            break
    else:
        health_points -=1
        if health_points == 0:
            print ("Przegrałeś")
            break
        
        print ("Zła odpowiedź, pozostałe żcyia: " + str(health_points))
    print("Hasło:")
    print(player_view)
    used_letters_set.add(litera)
    print("użyte litery: ")
    print (used_letters_set)
from random import randint

while True:
    random_number = randint(1, 100)
    guess = 0
    while True:
        print("Zgadnij liczbę od 1 do 100")
        while random_number != int(guess):
            try:
                
                guess = int(input("Jaka liczba?"))
            
                if guess < random_number:
                    print ("Za mało!")
                if guess > random_number:
                    print("Za dużo!")
                if random_number == int(guess):
                    break
            except: print("Podaj Liczbę a nie litere!")
        user_coice = input("Brawo\nWpisz cokolwiek by zacząć ponownie, lub naciśnij crtl + f4 by zakończyć")
        print("No to jeszcze raz!")
        break

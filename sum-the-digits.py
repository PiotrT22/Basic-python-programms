
numbers_list = []
digits_list =[]
number_of_number = 0


def get_user_input(number_of_number):
    while True:
        try:
            chosen_amount_of_numbers = int(input("Podaj ilość liczb : "))
            break
        except: print("Podaj wartość liczbową!") 


    while True:
        while True:
            try:
                print(f"Podaj {number_of_number + 1} liczbę: ")
                chosen_number = int(input(""))
                break
            except:
                print("Podaj wartość liczbową!")
        numbers_list.append(chosen_number)
        number_of_number += 1
        if chosen_amount_of_numbers == number_of_number:
            return numbers_list

def end_of_the_loop():
    ending = input("Jeszcze raz? \n1 - tak      2 - nie \n")
    if ending == "1":
        pass
    elif ending == "2":
        exit()
    else:
        print("Podaj wartości tylko 1 lub 2")
        end_of_the_loop()

print("Podaj dowolne liczby, a program zsumuje ich cyfry! ")
while True:
    
    get_user_input(number_of_number)

    for number in numbers_list:
        res = list(str(number))
        for _ in res:
            a_digit = int(_)
            digits_list.append(a_digit)

    sum_of_digits = sum(digits_list)
    print ("suma cyfr to: " + str(sum_of_digits))
    end_of_the_loop()
    
    
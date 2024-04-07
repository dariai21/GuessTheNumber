import random
game = True

while game:
    computer_number = random.randint(1, 100)
    number_of_tries = 5
    while number_of_tries != 0:
        player_input = input("Guess the number (1-100): ")
        if not player_input.isdigit():
            print("Input is invalid")
            continue
        player_number = int(player_input)



        if player_number == computer_number:
            print("Congratulations! You guessed the number!")
            break
        elif player_number > computer_number:
            if number_of_tries != 1:
                print("Go lower.")
            else:
                print("No more tries.")
        else:
            if number_of_tries != 1:
                print("Go higher")
            else:
                print("No more tries")
        number_of_tries -= 1


    answer = input('Keep playing? (y/n):')

    if answer == 'y':
        game = True
    elif answer == 'n':
        print("Sorry to see you go :(")
        game = False
    else:
        print("I don't understand. Exiting game.")
        game = False
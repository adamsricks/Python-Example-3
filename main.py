import cupgame as cg
import random as rand

def main():
    again = True
    win_streak = 0
    cg.welcome_message()

    while again:
        cup_number_loop = True
        while cup_number_loop:
            cup_number = int(input("How many cups would you like to play with? (2-9) "))
            if cup_number > 9 or cup_number < 1:
                print("Please input a number 2-9")
            else:
                cup_number_loop = False

        if cup_number == 1:
            print()
            print("You found the SECRET ENDING!!")
            cg.print_shrek()
            print("You're an all star my friend.")
            return
        
        cg.print_cup(cup_number)
        cg.print_numbers(cup_number)

        right_answer = rand.randint(1, cup_number)

        print()
        print("There's a ball in one of these cups.")
        print("Which cup is it in?")

        game_answer = int(input("> "))
        print()

        if game_answer == right_answer:
            print("You won!")
            win_streak += 1
            print("You've won {} times in a row!".format(win_streak))
        else:
            print("You lost...")
            print("You lost a win streak of {}".format(win_streak))
            win_streak = 0

        print()

        answer_loop = True
        while answer_loop:
            again_answer = input("Would you like to play again? (y/n) ")
            if again_answer == "n":
                again = False
                answer_loop = False
            elif again_answer == "y":
                again = True
                answer_loop = False
            else:
                print("Please enter 'y' or 'n'")



if __name__ == "__main__":
    main()
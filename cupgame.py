# For displaying cups in a row
def print_cup(number):
    string1 = "     __________      " 
    string2 = "    /          \     "
    string3 = "    /          \     "
    string4 = "   /            \    "
    string5 = "   /            \    "
    string6 = "  /              \   "
    string7 = "  /              \   "
    string8 = " /                \  "
    string9 = " /                \  "
    string10 = "/                  \ "
    string11 = "/__________________\ "

    string_array = [string1, string2, string3, string4, string5, string6, string7, string8, string9, string10, string11]

    for each in string_array:
        for x in range(0, number):
            print(each, end = "")
        print()


# For displaying the numbers under the cups
def print_numbers(number):
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    if number >= 1:
        line1 += "         __          "
        line2 += "        /  \         "
        line3 += "       (_/ /         "
        line4 += "        (__)         "
    if number >= 2:
        line1 += "        ____         "
        line2 += "       (___ \        "
        line3 += "        / __/        "
        line4 += "       (____)        "
    if number >= 3:
        line1 += "        ____         "
        line2 += "       ( __ \        "
        line3 += "        (__ (        "
        line4 += "       (____/        "
    if number >= 4:
        line1 += "         ___         "
        line2 += "        / _ \        "
        line3 += "       (__  (        "
        line4 += "         (__/        "
    if number >= 5:
        line1 += "         ___         "
        line2 += "        / __)        "
        line3 += "       (___ \        "
        line4 += "       (____/        "
    if number >= 6:
        line1 += "         ___         "
        line2 += "        / __)        "
        line3 += "       (  _ \        "
        line4 += "        \___/        "
    if number >= 7:
        line1 += "        ____         "
        line2 += "       (__  )        "
        line3 += "         / /         "
        line4 += "        (_/          "
    if number >= 8:
        line1 += "        ____         "
        line2 += "       / _  \        "
        line3 += "       ) _  (        "
        line4 += "       \____/        "
    if number >= 9:
        line1 += "        ___          "
        line2 += "       / _ \         "
        line3 += "       \__  )        "
        line4 += "       (___/         "
    print(line1)
    print(line2)
    print(line3)
    print(line4)


# For welcoming the user
def welcome_message():   
    print(" _______           _______    _______  _______  _______  _______  ")
    print("(  ____ \|\     /|(  ____ )  (  ____ \(  ___  )(       )(  ____ \ ")
    print("| (    \/| )   ( || (    )|  | (    \/| (   ) || () () || (    \/ ")
    print("| |      | |   | || (____)|  | |      | (___) || || || || (__     ")
    print("| |      | |   | ||  _____)  | | ____ |  ___  || |(_)| ||  __)    ")
    print("| |      | |   | || (        | | \_  )| (   ) || |   | || (       ")
    print("| (____/\| (___) || )        | (___) || )   ( || )   ( || (____/\ ")
    print("(_______/(_______)|/         (_______)|/     \||/     \|(_______/ ")
    print()
                                                                 


# For the secret ending
def print_shrek():
    print("⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ")
    print("⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ")
    print("⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ ")
    print("⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ ")
    print("⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ ")
    print("⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ ")
    print("⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ ")
    print("⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ ")
    print("⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ ")
    print("⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ ")
    print("⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ ")
    print("⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ ")
    print("⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉")



def main():
    welcome_message()


if __name__ == "__main__":
    main()
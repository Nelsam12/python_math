from my_math import *



while True:
    print("1- forme c(ax + b) c étant un réel")
    print("2- forme x(ax + b) x un inconnu")
    print("3- forme (ax + b)(cx + d)")
    print("4- Quitter")
    choice = my_int_input(4.0)
    if choice == 1:
        print(dev_1())
    elif choice == 2:
        print(dev_2())
    elif choice == 3:
        print(dev_3())
    else:
        print("Thanks")
        break
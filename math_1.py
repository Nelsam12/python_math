from my_math import *

while True:
    print("1- Fonction sous la forme f(x) = ax + b")
    print("2- Fonction sous la forme f(x) = ax^2 + bx +c")
    print("3- Fonction sous la forme f(x) = ax^3 + bx^2 +cx + d")
    print("4- Quitter")
    choice = my_int_input(4.0)
    if choice == 1:
        display_solution_1()
    elif choice == 2:
        resolve_functon_2()
    elif choice == 3:
        resolve_function_3()
    else:
        print("Thanks")
        break
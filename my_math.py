def my_int_input(max:float=None):
    x = input("-> ")
    if not x.replace("-", "").isdigit():
        return my_int_input(max)
    if max:
        if float(x) > max:
            return my_int_input(max)
    return float(x)

def get_function_1()->list:
    print('The value of a')
    a = my_int_input()
    print("The value of b")
    b = my_int_input()
    return [a,b]

def get_function_2()->list:
    param:list = get_function_1()
    print(param)
    print("The value of c")
    c = my_int_input()
    param.append(c)
    return param

def my_personal_input(nb: int):
    l = []
    for i in range(nb):
        print(f"The value of {chr(97+i)}")
        l.append(int(my_int_input()))
    print(l)
    return l

def dev_1() -> str:
    l = my_personal_input(3)
    print(f"function : {l[2]}({l[0]}x + {l[1]})")
    dv = f"Forme développée : ({l[2]*l[0]}x {'+' if l[2] * l[1] > 0 else ''} {l[2] * l[1]})"
    return dv

def dev_2() -> str:
    l = my_personal_input(2)
    print(f"function : x({l[0]}x + {l[1]})")
    dv = f"Forme dévloppée : {l[0]}x^2 {'+' if l[1] > 0 else ''} {l[1]}x"
    return dv

def dev_3() -> str:
    l = my_personal_input(4)
    print(f"function : ({l[0]}x + {l[1]})({l[2]}x + {l[3]})")
    dv = f"Forme développée : {l[0]*l[2]}x^2 {'+' if (l[0]*l[3] + l[1] * l[2]) > 0 else ''} {l[0]*l[3] + l[1] * l[2]}x {'+ ' if (l[1]*l[3]) > 0 else ''}{l[1]*l[3]}"
    return dv

def get_function_1()->list:
    print('The value of a')
    a = my_int_input()
    print("The value of b")
    b = my_int_input()
    return [a,b]

def resolve_functon_1() ->float:
    value = get_function_1()
    print("Function : f(x) = {}x + {}".format(value[0], value[1]))
    return float(-value[1]/value[0])

def display_solution_1(x:float = None)->None:
    if not x:
        result = resolve_functon_1()
        print("The solution is x = {}".format(result))
        return None
    print("The solution is x = {}".format(x))

def get_function_2()->list:
    param:list = get_function_1()
    print(param)
    print("The value of c")
    c = my_int_input()
    param.append(c)
    return param

def resolve_functon_2(value:list = None) -> None:
    if not value:
        value = get_function_2()        
    print(value)
    print("Function : f(x) = {}x^2 + {}x + {}".format(value[0], value[1], value[2]))
    delta = calutate_delta(value[0], value[1], value[2])
    print("Delta = {}^2 - 4({})({}) = {}".format(value[1], value[0], value[2], delta))
    if is_positif(delta) == 1:
        racine_delta = (delta)**0.5
        print("Racine delta : {} = {}".format(delta, racine_delta))
        resolve_delta_positive(racine_delta, value[0], value[1], value[2])
    elif is_positif(delta) == 0:
        resolve_delta_null(value[0], value[1])
    else:
        print("Impossible dans R ") 


def calutate_delta(a:float, b:float, c:float) -> float:
    delta = my_pow(b,2) - 4*(a*c)
    return delta

my_pow = lambda a,b : float(a**b)

def is_positif(delta : float) -> int:
    if delta > 0:
        return 1
    if delta == 0:
        return 0
    if delta < 0:
        return -1

def resolve_delta_positive(r_d:float, a:float, b:float, c:float)->None:
    x1 = (-b - r_d)/(2*a)
    x2 = (-b + r_d)/(2*a)
    display_solution_2(x1, x2)

def resolve_delta_null(a:float, b:float):
    x = -b/2*a
    display_solution_1(x)

def display_solution_2(x1:float, x2: float):
    print("The solutions")
    print("x1 = {}".format(x1))
    print("x2 = {}".format(x2))
    
def resolve_function_3() -> None:
    l = my_personal_input(4)
    print("ax^3 + bx^2 +cx + d")
    import os
    cpt = 0
    for i in range(-10000, 10001, 1):
        result = l[0]*my_pow(i, 3) + l[1]*my_pow(i, 2) + l[2] * i + l[3]
        if result == 0:
            cpt += 1
            if i < 0 :
                # rep = input("Voulez-vous les détails ?/n1-Oui/n2-Non")
                # if rep == 1:
                #     print(f"(x + {-i})(ax^2 + bx + c)")
                #     print(f"ax^3 + bx^2 + cx {show_number_and_sign(i)}ax^2 {show_number_and_sign(i)}bx {show_number_and_sign(i)}c")
                #     print(f"ax^3 + (b{show_number_and_sign(-i)}a)x^2 + (c{show_number_and_sign(-i)}b)x{show_number_and_sign(-i)}c = {l[0]}x^3{show_number_and_sign(l[1])}x^2{show_number_and_sign(l[2])}x{show_number_and_sign(l[3], True)}")
                #     print("Par identification")

                #     print(f"ax^3 = {l[0]}x^3\n(b{show_number_and_sign(-i)}a)x^2 = {l[1]}x^2\n(c{show_number_and_sign(-i)}b)x = {l[2]}x\n{i if i not in [-1,1] else ''}c = {l[3]}")
                #     print()
                #     print(f"a = {l[0]}\n(b{show_number_and_sign(-i)}a) = {l[1]}\n(c{show_number_and_sign(-i)}b) = {l[2]}\n{i if i not in [-1,1] else ''}c = {l[3]}")
                a = l[0]
                b = l[1] - a
                c = l[3]
                resolve_functon_2([a,b,c])
                print("x3 = {}".format(i))
            else:
                # print(f"(x - {i})(ax^2 + bx + c)")
                a = l[0]
                b = l[1] + a
                c = -l[3]
                resolve_functon_2([a,b,c])
                print("x3 = {}".format(i))
                
            return None
    print("Pas de solution Trouvé")


def show_number_and_sign(nb, b: bool = False) -> str:
    if nb > 0 and nb != 1:
        return " + " + str(nb)
    if nb < 0 and nb != -1:
        return " - " + str(nb).replace("-","")
    if nb == 0:
        return " 0 "
    if nb == -1:
        return " - "
    if nb == 1 and b:
        return " + " + str(nb)
    return " + "
    
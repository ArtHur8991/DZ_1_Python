#задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

#*Пример:*

#- 6 -> да
#- 7 -> да
#- 1 -> нет

#def InputNumbers(inputText):
#    is_OK = False
#   while not is_OK:
#        try:
#            number = int(input(f"{inputText}"))
#            is_OK = True
#        except ValueError:
#            print("Это не число!")
#    return number

#def checkNumber(num):
#    if 6 <= num <= 7:
#        print("Да")
#    elif 0 < num < 6:
#        print("Нет")
#    else:
#        print("число вне пределов 7 дней")


#num = InputNumbers("Введите число: ")
#checkNumber(num)










#Задача 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

#def inputNumbers(x):
#    xyz = ["X", "Y", "Z"]
#    a = []
#    for i in range(x):
#        a.append(input(f"Введите значение {xyz[i]}: "))
#    return a


#def checkPredicate(x):
#    left = not (x[0] or x[1] or x[2])
#    right = not x[0] and not x[1] and not x[2]
#    result = left == right
#    return result


#statement = inputNumbers(3)

#if checkPredicate(statement) == True:
#    print(f"Утверждение истинно")
#else:
#    print(f"Утверждение ложно")









#Задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#*Пример:*
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3

def inputKoord(x):
    a = [0] * x
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = float(input(f"Введите {i+1} координаты: "))
                a[i] = number
                is_OK = True
                if a[i] == 0:
                    is_OK = False
                    print("Координат не должен быть равен 0 ")
            except ValueError:
                print("Вводить надо числа!")
    return a

def checkCoordinates(xy):
    text = 4
    if xy[0] > 0 and xy[1] > 0:
        text = 1
    elif xy[0] < 0 and xy[1] > 0:
        text = 2
    elif xy[0] < 0 and xy[1] < 0:
        text = 3
    print(f"Точка находится в {text} четверти плоскости")


koordinate = inputKoord(2)
checkCoordinates(koordinate)
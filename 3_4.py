number1 = int(input("Число 1"))
number2 = int(input("Число 2"))
number3 = int(input("Число 3"))
if(number1 >=0 and number2>=0 and number3>=0):
    print("Количество положительных чисел 3, Количество отрицательных чисел 0")
else:
    if (number1 >= 0 and number2 >= 0 or  number3 >= 0 and number2 >= 0 ):
        print("Количество положительных чисел 2, Количество отрицательных чисел 1")
    else:
        if (number1 >= 0 or number2 >= 0 or number3 >= 0):
            print("Количество положительных чисел 1, Количество отрицательных чисел 2")
        else:
            print("Количество положительных чисел 0, Количество отрицательных чисел 3")

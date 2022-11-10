number1 = int(input('Введите число: '))
fuction1 = input('Введите действие +-/*')
number2 = int(input('Введите еще одно число: '))
if fuction1 == '+':
    print(number1 + number2)
elif fuction1 == '-':
    print(number1 - number2)
elif fuction1 == '*':
    print(number1 * number2)
elif fuction1 == '/':
    print(number1 / number2)
else:
    print('Вы ввели неверное действие')
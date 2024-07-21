first = input('Введите первое число: ')
second = input('Введите второе число: ')
thrid = input('Введите третье число: ')
if first == second == thrid:
    print(3)
elif first == second or second == thrid or first == thrid:
    print(2)
else:
    print(0)

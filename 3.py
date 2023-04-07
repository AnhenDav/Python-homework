# my_dict = {'a': 1, 'b': 2, 'c': 3}
# try:
#     value = my_dict['a']
# except KeyError:
#     print('Произошла ошибка KeyError!')
# else:
#     print('Ошибок не произошло!')
# finally:
#     print('Оператор finally выполнен!')
# a = int(input('Введите первое число:'))
# b = int(input('Введите второе число:'))
# try:
#     c = a / b
#     print('Квадрат деления:', c**2)
# except ZeroDivisionError:
#     print('Деление на ноль невозможно')
# finally:
#     print("Программа завершена")
#
# a = int(input('Введите первое число:'))
# b = int(input('Введите второе число:'))
try:
    a = int(input('Введите первое число:'))
    b = int(input('Введите второе число:'))
    c = a / b
except ZeroDivisionError:
    print('Деление на ноль невозможно')
except ValueError:
    print('Неверный тип данных')
except Exception:
    print('Общая ошибка')
finally:
    print('Программа завершена')





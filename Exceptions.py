# # task 1
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# try:
#     value = my_dict['a']
# except KeyError:
#     print('Произошла ошибка KeyError!')
# else:
#     print('Ошибок не произошло!')
# finally:
#     print('Оператор finally выполнен!')
# # task 2
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
# # task 3
# a = int(input('Введите первое число:'))
# b = int(input('Введите второе число:'))
# print()
# # task 4
# try:
#     a = int(input('Введите первое число:'))
#     b = int(input('Введите второе число:'))
#     c = a / b
# except ZeroDivisionError:
#     print('Деление на ноль невозможно')
# except ValueError:
#     print('Неверный тип данных')
# except Exception:
#     print('Общая ошибка')
# finally:
#     print('Программа завершена')
# print()
# def get_input():
#     try:
#         num_1 = int(input('Введите число 1: '))
#         num_2 = int(input('Введите число 2: '))
#     except ValueError:
#         print('Произошла ошибка, введите целочисленное числа!')
#         return get_input()
#     return num_1, num_2
# print(get_input())

import csv

def read_file(file_):
    try:
        f = open(file_)
        content = csv.reader(f)
        print(content)
        return content
    except FileNotFoundError:
        print('Файл не найден, проверьте имя файла')


def write_to_file(file_, content):
    f2 = open(file_, 'w', newline='')
    new_file = csv.DictWriter(f2, content)
    new_file.writerow(f2)

def main():
    donor_file = input('Введите имя исходного файла')
    read_file(donor_file)
    end_file = input('Введите имя конечного файла:')
    
    write_to_file(end_file, content)





read_file('data.csv')


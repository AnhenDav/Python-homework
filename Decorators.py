from datetime import datetime


# def count_the_time(func):
#     def wrapper():
#         start = datetime.now()
#         result = func()
#         print(datetime.now() - start)
#         return result
#
#     return wrapper
#
#
#
#
# @count_the_time
# def create_the_list():
#     list_ = []
#     for i in range (10**5):
#         if i % 2 == 0:
#             list_.append(i)
#     return list_
#
# a = create_the_list()

#  с аргументами:
#
# def count_the_time(func):
#     def wrapper(*args, **kwargs):
#         start = datetime.now()
#         result = func(*args, **kwargs)
#         print(datetime.now() - start)
#         return result
#
#     return wrapper
#
#
#
#
# @count_the_time
# def create_the_list(x):
#     list_ = []
#     for i in range(x):
#         if i % 2 == 0:
#             list_.append(i)
#     return list_
#
# a = create_the_list(125)
#
# def count_the_time(arg):
#     print(f'{arg} - аргумент декоратора count_of_time')
#
#     def outer(func):
#         def wrapper(*args, **kwargs):
#             start = datetime.now()
#             result = func(*args, **kwargs)
#             print(datetime.now() - start)
#             return result
#
#         return wrapper
#
#     return outer
#
#
# @count_the_time('kjcbkjbdvk')
# def create_the_list(x):
#     list_ = []
#     for i in range(x):
#         if i % 2 == 0:
#             list_.append(i)
#     return list_
#
#
# a = create_the_list(1256546)

#Task1
def counter(func):

    def wrapper(*args, **kwargs):
        wrapper.count += 1
        result = func(*args, **kwargs)
        print('{0} функция была вызвана: {1} раз(а)'.format(func.__name__, wrapper.count))
        return result

    wrapper.count = 0
    return wrapper
@counter
def any_function():
    print('123')

any_function()
any_function()
any_function()

# дан список списков. Написать функцию, чтобы получить новый список со значениями, кратными 3. И декоратор, который
# считает количество чисел, не кратных 3
# def not_three_counter(func):
#     def wrapped(some_list):
#         len_some_list = 0
#         for i in some_list:
#             len_some_list += len(i)
#         result = func(some_list)
#         number_not_tree = len_some_list - len(result)
#         return number_not_tree
#
#     return wrapped
#
#
# @not_three_counter
# def func_three(some_list):
#     new_list = []
#     for i in some_list:
#         for num in i:
#             if num % 3 == 0:
#                 new_list.append(num)
#     return new_list
#
#
# f = func_three([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(f)

#
# # ~~~~~~~~~~ второй вариант (ошибка внутри, нужно разбираться) ~~~~~~~~~~~
# def decorator(func):
#     def wrapperd(list_):
#         count = [num for item in list_ for num in item if num % 3 != 0]
#         print(len(count))
#
#     return wrapperd
#
#
# @decorator
# def func(list_):
#     new_list = [num for item in list_ for num in item if num % 3 == 0]
#     return new_list
#
#
# print(func([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

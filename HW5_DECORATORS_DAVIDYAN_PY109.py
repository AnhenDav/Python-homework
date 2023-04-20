'''
Напишите декоратор debug, который при каждом вызове
декорируемой функции выводит её имя (вместе со всеми
передаваемыми аргументами), а затем — какое значение
она возвращает. После этого выводится результат её
выполнения '''


def debug(func):
    def wrapped(*args):
        print(f'Название функции: {func.__name__}')
        print(*args)
        result = func(*args)
        print(f'Результат выполнения функции: {result}')

    return wrapped


@debug
def func_summ(a, b):
    return a + b


func_summ(2, 3)

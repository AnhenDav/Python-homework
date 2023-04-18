# class Human:
#     hands = 2
#
#     def __int__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def do_jump(self):
#         print(self.name, 'прыгнул')
#
#
# human_1 = Human('Richard', 18)
# human_2 = Human('Kate', 74)
#
# human_1.do_jump()
# human_2.do_jump()

# class car:
#     doors = 4
#     wheels = 4
#
#
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
#
#     def drive(self):
#         print(self.model, 'завелось')
#
# class bike(car):
#     doors = None
#     wheels = 2
#
#     def get_on_one_wheel(self):
#         print(self.model, 'встал на одно колесо')
#
#
# car_1 = car('5 series', 'yellow')
# car_2 = car('5 series', 'black')
# bike_1 = ('BMW-1', 'grey')


# class Example:
#     num1 = 1
#     num2 = 2
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def summy(self):
#         return self.num1 + self.num2
#
#     def degree(self):
#         return self.a ** self.b
#
#     def val_a(self):
#         return self.a
#
#
# f = Example(3, 4)
# print(f.summy())
# print(f.degree())
# print(f.val_a())

class Calculator:
    def __init__(self):
        self.num1 = int(input('Укажите первое число:'))
        self.num2 = int(input('Укажите второе число:'))

    def summy(self):
        print(self.num1 + self.num2)

    def dedact(self):
        print(self.num1 - self.num2)

    def mult(self):
        print(self.num1 * self.num2)

    def divis(self):
        print(self.num1 / self.num2)


a = Calculator()
a.summy()
a.dedact()
a.mult()
a.divis()


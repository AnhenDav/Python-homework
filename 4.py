class Human:
    default_name = 'Ivan'
    default_age = 20

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(self.name, self.age, self.__money, self.__house)

    @staticmethod
    def default_info():
        print(Human.default_name, Human.default_age)

    def earn_money(self, amount):
        self.__money += amount
        print(self.__money)


i = Human()
i.info()
i.default_info()
i.earn_money(10)

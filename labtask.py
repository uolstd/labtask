class Person:
    def __init__(self, name, age, address):
        self.__name = name
        self.__age = age
        self.__address = address

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address
person = Person("zaira", 21, "123 iqbal town.")
name = person.get_name()
age = person.get_age()
address = person.get_address()
person.set_name("esha")
person.set_age(20)
person.set_address("ittehad colony.")

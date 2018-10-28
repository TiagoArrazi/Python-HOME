class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        print('Happy Birthday ' + self.name + '!')
        self.age += 1

t = Person('Tiago', 19)

print(type(t))
print(t.name)
print(t.age)

t.birthday()

print(t.age)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self, to_name):
        print("hello " + to_name + 'to ' + self.name)
    
    def introduce(self):
        print('내 이름은' + self.name + "나는 " + str(self.age))

class police(Person):
    def arrest(self, to_arrest):
        print("은 체포됬다" + to_arrest)

class programmer(Person):
    def program(self, to_program):
        print(to_program)


paul = Person('paul', 20)
jenny = police('제니' , 25)
mike = programmer('mike', 15)

jenny.introduce()
jenny.arrest('maple')
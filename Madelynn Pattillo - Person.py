class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work" % self.name)


class Employee(Person):
    def __init__(self, name, age, gender):
        super(Employee, self).__init__(name, age)
        self.gender = gender

    def speak(self):
        print("%s discusses a project for work with their co-workers" % self.name)


class Programmer(Employee):
    def __init__(self, name, age, gender, coding_speed):
        super(Programmer, self).__init__(name, age, gender)
        self.speed = coding_speed

    def code(self):
        print("%s creates the program for a game for their employer. "
              "They type %d lines a minute." % (self.name, self.speed))

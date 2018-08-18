class Person():
    def __init__(self, first_name, last_name):
        self.last_name = last_name
        self.first_name = first_name

    def full_name(self):
        return self.first_name + " " + self.last_name


class Doctor(Person):
    def full_name(self):
        return "Dr. " + super().full_name()
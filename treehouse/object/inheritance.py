class Person():
    def __init__(self, first_name, last_name):
        self.last_name = last_name
        self.first_name = first_name

    def full_name(self):
        return self.first_name + " " + self.last_name


class Doctor(Person):
    def full_name(self):
        return "Dr. " + super().full_name()


class Gender(Person):

    def __init__(self, first_name, last_name, gender):
        super().__init__(first_name, last_name)
        self.gender = gender

    def address(self):
        if self.gender == "male":
            return "Mr." + self.last_name
        elif self.gender == "female":
            return "Ms." + self.last_name
        else:
            raise ValueError("Gender input maybe wrong.")


yang = Gender("Yang", "Hu", "dsafasdfasf")

try:
    yang.address()
except ValueError as err:
    print("Oh no! Something is wrong!")
    print("(Possible Error: {})".format(err))
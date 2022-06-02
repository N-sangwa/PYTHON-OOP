class Student: 
    def __init__(self,first_name, last_name,age):
        self.first_name = first_name
        self.last_name  = last_name
        self.age = age
    def full_name(self):
        return (self.first_name, self.last_name)

    def year_of_birth(self):
        return f"Hello {self.first_name}, you were born in {2022 - self.age}."
    def initials(self):
        x = {self.first_name[0]} , {self.last_name[0]}
        return x

    
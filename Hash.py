import hashlib

class Person:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    def employee_id(self):
        string_to_hash = self.name + self.date_of_birth
        hashed_details = hashlib.md5(string_to_hash.encode())
        return hashed_details.hexidigest()

tom = Person('Tom', '18-11-1992')

print(tom.name)
print(tom.date_of_birth)
print(tom.employee_id)
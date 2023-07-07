class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        if self.age <= 3:
            return 0
        elif self.age < 20:
            return 1000
        elif 20 <= self.age < 65:
            return 1500
        elif self.age >= 75:
            return 500
        else:
            return 1200

    def info_csv(self):
        return f"{self.first_name} {self.family_name},{self.age},{self.entry_fee()}"

    def info_tab(self):
        return f"{self.first_name} {self.family_name}\t{self.age}\t{self.entry_fee()}"

    def info_pipe(self):
        return f"{self.first_name} {self.family_name}|{self.age}|{self.entry_fee()}"

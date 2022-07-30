class User:
    def __init__(self, email, name):
        self.name = name
        self.email = email

    def sign_in(self):
        print("Logged in")


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email, name)
        self._power = power

    def attack(self):
        print(f"attacking with power of {self._power}")


class Archer(User):
    def __init__(self, name, num_arrows, email):
        super().__init__(email, name)
        self._num_arrows = num_arrows

    def attack(self):
        print(f"attacking with arrows: arrows left- {self._num_arrows}")


wizard = Wizard("Merlin", 50, "merlin@mail.com")
archer = Archer("Robin", 100, "robin@mail.com")

wizard.sign_in()
wizard.attack()
archer.attack()

print(isinstance(wizard, User))
print(isinstance(wizard, object))

print(wizard.email)
print(archer.name)

print(dir(wizard))

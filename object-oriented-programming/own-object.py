class PlayerCharacter:
    # class object attributes
    membership = True

    def __init__(self, name, age):
        if PlayerCharacter.membership:
            self.name = name  # attribute or propertie
            self.age = age  # attributes or properties

    def run(self):
        print("run")
        return self.name + " is running."

    def update_membership(self, value):
        self.membership = value


player1 = PlayerCharacter("Max", 22)
player2 = PlayerCharacter("Emily", 23)

player2.age = 28

print(player1.name)
print(player1.age)
print(player1.run())
print(player1.update_membership(False))
print(player1.membership)

# print(player2.name)
# print(player2.age)
# print(player2.run())

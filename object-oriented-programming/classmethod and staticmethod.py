class PlayerCharacter:
    # class object attributes
    membership = True

    def __init__(self, name, age):
        if PlayerCharacter.membership:
            self.name = name  # attribute or propertie
            self.age = age  # attributes or properties

    @classmethod
    def add_thing(cls, num1, num2):
        cls.membership = False

        return cls("Teddy", 56)

    @staticmethod
    def add_thing2(num1, num2):
        return num1 + num2


player = PlayerCharacter.add_thing(2, 3)

print(player)
print(PlayerCharacter.add_thing2(6, 4))
print(PlayerCharacter.membership)

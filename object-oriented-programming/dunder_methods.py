# Dunder methods are identify by starting and ending with "__".
# Dunder method allows us to use them as a function.


class Toy:
    def __init__(self, color, age):
        self.age = age
        self.color = color
        self.my_dict = {"name": "Yoyo", "has_pets": False}

    def __str__(self):
        return f"{self.color}"

    def __len__(self):
        return 5

    def __call__(self):
        return "yess?"

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy("red", 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure["name"])
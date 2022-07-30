class User:
    def sign_in(self):
        print("Logged in")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self._power = power

    def attack(self):
        print(f"attacking with power of {self._power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def check_arrow(self):
        print(f"{self.num_arrows} remaining")

    def run(self):
        print("run really faster than others")


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)


hb = HybridBorg("borgie", 60, 100)

hb.sign_in()
hb.attack()
hb.run()
hb.check_arrow()

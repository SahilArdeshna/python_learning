from ast import pattern
import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = "sahil.ardeshna@mail.com"

a = pattern.search(string)
print(a)

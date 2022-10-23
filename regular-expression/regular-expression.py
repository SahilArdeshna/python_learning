from ast import pattern
import re

pattern = re.compile("this")
string = "search this inside this text please!"

a = pattern.search(string)
# print(a.span()) # returns value of start and end index in tuple
# print(a.start()) # returns value of start index
# print(a.end()) # returns value of end index
# print(a.group())  # returns group value of search text

b = pattern.findall(string)
# print(b) # returns search value in list

c = pattern.fullmatch(string)
# print(c) # returns value if full string match

d = pattern.match(string)
print(d)  # returns value if string match from start

from collections import Counter, defaultdict, OrderedDict

# list = [1, 2, 3, 4, 5, 6, 3]
# print(Counter(list)) # Counter({3: 2, 1: 1, 2: 1, 4: 1, 5: 1, 6: 1})

# random_str = "blah blah blah thinking about python"
# print(Counter(random_str))

# new_dict = defaultdict(lambda: 6, {"a": 1, "b": 2})
# print(new_dict["c"])

dict = OrderedDict()
dict["a"] = 1
dict["b"] = 2

dict2 = OrderedDict()
dict2["a"] = 1
dict2["b"] = 2

print(dict == dict2)

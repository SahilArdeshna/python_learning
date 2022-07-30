class SuperList(list):
    def __len__(self):
        return 1000


super_list = SuperList()
print(super_list.__len__())
super_list.append(5)
print(super_list[0])

print(issubclass(SuperList, list))

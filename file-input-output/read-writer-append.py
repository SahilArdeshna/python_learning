# with open("test.txt") as test_file:
# print(test_file.readlines())

# Mode is for read, write, append and many more things

# Write
# with open("new_file.txt", mode="w") as new_file:
#     text = new_file.write("Hey, it's me!")
#     print(text)

# Read
# with open("new_file.txt", mode="r+") as new_file:
#     text = new_file.write("Hey, it's me!")
#     print(text)

# Append
with open("new_file.txt", mode="a") as new_file:
    text = new_file.write(" How are you?")
    print(text)

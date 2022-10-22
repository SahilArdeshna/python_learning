try:
    # Append
    with open("script.txt", mode="x") as new_file:
        print(new_file.read())
except FileNotFoundError as err:
    print("File not exist!")
    raise err
except IOError as err:
    print("IO error")
    raise err

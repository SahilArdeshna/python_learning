# Error handling

while True:
    try:
        age = int(input("What is you age?"))
        10 / age
        # raise ValueError("Hey, cut it out.")
        raise Exception("Hey, cut it out.")
    except ZeroDivisionError:
        print("Please enter age higher than 0!")
        break
    else:
        print("Thank You!")
        break
    finally:
        print("Ok, i am finally done")

    print("Can you hear me?")

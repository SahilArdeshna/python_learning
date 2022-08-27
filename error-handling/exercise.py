# Error handling

while True:
    try:
        age = int(input("What is you age?"))
        10 / age
    except ValueError:
        print("Please enter a number!")
        continue
    except ZeroDivisionError:
        print("Please enter age higher than 0!")
        break
    else:
        print("Thank You!")
        break
    finally:
        print("Ok, i am finally done")

    print("Can you hear me?")

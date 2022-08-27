# Error handling

while True:
    try:
        age = int(input("What is you age?"))
        10 / age
    except ValueError:
        print("Please enter a number!")
    except ZeroDivisionError:
        print("Please enter age higher than 0!")
    else:
        print("Thank You!")
        break

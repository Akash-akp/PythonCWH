a = int(input("Enter your age: "))

match a:
    case 18:
        print("Eligible for vote")
    case 0:
        print("Enter correct age")
    case _:
        print("Not Eligible for vote")
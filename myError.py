try:
    a = input()
    print(int(a)+1)
except ValueError:
    print("ValueError")

b = int(input("Enter a number between 2 and 5(inclusive) :"))

if 2 <= b <= 5:
    print(b)
else:
    raise ValueError("number should be between 2 and 5 inclusively")

from threading import Timer

print("---Welcome to KBC---".center(100))

def Q1():
    print ("""Question 1:
Which of the following program run with indentation?
1.Java
2.C++
3.C
4.Python""")
    a = int(input("Enter Answer :"))
    if a==4:
        print("Correct answer!! You win 10Rupees")
    else:
        print("Wrong answer!! You will get babaji ka thulu")
        return
    print()
    print("Get ready for question 2")
    Timer(2.0,Q2).start()

def Q2():
    print("""Which of the following is constant list?
1.String
2.List
3.Tuple
4.Array List""")
    a = int(input("Enter Answer :"))
    if a == 3:
        print("YAY!! You win 15Rupees... You become 15 rupees pati ")
    else:
        print("Wrong answer!! Go Home with 10Rupees")

print("Get ready for question 1.....")
t = Timer(2.0, Q1)
t.start()
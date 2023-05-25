import random
import string

choice = int(input("1:decode the secret message\n2:Encode a message to secret message\nEnter the choice:"))

def decode(x):
    temp = x.split()
    ans = ""
    for i in temp:
        if(len(i)<=3):
            ans = ans + i[::-1] +" "
        else:
            ans = ans + i[-4:-3] + i[3:-4] + " "
    return ans

print()
if choice == 1:
    print("For Example message: yM YjCamenMxU si VenuzanMtlM WtMibusujiKzmf")
s = input("Enter the message:");
if choice == 1:
    try:
        print(decode(s))
    except:
        print("Invalid secret code")
    quit()



li = s.split();

ans = [];

for i in li:
    if(len(i)<=3):
        ans.append(i[::-1])
    else:
        tf = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(3))
        tl = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(3))
        ans.append(tf+i[1:]+i[0]+tl)

a = ""

for i in ans:
    a = a+i+" "

print(a)

is_decode = input("Do you want to decode(y/n)")


if is_decode[0] == 'y':
    ans = decode(a)
    print(ans)

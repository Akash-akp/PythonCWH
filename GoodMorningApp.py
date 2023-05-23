import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)

timenow = int(time.strftime('%H'))
if(timenow<12):
    print("Good Morning")
elif (timenow==12):
    print("Noon")
elif (timenow<17):
    print("Good AfterNoon")
elif (timenow<20):
    print("Good Evening")
else:
    print("Good Night")
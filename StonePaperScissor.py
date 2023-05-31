import random

y = random.randint(0, 2)

match = {
    1: [0, -1, 1],
    2: [1, 0, -1],
    3: [-1, 1, 0]
}

x = int(input("""Hii Welcome to stone paper and scissor game
1:Stone
2:Paper
3:Scissor
Enter your choice:"""))

def choice(c):
    match c:
        case 1:
            return "Stone"
        case 2:
            return "Paper"
        case 3:
            return "Scissor"


def result(r):
    match r:
        case 0: return "Draw!!!"
        case 1: return "Congratulation!! You win"
        case -1: return "You lose..."

res = match[x][y]

print("You choose:",choice(x))
print("Computer choose:",choice(y+1))
print()
print(result(res))

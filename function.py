def average(*numbers):
    sum = 0
    for number in numbers:
        sum = sum + number
    return sum/len(numbers)

print(average(4,4,4,6,7,8))

def average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(average([10, 20]))
print(average([8]))
print(average([]))


def average(numbers):
    total = 0
    for number in numbers:
        total += number
    if len(numbers) > 0:
        return total / len(numbers)
    else:
        return 0.0
    
print(average([10, 20])) # 15.0
print(average([8])) # 8.0
print(average([])) # 0.0
#for loops

for loop_counter in range(9, 0, -1):
    print(f"Round {loop_counter}")
print("Finished!")


name = 'Tomas Sandnes'
print(name[:5])
print(name[6:13])


total = 0
for number in range(2, 21, 2):
    print(number)
total += number
print(f"Total: {total}")
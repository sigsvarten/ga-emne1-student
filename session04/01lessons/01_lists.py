
guests = ['Sigvart', 'Pelle', 'Batman']
print(guests)
print()

mixed = ['Sigvart', 37, True]
print(mixed)
print()

print(guests[0])
print(guests[1])
print(guests[-1])
print()

guests.append('Animal')
guests.remove('Batman')
print(guests)
print(len(guests))
print()

for guests in guests:
    print(f'Welcome, {guests}')

print()
scores = [44, 57, 96, 84, 28, 75]

print(len(scores))
print(sum(scores))

average = sum(scores) / len(scores)
print(f'Average is {average}')

print(min(scores))
print(max(scores))
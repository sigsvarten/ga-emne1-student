#Temperaturmåling

degree = [23, 21, 22, 32, 25, 12, 9]

for deg in degree:
    print(f'Degree {deg}')


average_degree = sum(degree) / len(degree)
print()
print(f'Lowest: {min(degree)}')
print(f'Highest: {max(degree)}')
print(f'Average: {average_degree}')

if deg < 10:
    print('Cold day')

# Finne det største nummeret

def find_largest(first_number,second_number):
    if first_number > second_number:
        print (f'{first_number} is the biggest')
        return first_number
    elif first_number < second_number:
        print(f'{second_number} is the biggest')
        return second_number
    else:
        print(f'{first_number} and {second_number} is the same')
        return first_number, second_number

find_largest(6,6)
find_largest(6,5)
find_largest(6,8)
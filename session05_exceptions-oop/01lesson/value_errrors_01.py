
try:
    age = int(input("Age: "))
except ValueError:
    print('Not valid!')
else:
    print(f"Next year: {age + 1}")

print('Done')

# Last line of the traceback:
# ValueError: invalid literal forint()
# with base 10: 'twenty'
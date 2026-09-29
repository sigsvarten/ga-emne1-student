#analyser tekst
while True:
    text = input('Tap in the text here: ')

    if not text.strip():
        print('This is not correct. Please try again')
        continue
    break

counting_with_space = len(text)
counting_without_space = len(text.replace(' ',''))
backwards = text[::-1]
contains_python = 'python' in text.lower()

print(f'Total sign with space is {counting_with_space}')
print(f'Total sign without space is {counting_without_space}')
print(f'The text in lower signs: {text.lower()}')
print(f'The text backwards: {backwards}')
print(f'Contains Python: {'Yes' if contains_python else 'No'}')















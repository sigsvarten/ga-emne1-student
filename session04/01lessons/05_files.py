import pathlib
from pathlib import Path

print(f'Current directory is: {Path.cwd()}')
data_directory = Path(' ') / 'data'
prices_path = data_directory / 'prices.txt'

print(data_directory)
print(f'Directory exists: {data_directory.exists()}')
print(prices_path)

with open(prices_path, 'r', encoding='utf-8') as file:
    content = file.read()
print()

prices  = []
with open(prices_path, 'r', encoding='utf-8') as file:
    for line in file:
        price = float(line.strip())
        prices.append(price)
print(prices)

report_path = data_directory / 'price_report.txt'

with open(prices_path, 'w', encoding='utf-8') as file:
    file.write('First line\n')


with open(prices_path, 'a', encoding='utf-8') as file:
    file.write('Another line\n')



report_lines = [
    'Item: Orange',
    'Amount: 24',
    'Price: 65.30'
]

with open(prices_path, 'w', encoding='utf-8') as file:
    for lines in report_lines:
        file.write(line + '\n')

with open(prices_path, 'a', encoding='utf-8') as file:
    file.write('Comment: Remember blueberry')



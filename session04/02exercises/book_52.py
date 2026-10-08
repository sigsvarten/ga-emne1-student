#bokinformawjon

book = {
    'author': 'Jo Nesbø',
    'title':  'Harry Hole',
    'pages': 369,
    'available': True
}

print(f'Title of the book is {book['title']} and the author is {book['author']}')
print()
book['available'] = False
book['year'] = 2012

print(book)
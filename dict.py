import json

book = {
    'title': 'To Kill a Mockingbird',
    'author': 'Harper Lee',
    'year': 1960,
    'genre': 'Fiction'
}
book_json = json.dumps(book)
print(book_json)

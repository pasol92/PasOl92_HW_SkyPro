from book import Book

library = [
    Book("Война и мир", "Лев Толстой"),
    Book("Путешествие из Петербурга в Москву", "Александр Радищев"),
    Book("Соловей и роза", "Оскар Уайльд")
]

for book in library:
    print(f"Автор книги {book.bookTitle} - {book.bookAuthor}")

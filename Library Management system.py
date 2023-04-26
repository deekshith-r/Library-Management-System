class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def list_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author} (ISBN: {book.isbn})")

library = Library()

while True:
    print("\nLibrary Management System\n")
    print("1. Add book")
    print("2. Remove book")
    print("3. Search book")
    print("4. List books")
    print("5. Exit")
    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        isbn = input("Enter ISBN: ")
        book = Book(title, author, isbn)
        library.add_book(book)
        print("Book added successfully.")

    elif choice == 2:
        title = input("Enter book title: ")
        book = library.search_book(title)
        if book is not None:
            library.remove_book(book)
            print("Book removed successfully.")
        else:
            print("Book not found.")

    elif choice == 3:
        title = input("Enter book title: ")
        book = library.search_book(title)
        if book is not None:
            print(f"{book.title} by {book.author} (ISBN: {book.isbn})")
        else:
            print("Book not found.")

    elif choice == 4:
        library.list_books()

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")

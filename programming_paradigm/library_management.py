class Book:
    """Represents a book with a title, author, and checkout status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns True if the book is not checked out."""
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    """Manages a collection of books."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by title if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"'{title}' has been checked out.")
                return
        print(f"Book '{title}' is not available for checkout.")

    def return_book(self, title):
        """Returns a book by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"'{title}' has been returned.")
                return
        print(f"Book '{title}' is not currently checked out.")

    def list_available_books(self):
        """Prints all books that are currently available."""
        available = [book for book in self._books if book.is_available()]
        if not available:
            print("No books available.")
        else:
            for book in available:
                print(book)

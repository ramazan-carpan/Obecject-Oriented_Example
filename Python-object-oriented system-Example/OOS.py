class Book:
    """Base Class representing a book."""

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True  # Added this attribute to track availability

    def borrow(self):
        """Method to borrow a book."""
        if self.is_available:
            self.is_available = False
            return f"You have successfully borrowed '{self.title}'."
        else:
            return f"Sorry, '{self.title}' is currently not available."

    def return_book(self):
        """Method to return a book."""
        self.is_available = True
        return f"'{self.title}' has been successfully returned."

    def __str__(self):
        """String representation of the Book object."""
        availability = "Available" if self.is_available else "Not Available"
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {availability}"


class EBook(Book):
    """Derived class representing an electronic book."""

    def __init__(self, title, author, isbn, file_format):
        super().__init__(title, author, isbn)
        self.file_format = file_format

    def read_online(self):
        """Method to read the ebook online."""
        return f"Reading '{self.title}' in {self.file_format} format online."

    def __str__(self):
        """Override the string representation for EBook."""
        return super().__str__() + f", Format: {self.file_format}"


class Library:
    """Class representing a library."""

    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Method to add a book to the library."""
        self.books.append(book)
        return f"'{book.title}' has been added to the library."

    def list_books(self):
        """List all books in the library."""
        return "\n".join(str(book) for book in self.books)

    def search_book(self, title):
        """Search for a book in the library by title."""
        for book in self.books:
            if book.title.lower() == title.lower():
                return str(book)
        return f"No book found with title '{title}'."


# Example Usage
if __name__ == "__main__": #enry point program
    # Create library
    library = Library()

    # Create books
    book1 = Book("1984", "George Orwell", "123456789")
    ebook1 = EBook("Digital Fortress", "Dan Brown", "987654321", "PDF")

    # Add books to library
    library.add_book(book1)
    library.add_book(ebook1)

    # List books in the library
    print("Books in the Library:")
    print(library.list_books())

    # Borrow and return books
    print(book1.borrow())
    print(ebook1.read_online())
    print(ebook1.borrow())
    print(ebook1.return_book())
    print(book1.borrow())

    # Search for books
    print(library.search_book("1984"))
    print(library.search_book("Inferno"))

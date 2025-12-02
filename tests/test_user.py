import pytest
from src.book import Book
from src.user import User, Librarian


class TestUser:
    def test_user_creation(self):
        user = User("Анна")
        assert user.name == "Анна"
        assert user.get_borrowed_books() == []

    def test_user_borrow_success(self):
        user = User("Анна")
        book = Book("Война и мир", "Толстой", 1869)

        assert user.borrow(book) == True
        assert book in user.get_borrowed_books()
        assert book.is_available() == False

    def test_user_borrow_failure(self):
        user1 = User("Анна")
        user2 = User("Мария")
        book = Book("Война и мир", "Толстой", 1869)

        user1.borrow(book)
        assert user2.borrow(book) == False
        assert book not in user2.get_borrowed_books()

    def test_user_return_book(self):
        user = User("Анна")
        book = Book("Война и мир", "Толстой", 1869)

        user.borrow(book)
        assert user.return_book(book) == True
        assert book not in user.get_borrowed_books()
        assert book.is_available() == True

    def test_user_return_book_not_borrowed(self):
        user = User("Анна")
        book = Book("Война и мир", "Толстой", 1869)

        assert user.return_book(book) == False


class TestLibrarian:
    def test_librarian_creation(self):
        librarian = Librarian("Мария")
        assert librarian.name == "Мария"
        assert isinstance(librarian, User)

    def test_librarian_inheritance(self):
        librarian = Librarian("Мария")
        book = Book("Война и мир", "Толстой", 1869)

        # Проверяем, что Librarian может использовать методы User
        assert librarian.borrow(book) == True
        assert book in librarian.get_borrowed_books()
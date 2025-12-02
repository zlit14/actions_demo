import pytest
from src.library import Library
from src.book import Book, PrintedBook
from src.user import User, Librarian


class TestLibrary:
    def setup_method(self):
        self.library = Library()
        self.book1 = Book("Война и мир", "Толстой", 1869)
        self.book2 = PrintedBook("Преступление и наказание", "Достоевский",
                                 1866, 480, "плохая")
        self.user = User("Анна")

    def test_add_book(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

        # Проверяем косвенно через поиск
        found = self.library.find_book("Война и мир")
        assert found == self.book1

    def test_remove_book_success(self):
        self.library.add_book(self.book1)
        assert self.library.remove_book("Война и мир") == True

        found = self.library.find_book("Война и мир")
        assert found is None

    def test_remove_book_failure(self):
        assert self.library.remove_book("Несуществующая книга") == False

    def test_add_user(self):
        self.library.add_user(self.user)
        # Проверяем через внутренний метод _find_user
        # Так как _find_user protected, можем проверить через публичные методы
        self.library.lend_book("Война и мир",
                               "Анна")  # Книги нет, но пользователь найдется

    def test_find_book(self):
        self.library.add_book(self.book1)

        found = self.library.find_book("Война и мир")
        assert found == self.book1

        not_found = self.library.find_book("Несуществующая")
        assert not_found is None

    def test_lend_book_success(self):
        self.library.add_book(self.book1)
        self.library.add_user(self.user)

        # Мокаем вывод в консоль
        import io
        import sys

        captured_output = io.StringIO()
        sys.stdout = captured_output

        result = self.library.lend_book("Война и мир", "Анна")

        sys.stdout = sys.__stdout__

        assert result == True
        assert not self.book1.is_available()
        assert self.book1 in self.user.get_borrowed_books()

    def test_lend_book_book_not_found(self):
        self.library.add_user(self.user)

        result = self.library.lend_book("Несуществующая", "Анна")
        assert result == False

    def test_lend_book_user_not_found(self):
        self.library.add_book(self.book1)

        result = self.library.lend_book("Война и мир", "Неизвестный")
        assert result == False

    def test_return_book_success(self):
        self.library.add_book(self.book1)
        self.library.add_user(self.user)

        # Сначала выдаем книгу
        self.library.lend_book("Война и мир", "Анна")

        # Затем возвращаем
        result = self.library.return_book("Война и мир", "Анна")
        assert result == True
        assert self.book1.is_available()
        assert self.book1 not in self.user.get_borrowed_books()
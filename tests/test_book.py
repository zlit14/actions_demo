import pytest
from src.book import Book, PrintedBook, EBook


class TestBook:
    def test_book_creation(self):
        book = Book("Война и мир", "Толстой", 1869)
        assert book.get_title() == "Война и мир"
        assert book.get_author() == "Толстой"
        assert book.get_year() == 1869
        assert book.is_available() == True

    def test_book_mark_as_taken(self):
        book = Book("Война и мир", "Толстой", 1869)
        book.mark_as_taken()
        assert book.is_available() == False

    def test_book_mark_as_returned(self):
        book = Book("Война и мир", "Толстой", 1869)
        book.mark_as_taken()
        book.mark_as_returned()
        assert book.is_available() == True

    def test_book_str(self):
        book = Book("Война и мир", "Толстой", 1869)
        assert '"Война и мир" - Толстой (1869) - доступна' in str(book)


class TestPrintedBook:
    def test_printed_book_creation(self):
        pbook = PrintedBook("Война и мир", "Толстой", 1869, 1225, "хорошая")
        assert pbook.get_title() == "Война и мир"
        assert pbook.pages == 1225
        assert pbook.condition == "хорошая"

    def test_printed_book_repair(self):
        pbook = PrintedBook("Книга", "Автор", 2020, 100, "плохая")
        pbook.repair()
        assert pbook.condition == "хорошая"

        pbook.repair()
        assert pbook.condition == "новая"

    def test_printed_book_str(self):
        pbook = PrintedBook("Война и мир", "Толстой", 1869, 1225, "хорошая")
        assert "1225 стр., хорошая" in str(pbook)


class TestEBook:
    def test_ebook_creation(self):
        ebook = EBook("Мастер и Маргарита", "Булгаков", 1966, 384, 5, "epub")
        assert ebook.get_title() == "Мастер и Маргарита"
        assert ebook.pages == 384
        assert ebook.file_size == 5
        assert ebook.format == "epub"

    def test_ebook_str(self):
        ebook = EBook("Мастер и Маргарита", "Булгаков", 1966, 384, 5, "epub")
        assert "384 стр., 5 МБ, epub" in str(ebook)
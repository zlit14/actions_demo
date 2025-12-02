class User:
    def __init__(self, name):
        self.name = name
        self.__borrowed_books = []

    def borrow(self, book):
        if book.is_available():
            book.mark_as_taken()
            self.__borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.__borrowed_books:
            book.mark_as_returned()
            self.__borrowed_books.remove(book)
            return True
        return False

    def show_books(self):
        if not self.__borrowed_books:
            print(f"{self.name} не имеет взятых книг")
        else:
            print(f"Книги {self.name}:")
            for book in self.__borrowed_books:
                print(f"  - {book.get_title()}")

    def get_borrowed_books(self):
        return self.__borrowed_books.copy()


class Librarian(User):
    def add_book(self, library, book):
        library.add_book(book)

    def remove_book(self, library, title):
        library.remove_book(title)

    def register_user(self, library, user):
        library.add_user(user)

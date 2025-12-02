class Library:
    def __init__(self):
        self.__books = []
        self.__users = []

    def add_book(self, book):
        self.__books.append(book)

    def remove_book(self, title):
        for book in self.__books:
            if book.get_title() == title:
                self.__books.remove(book)
                return True
        return False

    def add_user(self, user):
        self.__users.append(user)

    def find_book(self, title):
        for book in self.__books:
            if book.get_title() == title:
                return book
        return None

    def show_all_books(self):
        print("Все книги в библиотеке:")
        for book in self.__books:
            print(f"  - {book}")

    def show_available_books(self):
        print("Доступные книги:")
        for book in self.__books:
            if book.is_available():
                print(f"  - {book}")

    def lend_book(self, title, user_name):
        book = self.find_book(title)
        if not book:
            print(f"Книга '{title}' не найдена")
            return False

        user = self._find_user(user_name)
        if not user:
            print(f"Пользователь '{user_name}' не найден")
            return False

        if user.borrow(book):
            print(f"Книга '{title}' выдана пользователю {user_name}")
            return True
        else:
            print(f"Книга '{title}' недоступна")
            return False

    def return_book(self, title, user_name):
        book = self.find_book(title)
        if not book:
            print(f"Книга '{title}' не найдена")
            return False

        user = self._find_user(user_name)
        if not user:
            print(f"Пользователь '{user_name}' не найден")
            return False

        if user.return_book(book):
            print(f"Книга '{title}' возвращена пользователем {user_name}")
            return True
        else:
            print(f"Книга '{title}' не была взята пользователем {user_name}")
            return False

    def _find_user(self, name):
        for user in self.__users:
            if user.name == name:
                return user
        return None
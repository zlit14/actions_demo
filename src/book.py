class Book:
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__available = True

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__year

    def is_available(self):
        return self.__available

    def mark_as_taken(self):
        self.__available = False

    def mark_as_returned(self):
        self.__available = True

    def __str__(self):
        status = "доступна" if self.__available else "выдана"
        return f'"{self.__title}" - {self.__author} ({self.__year}) - {status}'


class PrintedBook(Book):
    def __init__(self, title, author, year, pages, condition):
        super().__init__(title, author, year)
        self.pages = pages
        self.condition = condition

    def repair(self):
        if self.condition == "плохая":
            self.condition = "хорошая"
        elif self.condition == "хорошая":
            self.condition = "новая"

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, {self.pages} стр., {self.condition}"


class EBook(Book):
    def __init__(self, title, author, year, pages, file_size, format):
        super().__init__(title, author, year)
        self.pages = pages
        self.file_size = file_size
        self.format = format

    def download(self):
        print(f"Книга '{self.get_title()}' загружается...")

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, {self.pages} стр., {self.file_size} МБ, {self.format}"

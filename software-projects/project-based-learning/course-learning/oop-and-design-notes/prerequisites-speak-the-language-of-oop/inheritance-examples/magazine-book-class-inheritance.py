class Book:
    def __init__(self, page_numbers: int, author: str, category: str):
        self.pageNumbers = page_numbers
        self.__author = author
        self.category = category

    def get_author(self) -> str:
        return self.__author

class Magazine(Book):
    def __init__(self, page_numbers: int, author: str, category: str, vogue: bool, adult_rated: bool):
        super().__init__(page_numbers, author, category)
        self.vogue = vogue
        self._adult_rated = adult_rated

    def __str__(self) -> str:
        return f"Info on Magazine -> Author: {self.get_author()}, Page Numbers: {self.pageNumbers}, Category: {self.category}, Vogue? : {self.vogue}, Adult Rated? : {self._adult_rated}"

Vogue = Magazine(23, "Anna Wintour", "Fashion", True, False)

print(Vogue)
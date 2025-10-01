class Book:
    def __init__(self, page_numbers: int, author: str, category: str):
        self.pageNumbers = page_numbers
        self.author = author
        self.category = category

    def __str__(self) -> str:
        return (f"Details of Book -> "
                f"Page Numbers: {self.pageNumbers} ->"
                f" Author: {self.author} ->"
                f" Category: {self.category}")

    def get_page_numbers(self)-> int:
        return self.pageNumbers

    def set_page_numbers(self, page_numbers: int):
        self.pageNumbers = page_numbers

    def get_author(self)-> str:
        return self.author

    def set_author(self, author: str):
        self.author = author

    def get_category(self)-> str:
        return self.author

    def set_category(self, category: str):
        self.category = category


Harry_Potter = Book(312321, "JK Rowling", "Sci Fi Fiction")

print(Harry_Potter)

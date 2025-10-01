class Book:
    def __init__(self, page_numbers: int, author: str, category: str):
        self.pageNumbers = page_numbers
        self.__author = author
        self.category = category

    def get_author(self) -> str:
        return self.__author

    def monologue(self):
        return (f"I am in the category '{self.category}' written by {self.get_author()}. "
                f"I hold {self.pageNumbers} pages of knowledge and imagination.")

    def __str__(self):
        return (f"{self.pageNumbers} "
                f"{self.category} "
                f"{self.get_author()}")

class Magazine(Book):
    def __init__(self, page_numbers: int, author: str, category: str, vogue: bool, adult_rated: bool):
        super().__init__(page_numbers, author, category)
        self.vogue = vogue
        self._adult_rated = adult_rated

    def monologue(self):
        return (f"I am a '{self.category}' magazine crafted by {self.get_author()}. "
                f"My {self.pageNumbers} glossy pages are filled with style, culture, "
                f"and trends that shape the modern world. "
                f"{'I define fashion at its peak. ' if self.vogue else ''}"
                f"{'Note: I’m tailored for adult audiences only.' if self._adult_rated else 'I’m suitable for all readers who crave inspiration.'}")

    def __str__(self) -> str:
        return f"Info on Magazine -> Author: {self.get_author()}, Page Numbers: {self.pageNumbers}, Category: {self.category}, Vogue? : {self.vogue}, Adult Rated? : {self._adult_rated}"

HarryPotter = Book(424, "J.K Rowling", "Fiction")
Vogue = Magazine(23, "Anna Win-tour", "Fashion", True, False)

print(HarryPotter)
print(Vogue)
print(HarryPotter.monologue())
print(Vogue.monologue())
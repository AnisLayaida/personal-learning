class Book:
    def __init__(self, page_numbers: int, author: str, category: str):
        self.pageNumbers = page_numbers
        self._author = author
        self.__category = category

    def get_author(self) -> str:
        return self._author

    def set_author(self, author: str):
        self._author = author

    def get_category(self) -> str:
        return self.__category

    def set_category(self, category: str):
        self.__category = category

    def monologue(self):
        return (f"I am in the category '{self.get_category()}' written by {self.get_author()}. "
                f"I hold {self.pageNumbers} pages of knowledge and imagination.")

    def __str__(self):
        return (f"{self.pageNumbers} "
                f"{self.get_category()} "
                f"{self.get_author()}")

class Magazine(Book):
    def __init__(self, page_numbers: int, author: str, category: str, vogue: bool,front_cover: str, adult_rated: bool):
        super().__init__(page_numbers, author, category)
        self.vogue = vogue
        self._frontCover = front_cover
        self.__adultRated = adult_rated

    def get_front_cover(self) -> str:
        return self._frontCover

    def set_front_cover(self, front_cover: str):
        self._frontCover = front_cover

    def get_adult_rated(self) -> bool:
        return self.__adultRated

    def set_adult_rated(self, adult_rated: bool):
        self.__adultRated = adult_rated

    def monologue(self):
        return (f"I am a '{self.get_category()}' magazine crafted by {self.get_author()}. "
                f"My {self.pageNumbers} glossy pages are filled with style, culture, "
                f"and trends that shape the modern world. "
                f"{'I define fashion at its peak. ' if self.vogue else ''}"
                f"{'Note: I’m tailored for adult audiences only.' if self.get_adult_rated else 'I’m suitable for all readers who crave inspiration.'}")

    def __str__(self) -> str:
        return f"Info on Magazine -> Author: {self.get_author()}, Page Numbers: {self.pageNumbers}, Category: {self.get_category()}, Vogue? : {self.vogue}, Adult Rated? : {self.get_adult_rated()}"

HarryPotter = Book(424, "J.K Rowling", "Fiction")
Vogue = Magazine(23, "Anna Win-tour", "Fashion", True, "Kim K", False)

print(HarryPotter)
print(Vogue)
print(HarryPotter.monologue())
print(Vogue.monologue())
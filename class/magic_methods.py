
class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return self.num_pages + other.num_pages
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            f"Key '{key}' was not found"
    
book1 = Book("prva", "Žiga", 2345)
book2 = Book("Ful dobra knjiga", "Mia", 456)
book3 = Book("prva", "Žiga", 67)

print(book1)
print(book2)
print(book1 == book3)
print(book1 < book3)
print(book2 > book3)
print(book1 + book2)
print("dobra" in book2)
print(book2['title'])
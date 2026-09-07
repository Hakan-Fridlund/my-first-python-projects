"""
Library system: handles books, loan and returns.
"""

CURRENT_YEAR = int(2026)

class Book:
    """
    Represents a book in the librarysystem.
    Handles title and author, year and if it is available.
    """
    def __init__(self, title, author, year, is_borrowed):
        self.title = title.strip().capitalize()
        self.author = author.strip().title()
        self.year = int(year)
        self.is_borrowed = is_borrowed


    def __str__(self):
        status = "The book is borrowed." if self.is_borrowed else "The book is available."
        return (
            f"Title: {self.title}, "
            f"Author: {self.author}, "
            f"Year: {self.year}, "
            f"{status}"
        )

    def borrow(self,):
        """
         Marks the book as borrowed.
         Returns:
            str: A message indicating whether the book was successfully borrowed
            or if it was already borrowed.
        """
        if self.is_borrowed:
            return "The book is already borrowed to someone."
        self.is_borrowed = True
        return f"{self.title} is now borrowed."

    def return_book(self,):
        """
        Marks a book as not borrowed.
        Returns:
             Str: A message indicating whether the book was successfully
             or if it was not borrowed.
        """
        if not self.is_borrowed:
            return "The book is already returned."
        self.is_borrowed = False
        return f"{self.title} by {self.author} is returned"


class Library:
    """
    Represents a library of books.
    Handles file for save and load, adding and removing books.
    """
    def __init__(self, filename):
        self.books = []
        self.filename = filename

    def __str__(self):
        return "\n".join(str(book) for book in self.books)

    def add_book(self, book):
        """
        Adds a book to the library.
        Parameters:
            book
        Returns:
            str: A message indicating whether the book was successfully added
        """
        self.books.append(book)
        return f"{book.title} by: {book.author} is added."

    def remove_book(self, book):
        """
        Removes a book from the library.
        :param: book
        :return: message indicating whether the book was successfully added
        :rtype: str
        """
        if not book in self.books:
            return "That book cannot be found in the library."
        self.books.remove(book)
        return f"{book.title} by {book.author} is now removed."


    def load_from_file(self):
        """
        loads a file with the library. and printing error messages for skipped lines
        """
        self.books = []
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                for line in file:
                    parts = line.strip().split(";")

                    if len(parts) != 4:
                        print(f"Skipping invalid line: {line.strip()}")
                        continue

                    title, author, year, is_borrowed = parts

                    if not year.isdigit():
                        print(f"Skipping line with invalid year: {line.strip()}")
                        continue

                    book = Book(title, author, int(year), is_borrowed == "True")
                    self.books.append(book)

        except FileNotFoundError:
            pass


    def save_to_file(self):
        """
        Saves the library to file.
        """
        with open(self.filename, "w", encoding="utf-8") as file:
            for book in self.books:
                line = f"{book.title};{book.author};{book.year};{book.is_borrowed}\n"
                file.write(line)




def menu(library):
    """
    Runs the menu and takes input to send to functions
    :param library: Library object that stores all books and provides operations.
    :return: None
    """
    while True:
        print("\n1. Add book")
        print("2. List books")
        print("3. Remove book")
        print("4. Loan book")
        print("5. Return book")
        print("6. Save to file")
        print("7. Load from file")
        print("8. Exit")

        choice = input("Choice: ")


        match choice:
            case "1":
                while True:
                    title = input("Please enter book title: ").strip().capitalize()
                    if title:
                        break
                    print("Title cannot be empty, try again.")

                while True:
                    author = input("Please enter book author: ").strip().title()
                    if author:
                        break
                    print("Author cannot be empty, try again.")

                while True:
                    year = input("Please enter book year: ").strip()

                    if not year:
                        print("Year cannot be empty")
                        continue
                    if not year.isdigit():
                        print("Year need to be a number")
                        continue
                    if int(year) > CURRENT_YEAR:
                        print("Year cannot be in the future")
                        continue
                    break
                year= int(year)
                book = Book(title, author, year, False)
                print(library.add_book(book))

            case "2":
                if not library.books:
                    print("There are no books in library.")
                else:
                    for book in library.books:
                        print(book)

            case "3":
                found = False
                title = input("Title to remove: ")
                title = title.lower().capitalize()
                for book in library.books[:]:
                    if book.title == title:
                        print (library.remove_book(book))
                        found = True

                if not found:
                    print("Title not found.")

            case "4":
                found = False
                title = input("Please enter book you want to borrow: ")
                title = title.lower().capitalize()
                for book in library.books:
                    if book.title == title:
                        print (book.borrow())
                        found = True
                        break

                if not found:
                    print("Title not found.")

            case "5":
                found = False
                title = input("Please enter book you want to return: ")
                title = title.lower().capitalize()
                for book in library.books:
                    if book.title == title:
                        print(book.return_book())
                        found = True
                        break

                if not found:
                    print("Title not found.")

            case "6":
                library.save_to_file()
            case "7":
                library.load_from_file()
            case "8":
                break
            case _:
                print("\nPlease enter a valid choice 1-8")



def main():
    """
    Main function. loads the library, prints the library as a functiontest and then runs the menu.
    the menu-item "list books" prints w the book-class I also wanted to print w the library-class
    """
    library = Library("library_save.txt")
    library.load_from_file()
    print(library)
    menu(library)


if __name__ == "__main__":
    main()



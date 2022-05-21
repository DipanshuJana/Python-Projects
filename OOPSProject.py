# first creaing a library class
# total four function to be written:
# display book
# add book
# lend book
# reutrn book

class Library:  # main class
    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.lended_books = []
        self.username = []

    def user_login(self):
        print(f"Welcome to {self.library_name}\n")
        user = input("Please enter your username:")
        self.username.append(user)

    def display_books(self):
        for items in self.list_of_books:
            print(items)

    def add_books(self):
        book_info_input = input("Enter the book name you want to add:")
        if book_info_input in self.list_of_books:
            self.list_of_books.append(book_info_input)
            print("Sucessfully added the following book in our books list.")

        else:
            print("Can't add the book, already available in our list.")

    def lend_books(self):
        l_book = input("Please enter the book you want to lend:")
        if l_book in self.list_of_books:
            self.list_of_books.remove(l_book)
            self.lended_books.append(l_book)
            print(
                f"Okay {self.username} lended {l_book} from {self.library_name}")
            print(f"The book you have lended : \n{self.lended_books}")

        else:
            print(f"You can't lend {l_book} as someone has already lended it.")

    def return_books(self):
        print(
            f"The list of the books which you have lended are: {self.lended_books}")
        r_book = input("\nEnter the book which you want to return")
        if r_book in self.lended_books:
            self.lended_books.remove(r_book)
            self.list_of_books.append(r_book)
        else:
            print("Can't return the book. Already in our list.")


def main_func():  # this is the main function
    while (True):
        display_books = "Display the list of books"
        add_books = "Add books"
        lend_books = "Lend books"
        return_books = "Return books"
        user_input = eval(input("What do you want to do in this library ?"))

        if user_input == display_books:
            py_library.display_books()

        elif user_input == add_books:
            py_library.add_books()

        elif user_input == lend_books:
            py_library.lend_books()

        elif user_input == return_books:
            py_library.return_books()


py_library = Library(["Charlotte’s Web",
                      "Mieko and the Fifth Treasure",
                      "The Outsiders",
                      "The House On Mango Street",
                      "Thirteen Reasons Why",
                      "Peter Pan",
                      "The Old Man and the Sea",
                      "The Giver",
                      "Number the Stars",
                      "A Wrinkle In Time"], "Py Library")

py_library.user_login()
main_func()

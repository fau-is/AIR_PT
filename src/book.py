'''
The Book class is aimed to test students' understanding of class basics:
1. variable
2. member function

'''


class Book:
    serial_num = 0

    def __init__(self, title, author):
        self.__title = title
        self.__author = author
        self.__available = True
        self.__serial_num = Book.serial_num
        self.__student_group = None
        self.__shelf_num = None

    # Mark burrowed
    def function1(self):
        self.__available = False

    # Mark returned
    def function2(self):
        self.__available = True

    def function3(self, shelf):
        if self.shelf_num is None:
            self.shelf_num = shelf

    # Help function
    def help(self):
        print("This class implements the entity of a book in a library, ",
              "all of the attributes in this class are set to private, ",
              "Use print_attr() function to examine the value of the object attributes",
              "it has 3 member functions, function1 and function2 take no extra arguments, function3 takes 1 integer argument")


    # Print Attr
    def print_attr(self):
        for attr_name, attr_value in vars(self).items():
            print(f"{attr_name}: {attr_value}")


class TextBook(Book):
    def __init__(self, title, author):
        super().__init__(title, author)


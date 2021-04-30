# Challenge: Document, 4/05/2021 by Zack Augustine
# program: Document.py
class Document:

    def __init__(self, title, body, author):
        self.__title = title
        self.__body = body
        self.__author = author

    # Return title
    def get_title(self):
        return self.__title
    # Return body
    def get_body(self):
        return self.__body
    # Return author
    def get_author(self):
        return self.__author

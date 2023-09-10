#!/usr/bin/env python3

class Book:
    def __init__(self, title ="title", page_count = 10):
        self.title = title
        self.page_count = page_count
    
    def get_title(self):
        return self._title

    def set_title(self, title):
        if (type(title)== str) and (1 < len(title) < 25):
            self._title = title
        else:
            print("not a real title")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    title = property(get_title, set_title)
    
    def get_page_count(self):
        return self._page_count

    def set_page_count(self, page_count):
        if (type(page_count) == int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    page_count = property(get_page_count, set_page_count)

    
    
    
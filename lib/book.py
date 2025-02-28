#!/usr/bin/env python3
import sys
class Book:
    def __init__(self, title, page_count, author="Unknown", genre="Unknown"):
        self.title = title
        self.page_count = page_count
        self.author = author
        self.genre = genre

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 50:
            self._title = value.title()
        else:
            raise ValueError("Title must be a string between 1 and 50 characters.")
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 50:
            self._author = value.title()
        else:
            raise ValueError("Author must be a string between 1 and 50 characters.")
    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int) and value > 0:
            self._page_count = value
        else:
            print("page_count must be an integer", file=sys.stdout)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!", file=sys.stdout)
    
        
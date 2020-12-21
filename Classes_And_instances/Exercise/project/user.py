class User:
    def __init__(self, user_id, username):
            self.user_id = user_id
            self.username = username
            self.books=[]

    def get_book(self,author: str, book_name: str, days_to_return: int, library): #Library
        if author in library.books_available:
            available_books=library.books_available[author]
            if book_name in available_books:
                self.books.append(book_name)
                if self.username not in library.rented_books:
                    library.rented_books[self.username] = {}
                dict_of_rented_books=library.rented_books[self.username]
                dict_of_rented_books[book_name]=days_to_return
                available_books.remove(book_name)
                return f"{book_name} successfully rented for the next {days_to_return} days!"
            for key,value in library.rented_books.items():
                for book,days in value.items():
                    if book==book_name:
                        days_left=days
            return f'The book "{book_name}" is already rented and will be available in {days} days!'
        else:
            for key,value in library.rented_books.items():
                for book,days in value.items:
                    if book==book_name:
                        days_left=days
            return f'The book "{book_name}" is already rented and will be available in {days} days!'

    def return_book(self,author:str, book_name:str, library):
        if book_name in library.rented_books[self.username]:
            books_dict=library.rented_books[self.username]
            del books_dict[book_name]
            list_of_availabales=library.books_available[author]
            list_of_availabales.append(book_name)
            self.books.remove(book_name)
        else:
            return f"{self.username} doesn't have this book in his/her records!"

    def info(self):
        return ", ".join(sorted(self.books))

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"



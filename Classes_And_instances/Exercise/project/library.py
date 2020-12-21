class Library:
    user_records=[]
    books_available={}
    rented_books={}

    def add_user(self,user): #User
        if user not in self.user_records:
            self.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user): #User
        if user in self.user_records:
            self.user_records.remove(user)
        else:
            return f"We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str):
        for user in self.user_records:
            if user.user_id==user_id and user.username != new_username:
                user.username=new_username
                return f"Username successfully changed to: {new_username} for userid: {user_id}"
            elif user.user_id==user_id and user.username == new_username:
                return "Please check again the provided username - it should be different than the username used so far!"
        else:
            return f"There is no user with id = {user_id}!"
    
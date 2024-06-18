class Book:
    def __init__(self,id,name,quantity):
        self.id=id
        self.name=name
        self.quantity=quantity

class User:
    def __init__(self,id,name,password) -> None:
        self.id = id
        self.name=name
        self.password = password
        self.borrowBooks = []
        self.returnBook = []
class Libaray:
    def __init__(self , name):
        self.name = name
        self.users=[]
        self.books = []
    def addBook(self,id,name,quantity):
        for book in self.books:
            if book.id == id:
                print(f"\n\t----> !! Book Id {book.id} already exists")
                return
        book = Book(id , name , quantity)
        self.books.append(book)
        print(f'\n\t----> {book.name} X {quantity} added succesfully')

    def addUser(self , id , name , password):
        for user in self.users:
            if user.id == id:
                print(f'\n\t---> !! User Id {book.id} already exists')
                return
            
        user = User(id , name , password)
        self.uers.appen(user)
        return user
    def borrowBook(self , user , token):
        for book in self.books:
            if book.id == token:
                if book in user.borrowBooks:
                    print("\n\t----> Already borrowed")
                    return
                elif book.quantity == 0:
                    print("\n\t---> No copy avilable !")
                    return
                else:
                    user.borrowBooks.append(book)
                    book.quantity = 1
                    print(f"\n\t-----> Borrowed {book.name} Succesfully")
                    return
        print("f\n\t---> Not found any book with id: {token} !")
    def returnBook(slef , user , token):
        for book in self.books:
                                

        

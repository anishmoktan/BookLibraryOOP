from Books import Book

class Library_C:
  def __init__(self):
    self.shelfNum=1
    self.bookList=[]

  def add(self):
    new_book = input(str(f"What is the name of the book you would like to add?\n"))
    shelf_num = self.shelfNum
    book = Book(new_book,shelf_num)
    self.bookList.append(book)
    print(f"Your book \"{new_book}\" was added on shelf #{shelf_num}")
    self.shelfNum +=1

  def show(self):
    if self.bookList== []:
      print("The library is empty!")
    else:
      print("These are the books that are currently in our library: ")
      for books in self.bookList:
        print(books)
  
  def update(self):
    shelf_num = input(f"Which shelf is the book located in?\n")
    if int(shelf_num) > len(self.bookList):
      print("That shelf is empty. Please try again!")
    else:
      book_name = input(str(f"What is the name of the new book you want to update?\n"))
      self.bookList[int(shelf_num)-1]=Book(book_name,shelf_num)
      return print(f"Your new book is updated!")  

  def delete(self):
    shelf_num = input(f"Which shelf number is the book located in?\n")
    if int(shelf_num)>len(self.bookList):
      print("That shelf is empty. Please try again!")
    else:
      shelf=int(shelf_num)-1
      self.bookList.pop(shelf)
      print("Book deleted!")

    
    # try:
    #   self.check_int(shelf_num)
    # except TypeError as type_error:
    #   print(type_error)
    # else:
    #   shelf_num = shelf_num - 1
    #   self.bookList.remove(shelf_num)
    #   print(f"Book Deleted!")
    # finally:
    #   print("finished")

  def check_int(self, user_input):
    if not type(user_input) is int:
      raise TypeError("Only integers are allowed.")

    try:
      self.check_str(book_name)
    except TypeError as type_error:
      print(type_error)
    else:
      print("finished")

  def check_str(self, user_input):
    if not type(user_input) is str:
      raise TypeError("Only string will be allowed.")



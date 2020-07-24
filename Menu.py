import sys
from Library import Library_C

class Menu_Screen:
  def __init__(self):
    self.library_C=Library_C()
    self.choices= {
       "1" : self.library_C.add,
       "2" : self.library_C.show,
       "3" : self.library_C.update,
       "4" : self.library_C.delete,
       "Q" : self.quit
       }
  def menuMessage(self):
    print("""
                  Welcome to Last Mile Library!\n    
                          MAIN MENU
                  Please enter your requests\n
          1. Add your book in our virtual library
          2. View the books in our virtual library 
          3. Update the books in our virtual library
          4. Delete the books in our virtual library
          Q. Quit the program
          """)
  def run(self):
    while True:
      self.menuMessage()
      choice = input("Enter an option: " )
      action = self.choices.get(choice)
      if action:
         action()
      else:
        print("{0} is not a valid choice".format(choice))
  def quit(self):
    choice = input("Do you want to save your session? y/n \n\n")
    if("y" in choice.lower()):
      self.Library.save() 
    print("Good Bye!")

    sys.exit(0) 

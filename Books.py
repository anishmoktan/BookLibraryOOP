class Book:
  def __init__(self, name, shelf_num):
    self.name = name
    self.shelf_num = shelf_num
  def __str__(self):
    return f"Book Name: \"{self.name}\" on shelf #{self.shelf_num}"
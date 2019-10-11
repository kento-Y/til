class parent():
  def __init__(self):
    print("this is parent class.")

class child1(parent):
  def __init__(self):
    print("this is child1 class.")

class child2(parent):
  def __init__(self):
    print("this is child2 class.")

if __name__ == '__main__':
  parent()
  child1()
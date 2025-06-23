class rect:
  def __init__(self,length,width):
    self.length=length
    self.width=width

  def __str__(self):
    return str(f"Area: {self.length*self.width}")
  
class squar(rect):
  def __init__(self,side):
    super(). __init__(side,side)

  def __str__(self):
    return str(f'Area of square is: {self.length*self.width}')
emp=rect(5,6)
imp=squar(4)
print(imp)
print(emp)
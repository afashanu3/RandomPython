class Circle: 
  def __init__(self, color, radius):
    self.color = color
    self.radius = radius
    
  def get_area(self):
    self.get_area = print(("What is the area?"))
    return self.radius ** 2 * 3.14 

  def get_circumference(self): 
    self.get_circumference = print("What is the circumference?")
    return self.radius * 2 * 3.14

circle1 = Circle( 'Blue' , 8 )
circle1.color
circle1.radius
circle1.get_area()
circle1.get_circumference()

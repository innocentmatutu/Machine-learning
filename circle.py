import math

class area:
    def __init__(self,radius):
        self.radius=radius

    def ci(self):
        mad=math.pi*self.radius*self.radius
        return f'Area of circle is: {mad:.1f}'
    
class perimeter(area):
    def __init__(self,radius):
        super().__init__(radius)
         
    def py(self):
        min=math.pi*2*self.radius
        return f'Perimeter of circle is: {min:.1f}' 
    
#radius_area=float(input('Enter radius of circle: '))
#radius_perimeter=float(input('Enter radius of circle: '))

#mes=area(radius_area)
#sem=perimeter(radius_perimeter)
#print(mes.ci())
#print(sem.py())


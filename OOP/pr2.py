class cylinder:
    
    pi = 3.14


    def __init__(self, height=1 , radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return (cylinder.pi * self.radius * self.radius * self.height)

    def surface( self):
        return((2*cylinder.pi*self.radius)*self.height) + ((cylinder.pi * self.radius**2)*2)


myCylinder = cylinder(2,3)

print(f"volume is {myCylinder.volume()}")
print(f"surface is {myCylinder.surface()}")


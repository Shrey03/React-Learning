class Line:
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        #self.coor1[0] - X1 , self.coor2[0] -X2
        return ((self.coor2[0] - self.coor1[0]) ** 2 + (self.coor2[1] - self.coor1[1]) ** 2)**0.5

    def slope (self):
        return ((self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[1]))


coordinate1 = (3,2)
coordinate2 = (8,10)
li = Line(coordinate1, coordinate2)
print(f"Distance is {li.distance()}")
print(f" Slope is {li.slope()}")
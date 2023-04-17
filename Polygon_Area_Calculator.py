# This is the boilerplate for the Polygon Area Calculator project. 
# Instructions for building your project can be found at 
# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/polygon-area-calculator

class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def set_width(self, n_width):
        self.width = n_width

    def set_height(self, n_height):
        self.height = n_height

    # Returns area (width * height)
    def get_area(self):
        return self.width*self.height

    # Returns perimeter (2 * width + 2 * height)
    def get_perimeter(self):
        return 2*(self.width+self.height)

    # Returns diagonal ((width ** 2 + height ** 2) ** .5)
    def get_diagonal(self):
        return (self.width**2+self.height**2)**0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        if self.width<=0 or self.height<=0:return ""
        lines="*"*self.width+"\n"
        return lines*self.height

    #Takes another shape(square or rectangle) as an argument. 
    # Returns the number of times the passed in shape could fit 
    # inside the shape(with no rotations). For instance, a rectangle with a width 
    # of 4 and a height of 8 could fit in two squares with sides of 4.
    def get_amount_inside(self, another_shape):
        return max((self.height//another_shape.height)*(self.width//another_shape.width),(self.width//another_shape.height)*(self.height//another_shape.width)) 

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side) -> None:
        super().__init__(side, side)

    def set_side(self,value):
        self.height=value
        self.width=value

    def set_height(self, n_height):
        return self.set_side(n_height)

    def set_width(self, n_width):
        return self.set_side(n_width)   

    def __str__(self) -> str:
        return f"Square(side={self.height})"  


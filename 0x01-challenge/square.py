#!/usr/bin/python3
"""Square class representing a class"""


class Square:
    """Representation of Square"""

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initialize new obj at point of
        creation
        """
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """

        return self.width * self.width

    def perimeter_of_my_square(self):
        """ perimeter of a square"""
        return 4 * self.width

    def __str__(self):
        """prints the str representation"""
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())


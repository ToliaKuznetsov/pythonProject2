import turtle
def square(x, y, a, angle, color):
    '''
    Function, drawing square.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a square
    :param angle: rotation angle of a square (counterclockwise)
    :param color: color of a square
    :return: None
    '''

    turtle.up()
    turtle.setposition(x, y)
    turtle.left(angle)
@@ -34,30 +34,27 @@ def square(x, y, a, angle, color):


def parallelogram(x, y, a, b, c, r):
    """
    Function, drawing parallelogram.
    :param x: upper  obtuse angle coordinate x
    :param y: upper obtuse angle coordinate y
    :param a: long side of the parallelogram
    :param b: short side of the parallelogram
    :param c: color
    :param r: degree of rotation relative OX
    """
    turtle.penup()
    turtle.color(c)
    turtle.setposition(x, y)
@@ -75,12 +72,12 @@ def parallelogram(x, y, a, b, c, r):
    turtle.end_fill()
    turtle.right(r)


def main():
    '''
    """
    Main function.
    :return: None
    '''


if __name__ == '__main__':
    main()
def triangle(x, y, a, b, ang, c):
    '''
    Function, drawing triangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a:long side length of a triangle
    :param b:short side length of a triangle
    :param ang: angle of a triangle
    :param c: color of a triangle
    :return: None
    '''
turtle.up()
turtle.setposition(x, y, ang)
turtle.down()
turtle.forward(b)
turtle.right(90)
turtle.forward(b)
turtle.right(135)
turtle.forward(a)
turtle.right(135)





def parallelogram(x, y, a):
    '''
    Function, drawing square.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a square
    :return: None
    '''


def main():
    '''
    Main function.
    :return: None
    '''
    square(-200, 200, 180)
    square(20, 200, 180)
    square(20, -20, 180)
    square(-200, -20, 3456)
    turtle.done()


if __name__ == '__main__':
    main()
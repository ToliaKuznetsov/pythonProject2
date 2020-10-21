# Case-study #1
# Developers:   Ivanov A. (20%),
#               Petrova S. (60%),
#               Sidorov M. (30%)
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
    turtle.color(color)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()
    turtle.right(angle)


def triangle(x, y, a, ang, c):
    '''
    Function, drawing triangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a triangle
    :param ang: angle of a triangle
    :param c: color of a triangle
    :return: None
    '''





def parallelogram(x, y, a, b, c, r):
    '''
    Function, drawing parallelogram.
    :param x: upper  obtuse angle coordinate x
    :param y: upper obtuse angle coordinate y
    :param a: long side of the parallelogram
    :param b: short side of the parallelogram
    :param c: color
    :param r: degree of rotation relative OX
    '''
    turtle.penup()
    turtle.color(c)
    turtle.setposition(x, y)
    turtle.left(r)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(45)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(45)
    turtle.end_fill()
    turtle.right(r)

def main():
    '''
    Main function.
    :return: None
    '''



if __name__ == '__main__':
    main()

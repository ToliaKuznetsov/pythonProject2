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
    :param angle: rotation angle of a square
    :param color: color of a square
    :return: None
    '''
    turtle.up()
    turtle.setposition(x, y)
    turtle.setheading(angle)
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
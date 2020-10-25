# Case-study #1
# Developers:   Lapochkin D. (25%),
#               Kuznetsov A. (30%),
#               Krivoshapova D. (35%)
import turtle

turtle.setup(1200, 800)
turtle.speed(20)


def square(x, y, a, angle, color):
    """
    Function, drawing square.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: side length of a square
    :param angle: rotation angle of a square (counterclockwise)
    :param color: color of a square
    :return: None
    """
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
    """
    Function, drawing triangle.
    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param a: short-side length of a triangle
    :param ang: rotation angle of a triangle
    :param c: color of a triangle
    :return: None
    """
    turtle.up()
    turtle.setposition(x, y)
    turtle.setheading(ang)
    turtle.down()
    turtle.color(c)
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(a * 2 ** .5)
    turtle.right(135)
    turtle.end_fill()
    turtle.right(ang)


def parallelogram(x, y, a, b, r, c):
    """
    Function, drawing parallelogram.
    :param x: upper  obtuse angle coordinate x
    :param y: upper obtuse angle coordinate y
    :param a: long side of the parallelogram
    :param b: short side of the parallelogram
    :param r: degree of rotation relative OX
    :param c: color
    """
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


def rabbit():
    """
    Function, drawing rabbit.
    TODO: Lapochkin D.
    :return: None
    """
    square(10, 260, 50, 0, '#FF9A5E')
    parallelogram(-15, 264, 70, 50, 135, '#9CBF4E')
    triangle(6, 255, 100, -90, '#FF552B')
    triangle(-94, 51, 100, 90, '#5BC78C')
    triangle(-15, 124, 75, -90, '#9CBF4E')
    triangle(39, 49, 50, 180, '#F2A0B6')
    triangle(10, 184, 50, -45, '#CCCACF')


def rooster():
    """
    Function, drawing rooster.
    TODO: Lapochkin D.
    :return: None
    """
    square(35, -115, 50, 0, '#5BC78C')
    triangle(35, -111, 45, 45, '#F2785C')
    triangle(-15, -269, 100, 90, '#9FAABF')
    triangle(60, -269, 50, 135, '#F2A0B6')
    triangle(-119, -109, 100, 0, '#FF552B')
    triangle(-119, -105, 71, 45, '#D9ADC5')
    parallelogram(-95, -138, 71, 35, -90, '#9CBF4E')


def dancer():
    """
    Function, drawing human.
    :return: None
    """
    square(400, 270, 50, 135, '#FF9A5E')
    triangle(402, 188, 80, 90, '#FFFF00')
    triangle(318, 268, 80, 360, '#FF0000')
    parallelogram(398, 136, 70, 50, 225, '#9CBF4E')
    triangle(472, 118, 70, 180, '#00B2EE')
    triangle(376, 108, 40, 270, '#912CEE')
    triangle(452, 114, 40, 0, '#7D26CD')


def runner():
    """
    Function, drawing human.
    :return: None
    """
    square(400, -100, 50, 135, '#FF9A5E')
    triangle(380, -189, 85, 90, '#FF0000')
    parallelogram(376, -148, 58, 44, 225, '#9CBF4E')
    triangle(406, -169, 85, 270, '#FFFF00')
    triangle(410, -220, 60, 315, '#00B2EE')
    triangle(406, -340, 44, 135, '#912CEE')
    triangle(282, -288, 44, 90, '#7D26CD')


def helicopter():
    """
    Function, drawing helicopter.
    :return: None
    """

    parallelogram(-320, 285, 71, 35, 0, '#D8BFD8')
    triangle(-455, 260, 75, 45, '#DB7093')
    triangle(-350, 115, 100, 135, '#D3D3D3')
    triangle(-345, 257, 100, -45, '#8FBC8F')
    triangle(-425, 185, 50, -135, '#20B2AA')
    triangle(-457, 145, 50, 45, '#CD5C5C')
    square(-570, 185, 50, 45, '#FF9A5E')


def rocket():
    """
    Function, drawing rocket.
    :return: None
    """
    triangle(-500, -10, 50, 45, '#20B2AA')
    triangle(-502, -14, 75, 0, '#DB7093')
    triangle(-502, -20, 100, -45, '#D3D3D3')
    triangle(-426, -233, 100, 135, '#8FBC8F')
    square(-535, -200, 50, 45, '#FF9A5E')
    parallelogram(-422, -234, 70, 50, 90, '#D8BFD8')
    triangle(-538, -203, 50, -45, '#CD5C5C')


def main():
    """
    Main function.
    :return: None
    """
    rabbit()
    rooster()
    dancer()
    runner()
    helicopter()
    rocket()
    turtle.done()


if __name__ == '__main__':
    main()

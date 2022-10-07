import turtle
import math
from turtle import *

Turtle()

side_num = 0
draw_rectangle = None
draw_circle = None
draw_trapezoid = None
draw_rhombus = None
draw_triangle = None
draw_polygon = None

#---2d shapes----------------------------------------------------------------------------------------
#---Rectangle----------------------------------------------------------------------------------------
def rectangle():
    length, height, area = 0, 0, 0
    while True:
        try:
            length = float(input("Insert length: "))
        except:
            print("Input valid number.")
        else:
            break
    while True:
        try:
            height = float(input("Insert height: "))
        except:
            print("Input valid number.")
        if length == 0 and height == 0:
            print("Input more non-zero numbers.")
        else:
            break
    while True:
        try:
            area = float(input("Insert area: "))
        except:
            print("Input valid number.")
        if length == 0 and area == 0 or height == 0 and area == 0:
            print("Input more non-zero numbers.")
        else:
            break
    if length == 0:
        length = (area / height)
    if height == 0:
        height = (area / length)
    if area == 0:
        area = (length * height)
    print("Length: " + str(round(length, 2)))
    print("Height: " + str(round(height, 2)))
    print("Area: " + str(round(area, 2)))
  
    begin_fill()
    color('red', 'yellow')
    for x in range(4):
        left(90)
        forward(100)
    else:
        end_fill()
        restart()


#---Circle----------------------------------------------------------------------------------------


def circle_shape():
    radius, area = 0, 0
    while True:
        try:
            radius = float(input("Insert radius: "))
        except:
            print("Input valid number.")
        else:
            break
    while True:
        try:
            area = float(input("Insert area: "))
        except:
            print("Input valid number.")
        if radius == 0 and area == 0:
            print("Input more non-zero numbers.")
        else:
            break
    if area == 0:
        area = (math.pi * pow(radius, 2))
    if radius == 0:
        radius = (math.sqrt(area / math.pi))
    print("Area: " + str(round(area, 2)))
    print("Radius: " + str(round(radius, 2)))
  
    color('red', 'yellow')
    begin_fill()
    circle(50)
    end_fill()
  
    restart()


#---Triangle----------------------------------------------------------------------------------------


def triangle():
    base, height, area = 0, 0, 0
    while True:
        try:
            base = float(input("Insert base: "))
        except:
            print("Input valid number.")
        else:
            break
    while True:
        try:
            height = float(input("Insert height: "))
        except:
            print("Input valid number.")
        if base == 0 and height == 0:
            print("Input more non-zero numbers.")
        else:
            break
    while True:
        try:
            area = float(input("Insert area: "))
        except:
            print("Input valid number.")
        if base == 0 and area == 0 or height == 0 and area == 0:
            print("Input more non-zero numbers.")
        else:
            break
    if base == 0:
        base = (2 * (area / height))
    if height == 0:
        height = (2 * (area / base))
    if area == 0:
        area = ((base * height) / 2)
    print("Base: " + str(round(base, 2)))
    print("Height: " + str(round(height, 2)))
    print("Area: " + str(round(area, 2)))
  
    begin_fill()
    color('red', 'yellow')
    for x in range(3):
        left(120)
        forward(80)
    else:
        end_fill()
        restart()


#---Rhombus----------------------------------------------------------------------------------------


def rhombus():
    diagonalA, diagonalB, area = 0, 0, 0
    while True:
        try:
            diagonalA = float(input("Insert the first diagonal: "))
        except:
            print("Input valid number.")
        else:
            break
    while True:
        try:
            diagonalB = float(input("Insert the second diagonal: "))
        except:
            print("Input valid number.")
        if diagonalA == 0 and diagonalB == 0:
            print("Input more non-zero numbers.")
        else:
            break
    while True:
        try:
            area = float(input("Insert area: "))
        except:
            print("Input valid number.")
        if diagonalA == 0 and area == 0 or diagonalB == 0 and area == 0:
            print("Input more non-zero numbers.")
        else:
            break
    if diagonalA == 0:
        diagonalA = (2 * (area / diagonalB))
    if diagonalB == 0:
        diagonalB = (2 * (area / diagonalA))
    if area == 0:
        area = ((diagonalA * diagonalB) / 2)
    print("First diagonal: " + str(round(diagonalA, 2)))
    print("Second diagonal: " + str(round(diagonalB, 2)))
    print("Area: " + str(round(area, 2)))
  
    begin_fill()
    color('red', 'yellow')
    left(45)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    end_fill()
  
    restart()


#---Trapezoid----------------------------------------------------------------------------------------


def trapezoid():
    baseA, baseB, height, area = 0, 0, 0, 0
    while True:
        try:
            baseA = float(input("Insert first base: "))
        except:
            print("Inuput valid number.")
        else:
            break
    while True:
        try:
            baseB = float(input("Insert second base: "))
        except:
            print("Inuput valid number.")
        if baseA == 0 and baseB == 0:
            print("Input more non-zero numbers.")
        else:
            break
    while True:
        try:
            height = float(input("Insert height: "))
        except:
            print("Inuput valid number.")
        if baseA == 0 and height == 0 or baseB == 0 and height == 0:
            print("Input more non-zero numbers.")
        else:
            break
    while True:
        try:
            area = float(input("Insert area: "))
        except:
            print("Input valid number.")
        if baseA == 0 and area == 0 or baseB == 0 and area == 0 or height == 0 and area == 0:
            print("Input more non-zero numbers.")
        else:
            break
    if baseA == 0:
        baseA = (2 * (area / height) - baseB)
    if baseB == 0:
        baseB = (2 * (area / height) - baseA)
    if height == 0:
        height = (2 * (area / (baseA * baseB)))
    if area == 0:
        area = (height * (baseA + baseB) / 2)
    print("First base: " + str(round(baseA, 2)))
    print("Second base: " + str(round(baseB, 2)))
    print("Height: " + str(round(height, 2)))
    print("Area: " + str(round(area, 2)))
  
    begin_fill()
    color('red', 'yellow')
    forward(180)
    left(120)
    forward(80)
    left(60)
    forward(100)
    left(60)
    forward(80)
    end_fill()
  
    restart()


#---Polygon----------------------------------------------------------------------------------------


def polygon():
    side_length, area = 0, 0
    while True:
        try:
            side_num = int(input("Insert number of sides: "))
        except:
            print("Input valid number.")
        else:
            break
    while True:
        try:
            side_length = float(input("Insert side length: "))
        except:
            print("Input valid number.")
        if side_length == 0 and area == 0:
            print("Input more non-zero numbers.")
        else:
            break
    perimeter = (side_num * side_length)
    apothem = (side_length / (2 * math.tan(math.pi / side_num)))
    area = (perimeter * apothem * 0.5)
    print("Area: " + str(round(area, 2)))
    
    begin_fill()
    color('red', 'yellow')
    for x in range(side_num):
        left(360 / side_num)
        forward(120 / (0.3 * side_num))
    else:
        end_fill()
        restart()


#---3d shapes----------------------------------------------------------------------------------------
#---Rectangular prism----------------------------------------------------------------------------------------


def rectangular_prism():
    length, height, width, volume = 0, 0, 0, 0
    while True:
        try:
            length = float(input("Insert length: "))
        except:
            print("Input valid number.")
        else:
            break
    while True:
        try:
            height = float(input("Insert height: "))
        except:
            print("Input valid number.")
        if length == 0 and height == 0:
            print("Input more non-zero numbers.")
        else:
            break
    while True:
        try:
            width = float(input("Insert width: "))
        except:
            print("Input valid number.")
        if length == 0 and width == 0 or height == 0 and width == 0:
            print("Input more non-zero numbers.")
        else:
            break
    while True:
        try:
            volume = float(input("Insert volume: "))
        except:
            print("Input valid number.")
        if length == 0 and volume == 0 or width == 0 and volume == 0 or height == 0 and volume == 0:
            print("Input more non-zero numbers.")
        else:
            break
    if length == 0:
        length = ((volume / width) / height)
    if height == 0:
        height = ((volume / length) / width)
    if width == 0:
        width = ((volume / length) / height)
    if volume == 0:
        volume = (length * height * width)
    sur_area = (2 * ((width * length) + (height * length) + (height * width)))
    print("Length: " + str(round(length, 2)))
    print("Height: " + str(round(height, 2)))
    print("Width: " + str(round(width, 2)))
    print("Volume: " + str(round(volume, 2)))
    print("Surface area: " + str(round(sur_area, 2)))

    color('red', 'yellow')
    goto(0, -50)
    goto(0, 0)
    goto(50, 0)
    goto(50, -50)
    goto(0, -50)
    goto(50, -50)
    goto(0, 0)
    goto(0, 50)
    goto(-50, 50)
    goto(-50, 0)
    goto(0, 0)
    goto(-50, 50)
    goto(0, 50)
    goto(50, 0)
    goto(0, -50)
    goto(-50, 0)
    restart()


#---Cone----------------------------------------------------------------------------------------


def cone():
    radius, height, volume = 0, 0, 0
    while True:
        try:
            radius = float(input("Insert radius: "))
        except:
            print("Input valid number.")
        else:
            break
    while True:
        try:
            height = float(input("Insert height: "))
        except:
            print("Input valid number.")
        if height == 0 and radius == 0:
            print("Input more non-zero numbers.")
        else:
            break
    while True:
        try:
            volume = float(input("Insert volume: "))
        except:
            print("Input valid number.")
        if height == 0 and volume == 0 or radius == 0 and volume == 0:
            print("Input more non-zero numbers.")
        else:
            break
    if radius == 0:
        radius = (math.sqrt((3 * volume) / (math.pi * height)))
    if height == 0:
        height = (3 * volume / (math.pi * (pow(radius, 2))))
    if volume == 0:
        volume = (math.pi * pow(radius, 2) * height / 3)
    sur_area = (math.pi * radius *
                (radius + math.sqrt(pow(height, 2) + pow(radius, 2))))
    print("Radius: " + str(round(radius, 2)))
    print("Height: " + str(round(height, 2)))
    print("Volume: " + str(round(volume, 2)))
    print("Surface area: " + str(round(sur_area, 2)))
  
    color('red', 'yellow')
    penup()
    setx(-50)
    sety(40)
    left(270)
    pendown()
    circle(50,180)
    penup()
    setx(45)
    pendown()
    for x in range(10):
      dot()
      penup()
      circle(45,20)
      pendown()
    penup()
    setx(50)
    sety(40)
    pendown()
    goto(0,150)
    goto(-50,40)
  
    restart()


#---Pyramid----------------------------------------------------------------------------------------


def pyramid():
    length, height, width, volume = 0, 0, 0, 0
    while True:
        try:
            length = float(input("Insert length: "))
        except:
            print("Input valid number.")
        else:
            break
    while True:
        try:
            height = float(input("Insert height: "))
        except:
            print("Input valid number.")
        if length == 0 and height == 0:
            print("Input more non-zero numbers.")
        else:
            break
    while True:
        try:
            width = float(input("Insert width: "))
        except:
            print("Input valid number.")
        if length == 0 and width == 0 or length == 0 and width == 0:
            print("Input more non-zero numbers.")
        else:
            break
    while True:
        try:
            volume = float(input("Insert volume: "))
        except:
            print("Input valid number.")
        if length == 0 and volume == 0 or width == 0 and volume == 0 or height == 0 and volume == 0:
            print("Input more non-zero numbers.")
        else:
            break
    if length == 0:
        length = (((volume * 3) / height) / width)
    if height == 0:
        height = (((volume * 3) / length) / width)
    if width == 0:
        width = (((volume * 3) / length) / height)
    if volume == 0:
        volume = ((length * height * width) / 3)
    sur_area = ((length * width) +
                (length * (math.sqrt(pow((width / 2), 2) + pow(height, 2)))) +
                (width * (math.sqrt(pow((length / 2), 2) + pow(height, 2)))))
    print("Length: " + str(round(length, 2)))
    print("Height: " + str(round(height, 2)))
    print("Width: " + str(round(width, 2)))
    print("Volume: " + str(round(volume, 2)))
    print("Surface area: " + str(round(sur_area, 2)))
  
    color('red', 'yellow')
    left(90)
    forward(100)
    left(160)
    forward(90)
    goto(0,0)
    right(160)
    forward(100)
    right(160)
    forward(90)
    goto(0,0)
    left(160)
    forward(100)
    left(160)
    forward(90)
    goto(0,30)
    right(160)
    forward(70)
    right(160)
    forward(90)
    goto(0,30)
    penup()
    goto(200,200)
  
    restart()
  
#---Sphere----------------------------------------------------------------------------------------


def sphere():
    radius, volume = 0, 0
    while True:
        try:
            radius = float(input("Insert radius: "))
        except:
            print("Input valid number.")
        else:
            break
    while True:
        try:
            volume = float(input("Insert volume: "))
        except:
            print("Input valid number.")
        if radius == 0 and volume == 0:
            print("Input more non-zero numbers.")
        else:
            break
    if volume == 0:
        volume = (((4 / 3) * math.pi) * pow(radius, 3))
    if radius == 0:
        radius = (pow((3 * volume / (4 * math.pi)), (1 / 3)))
    sur_area = (4 * math.pi * (pow(radius, 2)))
    print("Volume: " + str(round(volume, 2)))
    print("Radius: " + str(round(radius, 2)))
    print("Surface area: " + str(round(sur_area, 2)))

    color('red', 'yellow')
    circle(50)
    penup()
    goto(-48, 40)
    left(-55)
    pendown()
    circle(62,90)
    circle(30,90)
    penup()
    left(-20.5)
    goto(48, 38)
    pendown()
    penup()
    circle(60,10)
    circle(40,9.5)
    pendown()
    for x in range(7):
      dot()
      penup()
      circle(60,10)
      circle(40,9.5)
      pendown()
    seth(-45)
  
    restart()


#---Cylinder----------------------------------------------------------------------------------------


def cylinder():
    radius, height, volume = 0, 0, 0
    while True:
        try:
            radius = float(input("Insert radius: "))
        except:
            print("Input valid number.")
        else:
            break
    while True:
        try:
            height = float(input("Insert height: "))
        except:
            print("Input valid number.")
        if radius == 0 and height == 0:
            print("Input more non-zero numbers.")
        else:
            break
    while True:
        try:
            volume = float(input("Insert volume: "))
        except:
            print("Input valid number.")
        if height == 0 and volume == 0 or radius == 0 and volume == 0:
            print("Input more non-zero numbers.")
        else:
            break
    if radius == 0:
        radius = (math.sqrt(volume / (math.pi * height)))
    if height == 0:
        height = (volume / (math.pi * pow(radius, 2)))
    if volume == 0:
        volume = (math.pi * pow(radius, 2) * height)
    sur_area = (2 * math.pi * radius * height + 2 * math.pi * pow(radius, 2))
    print("Radius: " + str(round(radius, 2)))
    print("Height: " + str(round(height, 2)))
    print("Volume: " + str(round(volume, 2)))
    print("Surface area: " + str(round(sur_area, 2)))

    color('red', 'yellow')
    penup()
    goto(0, -100)
    pendown()
    circle(50)
    penup()
    goto(-50,20)
    pendown()
    penup()
    goto(-50, 70)
    pendown()
    goto(-50,-65)
    penup()
    goto(0, 30)
    pendown()
    circle(50)
    penup()
    goto(50,50)
    pendown()
    penup()
    goto(50, 70)
    pendown()
    goto(50,-65)
  
    restart()


#---Donut----------------------------------------------------------------------------------------


def donut():
    minorRadius, majorRadius, volume = 0, 0, 0
    while True:
        try:
            minorRadius = float(input("Insert minor radius: "))
        except:
            print("Input valid number.")
        else:
            break
    while True:
        try:
            majorRadius = float(input("Insert major radius: "))
        except:
            print("Input valid number.")
        if minorRadius == 0 and majorRadius == 0:
            print("Input more non-zero numbers.")
        else:
            break
    while True:
        try:
            volume = float(input("Insert volume: "))
        except:
            print("Input valid number.") 
        if minorRadius == 0 and volume == 0 or majorRadius == 0 and volume == 0:
            print("Input more non-zero numbers.")
        else:
            break
    if minorRadius == 0:
        minorRadius = ((math.sqrt(volume / 2 * majorRadius) / math.pi))
    if majorRadius == 0:
        majorRadius = ((1 / 2) * volume * pow(1 / (math.pi * radius), 2))
    if volume == 0:
        volume = ((math.pi * pow(minorRadius, 2)) * (2 * math.pi * majorRadius))
    sur_area = ((2 * math.pi * majorRadius) * (2 * math.pi * minorRadius))
    print("Minor radius: " + str(round(minorRadius, 2)))
    print("Major radius: " + str(round(majorRadius, 2)))
    print("Volume: " + str(round(volume, 2)))
    print("Surface area: " + str(round(sur_area, 2)))
  
    speed(60)
    for x in range(35):
      color('red', 'yellow')
      circle(50)
      left(53) 
      forward(x/50+20)
      x += 2
    else:
      restart()


#---Restart----------------------------------------------------------------------------------------


def restart():
    x = str(input("Would you like to restart? Y or N: "))
    if (x.__eq__("Y") or x.__eq__("y") or x.__eq__("yes") or x.__eq__("Yes")):
        reset()
        main()
    else:
        print("Thank you for using DIM")

  
#---Main----------------------------------------------------------------------------------------


def main():
    print(
        "If you don't know a value just put 0 as a place holder, also all final values have been rounded up for less confusion."
    )
    print(
        "Type a 0 for two dimensional shapes.\nType a 1 for three dimensional shapes."
    )
    while True:
        try:
            shape_dim = int(input("Choice: "))
        except:
            print("Please make a valid choice.")
        else:
            break


#---2d and 3d selections----------------------------------------------------------------------------------------

    if (shape_dim == 0):
        while True:
            try:
                two_dim = int(
                    input(
                        "Choose a shape: \n0: Rectangle\n1: Circle\n2: Triangle\n3: Rhombus\n4: Trapezoid\n5: Regular polygon\nChoice: "
                    ))
            except:
                print("Choose a valid shape.")
            else:
                if (two_dim == 0):
                    rectangle()
                elif (two_dim == 1):
                    circle_shape()
                elif (two_dim == 2):
                    triangle()
                elif (two_dim == 3):
                    rhombus()
                elif (two_dim == 4):
                    trapezoid()
                elif (two_dim == 5):
                    polygon()
                break
    elif (shape_dim == 1):
        while True:
            try:
                three_dim = int(
                    input(
                        "Choose a shape: \n0: Rectangular prism\n1: Cone\n2: Pyramid\n3: Sphere\n4: Cylinder\n5: Donut\nChoice: "
                    ))
            except:
                print("Choose a valid shape.")
            else:
                if (three_dim == 0):
                    rectangular_prism()
                elif (three_dim == 1):
                    cone()
                elif (three_dim == 2):
                    pyramid()
                elif (three_dim == 3):
                    sphere()
                elif (three_dim == 4):
                    cylinder()
                elif (three_dim == 5):
                    donut()
                break
    else:
        print("Please choose a valid shape.")
        main()
    reset()
main()

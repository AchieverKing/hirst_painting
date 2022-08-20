# import colorgram
#
# colors = colorgram.extract("hirst.jpg", 30)
# rgb_color = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
import random
import turtle
from turtle import *
turtle.colormode(255)

color_list = [(192, 165, 115), (138, 166, 190),(56, 102, 140), (141, 91, 50), (12, 23, 55), (222, 207, 123),
              (182, 154, 42), (61, 22, 11), (182, 146, 165), (142, 177, 151), (72, 117, 81), (58, 15, 26),
              (126, 79, 102), (130, 30, 16), (15, 39, 23), (24, 53, 127), (177, 188, 215), (164, 104, 134),
              (115, 31, 46), (97, 150, 100), (98, 121, 172), (210, 178, 197), (174, 105, 93), (74, 150, 165),
              (25, 91, 65), (172, 205, 180)]


tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
dot_number = 100
for count in range(1, dot_number + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    """to change the position of the turtle to the next line to start another painting"""
    if count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.mainloop()

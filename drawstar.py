from turtle import *
import random

def drawStar(x, y):
    pu()
    goto(x, y)
    pd()
    colormode(255)
    
    seth(0)
    for i in range(5):
        fd(40)
        rt(144)
        pencolor((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))

for x in range(0, 250, 50):
    drawStar(x, 0)
    
done()
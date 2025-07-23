from turtle import *
from math import *
def polygon(t, n , length):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

    
x = Turtle()
x.color("grey","cyan")
x.begin_fill()
polygon(x,50,20)
x.end_fill()

done()
from turtle import *
from math import *

x = Turtle()
x.speed(0)
for i in range(3):
    x.fd(100)
    x.lt(360/(i+1))

done()
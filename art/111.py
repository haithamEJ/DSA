# import turtle
# import colorsys

# t = turtle.Turtle()
# t.speed(0)
# turtle.bgcolor("black")
# h = 0

# # Draw a spiral with changing colors
# for i in range(100):
  
#     if i < 50 :
#         t.color("black")
#         t.forward(i)
#         t.right(60)
    
#     if i >= 50 :
#         t.color("blue")
#         t.forward(i)
#         t.right(60)
  

# turtle.done()

import turtle

t = turtle.Turtle()
t.speed(0)

for i in range(72):

        t.color("black","grey")
        t.begin_fill()
        t.circle(100-(i*1/2))
        t.end_fill()
        t.left(5)
       

   
for i in range (55) :
                t.color("black","grey")
                t.begin_fill()
                t.circle(64-(i*1/2))
                t.end_fill()
                t.right(5)

for i in range (25) :
                t.color("black","grey")
                t.begin_fill()
                t.circle(36.5-(i*1/2))
                t.end_fill()
                t.left(5)

for i in range (20) :
                t.color("black","grey")
                t.begin_fill()
                t.circle(24-(i*1/2))
                t.end_fill()
                t.left(5) 
                if i == 10:
                            t.color("black","grey")
                            t.begin_fill()
                            t.circle(10-(i*1/2))
                            t.end_fill()

                      
turtle.done()

# x = Turtle()
# x.color("grey","cyan")
# x.begin_fill()
# polygon(x,50,20)
# x.end_fill()
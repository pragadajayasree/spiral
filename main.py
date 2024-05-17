import turtle as t
import random
t.colormode(255)
def color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r,g,b)
    return colors
def draw(turns):
 for i in range(int(360/turns)):
  tt.color(color())
  tt.circle(100)
  tt.setheading(tt.heading()+turns)


tt = t.Turtle()
tt.speed(0)
draw(5)

screen = t.Screen()
screen.exitonclick()



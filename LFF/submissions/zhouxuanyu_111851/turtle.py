import turtle

def set_canvas():
    s = turtle.Screen()
    s.setup(450, 410)
    s.bgcolor('ivory')
    s.title('Turtle Program')
    return s

def set_pen(color):
    t = turtle.Turtle()
    t.shape('turtle')
    t.pen(pencolor=color,fillcolor=color, pensize=1, speed=10)
    return t

def draw_tree(t, branch, angle, iteration):
  if iteration > 0:
        t.color('brown')
        t.pensize(iteration)
        t.forward(branch)
        length = branch * 9/10
        t.left(angle)
      draw_tree(t, length, angle, iteration-1)
        t.color('brown')
        t.right(angle * 2)
        t.pensize(iteration)
        t.forward(branch/10)
      draw_tree(t, length, angle, iteration-1)
        t.color('brown')
        t.left(angle)
        t.backward(branch*11/10)
  else:
        t.color('green')
        t.pendown()
        t.dot(15)

s = set_canvas()
t = set_pen('brown')
t.penup()
t.goto(-45, -150)
t.left(90)
t.pendown()
draw_tree(t, 60, 20, 6)
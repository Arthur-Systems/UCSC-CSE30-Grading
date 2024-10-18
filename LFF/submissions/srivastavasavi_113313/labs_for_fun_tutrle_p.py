import turtle
import random

def lorenz(x, y, z, s=10, r=28, b=2.667):
    """
    Compute the next position in the Lorenz attractor.
    
    Args:
    x, y, z (float): Current position.
    s, r, b (float): Parameters of the Lorenz attractor.

    Returns:
    tuple: The next position.
    """
    x_dot = s * (y - x)
    y_dot = r * x - y - x * z
    z_dot = x * y - b * z
    x = x + x_dot * 0.01
    y = y + y_dot * 0.01
    z = z + z_dot * 0.01
    return x, y, z

def set_canvas():
    """
    Set up the turtle canvas.
    
    Returns:
    turtle.Screen: The turtle screen.
    """
    s = turtle.Screen()
    s.setup(800, 600)
    s.bgcolor('black')
    s.title('Lorenz Attractor')
    return s

def set_pen():
    """
    Set up the turtle pen.
    
    Returns:
    turtle.Turtle: The turtle pen.
    """
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(0, 0)
    t.pendown()
    return t

def draw_lorenz(t, x, y, z, n):
    """
    Draw the Lorenz attractor using the turtle.

    Args:
    t (turtle.Turtle): The turtle pen.
    x, y, z (float): Initial position.
    n (int): Number of iterations.
    """
    colors = ['red', 'yellow', 'blue', 'green', 'purple', 'orange']
    for i in range(n):
        t.pencolor(random.choice(colors))
        x, y, z = lorenz(x, y, z)
        t.goto(x * 8, y * 8)  # Scale the attractor for better visibility

# Main program
s = set_canvas()
t = set_pen()
draw_lorenz(t, 0.1, 0.0, 0.0, 10000)

turtle.done()
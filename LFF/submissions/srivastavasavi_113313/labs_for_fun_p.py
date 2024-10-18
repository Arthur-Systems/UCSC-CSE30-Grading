from turtle import *
from random import randint

def set_turtles(colors):
    """
    Create and set up turtles with the specified colors.
    
    Args:
    colors (list of str): Colors of the turtles.

    Returns:
    list of turtle.Turtle: List of turtles.
    """
    turtles = []
    for color in colors:
        t = Turtle()
        t.color(color)
        t.shape("turtle")
        t.speed(1)
        turtles.append(t)
    return turtles

def draw_track(start, finish):
    """
    Draw the track for the turtle race.

    Args:
    start (int): Starting x-coordinate.
    finish (int): Finishing x-coordinate.
    """
    t = Turtle()
    t.speed(0)
    position, size, step = 100, 200, 40
    count = 0
    for line in range(start, finish + step, step):
        t.penup()
        t.goto(line, position + 10)
        if line == start:
            t.color("blue")
            t.pensize(10)
            t.write("START", align="center", font=("Arial", 16, "bold"))
        elif line == finish:
            t.color("red")
            t.pensize(10)
            t.write("FINISH", align="center", font=("Arial", 16, "bold"))
        else:
            t.color("grey")
            t.pensize(1)
            t.write(count, align="center", font=("Arial", 12, "normal"))
        t.goto(line, position)
        count += 1
        t.right(90)
        t.pendown()
        t.forward(size)
        t.left(90)

def is_finish(t, finish):
    """
    Check if a turtle has reached the finish line.

    Args:
    t (turtle.Turtle): The turtle.
    finish (int): The finishing x-coordinate.

    Returns:
    bool: True if the turtle has reached the finish line, else False.
    """
    x, _ = t.pos()
    return x >= finish

def race(turtles, start, finish):
    """
    Run the turtle race.

    Args:
    turtles (list of turtle.Turtle): List of turtles.
    start (int): Starting x-coordinate.
    finish (int): Finishing x-coordinate.
    """
    position = 80
    distance = 40
    for t in turtles:
        t.penup()
        t.goto(start, position)
        position -= distance
        t.pendown()
    done = False
    while not done:
        for t in turtles:
            t.forward(randint(1, 10))
            if is_finish(t, finish):
                done = True
                break
    # Announce the winner
    winner = turtles.index(t) + 1
    penup()
    goto(0, -200)
    color("black")
    write(f"Turtle {winner} wins!", align="center", font=("Arial", 24, "bold"))

def start_race():
    """
    Start the turtle race.
    """
    global race_on
    if not race_on:
        race_on = True
        draw_track(start, finish)
        race(turtles, start, finish)
        race_on = False

def reset_race():
    """
    Reset the turtle race.
    """
    global race_on
    if not race_on:
        clear()
        penup()
        goto(0, 0)
        draw_track(start, finish)
        for t in turtles:
            t.penup()
            t.goto(start, position)
            position -= distance
            t.pendown()

# Main program
race_on = False
start = -200
finish = 200

# Set up the screen
screen = Screen()
screen.setup(500, 400)
screen.bgcolor("white")
screen.title("Enhanced Turtle Race")

# Set up turtles
turtles = set_turtles(["yellow", "crimson", "aqua", "green", "purple"])

# Draw track and position turtles
draw_track(start, finish)
position = 80
distance = 40

# Add buttons for starting and resetting the race
screen.onkey(start_race, "s")
screen.onkey(reset_race, "r")
screen.listen()

screen.mainloop()
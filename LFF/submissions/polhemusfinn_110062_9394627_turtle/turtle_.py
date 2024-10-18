import turtle 



# draw a side
def draw_side(t, size, iterations):
    if iterations == 0: #checks if iterations is equal to zero if it is it moves forward the parameter size
        t.fd(size)
    #if iterations doesnt equal 0 then a it will go a third of the side and draw a small triangle until iteration equals 0
    #it will not go forward until the iterations = 0(the lowest level)
    else:
        #line segment
        #first third
        
        draw_side(t, size/3, iterations-1)#calls the function and subtracts one from iterations to see if it gets to iteration 0 and check if it needs to go forward
        t.rt(60)
        #second third
        
        draw_side(t, size/3, iterations-1)
        t.lt(120)
        draw_side(t, size/3, iterations-1)
        t.rt(60)
        #third third
        draw_side(t, size/3, iterations-1)
    
#draws triangle
def draw_triangle(t, size, iterations):
    #repeats 3 times for 3 sides of the triangle
    for i in range(3): 
        #calls the draw_side to check if it needs to turn or if i can more forward
        draw_side(t, size, iterations)
        t.lt(120)

# main program
s = turtle.Screen()     # make a canvas window
s.setup(400, 400)
s.bgcolor("ivory4")
s.title("Turtle Program")

t = turtle.Turtle()     # make a pen
t.shape("turtle")  
t.pen(pencolor='dark violet',fillcolor='black', pensize=1, speed=0)
t.penup()

t.home()
t.goto(-100,-100)
t.pendown()
draw_triangle(t, 80, 3)

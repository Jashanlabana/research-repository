import turtle

# Create a Turtle screen
screen = turtle.Screen()
screen.bgcolor("blue")

# Create a Turtle object
design = turtle.Turtle()
design.speed(10)  # Set the speed of drawing

# Set the pen color and thickness
design.color("white")
design.pensize(2)

# Draw the design
for _ in range(10):
    for _ in range(4):
        design.forward(100)
        design.right(90)
        design.forward(50)
        design.right(90)
    design.right(36)

# Hide the turtle and display the drawing
design.hideturtle()
turtle.done()

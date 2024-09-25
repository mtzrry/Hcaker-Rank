# import turtle

# def draw_heart():
#     # Set up the screen and turtle
#     screen = turtle.Screen()
#     screen.title("I Love You")
#     screen.bgcolor("white")

#     pen = turtle.Turtle()
#     pen.shape("turtle")
#     pen.color("red")
#     pen.speed(2)  # Set the drawing speed

#     # Move to start position
#     pen.penup()
#     pen.goto(0, -100)  # Move the turtle to the starting position
#     pen.pendown()
    
#     # Draw the heart shape
#     pen.begin_fill()
#     pen.left(140)
#     pen.forward(180)
#     pen.circle(-90, 200)
#     pen.left(120)
#     pen.circle(-90, 200)
#     pen.forward(180)
#     pen.end_fill()
    
#     # Hide the turtle
#     pen.hideturtle()

#     # Draw the letter "i" on the left side
#     pen.penup()
#     pen.goto(-200, -20)  # Adjust position for "i"
#     pen.pendown()
#     pen.color("black")
#     pen.write("i", align="center", font=("Arial", 120, "bold"))

#     # Draw the letter "u" on the right side
#     pen.penup()
#     pen.goto(200, -20)  # Adjust position for "u"
#     pen.pendown()
#     pen.write("u", align="center", font=("Arial", 120, "bold"))

#     # Finish
#     screen.mainloop()

# # Call the function to draw the heart and letters
# draw_heart()



import turtle
import math

def draw_heart():
    # Set up the screen and turtle
    screen = turtle.Screen()
    screen.title("Turtle Heart Drawing")
    screen.bgcolor("white")
    
    pen = turtle.Turtle()
    pen.shape("turtle")
    pen.color("red")
    pen.speed(2)  # Set the drawing speed
    
    # Move to start position
    pen.penup()
    pen.goto(0, -150)  # Move the turtle to the starting position
    pen.pendown()
    
    # Draw the heart shape using parametric equations 
    pen.begin_fill()
    for t in range(0, 361):
        theta = math.radians(t)
        x = 16 * math.sin(theta) ** 3
        y = 13 * math.cos(theta) - 5 * math.cos(2 * theta) - 2 * math.cos(3 * theta) - math.cos(4 * theta)
        pen.goto(x * 10, y * 10)  # Scale the coordinates
    pen.end_fill()
    
    # Hide the turtle and finish
    pen.hideturtle()
    screen.mainloop()

# Call the function to draw the heart
draw_heart()
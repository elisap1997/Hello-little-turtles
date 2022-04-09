import turtle
wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Tess & Alex")

tess = turtle.Turtle()      # Create tess and set some attributes
tess.shape("turtle")        # my modification for turtle shape
tess.color("hotpink")
tess.pensize(5)

alex = turtle.Turtle()       # Create alex
alex.shape("turtle")         # my modification for turtle shape

for i in range(3):
  tess.forward(80)             # Make tess draw equilateral triangle
  tess.left(120)               # Complete the triangle

tess.right(180)              # Turn tess around
tess.forward(80)             # Move her away from the origin

for i in range(4):          #make alex draw a square
    alex.forward(50)
    alex.left(90)


wn.mainloop()
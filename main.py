import turtle
wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Tess & Alex")

tess = turtle.Turtle()      # Create tess and set some attributes
tess.shape("turtle")        # my modification for turtle shape
tess.color("hotpink")

alex = turtle.Turtle()       # Create alex
alex.shape("turtle")         # my modification for turtle shape

tess.penup()                # This is new
size = 20
for i in range(30):
   tess.stamp()             # Leave an impression on the canvas
   size = size + 3          # Increase the size on every iteration
   tess.forward(size)       # Move tess along
   tess.right(24)           #  ...  and turn her

clrs = ["yellow", "red", "purple", "blue"]
for c in clrs:               #make alex draw square
    alex.color(c)
    alex.speed(10)
    alex.forward(50)
    alex.left(90)


wn.mainloop()
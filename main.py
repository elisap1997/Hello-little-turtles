import turtle
userBackgroundColor = input("Enter Tk built in color for background: ")
userTessColor = input("Enter Tk built in color for Tess: ")
penWidth = int(input("Enter width of the pen: "))
wn = turtle.Screen()
wn.bgcolor(userBackgroundColor)      # Set the window background color
wn.title("Hi, Tess!")         # Set the window title

tess = turtle.Turtle()
tess.color(userTessColor)            # Tell tess to change her color
tess.pensize(penWidth)               # Tell tess to set her pen width

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.mainloop()
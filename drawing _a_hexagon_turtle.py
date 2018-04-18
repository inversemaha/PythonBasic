# Step 1: Make all the "turtle" commands available to us.
import turtle

# Step 2: Create a new turtle. We'll call it "maha"
maha = turtle.Turtle()

# declare a variables
num_side = 6
side_length = 70

# initial angle
angle = 360.0/num_side

# Loop  times. Everything I want to repeat is
# *indented* by four spaces.

for i in range(num_side):
    maha.forward(side_length)
    maha.left(angle)

turtle.done()
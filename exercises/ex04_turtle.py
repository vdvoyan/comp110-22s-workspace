"""House and scenery drawn by turtles!"""

__author__: str = "730518639"

import math 
# Used for accurate trig.
from turtle import Turtle, colormode, done 
colormode(255)


def main() -> None:
    """Turtle to draw the sky."""
    sky: Turtle = Turtle()
    # "Characteristics" of sky.
    sky.color(135, 206, 250)
    sky.fillcolor(135, 206, 250)
    sky.pencolor(135, 206, 250)
    sky.speed(50)
    sky.hideturtle()
    
    # What sky will do.
    sky.up()
    sky.goto(-640.0, 190.0)
    sky.down()

    sky.begin_fill()
    
    # Loop to simplify code. 
    i: int = 0
    while (i < 2):
        sky.forward(1500)
        sky.left(90)
        sky.forward(200)
        sky.left(90)
        i = i + 1
    
    sky.end_fill()


def ground() -> None:
    """Turtle to draw the ground."""
    ground: Turtle = Turtle()
    # "Characteristics" of ground.
    ground.color("Green")
    ground.fillcolor("Green")
    ground.pencolor("Green")
    ground.speed(50)
    ground.hideturtle()
    
    # What ground will do.
    ground.up()
    ground.goto(-640.0, -400.0)
    ground.down()

    ground.begin_fill()
    
    # Loop to simplify code. 
    i: int = 0
    while (i < 2):
        ground.forward(1500)
        ground.left(90)
        ground.forward(100)
        ground.left(90)
        i = i + 1
    
    ground.end_fill()


def sun() -> None:
    """Turtle for drawing sun in the sky."""
    sun: Turtle = Turtle()
    # "Characteristics" of sun.
    sun.color("Yellow")
    sun.fillcolor("Yellow")
    sun.pencolor("Yellow")
    sun.speed(50)
    sun.hideturtle()

    # What sun will do.
    sun.up()
    sun.goto(-580.0, 220.0)
    sun.down()

    sun.begin_fill()

    # Defining the sun as a circle with a radius.
    sun.circle(40)

    sun.end_fill()
    

def base() -> None:
    """Turtle for drawing base for house."""
    base: Turtle = Turtle()
    # "Characteristics" of base.
    base.color(150, 75, 0)
    base.fillcolor(150, 75, 0)
    base.pencolor(150, 75, 0)
    base.speed(50)
    base.hideturtle()
    
    # What base will do.
    base.up()
    base.goto(-200.0, -300.0)
    base.down()

    base.begin_fill()
    
    # Loop to simplify code. 
    i: int = 0
    while (i < 2):
        base.forward(400)
        base.left(90)
        base.forward(300)
        base.left(90)
        i = i + 1
    
    base.end_fill()


def roof() -> None:
    """Turtle for drawing roof for house."""
    roof: Turtle = Turtle()
    # "Characteristics" of roof.
    roof.color("Black")
    roof.fillcolor("Black")
    roof.pencolor("Black")
    roof.speed(50)
    roof.hideturtle()
    
    # What roof will do.
    roof.up()
    roof.goto(-200.0, 0.0)
    roof.down()

    roof.begin_fill()
    
    # Loop not needed since this is done only once.
    # Square root operation is used to precisely draw out the triangular roof. 
    roof.forward(400)
    roof.left(153.435)
    roof.forward(math.sqrt((100 * 100) + (200 * 200)))
    roof.left(53.13)
    roof.forward(math.sqrt((100 * 100) + (200 * 200)))

    roof.end_fill()


def door() -> None:
    """Turtle to draw door for house."""
    door: Turtle = Turtle()
    # "Characteristics" of door.
    door.color("Red")
    door.fillcolor("Red")
    door.pencolor("Red")
    door.speed(50)
    door.hideturtle()
    
    # What door will do.
    door.up()
    door.goto(-50.0, -300.0)
    door.down()

    door.begin_fill()
    
    # Loop to simplify code. 
    i: int = 0
    while (i < 2):
        door.forward(100)
        door.left(90)
        door.forward(150)
        door.left(90)
        i = i + 1
    
    door.end_fill()


def door_knob() -> None:
    """Turtle for drawing door knob for house's door."""
    door_knob: Turtle = Turtle()
    # "Characteristics" of door_knob.
    door_knob.color("Black")
    door_knob.fillcolor("Black")
    door_knob.pencolor("Black")
    door_knob.speed(50)
    door_knob.hideturtle()
    
    # What door_knob will do.
    door_knob.up()
    door_knob.goto(30.0, -230.0)
    door_knob.down()

    door_knob.begin_fill()
    
    # Loop to simplify code. 
    i: int = 0
    while (i < 2):
        door_knob.forward(20)
        door_knob.left(90)
        door_knob.forward(10)
        door_knob.left(90)
        i = i + 1
    
    door_knob.end_fill()    


def tree_trunk() -> None:
    """Turtle for drawing tree trunk next to house."""
    tree_trunk: Turtle = Turtle()
    # "Characteristics" of tree_trunk.
    tree_trunk.color(150, 75, 0)
    tree_trunk.fillcolor(150, 75, 0)
    tree_trunk.pencolor(150, 75, 0)
    tree_trunk.speed(50)
    tree_trunk.hideturtle()
    
    # What tree_trunk will do.
    tree_trunk.up()
    tree_trunk.goto(450.0, -300.0)
    tree_trunk.down()

    tree_trunk.begin_fill()
    
    # Loop to simplify code. 
    i: int = 0
    while (i < 2):
        tree_trunk.forward(70)
        tree_trunk.left(90)
        tree_trunk.forward(150)
        tree_trunk.left(90)
        i = i + 1
    
    tree_trunk.end_fill()


def tree_leaves() -> None:
    """Turtle for drawing leaves for tree next to house."""
    tree_leaves: Turtle = Turtle()
    # "Characteristics" of tree_leaves.
    tree_leaves.color("Green")
    tree_leaves.fillcolor("Green")
    tree_leaves.pencolor("Green")
    tree_leaves.speed(50)
    tree_leaves.hideturtle()

    # What tree_leaves will do.
    tree_leaves.up()
    tree_leaves.goto(485.0, -175.0)
    tree_leaves.down()

    tree_leaves.begin_fill()

    # Defining tree_leaves as a circle with a radius.
    tree_leaves.circle(100)

    tree_leaves.end_fill()


main()
ground()
sun()
base()
roof()
door()
door_knob()


def window_turtle() -> None:
    """Turtle for drawing window(s)."""
    # What window(s) will do and loop to simplify code. 
    window.begin_fill()
    i: int = 0
    while (i < 2):
        window.forward(60)
        window.left(90)
        window.forward(60)
        window.left(90)
        i = i + 1
    
    window.end_fill()


"""Window(s) for house."""
window: Turtle = Turtle()
# "Characteristics" of window(s).
window.color("Blue")
window.fillcolor("Blue")
window.pencolor("Blue")
window.speed(50)
window.hideturtle()

window.up()
window.goto(-160, -105)
window.down()
window_turtle()


window.up()
window.goto(100, -105)
window.down()
window_turtle()

tree_trunk()
tree_leaves()

if __name__ == "__main__":
    done()
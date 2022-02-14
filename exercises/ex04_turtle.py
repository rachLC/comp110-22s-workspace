"""EX04 - Turtle: Draw a scene from pacman."""

__author__ = "730394362"

from turtle import Turtle, colormode, done


def main() -> None:
    """The entrypoint of my scene."""
    # TODO: Declare your Turtle variable(s) here.
    raphael: Turtle = Turtle()
    # TODO: Call the procedures you define and pass your Turtle(s) as an argument.
    raphael.up()
    raphael.goto(400, -400.0)
    raphael.down()
    raphael.left(90)
    draw_outline(raphael, 300.0, -300.0)
    raphael.up()
    raphael.goto(0.0, 250.0)
    raphael.down()
    raphael.right(180)
    draw_pacman(raphael, 0.0, 250.0)
    raphael.up()
    raphael.goto(0.0, 200.0)
    raphael.down()
    draw_squares(raphael, 0.0, 200.0)
    raphael.up()
    raphael.goto(0.0, 150.0)
    raphael.down()
    draw_squares(raphael, 0.0, 150.0)
    raphael.up()
    raphael.goto(0.0, 100.0)
    raphael.down()
    draw_squares(raphael, 0.0, 100.0)
    raphael.up()
    raphael.goto(0.0, 0.0)
    raphael.down()
    raphael.color("pink")
    raphael.begin_fill()
    draw_ghost(raphael, 0.0, 0.0)
    raphael.end_fill()
    raphael.up()
    raphael.goto(0.0, -100.0)
    raphael.down()
    raphael.left(130)
    raphael.color("blue")
    raphael.begin_fill()
    draw_ghost(raphael, 0.0, -100.0)
    raphael.end_fill()
    raphael.up()
    raphael.goto(0.0, -200.0)
    raphael.down()
    raphael.right(250)
    draw_cherries(raphael, 0.0, -200.0)
    done()


# TODO: Define the procedures for other components in your scene here.

def draw_outline(raphael: Turtle, x: float, y: float) -> None:
    """Draws a box to outline the picture and provide a background."""
    i: int = 0
    raphael.color("black")
    raphael.begin_fill()
    while i < 5:
        raphael.forward(800)
        raphael.left(90)
        i += 1
    raphael.end_fill()


def draw_pacman(raphael: Turtle, x: float, y: float) -> None:
    """Draws circle with triangle missing to make pacman."""
    raphael.color("yellow")
    raphael.begin_fill()
    raphael.circle(40.0, 305.0)
    raphael.left(90)
    raphael.forward(40)
    raphael.right(120)
    raphael.forward(40)
    raphael.end_fill()


def draw_squares(raphael: Turtle, x: float, y: float) -> None:
    """Draws square dots that pacman follows."""
    i: int = 0
    raphael.color("white")
    raphael.begin_fill()
    while i < 5:
        raphael.forward(10)
        raphael.right(90)
        i += 1
    raphael.end_fill()


def draw_ghost(raphael: Turtle, x: float, y: float) -> None:
    """Draws semicircle, two parallel lines, and 4 lines to make ghost."""
    raphael.forward(20)
    raphael.circle(30, 180)
    raphael.forward(20)
    raphael.left(120)
    raphael.forward(20)
    raphael.right(80)
    raphael.forward(20)
    raphael.left(100)
    raphael.forward(20)
    raphael.right(95)
    raphael.forward(20)


def draw_cherries(raphael: Turtle, x: float, y: float) -> None:
    """Draws two circles and two lines to make cherries."""
    raphael.begin_fill()
    raphael.color("red")
    raphael.circle(20)
    raphael.end_fill()
    raphael.color("brown")
    raphael.forward(70)
    raphael.right(120)
    raphael.forward(70)
    raphael.color("red")
    raphael.begin_fill()
    raphael.circle(20)
    raphael.end_fill()


if __name__ == "__main__":
    main()
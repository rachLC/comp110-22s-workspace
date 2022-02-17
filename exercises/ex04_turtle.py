"""EX04 - Turtle: Draw pacman about to eat some ghosts and cherries."""

__author__ = "730394362"

from turtle import Turtle, done


def main() -> None:
    """The entrypoint of my scene."""
    # Declaring and establishing turtle variable.
    raphael: Turtle = Turtle()
    raphael.up()
    raphael.goto(400, -400.0)
    # Calling function that will create a black square for the background.
    draw_outline(raphael, 300.0, -300.0)
    raphael.up()
    raphael.goto(0.0, 250.0)
    # Calling function that will create pacman shape and color it.
    draw_pacman(raphael, 0.0, 250.0)
    n: float = 200.0
    # Creating loop in order to produce 3 white squares without having to keep calling the function.
    while n > 50.0:
        raphael.goto(0.0, n)
        draw_squares(raphael, 0.0, n)
        n -= 50.0
    raphael.goto(0.0, 0.0)
    # Assigning a color to the first ghost.
    raphael.color("pink")
    raphael.begin_fill()
    # Calling function that will creates the ghost shape.
    draw_ghost(raphael, 0.0, 0.0)
    raphael.end_fill()
    raphael.goto(0.0, -100.0)
    raphael.left(130)
    # Assigning color to the second ghost.
    raphael.color("blue")
    raphael.begin_fill()
    # Calling function that draws ghost shape again to create a second ghost.
    draw_ghost(raphael, 0.0, -100.0)
    raphael.end_fill()
    raphael.goto(0.0, -200.0)
    raphael.right(250)
    # Calling function that will draw and color cherries.
    draw_cherries(raphael, 0.0, -200.0)
    done()


def draw_outline(raphael: Turtle, x: float, y: float) -> None:
    """Draws a box to outline the picture and provide a background."""
    i: int = 0
    raphael.down()
    raphael.left(90)
    raphael.color("black")
    raphael.begin_fill()
    while i < 5:
        raphael.forward(800)
        raphael.left(90)
        i += 1
    raphael.end_fill()
    raphael.up()


def draw_pacman(raphael: Turtle, x: float, y: float) -> None:
    """Draws incomplete circle with two lines coming from center to make pacman with an open mouth, and lined and filled in with yellow."""
    raphael.down()
    raphael.right(180)
    raphael.color("yellow")
    raphael.begin_fill()
    raphael.circle(40.0, 305.0)
    raphael.left(90)
    raphael.forward(40)
    raphael.right(120)
    raphael.forward(40)
    raphael.end_fill()
    raphael.up()


def draw_squares(raphael: Turtle, x: float, y: float) -> None:
    """Draws white square dots that pacman follows."""
    i: int = 0
    raphael.color("white")
    raphael.begin_fill()
    while i < 5:
        raphael.down()
        raphael.forward(10)
        raphael.right(90)
        raphael.up()
        i += 1
    raphael.end_fill()


def draw_ghost(raphael: Turtle, x: float, y: float) -> None:
    """Draws semicircle, two parallel lines, and 4 lines to make ghost."""
    raphael.down()
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
    raphael.up()


def draw_cherries(raphael: Turtle, x: float, y: float) -> None:
    """Draws two circles and two connected lines to make cherries."""
    raphael.down()
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
    raphael.up()


if __name__ == "__main__":
    main()
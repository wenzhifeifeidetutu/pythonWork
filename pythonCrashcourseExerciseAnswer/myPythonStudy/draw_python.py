import turtle;

def draw_squre(some_turtle) :
    for i in range(1, 5) :
        some_turtle.forward(100);
        some_turtle.right(90);


def draw_art() :
    window = turtle.Screen();
    window.bgcolor("red");

    turtle1 = turtle.Turtle();
    turtle1.shape("turtle");
    turtle1.color("yellow");
    turtle1.speed(2);
    for i in range(1, 37):
        draw_squre(turtle1);
        turtle1.right(10);






    window.exitonclick();






draw_art();
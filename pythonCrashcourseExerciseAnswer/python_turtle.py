import turtle;


def draw_square():
    #get Screen
    windown = turtle.Screen();
    #change Screen bg is red
    windown.bgcolor("red");
    
    #get Turtle
    brad = turtle.Turtle();
    #draw turtle
    #change shape
    brad.shape("turtle");
    #change color
    brad.color("black");
    #change speed
    brad.speed(1);
    i = 0;
    while(i<4):
        brad.forward(100);
        brad.right(90);
        i = i+1;
    

    angel = turtle.Turtle();
    angel.color("blue");

    angel.circle(100);
    
    jiji = turtle.Turtle();
    jiji.circle(200);
        
    windown.exitonclick();
#change
def draw_square(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(100);
        some_turtle.right(90);
        i = i+1;
        
        
def draw_art():
    window = turtle.Screen()
    window.bgcolor("yellow");

    bread = turtle.Turtle();
    bread.shape("turtle");
    bread.speed(10);
    draw_square(bread);
    
    angel = turtle.Turtle();
    angel.color("blue");

    angel.circle(100);
    
    jiji = turtle.Turtle();
    jiji.circle(200);
    window.exitonclick();

#draw_square();
draw_art();

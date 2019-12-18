import turtle


def drawSquare(sq):



    i=1
    while(i<=4):
        sq.forward(100)
        sq.right(90)
        i = i+1



def drawCirle():
    cir = turtle.Turtle()
    cir.color("blue")
    cir.shape("arrow")
    cir.circle(150)

def drawtriangle():
    tri = turtle.Turtle()
    tri.color("yellow")
    i =1
    while(i<=3):
        tri.forward(100)
        tri.right(60)
        i=i+1
    tri.forward(100)
    tri.right(90)


def draw():
    window = turtle.Screen()
    window.bgcolor("red")
    sq = turtle.Turtle()
    sq.color("green")
    sq.speed(2)
    for i in range(1, 36):
        drawSquare(sq)
        sq.right(10)

#drawSquare()
#drawCirle()
#drawtriangle()
draw()



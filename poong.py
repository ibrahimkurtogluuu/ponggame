import turtle

wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width= 800, height= 600)
wn.tracer(10)

score_a = 0
score_b = 0

paddle_a = turtle.Turtle()
paddle_a.color("green")
paddle_a.penup()
paddle_a.goto(-350,0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len= 1 )
paddle_a.pensize(50)
paddle_a.speed(10)



paddle_b = turtle.Turtle()
paddle_b.color("green")
paddle_b.penup()
paddle_b.goto(350,0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len= 1 )
paddle_b.pensize(50)
paddle_b.speed(10)

ball = turtle.Turtle()
ball.color("yellow")
ball.penup()
ball.goto(0,0)
ball.shape("circle")
ball.pensize(50)
ball.speed(10)
ball.dx = 0.3
ball.dy = 0.3

pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.color("white")
pen.write("Player A : 0 Player B: 0", align= "center", font= ("Arial",20,"normal"))





def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx )
    ball.sety(ball.ycor() + ball.dy )

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(320,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A :{} Player B:{}".format(score_a, score_b) , align="center", font=("Arial", 20, "normal"))


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() < -390:
        ball.goto(-320,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A :{} Player B:{}".format(score_a, score_b), align="center", font=("Arial", 20, "normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 45 and ball.ycor() > paddle_b.ycor() -45):
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 45 and ball.ycor() >  paddle_a.ycor() - 45):
        ball.dx *= -1


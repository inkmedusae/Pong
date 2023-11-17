import turtle

# screen settings
main = turtle.Screen()
main.title("Pong - wd")
main.bgcolor("black")
main.setup(width=900, height=600)
main.tracer
playerOne_Score = 0
playerTwo_Score = 0

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 20, "normal"))

# first paddle characteristics
firstPaddle = turtle.Turtle()
firstPaddle.speed(0)

firstPaddle.shape("square")
firstPaddle.shapesize(stretch_wid=5, stretch_len=1 )
firstPaddle.color("white")
firstPaddle.penup()
firstPaddle.goto(-400, 0)

# second paddle characteristics
secondPaddle = turtle.Turtle()
secondPaddle.speed(0)

secondPaddle.shape("square")
secondPaddle.shapesize(stretch_wid=5, stretch_len=1 )
secondPaddle.color("white")
secondPaddle.penup()
secondPaddle.goto(400, 0)

# ball characteristics
ball = turtle.Turtle()
ball.speed(0)

ball.shape("square")
ball.shapesize(stretch_wid=1, stretch_len=1 )
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3.5
ball.dy = 3.5

#  game mechanics
main.listen()
def firstPaddleMoveup ():
    yCoord = firstPaddle.ycor()
    yCoord += 20
    firstPaddle.sety(yCoord)
def firstPaddleMovedown ():
    yCoord = firstPaddle.ycor()
    yCoord -= 20
    firstPaddle.sety(yCoord)

main.onkeypress(firstPaddleMoveup, "w")
main.onkeypress(firstPaddleMovedown, "s")
    # second paddle movement
def secondPaddleMoveup (): 
    yCoord = secondPaddle.ycor()
    yCoord += 20
    secondPaddle.sety(yCoord)
def secondPaddleMovedown ():
    yCoord = secondPaddle.ycor()
    yCoord -= 20
    secondPaddle.sety(yCoord)
main.onkeypress(secondPaddleMoveup, "Up")
main.onkeypress(secondPaddleMovedown, "Down")
# init loop
while True:
    main.update()
    
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    elif ball.xcor() > 440:
        ball.goto(0, 0)
        ball.dx *= -1
        playerOne_Score += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(playerOne_Score, playerTwo_Score), align="center", font=("Courier", 20, "normal"))
    elif ball.xcor() < -440:
        ball.goto(0, 0)
        ball.dx *= -1
        playerTwo_Score += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(playerOne_Score, playerTwo_Score), align="center", font=("Courier", 20, "normal"))


    # collisions with paddle
    if ball.xcor() < -380 and ball.ycor() < firstPaddle.ycor() + 60 and ball.ycor() > firstPaddle.ycor() - 60:
        ball.dx *= -1 
    
    elif ball.xcor() > 380 and ball.ycor() < secondPaddle.ycor() + 60 and ball.ycor() > secondPaddle.ycor() - 60:
        ball.dx *= -1

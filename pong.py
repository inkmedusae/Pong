import turtle

# screen settings
main = turtle.Screen()
main.title("Pong - wd")
main.bgcolor("black")
main.setup(width=900, height=600)
main.tracer

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

ball.shape("circle")
ball.shapesize(stretch_wid=1, stretch_len=1 )
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

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
    elif ball.xcor() > 440 or ball.xcor() < -440:
        ball.goto(0, 0)
        ball.dx *= -1
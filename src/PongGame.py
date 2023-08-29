#First game in python by using turtle
#This is for more a simpler game, later on we will be using pygame for more advance games
#However, for now we will just be using turtle for this simple game


#first lets import turtle
import turtle

#next lets create a window

wn = turtle.Screen() #the window
wn.title("Pong By Raymond") #creating the title
wn.bgcolor("black")#this changes the background color, in this case into black
wn.setup(width = 800, height = 600)#this will change the size of the window
wn.tracer(0)#this basically stops the window from updating, making us manualy update it. Allowing us to speed up our games


# Here is where we will create the "score board" for the game
score_a = 0 # creating the variable score a, to keep score of the a side
score_b = 0 # creating the variable score_b to keep score of the b side

# Now we are going to add the "poles" into the screen
# Paddle A, the left paddle
paddle_a = turtle.Turtle() #the first turtle is lower case because that is the name of model (the import) and capital "T" for the method name
paddle_a.speed(0) #this will set the speed for the animation, at zero being maximum speed
paddle_a.shape("square")#making the shape of the paddle
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0) #the -350 is a x-coordinate, basically making this paddle to the left, the 0 makes it start in the middle

#Paddle B, the right paddle
paddle_b = turtle.Turtle() #the first turtle is lower case because that is the name of model (the import) and capital "T" for the method name
paddle_b.speed(0) #this will set the speed for the animation, at zero being maximum speed
paddle_b.shape("square")#making the shape of the paddle
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0) #the +350 is a x-coordinate, basically making this paddle to the right, the 0 makes it start in the middle


#Ball
ball = turtle.Turtle() #the first turtle is lower case because that is the name of model (the import) and capital "T" for the method name
ball.speed(0) #this will set the speed for the animation, at zero being maximum speed
ball.shape("square")#making the shape of the paddle
ball.color("white")
ball.penup()
ball.goto(0, 0) #the first 0 is the x-coordinate, basically making the ball start in the center, the other zero is the y-coordinate makes it start in the middle
ball.dx = 5 #the "d" in dx means delta, or in other words, change
ball.dy = -5 #this means that every time our ball move, its movng by 0.2 px


# Next we are going to create some functions, remeber a function is a piece of a program thats been defied for it
def paddle_a_up():
    y = paddle_a.ycor() #the ".ycor()" is from the turtle module, it returns the y coordinate
    y += 30 #since we want the padddle to move up, we added 30 to the y coordinate, making the paddle move up 30 px
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() #the ".ycor()" is from the turtle module, it returns the y coordinate
    y -= 30 #since we want the padddle to move down, we subtarcted 30 to the y coordinate, making the paddle move down 30 px
    paddle_a.sety(y)

# Creating funchtions for paddle_b
def paddle_b_up():
    y = paddle_b.ycor() #the ".ycor()" is from the turtle module, it returns the y coordinate
    y += 30 #since we want the padddle to move up, we added 30 to the y coordinate, making the paddle move up 30 px
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() #the ".ycor()" is from the turtle module, it returns the y coordinate
    y -= 30 #since we want the padddle to move down, we subtracted 30 to the y coordinate, making the paddle move down 30 px
    paddle_b.sety(y)

# Now its time to create the remainder design for the pong game
# first lets draw the score on the screen, we do this by basically making a pen

pen = turtle.Turtle() # creating the pen here, same way we created the paddle
pen.speed(0) # remember this is to make sure that the speed of the turtle is quickly
pen.color("white") # when the pen is drawing/writting, the color will be white
pen.penup() # We want the pen up, so when the pen is moving, we wont end up drawing a line
                # because every turtle starts dead center in the screen (0, 0), unitl you change the location

pen.hideturtle() # we are hiding the turtle because we dont need to see it, now as we did before, we did not do this
                     # with the ball and the paddles because we want to see them, but the pen we dont want to see, we
                     # just want to see the text that the pen is going to write (in this case the score of course)

pen.goto(0, 260) # we chose the y for 260 because the height of the screen is 600 (can see that by scrolling up to the window setup)
                     #since the x - coordinate is 0, the text writing will be in the center of the window

pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal")) # This will write what we have in the quotations, also, the align
                                                                                        # command makes the text be center, automatically
#keyboard binding
wn.listen() #tells the program (the window) to listen for the keyboard input
wn.onkey(paddle_a_up, "q") #listens for when the key is pressed for q, wont work if we use capital Q
wn.onkey(paddle_a_down, "a") #we use "onkey" instead of onkeypress, onkeypress is suppose to be Python 3 but for some reason it isnt working
wn.onkey(paddle_b_up, "p") #listens for when the key is pressed for q, wont work if we use capital Q
wn.onkey(paddle_b_down, "l") #we use "onkey" instead of onkeypress, onkeypress is suppose to be Python 3 but for some reason it isnt working
                            #Now if I want to use the up and down arrows, I would need to put UP in all caps, the same for down

# Next, is the main game loop
while True:
    wn.update()#everytime the loop runs, it update the Screen

# next part of code is to move the ball, its going to be in the while loop, so it can continue to randomly move
    ball.setx(ball.xcor() + ball.dx) #remember that the ball startts at (0,0), so first time through the loop, its gonna go (2,0) and so on
    ball.sety(ball.ycor() + ball.dy)

# Now we going to do some boarder checking, meaning we are going limit where the ball goes so it doesnt go off screen
# If statements in python is weird, in order to make sure that the program reads both the "if statements"
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1


# Now we have to do the left and right border of the window, so if it goes off to the right or left side, it
# will reset back to the center
# the score_a part in the first if statement, basically means since the ball went off to the right
#(remember the right is the players b side, so this means player b missed the ball)
# player a (player_a, in this case) scored a point. now same goes for the second if - statement, with the score_b
# which means that player_a has missed the ball which means that player_b has scored a point
# Lastly, in order to actually update the score (meaning, in order to make the numbers change, we would need to update the pen.write)
# we copy the same line of code for pen.write, we would use the ".format( , )" printing style
# again, since this is the turtle module, we will need to clear the previous number print of the score,so that, when the
# score updates, it will not print over the previous print number. We do this by using the "pen.clear()"
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear() # will clear the previous printed number before the number updates
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


# This will be for when the ball hits the paddle from the right, it will bounce off the paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

# This will be for when the ball hits the paddle, on the left side, it will bounce off the paddle from the left
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1


            
# Next, we will make a game over, so if one side scores a certain amount of times, then the game should end and announce
# who the winner is
    if score_a == 10:
        pen.clear()
        pen.write("Player A has won!!", align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx = 0
        ball.dy = 0

    if score_b == 10:
        pen.clear()
        pen.write("Player B has won!!", align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx = 0
        ball.dy = 0

#Next, we will have a speed up round, for when either player A or player B makes it to five points
    #if score_a == 5 or score_b == 5:
           # ball.dx = 12
            #ball.dy = -12

           
# Next, we gonna learn how to add sound into the game. In order to do this, you would need to have some kind of
# sound file. (the website we could use is bounce.wave, it contains a bunch of old school sound effects)
# You have to put the sound file in the same folder as the turtle file (which in this case is the pongGame)
# so first we have to import os, this will operate with the operating system through text commands
# Then we would do an os.system("") and in the parenthesis we would put "afplay bounce.wav" (this is only for mac)
# and at the end of that, we add the "&" symbol, so the whole thing doesnt freeze when it makes the sound
# so it would look like "afplay bounce.wav&" (I believe in this case, since this is based off the video, the bounce.way is only his file name)

import turtle
import os
import math

#Set ut the screen
ms = turtle.Screen()
ms.bgcolor("black")
ms.title("Space Indvaders")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("red")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()


#Create the player
player = turtle.Turtle()
player.color("green")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

#Movement of the player
playerspeed = 15

#Define bullet state
#Read
#Fire
bulletstate = "ready"

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x <= -285:
        x = -285
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x >= 285:
        x = 285    
    player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate == "ready" : # "ready":
        bulletstate = "fire"
        #move the bullet to just above the player
        x = player.xcor()
        y = player.ycor()+10
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollision(t1, t2): 
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15: 
        return True
    else:
        return False


#Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#Create the enemy
enemy = turtle.Turtle()
enemy.color("pink")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200,250)

enemyspeed = 2

#Create the player bullet

bullet = turtle.Turtle()
bullet.color("white")
bullet.shape("circle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)

bulletspeed = 20
bullet.hideturtle()



#Main game loop
while True:
    #Move the enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    # reverse the enemy
    if enemy.xcor() > 280:
        enemyspeed *= -1
        y = enemy.ycor()
        y -= 50
        enemy.sety(y)

    if enemy.xcor() < -280:
        enemyspeed *= -1
        y = enemy.ycor()
        y -= 50
        enemy.sety(y)

    #Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    if bullet.ycor() > 299:
        bullet.hideturtle()
        bulletstate = "ready" 

    #Check for collision
    if isCollision(bullet, enemy):
        #reset the bullet
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0, -400)
        #Reset the enemy
        enemy.setposition(-200,250)

    if isCollision(enemy, player):
        player.hideturtle()
        enemy.hideturtle()
        print ("GAME OVER")
        break
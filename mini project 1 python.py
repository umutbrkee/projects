import turtle
import random

# this function is for semi circle movement
def semi_circle(my_turtle, step):
    my_turtle.left(270)
    my_turtle.circle(step/2, -180)
    my_turtle.right(90)


# this function is for stairs movement
def stairs(my_turtle, step):
    for x in range(2):
        my_turtle.forward(step / 5)
        my_turtle.left(90)
        my_turtle.forward(step / 5)
        my_turtle.right(90)
    for x in range(2):
        my_turtle.forward(step / 5)
        my_turtle.right(90)
        my_turtle.forward(step / 5)
        my_turtle.left(90)
    my_turtle.forward(step / 5)


# this function is for forward movement
def forward(my_turtle, step):
    my_turtle.forward(step)


# this function is for random choose from 3 pre defined movements
def random_movement(my_turtle, step):
    movements = ["semi_circle", "stairs", "forward"]
    if random.choice(movements) == "semi_circle":
        print "semi circle"
        semi_circle(my_turtle, step)
    elif random.choice(movements) == "stairs":
        print "stairs"
        stairs(my_turtle, step)
    else:
        print "forward"
        forward(my_turtle, step)


# this function is for movement chance for a player from user input
def player(my_turtle, step):
    random_step = random.randint(0, 100)
    if random_step > 0 and random_step <= 100 - step:
        print "Success :))))"
        random_movement(my_turtle, step)
        return True
    else:
        print"You Failed :(((( "
        return False

#this function is showing points of every player
def show_points(first, second):
    print first_turtle_name, "'s score:", first
    print second_turtle_name, "'s score:", second


# this function is for adding points to the player if moves
def add_point(player, count_point, step):
    if player == True:
        return count_point+step
    else:
        return count_point


# this function is for checking win
def check_win(count_point_1, count_point_2):
    if count_point_1 >= 200:
        print first_turtle_name, "win"
        return True
    elif count_point_2 >= 200:
        print second_turtle_name, "win"
        return True
    else:
        return False


count_round = 1
win = False


# this function is for looping everything and keep them poroperly
def round(round):
    count_point_1 = 0
    count_point_2 = 0
    turtle_list = ["turtle1", "turtle2"]
    if random.choice(turtle_list) == "turtle1":
        while count_point_1 < 200 or count_point_2 < 200:
            print "+++++++++++ round", round, "+++++++++++"
            show_points(count_point_1, count_point_2)
            print first_turtle_name, "plays"
            step = input("How many steps would you like to take? ")
            count_point_1 = add_point(player(first_turtle, step), count_point_1, step)
            win = check_win(count_point_1, count_point_2)
            round += 1
            if win == True:
                break
            print "+++++++++++ round", round, "+++++++++++"
            show_points(count_point_1, count_point_2)
            print second_turtle_name, "plays"
            step = input("How many steps would you like to take? ")
            count_point_2 = add_point(player(second_turtle, step), count_point_2, step)
            win = check_win(count_point_1, count_point_2)
            round += 1
            if win == True:
                break
            elif win == False:
                continue

    else:
        while count_point_1 < 200 or count_point_2 < 200:
            print "+++++++++++ round", round, "+++++++++++"
            show_points(count_point_1, count_point_2)
            print second_turtle_name, "plays"
            step = input("How many steps would you like to take? ")
            count_point_2 = add_point(player(second_turtle, step), count_point_2, step)
            win = check_win(count_point_1, count_point_2)
            if win == True:
                break
            round += 1
            print "+++++++++++ round", round, "+++++++++++"
            show_points(count_point_1, count_point_2)
            print first_turtle_name, "plays"
            step = input("How many steps would you like to take? ")
            count_point_1 = add_point(player(first_turtle, step), count_point_1, step)
            win = check_win(count_point_1, count_point_2)
            round += 1
            if win == True:
                break
            elif win == False:
                continue

# this loop is for creating turtles giving them color and names
while True:
    wd=turtle.Screen()
    while True:
            first_turtle=raw_input("What is the name of first turtle?")
            first_turtle_name = first_turtle
            if first_turtle_name == "":
                print"Please write a name for your turtle!!"
                continue
            break
    first_turtle = turtle.Turtle()  # turtle instance creation
    first_turtle.shape("turtle")
    first_turtle.hideturtle()           # make the turtle invisible
    first_turtle.penup()                # don't draw when turtle moves
    first_turtle.goto(-300, -200)       # move the turtle to a location
    first_turtle.showturtle()           # make the turtle visible
    first_turtle.pendown()              # draw when the turtle moves
    while True:
            first_turtle_color = raw_input("please select a color for your Turtle red-blue-yellow?")
            if first_turtle_color in ("red","blue","yellow","RED","BLUE","YELLOW"):
                first_turtle.color(first_turtle_color)
                print "----", first_turtle_name, " IS READY TO GO :)----"
                break
            else:
                print first_turtle_color, " is not a valid color please select one of  red-blue-yellow"
                continue
    while True:
            second_turtle=raw_input("What is the name of second turtle?")
            second_turtle_name = second_turtle
            if second_turtle_name == "":
                print"Please write a name for your turtle!!"
                continue
            if second_turtle_name == first_turtle_name:
                print second_turtle_name, "is taken, please choose another name"
                continue
            break
    second_turtle = turtle.Turtle()  # turtle instance creation
    second_turtle.shape("turtle")
    second_turtle.hideturtle()           #make the turtle invisible
    second_turtle.penup()                #don't draw when turtle moves
    second_turtle.goto(-300, -250)       #move the turtle to a location
    second_turtle.showturtle()           #make the turtle visible
    second_turtle.pendown()              #draw when the turtle moves
    while True:
            second_turtle_color = raw_input("please select a color for your Turtle red-blue-yellow?")
            if second_turtle_color == first_turtle_color:
                print "This color already taken please choose another one"
                continue
            elif second_turtle_color in ("red", "blue", "yellow", "RED", "BLUE", "YELLOW"):
                second_turtle.color(second_turtle_color)
                print "----", second_turtle_name, " IS READY TO GO :)----"
                break
            else:
                print second_turtle_color, " is not a valid color please select one of  red-blue-yellow"
                continue
    round(count_round)
    while True:
        answer = raw_input('Do you want to play again? (yes/no): ')
        if answer in ('yes', 'no'):
            break
        print 'Invalid input.'
    if answer == 'yes':
        wd.clear()
        continue
    else:
        print 'Goodbye'
        break




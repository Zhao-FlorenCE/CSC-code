from turtle import Turtle, Screen
import random

# States of the game
game_state = 0
start = 0
pause = 9
run = 1
win = 2
lose = -1

# Initial settings about the upper status
contact = 0
food_left = 0
past_time = 0
motion = 'PAUSE'
original_motion = 'PAUSE'

# Set the initial screen
def set_screen():

    global screen
    screen = Screen()
    screen.setup(width = 662, height = 744, starty = 20)
    screen.tracer(False)
    screen.title('Snake by Guangxin Zhao')

# Set the bounders of the game and the status
def set_table():

    table = Turtle()
    table.hideturtle()
    table.up()
    table.goto(-251, 209)
    table.down()
    table.goto(-251, -292)
    table.goto(251, -292)
    table.goto(251, 210)
    table.goto(-251, 210)
    table.goto(-251, 211)
    table.goto(251, 211)
    table.goto(251, 292)
    table.goto(-251, 292)
    table.goto(-251, 211)

# Set the words in the status
def set_box():

    global box
    box = set_turtle(pos = (-230, 240))
    box.write('Contact: {}               Time: {}               Motion: {}'.format(contact, past_time, 'PAUSE'), \
              font = ('Arial', 14, 'normal'))

# Set the welcome text
def set_text():

    global words
    words = set_turtle(pos = (0, -50))
    words.write('Welcome to Guangxin\'s version of snake...\n\n' 
                'You are going to use the 4 arrow keys to move the snake\n' 
                'around the screen, trying to sonsume all the food items\n'
                'brefore the moster catches you...\n\n'
                'Click anywhere on the screen to start the game, have fun!!', \
                align = 'center', font = ('Arial', 12, 'normal'))

# Set the end of the game
def show_result():

    global game_state, motion, original_motion
    result_turtle = set_turtle(pos = (0, -41))

    if game_state == win:
        result_turtle.pencolor('red')
        result_turtle.write('Winner!!', align = 'center', font = ('Arial', 12, 'normal'))
    elif game_state == lose:
        result_turtle.pencolor('purple')
        result_turtle.write('Game over!!', align = 'center', font = ('Arial', 12, 'normal'))
    
    motion = 'PAUSE'
    original_motion = ''
    box.write('Contact: {}               Time: {}               Motion: {}'.format(contact, past_time, motion), \
              font = ('Arial', 14, 'normal'))

# The function to set all turtle objects
def set_turtle(show = False, color = 'black', pos = (0, -41)):

    turtle = Turtle(shape = 'square')
    turtle.color(color, color)
    turtle.up()
    turtle.setpos(pos)

    if not show:
        turtle.hideturtle()

    return turtle

# Set the information of the monster
def set_monster():

    global monster
    monster_pos = [(-140, -141), (140, -141), (-140, 139), (140, 139)]
    monster = set_turtle(show = True, color = 'purple', pos = monster_pos[random.randint(0, 3)])

# Set the information of the snake
def set_snake():

    global snake
    snake = []
    head = set_turtle(show = True, color = 'red', pos = (0, -41))
    snake.append(head)

# Set the information of the foods
def set_food():

    global foods, food_turtles
    foods = []
    food_turtles = []
    map_foods = []

    while len(foods) < 9:
        food_x = random.randrange(-200, 200, step = 20)
        food_y = random.randrange(-241, 159, step = 20)
        if(food_x, food_y) not in map_foods:
            food_turtle = set_turtle(show = False, pos = (food_x, food_y - 10))
            food_turtles.append(food_turtle)
            food_number = len(food_turtles)
            foods.append({'number' : food_number, 'pos' : (food_x, food_y), 'state' : 1})
            map_foods.append((food_x, food_y))
            food_turtle.write(str(food_number), align = 'center', font = ('Arial', 12, 'normal'))
    
    food_turtle = set_turtle(show = False)
    food_turtles.append(food_turtle)
    foods.append({"number": 5, "pos": (0, -41), "state": 1})
    screen.update()

# Get the position of the turtle object called
def get_pos(turtle):

    x = round(turtle.xcor())
    y = round(turtle.ycor())
    return(x, y)

# Check whether the foods are all eaten
def check_eat():

    global foods
    for food in foods:
        if food['state'] == 1:
            return True

    return False

# Realize the function of eating food
def eat_food(number, pos):

    global food_left, foods
    food_left += number

    for i in range(len(food_turtles)):
        if foods[i]['pos'] == pos:
            foods[i]['state'] = 0
            food_turtles[i].clear()

# The function of moving the snake
def snake_move():

    global game_state, contact, food_left, snake, foods

    if original_motion:
        box.clear()
        t = 200
        if game_state == run:
            head = snake[0].clone()
            head_pos = get_pos(head)
            x = head_pos[0]
            y = head_pos[1]
            food_pos = [food['pos'] for food in foods]
            if head_pos in food_pos:
                food = food_pos.index(head_pos)
                if foods[food]['state'] == 1:
                    eat_food(foods[food]['number'], foods[food]['pos'])
            if (-250 >= (x - 20) and head.heading() == 180) or \
            ((x + 20) >= 250 and head.heading() == 0) or \
            (-291 >= (y -20) and head.heading() == 270) or \
            ((y + 20) >= 209 and head.heading() == 90):
                head.hideturtle()
                box.write('Contact: {}               Time: {}               Motion: {}'.format(contact, past_time, 'PAUSE'), \
                          font = ('Arial', 14, 'normal'))
            else:
                head.forward(20)
                snake.insert(0, head)
                snake[1].color('blue', 'black')
                snake[-1].hideturtle()
                if food_left == 0:
                    snake.pop()
                else:
                    food_left -= 1
                    t = 400
                if not check_eat():
                    game_state = win
                    show_result()
                box.write('Contact: {}               Time: {}               Motion: {}'.format(contact, past_time, motion), \
                          font = ('Arial', 14, 'normal'))
        else:
            box.write('Contact: {}               Time: {}               Motion: {}'.format(contact, past_time, 'PAUSE'), \
                      font = ('Arial', 14, 'normal'))

        screen.ontimer(snake_move, t = t)

# The function of moving the monster
def monster_move():

    global contact, game_state, past_time, monster
    differ_x = monster.xcor() - snake[0].xcor()
    differ_y = monster.ycor() - snake[0].ycor()
    
    if game_state == run:
        if abs(differ_x) > abs(differ_y):
            if differ_x > 0:
                monster.setheading(180)
            elif differ_x < 0:
                monster.setheading(0)
        else:
            if differ_y > 0:
                monster.setheading(270)
            elif differ_y < 0:
                monster.setheading(90)
        monster.forward(20)
        monster.hideturtle()
        monster = monster.clone()
        monster.showturtle()

    for i in range(len(snake)):
        if game_state == run and get_pos(snake[i]) == get_pos(monster):
            if i == 0:
                game_state = lose
                show_result()
            else:
                if game_state != pause and game_state != win and game_state != lose:
                    contact += 1

    t = random.randint(400, 500)
    screen.ontimer(monster_move, t = t)

# Initialize the start of the game
def game_start(x, y):

    global game_state, words, motion

    if game_state == start:
        words.clear()
        set_food()
        game_state = run
        motion = 'RIGHT'

# Change the state of pause
def game_pause():

    global game_state, motion, original_motion

    if game_state == run:
        game_state = pause
        original_motion = motion
        motion = 'PAUSE'
    elif game_state == pause:
        game_state = run
        motion = original_motion

# The function of the four directions
def move_up():

    global snake, motion
    snake[0].setheading(90)
    motion = 'UP'

def move_down():

    global snake, motion
    snake[0].setheading(270)
    motion = 'DOWN'

def move_left():

    global snake, motion
    snake[0].setheading(180)
    motion = 'LEFT'

def move_right():

    global snake, motion
    snake[0].setheading(0)
    motion = 'RIGHT'

# Mapping functional keys
def key_mapping():

    global screen
    screen.onclick(game_start)
    screen.onkey(move_up, "Up")    
    screen.onkey(move_down, "Down")
    screen.onkey(move_left, "Left")
    screen.onkey(move_right, "Right")
    screen.onkey(game_pause, "space")

# Set timer for the game status
def set_timer():

    global contact, past_time, game_state

    if game_state == run:
        past_time += 1

    screen.ontimer(set_timer, t = 1000)

# Set the udpate time of the screen
def screen_update():

    global game_state

    if game_state == run:
        screen.update()

    screen.ontimer(screen_update, t = 100)

# Call all the functions to start the game
if __name__ == '__main__':
    set_screen()
    set_table()
    set_box()
    set_text()
    screen.update()
    set_monster()
    set_snake()
    screen.listen()
    key_mapping()
    snake_move()
    monster_move()
    set_timer()
    screen_update()
    screen.mainloop()
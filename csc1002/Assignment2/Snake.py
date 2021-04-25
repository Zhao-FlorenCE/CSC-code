from turtle import Turtle, Screen
import random

AUTHOR = 'FlorenCE'

SCREEN_W = 662
SCREEN_H = 744
SCREEN_TITLE = 'snake'
HEAD_COLOR, BODY_COLOR, MONSTER_COLOR = 'red', 'black', 'purple'

food_left = 0

def set_screen():
    
    global screen
    screen = Screen()
    screen.setup(width = 662, height = 744, startx = None, starty = 20)
    screen.tracer(False)
    screen.title('Snake')

# Set the text of the initial interface
def set_text():

    global words
    words = set_turtle(pos = (-220, 251))
    words.write('Contact: Time: Motion:', \
                align = 'center', font = ('Arial', 20, 'bold'))

# Create turtle object
def set_turtle(show = False, color = 'black', pos = (0, 0)):

    turtle = Turtle(shape = 'square')
    turtle.color(color)
    turtle.up()
    turtle.setpos(pos)

    if not show:
        turtle.hideturtle()
    return turtle

# Create a monster object
def set_monster():

    global monster
    monster = set_turtle(show = True, color = 'purple', pos = ('noset', 'noset'))

# Create a snake onject
def set_snake():

    global set_snake
    snake = list()
    head = set_turtle(show = True, color = 'red')
    snake.append(head)

def set_food():

    global foods, food_turtles
    foods = list()
    food_turtles = list()

    while len(foods) < 9:
        food_x = random.randrange(-200, 200, step = 25)
        food_y = random.randrange(-200, 200, step = 25)
        if(food_x, food_y) not in foods:
            food_turtle = set_turtle(show = False, pos = (food_x, food_y))
            food_turtles.append(food_turtle)
            food_number = len(food_turtles)
            foods.append({'number' : food_number, 'pos' : (food_x, food_y), 'eaten' : 1})
            food_turtle.write(str(food_number), align = 'center', font = ('Arial', 12, 'normal'))

    screen.update()

def get_pos(turtle):

    x = round(turtle.xcor())
    y = round(turtle.ycor())
    return(x, y)

def check_win():

    global foods
    for food in foods:
        if food['eaten'] == 1:
            return True
    return False

def eat_food(number, pos):
    global food_left, foods
    food_left += number

    for i in range(len(food_turtles)):
        if foods[i]['pos'] == pos:
            foods[i]['state'] = 0
            food_turtles[i].clear()

def snake_move():
    global game_state, contact, foods_left, snake, foods
    t = 200

    if game_state == 0:
        head = snake[0].clone()
        head_pos = get_pos(head)
        x, y = head_pos[0], head_pos[1]

        food_pos = [food['pos'] for food in foods]
        if head_pos in food_pos:
            i = food_pos.index(head_pos)
            if foods[i]['state'] == 1:
                eat_food(foods[i]['number'], foods[i]['pos'])
                
        if (-250 >= (x - 25) and head.heading() == 180) or \
           ((x + 25) >= 250 and head.heading() == 0) or \
           (-250 >= (y -25) and head.heading() == 270) or \
           ((y + 25) >= 250 and head.heading() == 90):
            head.hideturtle()
        
        else:
            
if __name__ == '__main__':
    set_screen()
    set_text()
    
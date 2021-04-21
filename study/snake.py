from turtle import Turtle, Screen

""" Simulate motion of Mercury, Venus, Earth, and Mars """

planets = {
    'mercury': {'diameter': 0.383, 'orbit': 58, 'speed': 7.5, 'color': 'gray'},
    'venus': {'diameter': 0.949, 'orbit': 108, 'speed': 3, 'color': 'yellow'},
    'earth': {'diameter': 1.0, 'orbit': 150, 'speed': 2, 'color': 'blue'},
    'mars': {'diameter': 0.532, 'orbit': 228, 'speed': 1, 'color': 'red'},
}

def setup_planets(planets):
    for planet in planets:
        dictionary = planets[planet]
        turtle = Turtle(shape='circle')

        turtle.speed("fastest")  # speed controlled elsewhere, disable here
        turtle.shapesize(dictionary['diameter'])
        turtle.color(dictionary['color'])
        turtle.pu()
        turtle.sety(-dictionary['orbit'])
        turtle.pd()

        dictionary['turtle'] = turtle

    screen.ontimer(revolve, 50)

def revolve():
    for planet in planets:
        dictionary = planets[planet]
        dictionary['turtle'].circle(dictionary['orbit'], dictionary['speed'])

    screen.ontimer(revolve, 50)

screen = Screen()

setup_planets(planets)

screen.exitonclick()
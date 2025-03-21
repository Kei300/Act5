from random import *
from turtle import *
from freegames import path
import string

car = path('car.gif')
tiles = list(range(8)) * 2 # Since we want a 4x4 grid, with paired tiles

letters = list(string.ascii_uppercase[:8]) * 2  # Usar letras en lugar de números
shuffle(letters)

state = {'mark': None}
hide = [True] * 16
writer = Turtle(visible=False)
taps = 0

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 100) // 50 + ((y + 100) // 50) * 4)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 4) * 50 - 100, (count // 4) * 50 - 100

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']
    countTaps()

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
    checkTiles()

def countTaps():
    "Count the taps and draw them on the screen."
    global taps
    taps += 1
    writer.goto(210, 180)
    writer.clear()
    writer.write(taps)  

def checkTiles():
    "Check that all the tiles have been show"
    global taps
    for count in range(len(tiles)):
        if hide[count] == True:
            return

    print(f'You win with {taps} taps')
    writer.goto(210, 180)
    writer.clear()
    writer.write(f'You win with {taps} taps')

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(16): # A 4x4 grid gives us 16 tiles
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 15, y + 5)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()

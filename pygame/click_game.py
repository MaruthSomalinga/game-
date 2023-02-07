ortiz = Actor("character1")
ortiz.pos = 100, 50

WIDTH = 500
HEIGHT = ortiz.height + 20

def draw():
    screen.clear()
    screen.fill((255, 255, 255))
    ortiz.draw()

def update():
    ortiz.left = ortiz.left + 2
    if ortiz.left > WIDTH:
        ortiz.right = 8

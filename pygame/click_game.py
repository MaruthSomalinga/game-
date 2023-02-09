import time

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
def on_mouse_down(pos):
    if ortiz.collidepoint(pos):
        print("Eek!")
        sounds.eep.play()
        ortiz.image = 'character2'
        time.sleep(.25)
    else:
        print("You missed me!")

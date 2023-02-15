from random import randint

WIDTH = 400
HEIGHT = 400
score = 0
game_over = False
Character1 = Actor("character1")
Character1.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200


def draw():
    screen.fill("magenta")
    Character1.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="blue", topleft=(10, 10))

    if game_over:
        screen.fill("red")
        screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60)


def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))


def time_up():
    global game_over
    game_over = True


def update():
    global score

    if keyboard.left:
        Character1.x = Character1.x - 2
    elif keyboard.right:
        Character1.x = Character1.x + 2
    elif keyboard.up:
        Character1.y = Character1.y - 2
    elif keyboard.down:
        Character1.y = Character1.y + 2

    coin_collected = Character1.colliderect(coin)
    if coin_collected:
        score = score + 10
        place_coin()


clock.schedule(time_up, 100.05)
place_coin()

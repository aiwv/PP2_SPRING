import pygame
import random
import time
pygame.init()
WIDTH = 600
HEIGHT = 600

BLUE = (0, 0, 255)
RED = (255,0,0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')
font = pygame.font.SysFont('Algerian', 30)
FPS = 30
clock = pygame.time.Clock()

class Snake:
    def __init__(self, color):
        self.color = color
        self.speed = 2
        self.size = 3
        self.radius = 10
        self.dx = 2
        self.dy = 0
        self.elements = [[300, 300], [120, 100], [140, 100]]
        self.score = 0
        self.is_add = False
    
    def draw(self): 
        for element in self.elements:
            pygame.draw.circle(screen, self.color, element, self.radius)
    
    def add_snake(self):
        self.size += 1
        self.score += 1
        self.elements.append([0, 0])
        self.is_add = False
    
    def move(self):
        if self.is_add:
            self.add_snake()
        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]
        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

class Food:
    def __init__(self):
        self.x = random.randint(100, WIDTH - 70)
        self.y = random.randint(100, HEIGHT - 70)
        self.image = pygame.transform.scale(pygame.image.load("hamburger.png"),[30,30])

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

def show_score(x, y, score,color):
    show = font.render('Score: ' + str(score), True, color)
    screen.blit(show, (x, y))

def eat():
    global X1, X2, Y1, Y2
    X1 = snake1.elements[0][0]    
    X2 = snake2.elements[0][0]
    Y1 = snake1.elements[0][1]
    Y2 = snake2.elements[0][1]
    if food.x <= X1 <= food.x + 30 and food.y <= Y1 <= food.y + 30:
        snake1.is_add = True
        food.x = random.randint(50, WIDTH - 70)
        food.y = random.randint(50, HEIGHT - 70)
    if food.x <= X2 <= food.x + 30 and food.y <= Y2 <= food.y + 30:
        snake2.is_add = True
        food.x = random.randint(50, WIDTH - 70)
        food.y = random.randint(50, HEIGHT - 70)

wall_image = pygame.transform.scale(pygame.image.load('wall.png'),[30,45])
pt = False
def create_map(level_num):
    global lose
    with open(f'lvl/{level_num}.txt', mode='r') as file:
        y = 0  # row number
        for row in file:
            for i in range(len(row)):
                if row[i] == '1':
                    screen.blit(wall_image, (i * 30, y * 40))                   
                    if i*30 - 10 < X1 < i*30 + 40 and y*40 - 5 < Y1 < y*40 + 40:
                        lose = True
                        time.sleep(1)
                    if i*30 - 10 < X2 < i*30 + 40 and y*40 - 5 < Y2 < y*40 + 40:
                        lose = True
                        time.sleep(1)
            y += 1            



def game_over():
    # screen.fill((255, 0, 0))
    screen.blit(pygame.image.load("sn.png"), (0, 0))

    txt = font1.render('GAME OVER!', True, (250, 210, 1))
    result1 = font.render('Snake 1 scored: ' + str(snake1.score), True, (139, 0, 0))
    result2 = font.render('Snake 2 scored: ' + str(snake2.score), True, (139, 0, 0))

    screen.blit(txt, (300, 325))
    screen.blit(result1, (300, 390))
    screen.blit(result2, (300, 440))

    pygame.display.flip()
    time.sleep(3)
    lose = False
    pygame.quit()
snake1 = Snake(BLUE)
snake2 = Snake(RED)
food = Food()
lose = False
go = True
def play():
    global lose, go, snake1, snake2, food, pt
    lose = False
    snake1 = Snake(BLUE)
    snake2 = Snake(RED)
    food = Food()
    stop = True
    while go:
        eat()
        screen.fill((165, 206, 216))
        sc1=snake1.score//3
        sc2=snake2.score//3
        print (snake1.speed, snake2.speed)
        if sc1 > sc2 or sc2 > sc1:
            pt = True
        if pt == True and sc1 == sc2:
            snake1.speed += 1
            snake2.speed += 1
            pt = False
        create_map(max(sc2,sc1)+1)
        mil = clock.tick(FPS)
        if lose:
            game_over()
            go = False
        snake1.move()
        snake1.draw()
        snake2.move()
        snake2.draw()
        food.draw()
        show_score(35, 45, snake1.score,BLUE)
        show_score(435, 45, snake2.score,RED)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                go = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake1.dx = snake1.speed
                    snake1.dy = 0
                if event.key == pygame.K_LEFT:
                    snake1.dx = -snake1.speed
                    snake1.dy = 0
                if event.key == pygame.K_UP:
                    snake1.dx = 0
                    snake1.dy = -snake1.speed
                if event.key == pygame.K_DOWN:
                    snake1.dx = 0
                    snake1.dy = snake1.speed
                if event.key == pygame.K_d:
                    snake2.dx = snake2.speed
                    snake2.dy = 0
                if event.key == pygame.K_a:
                    snake2.dx = -snake2.speed
                    snake2.dy = 0
                if event.key == pygame.K_w:
                    snake2.dx = 0
                    snake2.dy = -snake2.speed
                if event.key == pygame.K_s:
                    snake2.dx = 0
                    snake2.dy = snake2.speed
                if event.key == pygame.K_k:
                    saves=[snake1.elements,snake2.elements,snake1.score,snake2.score,food.x,food.y,snake1.dx,snake1.dy,
                    snake2.dx,snake2.dy,snake1.size,snake2.size]
                    with open('lvl/save.txt', mode='w') as f:
                        for i in saves:
                            f.write("%s \n" % (i))
                        f.close()
                    go=False
                if event.key == pygame.K_SPACE:
                    stop = True
            while stop:
                    screen.fill((165, 206, 216))
                    create_map(1)
                    # mil = clock.tick(FPS)
                    snake1.draw()
                    snake2.draw()
                    food.draw()
                    show_score(35, 45, snake1.score,BLUE)
                    show_score(435, 45, snake2.score,RED)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            stop=False
                            go = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                stop = False
        pygame.display.flip()
    go=True

def saved_game():
    global lose,go,snake1,snake2,food, pt
    with open('lvl/save.txt', mode='r') as f:
        data = f.read().splitlines()
    lose=False
    pt = False
    snake1 = Snake(BLUE)
    snake2 = Snake(RED)
    food = Food()
    stop=True
    snake1.elements=eval(data[0])
    snake2.elements=eval(data[1])
    snake1.score=eval(data[2])
    snake2.score=eval(data[3])
    food.x=eval(data[4])
    food.y=eval(data[5])
    snake1.dx=eval(data[6])
    snake1.dy=eval(data[7])
    snake2.dx=eval(data[8])
    snake2.dy=eval(data[9])
    snake1.size=eval(data[10])
    snake2.size=eval(data[11])
    f.close()

    while go:

        eat()
        screen.fill((165, 206, 216))
        sc1=snake1.score//3
        sc2=snake2.score//3
        if sc1 > sc2 or sc2 > sc1:
            pt = True
        if pt and sc1 == sc2:
            snake1.speed += 1
            snake2.speed += 1
            pt = False

        create_map(max(sc2,sc1)+1)
        mil = clock.tick(FPS)
        if lose:
            game_over()
            go = False
        snake1.move()
        snake1.draw()
        snake2.move()
        snake2.draw()
        food.draw()
        show_score(35, 45, snake1.score,BLUE)
        show_score(435, 45, snake2.score,RED)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                go = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake1.dx = snake1.speed
                    snake1.dy = 0
                if event.key == pygame.K_LEFT:
                    snake1.dx = -snake1.speed
                    snake1.dy = 0
                if event.key == pygame.K_UP:
                    snake1.dx = 0
                    snake1.dy = -snake1.speed
                if event.key == pygame.K_DOWN:
                    snake1.dx = 0
                    snake1.dy = snake1.speed
                if event.key == pygame.K_d:
                    snake2.dx = snake2.speed
                    snake2.dy = 0
                if event.key == pygame.K_a:
                    snake2.dx = -snake2.speed
                    snake2.dy = 0
                if event.key == pygame.K_w:
                    snake2.dx = 0
                    snake2.dy = -snake2.speed
                if event.key == pygame.K_s:
                    snake2.dx = 0
                    snake2.dy = snake2.speed
                if event.key == pygame.K_k:
                    saves=[snake1.elements,snake2.elements,snake1.score,snake2.score,food.x,food.y,snake1.dx,snake1.dy,
                    snake2.dx,snake2.dy,snake1.size,snake2.size]
                    with open('lvl/save.txt', mode='w') as f:
                        for i in saves:
                            f.write("%s \n" % (i))
                        f.close()
                    go=False
                if event.key == pygame.K_SPACE:
                    stop = True
            while stop:
                    screen.fill((165, 206, 216))
                    create_map(1)
                    mil = clock.tick(FPS)
                    snake1.draw()
                    snake2.draw()
                    food.draw()
                    show_score(35, 45, snake1.score,BLUE)
                    show_score(435, 45, snake2.score,RED)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            stop=False
                            go = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                stop = False
        pygame.display.flip()
    go=True


font1 = pygame.font.SysFont('Algerian', 50)
def MainMenu():
    global click
    click = False
    while True:
        screen.blit(pygame.image.load("sn.png"), (0, 0))
        mx,my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(300, 325, 300, 50)
        button_2 = pygame.Rect(270, 400, 300, 50)
        screen.blit(font1.render('New Game', True, (139, 0, 0)), (300, 325))
        screen.blit(font1.render('Saved Game', True, (139, 0, 0)), (270, 390))

        if button_1.collidepoint((mx,my)):
            screen.blit(font1.render('New Game', True, (255, 255, 255)), (300, 325))
            if click :
                play()
        if button_2.collidepoint((mx,my)):
            screen.blit(font1.render('Saved Game', True, (255, 255, 255)), (270, 390))
            if click:
               saved_game()

        click=False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.flip()
        pygame.time.Clock().tick(30)

MainMenu()
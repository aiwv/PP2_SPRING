import pygame, sys
from pygame.locals import *
pygame.init()

FPS = 60
clock = pygame.time.Clock()

## Colors list
GREEN = (0, 255, 0)
GRAY = (197, 197, 197)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
DARK_GRAY = (107, 104, 99)
PINK = (249, 57, 255)
LIGHT_BLUE = (54, 207, 241)
YELLOW = (255, 241, 73)
ORANGE = (252, 155, 64)
PURPLE = (167, 0, 238)
DARK_GREEN = (58, 158, 73)
WHITE = (255, 255, 255)
BROWN = (85, 46, 46)
PRETTY_BLUE = (0, 238, 195)

SCREEN = pygame.display.set_mode((1000, 600))
SCREEN.fill(WHITE)
eraser = pygame.transform.scale(pygame.image.load("eraser.png"), (40, 40))
pencil = pygame.transform.scale(pygame.image.load("pencil.png"), (40, 40))
clear = pygame.transform.scale(pygame.image.load("clear.png"), (70, 70))


## font setup
menu_font = pygame.font.SysFont("Comic Sans MS", 20)
menu_text = menu_font.render("Colors", True, BLACK)
brush_text = menu_font.render("Brushes", True, BLACK)

draw = False
brush_size = 5
brush_color = GREEN


menu_rect = pygame.Rect(0, 0, 100, 600)
screen_rect = pygame.Rect(100, 0, 900, 600)

green_rect = pygame.Rect(8, 55, 40, 40)
red_rect = pygame.Rect(52, 55, 40, 40)
blue_rect = pygame.Rect(8, 99, 40, 40)
pink_rect = pygame.Rect(52, 99, 40, 40)
light_blue_rect = pygame.Rect(8, 143, 40, 40)
yellow_rect = pygame.Rect(52, 143, 40, 40)
orange_rect = pygame.Rect(8, 187, 40, 40)
purple_rect = pygame.Rect(52, 187, 40, 40)
dark_green_rect = pygame.Rect(8, 231, 40, 40)
brown_rect = pygame.Rect(52, 231, 40, 40)
black_rect = pygame.Rect(8, 275, 40, 40)
pretty_blue_rect = pygame.Rect(52, 275, 40, 40)

clear_rect = pygame.Rect(15, 500, 70, 70)
eraser_rect = pygame.Rect(8, 400, 40, 40)
pencil_rect = pygame.Rect(50, 400, 40, 40)

thin_brush = pygame.Rect(8, 360, 20, 20)
medium_brush = pygame.Rect(30, 360, 20, 20)
thick_brush = pygame.Rect(52, 360, 20, 20)
supa_brush = pygame.Rect(74, 360, 20, 20)

first = None
last = None
figure = "line"
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.draw.rect(SCREEN, WHITE, menu_rect)
            pygame.image.save(SCREEN, "Picture.png")
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.draw.rect(SCREEN, WHITE, menu_rect)
                pygame.image.save(SCREEN, "Picture.png")
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_s:
                figure = "rectangle"
            if event.key == pygame.K_c:
                figure = "circle" 
        if event.type == MOUSEBUTTONDOWN:
            draw = True
            first = pygame.mouse.get_pos()
        if event.type == MOUSEMOTION:
            last = pygame.mouse.get_pos()
            if first and figure == "line":
                pygame.draw.line (SCREEN, brush_color, first, last, brush_size)
                first = last
            if first and figure == "eraser":
                pygame.draw.line (SCREEN, WHITE, first, last, 10)
                first = last
        if event.type == MOUSEBUTTONUP:
            if figure == "circle":
                pygame.draw.circle(SCREEN, brush_color, first, abs(first[0]-last[0]), 2)
            if figure == "rectangle":
                pygame.draw.rect(SCREEN, brush_color, [first[0], first[1], abs(last[0]-first[0]), abs(last[1]-first[1])], 2)
            first = None
            draw = True
    
    mouse_pos = pygame.mouse.get_pos()
    if draw == True:
        pressed = pygame.mouse.get_pressed()        
        if green_rect.collidepoint(mouse_pos):
            if pressed[0]:
                brush_color = GREEN
        if red_rect.collidepoint(mouse_pos):
            if pressed[0]:
                brush_color = RED
        if blue_rect.collidepoint(mouse_pos):
            if pressed[0]:
                brush_color = BLUE
        if pink_rect.collidepoint(mouse_pos):
            if pressed[0]:
                brush_color = PINK
        if light_blue_rect.collidepoint(mouse_pos):
            if pressed[0]:
                brush_color = LIGHT_BLUE
        if yellow_rect.collidepoint(mouse_pos):
            if pressed[0]:
                brush_color = YELLOW
        if orange_rect.collidepoint(mouse_pos):
            if pressed[0]:
                brush_color = ORANGE
        if purple_rect.collidepoint(mouse_pos):
            if pressed[0]:
                brush_color = PURPLE
        if dark_green_rect.collidepoint(mouse_pos):
            if pressed[0]:
                brush_color = DARK_GREEN
        if black_rect.collidepoint(mouse_pos):
            if pressed[0]:
                brush_color = BLACK
        if brown_rect.collidepoint(mouse_pos):
            if pressed[0]:
                brush_color = BROWN
        if pretty_blue_rect.collidepoint(mouse_pos):
            if pressed[0]:
                brush_color = PRETTY_BLUE

    # if draw == True:
        if eraser_rect.collidepoint(mouse_pos):
            if pressed[0]:
                brush_color = WHITE
            figure = "eraser"
        if pencil_rect.collidepoint(mouse_pos):
            if pressed[0]:
                brush_color = BLACK
            figure = "line"
        if clear_rect.collidepoint(mouse_pos):
            if pressed[0]:
                SCREEN.fill(WHITE)
    
    
    pygame.draw.rect(SCREEN, GRAY, menu_rect)
    pygame.draw.rect(SCREEN, DARK_GRAY, clear_rect)
    SCREEN.blit(brush_text, (11, 327))
    SCREEN.blit(menu_text, (18, 13))

    if draw == True:
        if thin_brush.collidepoint(mouse_pos):
            if pressed[0]:
                brush_size = 1
        if medium_brush.collidepoint(mouse_pos):
            if pressed[0]:
                brush_size = 3
        if thick_brush.collidepoint(mouse_pos):
            if pressed[0]:
                brush_size = 5
        if supa_brush.collidepoint(mouse_pos):
            if pressed[0]:
                brush_size = 20
    
    pygame.draw.rect(SCREEN, GREEN, green_rect)
    if brush_color == GREEN:
        border = 3
    else:
        border = 1
    pygame.draw.rect(SCREEN, BLACK, green_rect, border)
    
    pygame.draw.rect(SCREEN, RED, red_rect)
    if brush_color == RED:
        border = 3
    else:
        border = 1
    pygame.draw.rect(SCREEN, BLACK, red_rect, border)
    
    pygame.draw.rect(SCREEN, BLUE, blue_rect)
    if brush_color == BLUE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(SCREEN, BLACK, blue_rect, border)

    pygame.draw.rect(SCREEN, PINK, pink_rect)
    if brush_color == PINK:
        border = 3
    else:
        border = 1
    pygame.draw.rect(SCREEN, BLACK, pink_rect, border)

    pygame.draw.rect(SCREEN, LIGHT_BLUE, light_blue_rect)
    if brush_color == LIGHT_BLUE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(SCREEN, BLACK, light_blue_rect, border)

    pygame.draw.rect(SCREEN, YELLOW, yellow_rect)
    if brush_color == YELLOW:
        border = 3
    else:
        border = 1
    pygame.draw.rect(SCREEN, BLACK, yellow_rect, border)

    pygame.draw.rect(SCREEN, ORANGE, orange_rect)
    if brush_color == ORANGE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(SCREEN, BLACK, orange_rect, border)
    
    pygame.draw.rect(SCREEN, ORANGE, orange_rect)
    if brush_color == ORANGE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(SCREEN, BLACK, orange_rect, border)
    
    pygame.draw.rect(SCREEN, DARK_GREEN, dark_green_rect)
    if brush_color == DARK_GREEN:
        border = 3
    else:
        border = 1
    pygame.draw.rect(SCREEN, BLACK, dark_green_rect, border)
    
    pygame.draw.rect(SCREEN, PURPLE, purple_rect)
    if brush_color == PURPLE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(SCREEN, BLACK, purple_rect, border)
    
    pygame.draw.rect(SCREEN, BLACK, black_rect)
    if brush_color == BLACK:
        border = 3
    else:
        border = 1
    pygame.draw.rect(SCREEN, BLACK, black_rect, border)
    
    pygame.draw.rect(SCREEN, BROWN, brown_rect)
    if brush_color == BROWN:
        border = 3
    else:
        border = 1
    pygame.draw.rect(SCREEN, BLACK, brown_rect, border)
    
    pygame.draw.rect(SCREEN, PRETTY_BLUE, pretty_blue_rect)
    if brush_color == PRETTY_BLUE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(SCREEN, BLACK, pretty_blue_rect, border)
    
    ### RECT FOR ERASER
    SCREEN.blit(eraser, eraser_rect)
    SCREEN.blit(pencil, pencil_rect)
    SCREEN.blit(clear, clear_rect)


    if brush_color == BLACK:
        border = 3
    else:
        border = 1
    # pygame.draw.rect(SCREEN, BLACK, eraser_rect, border)
 
    # Rect for brush size
    if brush_size == 1:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.rect(SCREEN, BLACK, thin_brush, brush_border)
    pygame.draw.circle(SCREEN, BLACK, thin_brush.center, 1)
    pygame.draw.rect(SCREEN, BLACK, thin_brush, brush_border)
    
    
    if brush_size == 3:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.rect(SCREEN, BLACK, medium_brush, brush_border)
    pygame.draw.circle(SCREEN, BLACK, medium_brush.center, 3)
    pygame.draw.rect(SCREEN, BLACK, medium_brush, brush_border)
    
    
    if brush_size == 5:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.rect(SCREEN, BLACK, thick_brush, 1)
    pygame.draw.circle(SCREEN, BLACK, thick_brush.center, 5)
    pygame.draw.rect(SCREEN, BLACK, thick_brush, brush_border)
    
    
    if brush_size == 10:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.rect(SCREEN, BLACK, supa_brush, brush_border)
    pygame.draw.circle(SCREEN, BLACK, supa_brush.center, 10)
    pygame.draw.rect(SCREEN, BLACK, supa_brush, brush_border)
    
    clock.tick(FPS)
    pygame.display.flip()
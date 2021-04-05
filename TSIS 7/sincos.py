import pygame
import math
pygame.init()

red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

size = width, height = (840, 600)
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))

#rectangle and axis
pygame.draw.rect(screen, black, (60, 20, 760, 520), 2) 
pygame.draw.line(screen, black, [440, 20], [440, 540], 2)
pygame.draw.line(screen, black, [60, 280], [820, 280], 2)

#long vertical lines
for i in range(80, 801, 120):
    if i == 560:
        pygame.draw.line(screen, black, [560, 20], [560, 40], 1)
        pygame.draw.line(screen, black, [560, 100], [560, 540], 1)
    else:
        pygame.draw.line(screen, black, [i, 20], [i, 540], 1)

# long horizontal lines
for i in range(40, 521, 60):
    pygame.draw.line(screen, black, [60, i], [820, i], 1)

#short vertical lines
for i in range(95, 786, 30):
    pygame.draw.line(screen, black, [i, 20], [i, 25], 1)
    pygame.draw.line(screen, black, [i, 540], [i, 535], 1)

for i in range(110, 771, 60):
    pygame.draw.line(screen, black, [i, 20], [i, 30], 1)
    pygame.draw.line(screen, black, [i, 540], [i, 530], 1)

for i in range(140, 741, 120):
    pygame.draw.line(screen, black, [i, 20], [i, 35], 1)
    pygame.draw.line(screen, black, [i, 540], [i, 525], 1)

# short horizontal lines
for i in range(55, 506, 30):
    pygame.draw.line(screen, black, [60, i], [65, i], 1)
    pygame.draw.line(screen, black, [815, i], [820, i], 1)

for i in range(70, 491, 60):
    pygame.draw.line(screen, black, [60, i], [70, i], 1)
    pygame.draw.line(screen, black, [810, i], [820, i], 1)

# sine curve
sin_points = []
for x in range(80, 801):
    y = float(math.sin(abs(80 - x) * (math.pi / 120)) * 240 + 280)
    sin_points.append([x, y])
pygame.draw.aalines(screen, red, False, sin_points, 3)

# dashed cosine curve
for x in range(80, 801, 3):
    y1 = 240 * math.cos((x - 80) / 120 * math.pi) + 280
    y2 = 240 * math.cos((x - 79) / 120 * math.pi) + 280
    pygame.draw.aalines(screen, blue, False, [(x, y1), ((x + 1), y2)])

# y-axis numbering
font = pygame.font.SysFont("Times New Roman", 20, italic = True)
v = 1.00
i = 0
while v >= -1:
    screen.blit(font.render(str(v), True, black), (10, 30 + i))
    i += 60
    v -= 0.25

# x-axis numbering
h = '-3π      -5π/2      -2π    -3π/2      -π       -π/2        0        π/2         π       3π/2       2π       5π/2     3π'
screen.blit(font.render(h, True, black), (60, 540))

# остальные тексты 
txt = font.render("X", False, black)
screen.blit(txt, (430, 570))

numbs = font.render ('-3               -2               -1', True, black)
screen.blit(numbs, (85, 320))

font2 = pygame.font.SysFont("Calibri", 25)
sin_txt = font2.render(" sin x", True, black)
screen.blit(sin_txt, (530, 50))
sin_line_txt = font2.render("____", True, red)
screen.blit(sin_line_txt, (590, 40))

cos_txt = font2.render(" cos x", True, black)
screen.blit(cos_txt, (530, 70))
cos_line_txt = font2.render(" - - -", True, blue)
screen.blit(cos_line_txt, (590, 70))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
pygame.quit()
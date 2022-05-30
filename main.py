import pygame, random, colorsys

SPEED = 100 # 1 to 1000
RANDOMNESS = 20 # Note: higher randomness will slow down program speed

rows, cols = [100, 100]
grid = [[0 for i in range(cols)] for j in range(rows)]

#spawn point  Note: you can also add multiple spawn points if you wish
grid[50][50] = 1

# Wall 1
# for i in range(100):
#     grid[20][i] = 3

# Wall 2
# for i in range(20, 80):
#     grid[20][i] = 3

# Wall 3
# for i in range(20, 100):
#     grid[i][20] = 3
# for i in range(20, 100):
#     grid[i][80] = 3

# Wall 4
# for i in range(20, 100):
#     grid[i][20] = 3
# for i in range(80):
#     grid[i][80] = 3


def hsv2rgb(h,s,v):
    h /= 100
    return tuple([round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v)])

pygame.init()

screen = pygame.display.set_mode((520,540))

pygame.font.init()
font = pygame.font.SysFont('Helvetica', 20)

def update():
    global grid
    last = [[j for j in i] for i in grid]

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                color = (0,0,0)
            elif grid[i][j] == 1:
                color = (100,100,100)
            elif grid[i][j] == 3:
                color = (255, 0, 0)
            else:
                color = (255,255,255)

            pygame.draw.rect(screen, color, pygame.Rect(j*5+10, i*5+10, 5, 5))
            if random.randint(1, RANDOMNESS) == 1 and next(i, j) and grid[i][j] < 2:
                last[i][j] += 1

    grid = [[j for j in i] for i in last]

def next(row, column):
    n = False
    for a in range(-1,2):
        for b in range(-1,2):
            try:
                if row+a >= 0 and column+b >= 0 and grid[row+a][column+b] > 0 and grid[row+a][column+b] < 3:
                    n = True
                    break
            except:
                pass

    return n

gen = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0,0,0))

    gen += 1
    gen_label = font.render('Generation ' + str(gen), False, (255, 255, 255))
    screen.blit(gen_label, (10, 515))
    update()
    pygame.display.flip()

    pygame.time.wait(round(1000/SPEED))
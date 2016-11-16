# Imports
import pygame
import math
import random

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "The Rain Is Endless"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
''' add colors you use as RGB values here '''
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125, 0)
SMILE_YELLOW = (244, 241, 66)
NIGHT = (1, 14, 35)
GRASS = (8, 40, 0)
SNOW = (13, 145, 37)
CLOUDS = (114, 122, 135)
CLOUDS2 = (20, 32, 51)
MOON = (232,227,226)
SEA = (18, 48, 96)
RAIN = (0, 6, 17)
FENCE = (60, 71, 57)
PUDDLE = (48, 37, 9)
DAY = (71, 114, 183)

'''making clouds'''
def draw_cloud(x, y):
    pygame.draw.ellipse(screen, CLOUDS2, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, CLOUDS2, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, CLOUDS2, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, CLOUDS2, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, CLOUDS2, [x + 20, y + 20, 60, 40])
'''making stickman'''
def draw_stick_man(screen, x, y):
    
    pygame.draw.ellipse(screen, SMILE_YELLOW, [x, y, 100, 100])
    pygame.draw.ellipse(screen, RED, [x+45, y+45, 15, 15])
    pygame.draw.ellipse(screen, BLACK, [x+30, y+20, 15, 15])
    pygame.draw.ellipse(screen, BLACK, [x+60, y+20, 15, 15])
    
    pygame.draw.line(screen, BLACK, [x+40, y+75], [x+60,y+75], 5)
    pygame.draw.line(screen, RED, [x+49, y+99], [x+49,y+190], 10)
    pygame.draw.line(screen, BLUE, [x+49, y+141], [x+49,y+190], 10)
    pygame.draw.line(screen, RED, [x+49, y+99], [x+25,y+140], 7)
    pygame.draw.line(screen, RED, [x+49, y+99], [x+69,y+140], 7)
    pygame.draw.line(screen, BLUE, [x+49, y+180], [x+35,y+231], 7)
    pygame.draw.line(screen, BLUE, [x+49, y+180], [x+69,y+231], 7)

clouds = []
for i in range(20):
    x = random.randrange(-100, 1600)
    y = random.randrange(0,200)
    clouds.append([x, y])
'''making rain'''
rain = []
for n in range(200):
    x = random.randrange(0, 800)
    y = random.randrange(0, 400)
    r = random.randrange(1, 5)
    rain.append([x, y, r, r])
'''makiing toggle'''
dayrain = True
nightrain = False


# Game loop
done = False
up = False
down = False
left = False
right = False

stick_x = 300
stick_y = 230

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    '''day/ night toogle'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dayrain = not dayrain
            elif event.key == pygame.K_l:
                nightrain = not nightrain
    state = pygame.key.get_pressed()

    up = state[pygame.K_UP]
    down = state[pygame.K_DOWN]
    left = state[pygame.K_LEFT]
    right = state[pygame.K_RIGHT]
    
    
    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now ''' 
    '''clouds moving'''
    if up:
        stick_y -= 1
    elif down:
        stick_y += 1
    if left:
        stick_x -= 1
    elif right:
        stick_x += 1    
    
    for c in clouds:
            c[0] -= .5
            if c[0] < -100:
                c[0] = random.randrange(800, 1600)
                c[1] = random.randrange(0, 100)

    '''for s in rain'''
    for r in rain:
        r[1] += 7
        r[0] -= 2

        if r[1] > 800:
            r[0] = random.randrange(000, 1000)
            r[1] = random.randrange(-200, 0)

        
        

    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    if nightrain:
        screen.fill(NIGHT)
        pygame.draw.ellipse(screen, MOON, [600, 100, 100, 100])
    else:
        screen.fill(DAY)  

    '''sky'''
    
    for r in rain:
        pygame.draw.ellipse(screen, CLOUDS2, r)
    for c in clouds:
        draw_cloud(c[0], c[1])
        pygame.draw.rect(screen, GRASS, [0, 400, 800, 200])
    pygame.draw.ellipse(screen, PUDDLE, [500, 475, 70, 50])
    '''Fence'''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, FENCE, [[x+5, y], [x+10, y+5],
        [x+10, y+40], [x, y+40],
        [x, y+5]])
    pygame.draw.line(screen, FENCE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, FENCE, [0, 410], [800, 410])

    '''stick figure'''

    draw_stick_man(screen, stick_x, stick_y)
   
    
    ''' angles for arcs are measured in radians (a pre-cal topic) 
    pygame.draw.arc(screen, ORANGE, [100, 100, 100, 100], 0, math.pi/2, 1)
    pygame.draw.arc(screen, BLACK, [100, 100, 100, 100], 0, math.pi/2, 50)'''                        
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()

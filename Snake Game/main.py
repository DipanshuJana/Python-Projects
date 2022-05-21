import random
import pygame
from pygame.locals import *
import sys


pygame.init ()


# COLORS 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


# CREATING WINDOW
SCREENWIDTH = 900 
SCREENHEIGHT = 600
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

# LODAING ALL THE SOUNDS
HIT = pygame.mixer.Sound('D:\\Productivity\\Python\\Projects\\SnakeGame\\audio\\hit.wav')
POINT = pygame.mixer.Sound('D:\\Productivity\\Python\\Projects\\SnakeGame\\audio\\point.wav')
GAMEOVER = pygame.mixer.Sound('D:\\Productivity\\Python\\Projects\\SnakeGame\\audio\\game_over.wav')

# GAME TITLE
pygame.display.set_caption = ("SNAKE GAME")
pygame.display.update()

CLOCK = pygame.time.Clock()

# SCORE ON SCREEN
FONT = pygame.font.SysFont(None, 40)
def textScreen(text, color, x, y):
    SCREEN_TEXT = FONT.render(text, True, color)
    SCREEN.blit(SCREEN_TEXT, [x, y])

# LOGIC FOR INCREMENTING THE THE LENGTH OF THE SNAKE
def incrementSnakeSize(screen, color, snake_list, snake_size):
    for x, y in snake_list:
            pygame.draw.rect(screen, color, [x, y, snake_size, snake_size])


# GAME LOOP 
def Game():
    # GAME SPECIFIED VARIBALES
    FPS = 60
    SNAKE_X = 55
    SNAKE_Y = 45
    SNAKE_SIZE = 10
    SNAKE_LENGTH = 1
    SNAKE_LIST = []
    SNAKE_VEL_X = 0
    SNAKE_VEL_Y = 0
    OBJECT_X = random.randint(30, SCREENWIDTH - 50)
    OBJECT_Y = random.randint(30, SCREENHEIGHT - 50)
    OBJECT_HEIGHT = 10
    OBJECT_WIDTH = 10
    SCORE = 0 
    GAME_OVER = False

    while True:
        if GAME_OVER == True:
            SCREEN.fill(WHITE)            
            textScreen("Game Over! Press Enter to Continue", RED, SCREENWIDTH/4.3, (SCREENHEIGHT - 40)/2.3)
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN and (event.key == K_RETURN):
                    Game()
                
        else:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                
                elif event.type == KEYDOWN and (event.key == K_UP):
                    SNAKE_VEL_Y = - 5
                    SNAKE_VEL_X = 0
                elif event.type == KEYDOWN and (event.key == K_DOWN):
                    SNAKE_VEL_Y = 5
                    SNAKE_VEL_X = 0

                elif event.type == KEYDOWN and (event.key == K_LEFT):
                    SNAKE_VEL_X = - 5
                    SNAKE_VEL_Y = 0

                elif event.type == KEYDOWN and (event.key == K_RIGHT):
                    SNAKE_VEL_X = 5
                    SNAKE_VEL_Y = 0

            SNAKE_X = SNAKE_X + SNAKE_VEL_X
            SNAKE_Y = SNAKE_Y + SNAKE_VEL_Y

            if abs(SNAKE_X - OBJECT_X) < 4 and abs(SNAKE_Y - OBJECT_Y) < 4:
                SCORE = SCORE + 1
                OBJECT_X = random.randint(30, SCREENWIDTH - 50)
                OBJECT_Y = random.randint(30, SCREENHEIGHT - 50)   
                SNAKE_LENGTH += 5
                POINT.play()
            
            SCREEN.fill(BLACK)

            # GENERATING SCORE
            textScreen("SCORE: "+str(SCORE * 10), WHITE, 5, 5)

            # GENERATING FOOD
            pygame.draw.rect(SCREEN, RED, [OBJECT_X, OBJECT_Y, OBJECT_HEIGHT, OBJECT_WIDTH])

            HEAD = []
            HEAD.append(SNAKE_X)
            HEAD.append(SNAKE_Y)
            SNAKE_LIST.append(HEAD)

            if len(SNAKE_LIST)> SNAKE_LENGTH:
                del SNAKE_LIST[0]
            
            if HEAD in SNAKE_LIST[:-1]:
                GAME_OVER = 0
                HIT.play()

            # GENERATING SNAKE
            pygame.draw.rect(SCREEN, WHITE, [SNAKE_X, SNAKE_Y, SNAKE_SIZE, SNAKE_SIZE])

            # GAME OVER FUNCTIONAILTY 
            if SNAKE_X<0 or SNAKE_X>SCREENWIDTH or SNAKE_Y<0 or SNAKE_Y<0 or SNAKE_Y>SCREENHEIGHT:
                GAME_OVER = True
                GAMEOVER.play()
        
            incrementSnakeSize(SCREEN , WHITE, SNAKE_LIST, SNAKE_SIZE)
        pygame.display.update()
        CLOCK.tick(FPS) 

Game()  
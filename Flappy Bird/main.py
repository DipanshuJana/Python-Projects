import random # For generating random pipes
import sys # For adding exit functionality to the game
import pygame 
from pygame.locals import *  # Basic pygame imports


# GLOBAL VARIABLES
FPS = 60
GAME_SPRITES = {}
GAME_SOUND = {}
BACKGROUND = 'D:\\Productivity\\Python\\Projects\\Flappy Bird\\sprites\\background.jpg'
PLAYER = 'D:\\Productivity\\Python\\Projects\\Flappy Bird\\sprites\\bird.png'
PIPE = 'D:\\Productivity\\Python\\Projects\\Flappy Bird\\sprites\\pipe.png'
MENU = 'D:\\Productivity\\Python\\Projects\\Flappy Bird\\sprites\\menu.jpg'

# GENERATING SCREEN
SCREENHEIGHT = 570
SCREENWIDTH  = 360
SCREEN = pygame.display.set_mode((SCREENHEIGHT, SCREENWIDTH))
CAPTION = pygame.display.set_caption('Flappy Bird')
pygame.display.update()

# GAME FUNCTIONS
def welcomeScreen():
    '''
    Shows welcome image on staring of the game
    '''

    menux = int((SCREENWIDTH - GAME_SPRITES['menu'].get_width())/8)
    menuy = int(SCREENHEIGHT * 0.003)

    while True:
        for event in pygame.event.get():
            # if user clicks on the cross button or presses the escape key on the keyboard then the game should close
            if event.type == QUIT or (event.type == KEYDOWN  and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_KP_ENTER):
                return
            else:
                # SCREEN.blit (GAME_SPRITES['menu'], (menux, menuy))
                SCREEN.blit (GAME_SPRITES['menu'], (menux, menuy))
                pygame.display.update()
                FPSCLOCK.tick(FPS)


def main():
    score = 0
    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENWIDTH/2)
    pipeVelX = -4
    playerVelY = -9
    playerMaxVelY = 10 
    playerAccY = 1
    playerFlapVel = -8 # Velocity while falpping
    playerFlapped = False # it is true only when the bird is flapping


    # generate 2 pipes for blitiing on the screen

    newPipe1 = getRandomPipes() 
    newPipe2 = getRandomPipes() 

    # my list of upper pipes
    upperPipes = [
        {'x': SCREENWIDTH + 200, 'y': newPipe1[0]['y']},
        {'x': SCREENWIDTH +200+(SCREENWIDTH/2), 'y': newPipe1[0]['y']}
    ]
    
    # my list of lower pipes
    lowerPipes = [
        {'x': SCREENWIDTH + 200, 'y': newPipe2[1]['y']},
        {'x': SCREENWIDTH +200+(SCREENWIDTH/2), 'y': newPipe2[1]['y']}
    ]
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapVel
                    playerFlapped = True
                    GAME_SOUND['wing'].play()

        crashCheck = isCollide(playerx, playery, upperPipes, lowerPipes) # this function will return true if the player get crashed

        if crashCheck:
            return

        # check for score
        playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2

        for pipe in upperPipes:

            pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
            
            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                score = score + 1
                print (f"Your score is {score}")
                GAME_SOUND['point'].play()

        if playerVelY < playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False

        playerHeight = GAME_SPRITES['player'].get_height()

        playery = playery + min(playerVelY, SCREENHEIGHT - 310 - playery - playerHeight)

        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX

        # add a new pipe when the first pipe is about to cross the leftmost part of the screen
        if 0 <upperPipes[0]['x'] <5:
            newPipe = getRandomPipes()
            upperPipes.append(newPipe[0])  
            lowerPipes.append(newPipe[1])  
        
        # if the pipe is out of the screen, remove it
        if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)

        # blit all the sprites 
        SCREEN.blit(GAME_SPRITES['background'], (0, 0))
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(GAME_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
            SCREEN.blit(GAME_SPRITES['pipe'][1], (upperPipe['x'], lowerPipe['y']))

        SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
        myScore = [int(x) for x in list(str(score))]
        width = 0

        for digit in myScore:
            width += GAME_SPRITES['numbers'][digit].get_width()
        Xoffset = (SCREENWIDTH - width)/1.2

        for digit in myScore:
            SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT * 0.12))
            Xoffset += GAME_SPRITES['numbers'][digit].get_width()

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def getRandomPipes():
    '''
    Generate positions of two pipes(one bottom straight and one top rotated) for blitting on the screen
    '''

    pipeHight = GAME_SPRITES['pipe'][0].get_height()
    offset = SCREENHEIGHT/4
    y2 = offset + random.randrange(0, int(SCREENHEIGHT - 275 - 1.2*offset))
    pipeX = SCREENWIDTH + 10
    y1 = pipeHight - y2 + offset
    pipe = [
        {'x' : pipeX, 'y': -y1}, # upper pies
        {'x' : pipeX, 'y': y2} # lower pipes
    ]

    return pipe

def isCollide(playerx, playery, upperPipes, lowerPipes):
    if playery > (SCREENHEIGHT * 1.8) - 100 or playery<0:
        GAME_SOUND['die'].play()
        return True 

    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()

        if playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
            GAME_SOUND['hit'].play()
            return True 
    for pipe in lowerPipes:
            if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
                GAME_SOUND['hit'].play()
                return True 


    return False

    
if __name__ == '__main__':
    # this is the main point from where our game will start

    pygame.init() # Initalize all pygame functions

    FPSCLOCK = pygame.time.Clock()

    # Game Sprites

    GAME_SPRITES['numbers'] = (
        pygame.image.load('D:\\Productivity\\Python\\Projects\\Flappy Bird\\sprites\\0.png').convert_alpha(),
        pygame.image.load('D:\\Productivity\\Python\\Projects\\Flappy Bird\\sprites\\1.png').convert_alpha(),
        pygame.image.load('D:\\Productivity\\Python\\Projects\\Flappy Bird\\sprites\\2.png').convert_alpha(),
        pygame.image.load('D:\\Productivity\\Python\\Projects\\Flappy Bird\\sprites\\3.png').convert_alpha(),
        pygame.image.load('D:\\Productivity\\Python\\Projects\\Flappy Bird\\sprites\\4.png').convert_alpha(),
        pygame.image.load('D:\\Productivity\\Python\\Projects\\Flappy Bird\\sprites\\5.png').convert_alpha(),
        pygame.image.load('D:\\Productivity\\Python\\Projects\\Flappy Bird\\sprites\\6.png').convert_alpha(),
        pygame.image.load('D:\\Productivity\\Python\\Projects\\Flappy Bird\\sprites\\7.png').convert_alpha(),
        pygame.image.load('D:\\Productivity\\Python\\Projects\\Flappy Bird\\sprites\\8.png').convert_alpha(),
        pygame.image.load('D:\\Productivity\\Python\\Projects\\Flappy Bird\\sprites\\9.png').convert_alpha()
    )

    GAME_SPRITES['menu'] = pygame.image.load(MENU).convert_alpha()
    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert_alpha()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()
    GAME_SPRITES['pipe'] = (
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
        pygame.image.load(PIPE).convert_alpha()   
    )

    # Game Sounds

    GAME_SOUND['die'] = pygame.mixer.Sound('D:\\Productivity\\Python\\Projects\\Flappy Bird\\audio\\die.wav')
    GAME_SOUND['hit'] = pygame.mixer.Sound('D:\\Productivity\\Python\\Projects\\Flappy Bird\\audio\\hit.wav')
    GAME_SOUND['point'] = pygame.mixer.Sound('D:\\Productivity\\Python\\Projects\\Flappy Bird\\audio\\point.wav')
    GAME_SOUND['swoosh'] = pygame.mixer.Sound('D:\\Productivity\\Python\\Projects\\Flappy Bird\\audio\\swoosh.wav')
    GAME_SOUND['wing'] = pygame.mixer.Sound('D:\\Productivity\\Python\\Projects\\Flappy Bird\\audio\\wing.wav')


    while True:
        welcomeScreen() # shows welcome screen tto the user until the the space key is pressed
        main() # this will contain the main game function
import pygame
import sys
import random
import pygame
from pygame.locals import *

# GLOBAL SETTINGS
BLOCKS = 50
BLOCK_WIDTH = 10
DISPLAY_WIDTH = BLOCK_WIDTH * BLOCKS
DISPLAY_HEIGHT = 200
BLOCK_HEIGHTS = list(range(1,BLOCKS+1))
R_COLOR = pygame.Color(255,0,0)
G_COLOR = pygame.Color(0,255,0)
B_COLOR = pygame.Color(0,0,255)
#########################################

# Shuffle data and determinates the block height based on BLOCK_HEIGHTS and DISPLAY_HEIGHT
random.shuffle(BLOCK_HEIGHTS)
max_num = max(BLOCK_HEIGHTS)
for x in range(0,len(BLOCK_HEIGHTS)):
    BLOCK_HEIGHTS[x] = int(DISPLAY_HEIGHT/max_num) * BLOCK_HEIGHTS[x]

# Calculate useful variables
max_num = max(BLOCK_HEIGHTS)
min_num = min(BLOCK_HEIGHTS)
SORTED = False
BLOCK_HEIGHTS_LEN = len(BLOCK_HEIGHTS)

pygame.init()
display = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))

# Scales data between 0 and 1
def scale_number(min,max,number):
    return (number-min)/(max-min)

# Draws all blocks inside BLOCK_HEIGHTS and change colors depending on BLOCK_HEIGHTS value
def show():
    xOffset=0
    for number in BLOCK_HEIGHTS:
        mySurface = pygame.Surface((BLOCK_WIDTH, number))
        if number < max_num/2:
            myColor = R_COLOR.lerp(B_COLOR, scale_number(min_num,max_num/2,number))
        else:
            myColor = B_COLOR.lerp(G_COLOR, scale_number(max_num/2,max_num,number))
        mySurface.fill(myColor)
        display.blit(mySurface, (xOffset,DISPLAY_HEIGHT-number))
        xOffset=xOffset+BLOCK_WIDTH

while True:
    # Exit pygame without bugs
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # For each step on the algorithm draws the changes
    if not SORTED:
        for i in range(BLOCK_HEIGHTS_LEN-1):
            for j in range(BLOCK_HEIGHTS_LEN-i-1):
                if BLOCK_HEIGHTS[j] > BLOCK_HEIGHTS[j+1]:
                    aux = BLOCK_HEIGHTS[j]
                    BLOCK_HEIGHTS[j] = BLOCK_HEIGHTS[j+1]
                    BLOCK_HEIGHTS[j+1] = aux
                
                display.fill((255,255,255))
                show()
                pygame.time.delay(10)
                pygame.display.update()
        SORTED=True
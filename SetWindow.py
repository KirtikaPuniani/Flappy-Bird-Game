# set the height and width of the screen to which the game will be played. Now we have to define 
# some images which we shall use in our game like pipes as hurdles, birds images, and also a 
# background image of the flappy bird game.


# For generating random height of pipes
import random  
import sys 
import pygame
from pygame.locals import * 

# Global Variables for the game
window_width = 600
window_height = 499

# set height and width of window
window = pygame.display.set_mode((window_width, window_height))   
elevation = window_height * 0.8
game_images = {}      
framepersecond = 32
pipeimage = 'images/pipe.png'
background_image = 'images/background.jpg'
birdplayer_image = '/images/bird.png'
sealevel_image = '/images/base.jfif'
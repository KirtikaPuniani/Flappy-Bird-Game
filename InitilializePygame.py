# Initialize the program using pygame.init() and set the caption of the window. 
# Here pygame.time.Clock() will be used further in the main loop of the game to alter the speed 
# the bird. Load the images from the system in pygame using pygame.image.load().

from SetWindow import *
# program where the game starts
if __name__ == "__main__":          
    
    # For initializing modules of pygame library
    pygame.init()  
    framepersecond_clock = pygame.time.Clock()
    
    # Sets the title on top of game window
    pygame.display.set_caption('Flappy Bird Game')      

    # Load all the images which we will use in the game
    # images for displaying score
    game_images['scoreimages'] = (
        pygame.image.load('images/0.png').convert_alpha(),
        pygame.image.load('images/1.png').convert_alpha(),
        pygame.image.load('images/2.png').convert_alpha(),
        pygame.image.load('images/3.png').convert_alpha(),
        pygame.image.load('images/4.png').convert_alpha(),        
        pygame.image.load('images/5.png').convert_alpha(),
        pygame.image.load('images/6.png').convert_alpha(),
        pygame.image.load('images/7.png').convert_alpha(),
        pygame.image.load('images/8.png').convert_alpha(),
        pygame.image.load('images/9.png').convert_alpha()
    )
    game_images['flappybird'] = pygame.image.load(birdplayer_image).convert_alpha()                  
    game_images['sea_level'] = pygame.image.load(sealevel_image).convert_alpha()
    game_images['background'] = pygame.image.load(background_image).convert_alpha()
    game_images['pipeimage'] = (pygame.transform.rotate(pygame.image.load(pipeimage)
                                                        .convert_alpha(),
                                                        180),
                                pygame.image.load(pipeimage).convert_alpha())

    print("WELCOME TO THE FLAPPY BIRD GAME")
    print("Press space or enter to start the game")
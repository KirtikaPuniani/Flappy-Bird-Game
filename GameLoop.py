# Initialize the position of bird and sea level to the ground. Adding conditions in the loop 
# defines the game conditions. The variable horizontal and vertical is used to set the position 
# of the bird. We have to run the program until the user stops or exits (using sys.exit())if the 
# program so, we create an infinite while loop.

while True:

        # sets the coordinates of flappy bird
        horizontal = int(window_width/5)
        vertical = int((window_height - game_images['flappybird'].get_height())/2)
        
        # for selevel
        ground = 0  
        while True:
            for event in pygame.event.get():

                # if user clicks on cross button, close the game
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    
                    # Exit the program
                    sys.exit()   

                # If the user presses space or up key,
                # start the game for them
                elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                    flappygame()
                
                # if user doesn't press anykey Nothing happen
                else:
                    window.blit(game_images['background'], (0, 0))
                    window.blit(game_images['flappybird'], (horizontal, vertical))
                    window.blit(game_images['sea_level'], (ground, elevation))
                    
                    # Just Refresh the screen
                    pygame.display.update()        
                    
                    # set the rate of frame per second
                    framepersecond_clock.tick(framepersecond)
import pygame

# Start the game
pygame.init()
game_width = 1920
game_height = 1080
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock()
running = True

# Storing photos of the background and the player(bird) in variables so we can use them later on
background = pygame.image.load("../assets/background.png")
player = pygame.image.load("../assets/bird.png")

# Creating the player's variables
player_x = 15

player_y = 30

player_speed = 10

player_size = 80

player_facing_left = False


# Everything under 'while running' will be repeated over and over again
while running:
    # Makes the game stop if the player clicks the X or presses esc
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

     # Check to see what keys user is pressing for moving

    # Creates variable to get called on later
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:

        # Allows the the player to move forward
        player_y -= player_speed

    # Allows the player to move to the left
    if keys[pygame.K_a]:
        player_x -= player_speed
        player_facing_left = True

    # Allows the player to move backwards
    if keys[pygame.K_s]:
        player_y += player_speed

    # Allows the player to move to the right
    if keys[pygame.K_d]:
        player_x += player_speed
        player_facing_left = False

    # Allows the player to enlarge(For testing and debugging)
    if keys [pygame.K_SPACE]:
        player_size += 3

    # Allows the player to diminish in size(For testing and debugging)
    if keys [pygame.K_k]:
        player_size -= 2

    # Draws Background
    screen.blit(background, (0, 0))

    # Prevents Pixelation
    player_small = pygame.transform.scale(player, (int(player_size*1.25), player_size))

    # If bird goes to the left the bird picture flips to left
    # If bird goes to the right the bird picture flips to the right
    if player_facing_left:
        player_small = pygame.transform.flip(player_small, True, False)
    screen.blit(player_small, (player_x, player_y))


    pygame.display.flip()
    clock.tick(1000)
    pygame.display.set_caption("FPS: " + str(clock.get_fps()))

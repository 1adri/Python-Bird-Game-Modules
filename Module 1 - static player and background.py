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

player_speed = 4

player_size = 80

player_facing_left = False

# Every line of code under this loop will be repeated until the game stops/quits
while running:
    # If the player clicks the X button or the escape key the game will quit itself
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # Draws Background
    screen.blit(background, (0, 0))

    # Prevents Pixelation
    player_small = pygame.transform.scale(player, (int(player_size * 1.25), player_size))

    # If bird goes to the left the bird picture flips to left
    # If bird goes to the right the bird picture flips to the right
    if player_facing_left:
        player_small = pygame.transform.flip(player_small, True, False)

    # Draws the player
    screen.blit(player_small, (player_x, player_y))

    pygame.display.flip()
    clock.tick(1000)
    pygame.display.set_caption("FPS: " + str(clock.get_fps()))

import pygame
import random

# Set up how the enemy thinks
class Enemy():
    # Enemy constructor function
    def __init__(self, x , y, speed, size):
        #Make the Enemy's variables
        self.x = x
        self.y = y
        self.pic = pygame.image.load("../assets/mos.png")
        self.speed = speed
        self.size = size
        self.hitbox = pygame.Rect(self.x, self.y, int(self.size*1.25), self.size)

        # Shrink enemy pic
        self.pic = pygame.transform.scale(self.pic, (int(self.size*1.25), self.size))

        # Flip the pic if the Enemy is moving left
        if self.speed < 0:
            self.pic = pygame.transform.flip(self.pic, True, False)

    # Enemy Update Function
    def update(self, screen):
        self.x += self.speed
        self.hitbox.x += self.speed
        #pygame.draw.rect(screen, (255, 255, 255), self.hitbox)
        screen.blit(self.pic, (self.x, self.y))



# Start the game
pygame.init()
game_width = 1920
game_height = 1080
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock()
running = True

background = pygame.image.load("../assets/background.png")
player = pygame.image.load("../assets/bird.png")

player_x = 15

player_y = 30

player_speed = 12

player_size = 60

player_facing_left = False

player_hitbox = pygame.Rect(player_x, player_y, int(player_size*1.25), player_size)

player_alive =  True

#Enemy spawning timer variables
enemy_timer_max = 40
enemy_timer = enemy_timer_max

# Make enemy array
enemies = []



# Everything under 'while running' will be repeated over and over again
while running:
    # Makes the game stop if the player clicks the X or presses esc
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

# Check to see what keys user is pressing
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_y -= player_speed

    if keys[pygame.K_a]:
        player_x -= player_speed
        player_facing_left = True

    if keys[pygame.K_s]:
        player_y += player_speed

    if keys[pygame.K_d]:
        player_x += player_speed
        player_facing_left = False

    if keys [pygame.K_SPACE]:
        player_size += 2

    if keys [pygame.K_k]:
        player_size -= 2


    screen.blit(background, (0, 0))

    # Spawn a new Enemy whenever enemy_timer hits 0
    enemy_timer -= 1
    if enemy_timer <= 0:
        new_enemy_y = random.randint(0, game_height)

        new_enemy_speed = random.randint(1, 6)

        new_enemy_size = random.randint(player_size/2, player_size*2)


        if random.randint(0, 1) == 0:
            enemies.append(Enemy(-new_enemy_size*2, new_enemy_y, new_enemy_speed, new_enemy_size))

        else:
            enemies.append(Enemy(game_width, new_enemy_y, -new_enemy_speed, new_enemy_size))
        enemy_timer = enemy_timer_max


    # Update all enemies
    for enemy in enemies:
        enemy.update(screen)

    if player_alive:
        # Update Player Hitbox
        player_hitbox.x = player_x
        player_hitbox.y = player_y
        player_hitbox.width = int(player_size * 1.25)
        player_hitbox.height = player_size
        #pygame.draw.rect(screen, (255, 255, 255), player_hitbox)


        # Check to see when a player hits a enemy
        for enemy in enemies:
            if player_hitbox.colliderect(enemy.hitbox):
                if player_size >= enemy.size:
                    player_size += 2
                    enemies.remove(enemy)
                else:
                    player_alive = False




        # Draw Player
        player_small = pygame.transform.scale(player, (int(player_size*1.25), player_size))
        if player_facing_left:
            player_small = pygame.transform.flip(player_small, True, False)
        screen.blit(player, (player_x, player_y))

    # Update Screen
    pygame.display.flip()
    clock.tick(1000)
    pygame.display.set_caption("FPS: " + str(clock.get_fps()))

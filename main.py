import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
SCREEN = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pac-Man")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)

# Constants
block_size = 20
pacman_radius = block_size // 2 - 2
ghost_radius = block_size // 2 - 2
maze_width = 19
maze_height = 19
maze = [
    "###################",
    "#........#........#",
    "#.####..##..####.#",
    "#.####..##..####.#",
    "#.................#",
    "#.##.#########.##.#",
    "#.##.#########.##.#",
    "#....##.....##....#",
    "####.##.....##.####",
    "####.##.....##.####",
    "    .##.....##.    ",
    "    .##.....##.    ",
    "####.##.....##.####",
    "####.##.....##.####",
    "#.................#",
    "#.##.#########.##.#",
    "#.##.#########.##.#",
    "#........#........#",
    "###################"
]

# Pac-Man
pacman_x = 10 * block_size
pacman_y = 15 * block_size
pacman_speed = 5

# Ghost
ghost_x = random.randint(1, maze_width - 2) * block_size
ghost_y = random.randint(1, maze_height - 2) * block_size
ghost_speed = 3

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move Pac-Man
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_x -= pacman_speed
    if keys[pygame.K_RIGHT]:
        pacman_x += pacman_speed
    if keys[pygame.K_UP]:
        pacman_y -= pacman_speed
    if keys[pygame.K_DOWN]:
        pacman_y += pacman_speed

    # Collision with walls
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == '#':
                wall_rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
                pacman_rect = pygame.Rect(pacman_x, pacman_y, block_size, block_size)
                if wall_rect.colliderect(pacman_rect):
                    pacman_x, pacman_y = pacman_x - pacman_speed, pacman_y - pacman_speed

    # Move Ghost randomly
    ghost_direction = random.choice(["left", "right", "up", "down"])
    if ghost_direction == "left":
        ghost_x -= ghost_speed
    elif ghost_direction == "right":
        ghost_x += ghost_speed
    elif ghost_direction == "up":
        ghost_y -= ghost_speed
    elif ghost_direction == "down":
        ghost_y += ghost_speed

    # Collision detection between Pac-Man and Ghost
    pacman_rect = pygame.Rect(pacman_x, pacman_y, block_size, block_size)
    ghost_rect = pygame.Rect(ghost_x, ghost_y, block_size, block_size)
    if pacman_rect.colliderect(ghost_rect):
        print("Pac-Man got caught by the ghost!")
        running = False

    # Draw everything
    SCREEN.fill(black)
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == '#':
                pygame.draw.rect(SCREEN, white, (x * block_size, y * block_size, block_size, block_size))
    pygame.draw.circle(SCREEN, yellow, (pacman_x + pacman_radius, pacman_y + pacman_radius), pacman_radius)
    pygame.draw.circle(SCREEN, red, (ghost_x + ghost_radius, ghost_y + ghost_radius), ghost_radius)

    pygame.display.update()

    # Limit frames per second
    pygame.time.Clock().tick(30)

pygame.quit()


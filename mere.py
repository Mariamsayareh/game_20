import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game(m22)")

# Initialize snake and food
snake = [(100, 100), (80, 100), (60, 100)]
snake_direction = pygame.K_RIGHT
score = 0

def create_food():
    x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    return (x, y)

food = create_food()

# Function to draw the snake and food
def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

def draw_food():
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

def game_over():
    font = pygame.font.SysFont(None, 40)
    text = font.render("Game Over!:( \n try again:)", True, WHITE)
    screen.blit(text, (WIDTH // 3, HEIGHT // 3))
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

# Main game loop
clock = pygame.time.Clock()
while True:
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                if (event.key == pygame.K_UP and snake_direction != pygame.K_DOWN) or \
                   (event.key == pygame.K_DOWN and snake_direction != pygame.K_UP) or \
                   (event.key == pygame.K_LEFT and snake_direction != pygame.K_RIGHT) or \
                   (event.key == pygame.K_RIGHT and snake_direction != pygame.K_LEFT):
                    snake_direction = event.key

    # Move the snake
    x, y = snake[0]
    if snake_direction == pygame.K_UP:
        y -= CELL_SIZE
    elif snake_direction == pygame.K_DOWN:
        y += CELL_SIZE
    elif snake_direction == pygame.K_LEFT:
        x -= CELL_SIZE
    elif snake_direction == pygame.K_RIGHT:
        x += CELL_SIZE
    new_head = (x, y)

    # Check for collision with walls or snake's own body
    if (
        x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or new_head in snake
    ):
        game_over()

    # Add new head to the snake
    snake.insert(0, new_head)

    # Check if snake has eaten the food
    if new_head == food:
        score += 1
        food = create_food()
    else:
        snake.pop()

    # Draw the snake and food
    draw_snake()
    draw_food()

    # Update the display
    pygame.display.flip()
    clock.tick(10)
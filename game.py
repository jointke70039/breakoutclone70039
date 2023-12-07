import pygame
import sys
import math
import random

from obstacles import Obstacle, obstacles

# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Klon Breakout by 70039")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up the paddle
paddle_width, paddle_height = 100, 10
paddle_x = (width - paddle_width) // 2
paddle_y = height - 20

# Set up the ball
ball_radius = 10
ball_x, ball_y = width // 2, height // 2
ball_speed = 10
ball_angle = math.radians(random.uniform(30, 60))  # Initial random angle in radians

#Set-up obstacles
obstacles_list = [
    Obstacle(obstacle.x, obstacle.y, obstacle.width, obstacle.height, obstacle.color)
    for obstacle in obstacles
]

# Game loop
clock = pygame.time.Clock()
game_over = False
win = False  # New flag for winning condition

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= 10
    if keys[pygame.K_RIGHT] and paddle_x < width - paddle_width:
        paddle_x += 10

    if not game_over and not win:
        # Update ball position
        ball_x += ball_speed * math.cos(ball_angle)
        ball_y += ball_speed * math.sin(ball_angle)

        # Ball collisions with walls
        if ball_x - ball_radius < 0 or ball_x + ball_radius > width:
            ball_angle = math.pi - ball_angle  # Reflect horizontally
        if ball_y - ball_radius < 0:
            ball_angle = -ball_angle  # Reflect vertically

        # Ball collision with paddle
        if (
            paddle_x - ball_radius < ball_x < paddle_x + paddle_width + ball_radius
            and paddle_y - ball_radius < ball_y < paddle_y + paddle_height + ball_radius
        ):
            # Calculate reflection angle based on the position where the ball hits the paddle
            relative_position = (ball_x - paddle_x) / paddle_width
            angle_offset = (relative_position - 0.5) * math.pi / 2
            ball_angle = -ball_angle + angle_offset

        # Ball hit the bottom, set game_over to True
        if ball_y + ball_radius > height:
            game_over = True

        # Ball collisions with obstacles
        for obstacle in obstacles_list:
            if (
                obstacle.x - ball_radius < ball_x < obstacle.x + obstacle.width + ball_radius
                and obstacle.y - ball_radius < ball_y < obstacle.y + obstacle.height + ball_radius
            ):
                # Remove the obstacle from the list
                obstacles_list.remove(obstacle)
                ball_speed = -ball_speed


         # Check for the cheat code
        if keys[pygame.K_p]:
            win = True
            
        # Check for winning condition
        if not obstacles_list:
            win = True

    # Clear the screen
    screen.fill(black)

    # Draw the paddle
    pygame.draw.rect(screen, white, (paddle_x, paddle_y, paddle_width, paddle_height))

    # Draw the ball
    pygame.draw.circle(screen, white, (int(ball_x), int(ball_y)), ball_radius)

    # Draw obstacles with random colors
    for obstacle in obstacles_list:
        pygame.draw.rect(
            screen,
            obstacle.color,
            (obstacle.x, obstacle.y, obstacle.width, obstacle.height),
        )
    
     # Display the number of obstacles left
    font = pygame.font.Font(None, 24)
    obstacles_left_text = font.render(f"Obstacles left: {len(obstacles_list)}", True, white)
    screen.blit(obstacles_left_text, (10, height - 30))

    # Display messages
    if game_over:
        font = pygame.font.Font(None, 36)
        message = font.render("You noob! Press R to restart or Q to quit", True, white)
        screen.blit(message, (width // 2 - 200, height // 2))
    elif win:
        font = pygame.font.Font(None, 36)
        message = font.render("You won! Press R to restart or Q to quit", True, white)
        screen.blit(message, (width // 2 - 200, height // 2))
    

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

    # Check for restart or quit key press
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        game_over = False
        win = False
        # Reset game state, variables, or any necessary setup for a new game
        ball_x, ball_y = width // 2, height // 2
        ball_angle = math.radians(random.uniform(30, 60))  # Initial random angle in radians
        # Recreate obstacles with new random colors
        obstacles_list = [
    Obstacle(obstacle.x, obstacle.y, obstacle.width, obstacle.height)
    for obstacle in obstacles
]
        

 # Reset paddle position
        paddle_x = (width - paddle_width) // 2
        paddle_y = height - 20

    elif keys[pygame.K_q]:
        pygame.quit()
        sys.exit()

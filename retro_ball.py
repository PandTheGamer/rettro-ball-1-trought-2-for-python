import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 20
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
BALL_SPEED = 5
PADDLE_SPEED = 7
AI_DIFFICULTY = 0.3
WINNING_SCORE = 5  # Adjust the winning score as needed

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Retro Ball Game")

# Create the ball
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_velocity = [random.choice([-1, 1]) * BALL_SPEED, random.choice([-1, 1]) * BALL_SPEED]

# Create paddles
left_paddle_pos = [0, HEIGHT // 2 - PADDLE_HEIGHT // 2]
right_paddle_pos = [WIDTH - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2]

# Initialize scores
player_score = 0
ai_score = 0

# Fullscreen mode toggle
fullscreen = False

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    keys = pygame.key.get_pressed()

    # Update left paddle
    if keys[pygame.K_UP] and left_paddle_pos[1] > 0:
        left_paddle_pos[1] -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and left_paddle_pos[1] < HEIGHT - PADDLE_HEIGHT:
        left_paddle_pos[1] += PADDLE_SPEED

    # Update right paddle (AI)
    if ball_velocity[0] > 0:  # Only update AI if the ball is moving towards the AI
        target_pos = ball_pos[1] + (ball_pos[1] - right_paddle_pos[1]) * BALL_SPEED / ball_velocity[0]
        if target_pos < right_paddle_pos[1] and right_paddle_pos[1] > 0:
            right_paddle_pos[1] -= PADDLE_SPEED
        elif target_pos > right_paddle_pos[1] + PADDLE_HEIGHT and right_paddle_pos[1] < HEIGHT - PADDLE_HEIGHT:
            right_paddle_pos[1] += PADDLE_SPEED

    # Update ball position
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]

    # Bounce off the paddles
    if (
        left_paddle_pos[0] <= ball_pos[0] - BALL_RADIUS <= left_paddle_pos[0] + PADDLE_WIDTH
        and left_paddle_pos[1] <= ball_pos[1] <= left_paddle_pos[1] + PADDLE_HEIGHT
    ) or (
        right_paddle_pos[0] - BALL_RADIUS <= ball_pos[0] <= right_paddle_pos[0] + PADDLE_WIDTH
        and right_paddle_pos[1] <= ball_pos[1] <= right_paddle_pos[1] + PADDLE_HEIGHT
    ):
        ball_velocity[0] = -ball_velocity[0]

    # Bounce off the walls
    if ball_pos[0] - BALL_RADIUS <= 0:
        # Player scores a point
        ai_score += 1
        if ai_score == WINNING_SCORE:
            print("AI wins!")
            pygame.quit()
            sys.exit()
        # Reset ball position
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_velocity = [random.choice([-1, 1]) * BALL_SPEED, random.choice([-1, 1]) * BALL_SPEED]

    elif ball_pos[0] + BALL_RADIUS >= WIDTH:
        # AI scores a point
        player_score += 1
        if player_score == WINNING_SCORE:
            print("Player wins!")
            pygame.quit()
            sys.exit()
        # Reset ball position
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_velocity = [random.choice([-1, 1]) * BALL_SPEED, random.choice([-1, 1]) * BALL_SPEED]

    if ball_pos[1] - BALL_RADIUS <= 0 or ball_pos[1] + BALL_RADIUS >= HEIGHT:
        ball_velocity[1] = -ball_velocity[1]

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the ball
    pygame.draw.circle(screen, WHITE, (int(ball_pos[0]), int(ball_pos[1])), BALL_RADIUS)

    # Draw the paddles
    pygame.draw.rect(screen, WHITE, (left_paddle_pos[0], left_paddle_pos[1], PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (right_paddle_pos[0], right_paddle_pos[1], PADDLE_WIDTH, PADDLE_HEIGHT))

    # Display scores
    font = pygame.font.Font(None, 36)
    player_text = font.render(f"Player: {player_score}", True, WHITE)
    ai_text = font.render(f"AI: {ai_score}", True, WHITE)
    screen.blit(player_text, (20, 20))
    screen.blit(ai_text, (WIDTH - 120, 20))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 20
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
BALL_SPEED = 5
PADDLE_SPEED = 7
AI_DIFFICULTY = 0.3
WINNING_SCORE = 5  # Adjust the winning score as needed

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Retro Ball Game")

# Create the ball
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_velocity = [random.choice([-1, 1]) * BALL_SPEED, random.choice([-1, 1]) * BALL_SPEED]

# Create paddles
left_paddle_pos = [0, HEIGHT // 2 - PADDLE_HEIGHT // 2]
right_paddle_pos = [WIDTH - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2]

# Initialize scores
player_score = 0
ai_score = 0

# Fullscreen mode toggle
fullscreen = False

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    keys = pygame.key.get_pressed()

    # Update left paddle
    if keys[pygame.K_UP] and left_paddle_pos[1] > 0:
        left_paddle_pos[1] -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and left_paddle_pos[1] < HEIGHT - PADDLE_HEIGHT:
        left_paddle_pos[1] += PADDLE_SPEED

    # Update right paddle (AI)
    if ball_velocity[0] > 0:  # Only update AI if the ball is moving towards the AI
        target_pos = ball_pos[1] + (ball_pos[1] - right_paddle_pos[1]) * BALL_SPEED / ball_velocity[0]
        if target_pos < right_paddle_pos[1] and right_paddle_pos[1] > 0:
            right_paddle_pos[1] -= PADDLE_SPEED
        elif target_pos > right_paddle_pos[1] + PADDLE_HEIGHT and right_paddle_pos[1] < HEIGHT - PADDLE_HEIGHT:
            right_paddle_pos[1] += PADDLE_SPEED

    # Update ball position
    ball_pos[0] += ball_velocity[0]
    ball_pos[1] += ball_velocity[1]

    # Bounce off the paddles
    if (
        left_paddle_pos[0] <= ball_pos[0] - BALL_RADIUS <= left_paddle_pos[0] + PADDLE_WIDTH
        and left_paddle_pos[1] <= ball_pos[1] <= left_paddle_pos[1] + PADDLE_HEIGHT
    ) or (
        right_paddle_pos[0] - BALL_RADIUS <= ball_pos[0] <= right_paddle_pos[0] + PADDLE_WIDTH
        and right_paddle_pos[1] <= ball_pos[1] <= right_paddle_pos[1] + PADDLE_HEIGHT
    ):
        ball_velocity[0] = -ball_velocity[0]

    # Bounce off the walls
    if ball_pos[0] - BALL_RADIUS <= 0:
        # Player scores a point
        ai_score += 1
        if ai_score == WINNING_SCORE:
            print("AI wins!")
            pygame.quit()
            sys.exit()
        # Reset ball position
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_velocity = [random.choice([-1, 1]) * BALL_SPEED, random.choice([-1, 1]) * BALL_SPEED]

    elif ball_pos[0] + BALL_RADIUS >= WIDTH:
        # AI scores a point
        player_score += 1
        if player_score == WINNING_SCORE:
            print("Player wins!")
            pygame.quit()
            sys.exit()
        # Reset ball position
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_velocity = [random.choice([-1, 1]) * BALL_SPEED, random.choice([-1, 1]) * BALL_SPEED]

    if ball_pos[1] - BALL_RADIUS <= 0 or ball_pos[1] + BALL_RADIUS >= HEIGHT:
        ball_velocity[1] = -ball_velocity[1]

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the ball
    pygame.draw.circle(screen, WHITE, (int(ball_pos[0]), int(ball_pos[1])), BALL_RADIUS)

    # Draw the paddles
    pygame.draw.rect(screen, WHITE, (left_paddle_pos[0], left_paddle_pos[1], PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (right_paddle_pos[0], right_paddle_pos[1], PADDLE_WIDTH, PADDLE_HEIGHT))

    # Display scores
    font = pygame.font.Font(None, 36)
    player_text = font.render(f"Player: {player_score}", True, WHITE)
    ai_text = font.render(f"AI: {ai_score}", True, WHITE)
    screen.blit(player_text, (20, 20))
    screen.blit(ai_text, (WIDTH - 120, 20))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
BALL_RADIUS = 20
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
BALL_SPEED = 5
PADDLE_SPEED = 7
WINNING_SCORE = 5  # Adjust the winning score as needed

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_width(), screen.get_height()
pygame.display.set_caption("Retro Ball Game")

# Create the ball
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_velocity = [random.choice([-1, 1]) * BALL_SPEED, random.choice([-1, 1]) * BALL_SPEED]

# Create paddles
left_paddle_rect = pygame.Rect(0, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle_rect = pygame.Rect(WIDTH - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Initialize scores
player_score = 0
ai_score = 0

# Difficulty levels
EASY_DIFFICULTY = 0.2
NORMAL_DIFFICULTY = 0.5
HARD_DIFFICULTY = 0.8

# Default difficulty
current_difficulty = NORMAL_DIFFICULTY

# Game states
START_MENU = "start_menu"
RUNNING = "running"
PAUSED = "paused"

game_state = START_MENU

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif game_state == START_MENU:
                if event.key == pygame.K_e:
                    current_difficulty = EASY_DIFFICULTY
                    game_state = RUNNING
                elif event.key == pygame.K_n:
                    current_difficulty = NORMAL_DIFFICULTY
                    game_state = RUNNING
                elif event.key == pygame.K_h:
                    current_difficulty = HARD_DIFFICULTY
                    game_state = RUNNING
            elif game_state == RUNNING and event.key == pygame.K_p:
                game_state = PAUSED
            elif game_state == PAUSED and event.key == pygame.K_p:
                game_state = RUNNING

    keys = pygame.key.get_pressed()

    if game_state == RUNNING:
        # Update left paddle
        if keys[pygame.K_UP] and left_paddle_rect.top > 0:
            left_paddle_rect.move_ip(0, -PADDLE_SPEED)
        if keys[pygame.K_DOWN] and left_paddle_rect.bottom < HEIGHT:
            left_paddle_rect.move_ip(0, PADDLE_SPEED)

        # Update right paddle (AI)
        if ball_velocity[0] > 0:  # Only update AI if the ball is moving towards the AI
            target_pos = ball_pos[1] + (ball_pos[1] - right_paddle_rect.centery) * BALL_SPEED / ball_velocity[0]
            if target_pos < right_paddle_rect.centery and right_paddle_rect.top > 0:
                right_paddle_rect.move_ip(0, -PADDLE_SPEED * current_difficulty)
            elif target_pos > right_paddle_rect.centery and right_paddle_rect.bottom < HEIGHT:
                right_paddle_rect.move_ip(0, PADDLE_SPEED * current_difficulty)

        # Update ball position
        ball_pos[0] += ball_velocity[0]
        ball_pos[1] += ball_velocity[1]

        # Bounce off the paddles
        if left_paddle_rect.colliderect(ball_pos[0] - BALL_RADIUS, ball_pos[1] - BALL_RADIUS, 2 * BALL_RADIUS, 2 * BALL_RADIUS) or \
           right_paddle_rect.colliderect(ball_pos[0] - BALL_RADIUS, ball_pos[1] - BALL_RADIUS, 2 * BALL_RADIUS, 2 * BALL_RADIUS):
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

    if game_state == START_MENU:
        # Display start menu
        font = pygame.font.Font(None, 36)
        title_text = font.render("Choose Difficulty:", True, WHITE)
        easy_text = font.render("Press 'E' for Easy", True, WHITE)
        normal_text = font.render("Press 'N' for Normal", True, WHITE)
        hard_text = font.render("Press 'H' for Hard", True, WHITE)
        screen.blit(title_text, (WIDTH // 2 - 150, HEIGHT // 2 - 50))
        screen.blit(easy_text, (WIDTH // 2 - 120, HEIGHT // 2))
        screen.blit(normal_text, (WIDTH // 2 - 130, HEIGHT // 2 + 40))
        screen.blit(hard_text, (WIDTH // 2 - 120, HEIGHT // 2 + 80))
    elif game_state == RUNNING:
        # Draw the ball
        pygame.draw.circle(screen, WHITE, (int(ball_pos[0]), int(ball_pos[1])), BALL_RADIUS)

        # Draw the paddles
        pygame.draw.rect(screen, WHITE, left_paddle_rect)
        pygame.draw.rect(screen, WHITE, right_paddle_rect)

        # Display scores
        font = pygame.font.Font(None, 36)
        player_text = font.render(f"Player: {player_score}", True, WHITE)
        ai_text = font.render(f"AI: {ai_score}", True, WHITE)
        screen.blit(player_text, (20, 20))
        screen.blit(ai_text, (WIDTH - 120, 20))
    elif game_state == PAUSED:
        # Display pause menu
        font = pygame.font.Font(None, 36)
        pause_text = font.render("Game Paused", True, WHITE)
        resume_text = font.render("Press 'P' to Resume", True, WHITE)
        screen.blit(pause_text, (WIDTH // 2 - 100, HEIGHT // 2 - 20))
        screen.blit(resume_text, (WIDTH // 2 - 120, HEIGHT // 2 + 20))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)

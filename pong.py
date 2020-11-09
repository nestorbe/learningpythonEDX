import random
import pygame
from pygame.locals import *

# Screen Dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Paddle(pygame.sprite.Sprite):
    paddle_width = 10
    paddle_length = 75
    paddle_buffer = 15
    move_speed = 9
    player_control = {
        # Store the inputs players can make and associated direction in dictionary
        pygame.K_w: -1,
        pygame.K_s: 1,
        pygame.K_UP: -1,
        pygame.K_DOWN: 1
    }

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((Paddle.paddle_width, Paddle.paddle_length))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

    def move(self, direction):
        """moves the paddle in the direction of user input"""
        move_speed = Paddle.move_speed * direction
        current_pos = self.rect
        new_pos = self.rect.move((0, move_speed))

        # Check if new_pos is still within the screen
        if new_pos.y >= (SCREEN_HEIGHT - Paddle.paddle_length - Paddle.paddle_buffer):  # Stop the paddle moving off
            # bottom of the screen. Small buffer exists between bottom of screen and paddle.
            new_pos = current_pos
        elif new_pos.y <= Paddle.paddle_buffer:  # Stop the paddle moving off top of the screen. Small buffer exists
            # between top of screen and paddle.
            new_pos = current_pos

        self.rect = new_pos


class Ball(pygame.sprite.Sprite):
    ball_radius = 10
    surf_dim = ball_radius * 2
    velocity = 10

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((Ball.surf_dim, Ball.surf_dim), pygame.SRCALPHA)
        pygame.draw.circle(self.image, WHITE, (Ball.ball_radius, Ball.ball_radius), Ball.ball_radius)
        self.rect = self.image.get_rect()

        self.move_x = random.choice([v for v in range(-5, 5) if v not in [0]])  # Choose a random number between -5
        # and 5, while excluding 0
        self.move_y = ((Ball.velocity ** 2) - (self.move_x ** 2)) ** 0.5  # Calculate the y component of velocity

    def update(self):
        """Moves the ball and reflects the ball if it collides with top/bottom side of screen"""
        screen_surface = pygame.display.get_surface()
        screen_rect = screen_surface.get_rect()

        pos_y = self.rect.y
        new_pos = self.rect.move((self.move_x, self.move_y))
        # Check if the ball has collided with top or bottom side of screen
        if (pos_y < 0) or (pos_y > screen_rect.height - Ball.surf_dim):
            self.move_y *= -1  # Flip the direction of y-component of velocity
            new_pos = self.rect.move((self.move_x, self.move_y))
        self.rect = new_pos

    def paddle_collide(self, paddle_rects):
        """Detects collision with paddles"""
        # paddle_rects represents a list which contains the rect of both player one paddle and player two paddle
        for rect in paddle_rects:
            rect_collision = rect.inflate(-5, -5)  # Decrease the hit-box of paddle
            if self.rect.colliderect(rect_collision):
                self.move_x *= -1

    def wall_collide(self):
        """Detects collision with left/right side of screen, and returns boolean to handle score increase and screen
        reset """
        screen_surface = pygame.display.get_surface()
        screen_rect = screen_surface.get_rect()

        pos_x = self.rect.x

        reset = 0
        two_scored = 0
        one_scored = 0

        # Detect collision with left/right side of screen
        if pos_x < 0:  # Collision with left side of screen
            two_scored = 1
            reset = 1
        elif pos_x > screen_rect.width - Ball.surf_dim:  # Collision with right side of screen
            one_scored = 1
            reset = 1

        return reset, one_scored, two_scored


class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(None, 100)
        self.score = 0
        self.image = self.font.render(str(self.score), 0, WHITE)
        self.rect = self.image.get_rect()


def main():
    # Basic initialisation
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Pong Game')
    clock = pygame.time.Clock()

    # Prepare the background
    background = pygame.Surface(screen.get_size())
    border_rect = background.get_rect()
    background.fill(BLACK)  # Make sure the background is black
    pygame.draw.rect(background, WHITE, border_rect, 5)  # Draw white borders
    pygame.draw.line(background, WHITE, ((SCREEN_WIDTH / 2), 0), ((SCREEN_WIDTH / 2), SCREEN_HEIGHT))  # Draw middle
    # line

    # Load in all the sprites
    player_one = Paddle()
    player_one.rect.center = (50, (SCREEN_HEIGHT / 2))  # Position the first player paddle

    player_two = Paddle()
    player_two.rect.center = (590, (SCREEN_HEIGHT / 2))  # Position the second player paddle

    ball = Ball()
    ball.rect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))  # Position the ball

    score_one = Score()
    score_one.rect.center = (150, 80)  # Position score for player one

    score_two = Score()
    score_two.rect.center = (480, 80)  # Position score for player two

    all_sprites = pygame.sprite.RenderPlain(ball, player_one, player_two, score_one, score_two)

    running = 1

    while running:
        clock.tick(40)
        key = pygame.key.get_pressed()

        # Detect closing of program
        for event in pygame.event.get():
            if event.type == QUIT:
                running = 0

        # Iterate over the dictionary which holds data for player input and associated direction
        for player_input, direction in Paddle.player_control.items():
            if key[player_input]:
                if player_input == pygame.K_w or player_input == pygame.K_s:  # Detect player one input
                    player_one.move(direction)
                elif player_input == pygame.K_UP or player_input == pygame.K_DOWN:  # Detect player two input
                    player_two.move(direction)

        player_rects = [player_one.rect, player_two.rect]  # Create list which contains the most up-to-date rect of
        # paddles
        ball.paddle_collide(player_rects)  # Check for collision with paddles
        collide_result = (ball.wall_collide())  # Check for collision with left/right side of screen

        if collide_result[0]:  # Check if ball has collided with either left or right side of screen
            if collide_result[1]:  # Ball has collided with right side of screen
                score_one.score += 1
                score_one.image = score_one.font.render(str(score_one.score), 0, WHITE)
            elif collide_result[2]:  # Ball has collided with left side of screen
                score_two.score += 1
                score_two.image = score_two.font.render(str(score_two.score), 0, WHITE)

            ball.rect.center = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))  # Reset the position of the ball

            # Get new random velocity components for the ball
            ball.move_x = random.choice([v for v in range(-5, 5) if v not in [0]])
            ball.move_y = ((Ball.velocity ** 2) - (ball.move_x ** 2)) ** 0.5

            pygame.time.delay(500)  # Delay the program to represent the end of the round

        # Win condition
        if score_one.score == 5 or score_two == 5:
            running = 0

        all_sprites.update()  # Update all sprites

        screen.blit(background, (0, 0))  # Draw the background
        all_sprites.draw(screen)  # Draw the sprites to the screen

        pygame.display.flip()  # Update the whole screen

    pygame.quit()


if __name__ == '__main__': main()
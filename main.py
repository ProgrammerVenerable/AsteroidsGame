import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FILE
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_event
from score import *
import sys
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font(None, 56)
    timer = pygame.time.Clock()
    dt = 0
    score = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    field = AsteroidField()
    player = Player(x, y)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for draw_group in drawable:
            draw_group.draw(screen)

        # Creating the text surface for the scoreboard
        score_text = font.render(f"Score:{score}", True, (255, 255, 255))

        # Drawing it at the screen
        screen.blit(score_text, (10, 10))

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                if check_highscore(score, FILE):
                    print(f"NEW HIGHSCORE: {score}")
                    change_score(score, FILE)
                else:
                    print(f"Score: {score}")
                sys.exit()

            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
                    score += 10
        pygame.display.flip()
        dt = timer.tick(60) / 1000




if __name__ == "__main__":
    main()

import pygame
from .settings import Settings
from .sprites.player import Player


def main(screen: pygame.Surface):
    group = pygame.sprite.Group()
    player = Player(group)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[Settings.KEY_RIGHT]:
            player.move(1, 0)
        if keys[Settings.KEY_LEFT]:
            player.move(-1, 0)
        if keys[Settings.KEY_UP]:
            player.move(0, -1)
        if keys[Settings.KEY_DOWN]:
            player.move(0, 1)
        screen.fill(Settings.BACKGROUND)
        group.update()
        group.draw(screen)
        pygame.display.flip()
        clock.tick(Settings.FPS)

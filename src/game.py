import pygame
from .settings import Settings
from .sprites.player import Player
from .functions import load_map
from gamemap import GameMap


def main(screen: pygame.Surface):
    group = pygame.sprite.Group()
    player = Player(0, 0, group)
    clock = pygame.time.Clock()
    game_map = GameMap(load_map('level_1.txt'), Settings.CELL_SIZE)
    player.add_observer(game_map)
    player.move_ip(300, 200)
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
        game_map.draw(screen)
        group.update()
        group.draw(screen)
        pygame.display.flip()
        clock.tick(Settings.FPS)

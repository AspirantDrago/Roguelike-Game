import pygame
import src.game as game

SIZE = WIDTH, HEIGHT = 600, 400

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Roguelike')
game.main(screen)
pygame.quit()

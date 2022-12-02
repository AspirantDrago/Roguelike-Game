import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', 'images', name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображением {name} отсутствует')
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image

def get_sub_sprite(
        sprite: pygame.Surface,
        row,
        col,
        width,
        height,
        left_offset=0,
        top_offset=0,
        vertical_spacing=0,
        horisontal_spacing=0
):
    x = left_offset + col * (width + horisontal_spacing)
    y = top_offset + row * (height + vertical_spacing)
    return sprite.subsurface((x, y, width, height))

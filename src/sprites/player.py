import pygame
from ..settings import Settings
from ..functions import load_image, get_sub_sprite


class Player(pygame.sprite.Sprite):
    WIDTH = 48
    HEIGHT = 48

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _image = load_image('player.png', -1)
        self.images = []
        for i in range(11):
            im = get_sub_sprite(
                _image,
                i // 7, i % 7, self.WIDTH, self.HEIGHT,
                left_offset=16,
                top_offset=16,
                horisontal_spacing=16,
                vertical_spacing=16
            )
            im = pygame.transform.scale(im, (48 * 5, 48 * 5))
            self.images.append(im)
        self.current_cadr = 0
        self.image = self.images[self.current_cadr]
        self.rect = self.image.get_rect()


    def move(self, dx, dy):
        self.rect.move_ip(dx * Settings.STEP_SIZE, dy * Settings.STEP_SIZE)

    def update(self, *args, **kwargs):
        self.current_cadr += 1
        self.current_cadr %= 2
        self.image = self.images[self.current_cadr]

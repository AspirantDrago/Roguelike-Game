import pygame
from ..settings import Settings
from ..functions import load_image, get_sub_sprite


LEFT_DIRECTION = 0
RIGHT_DIRECTION = 1


class Player(pygame.sprite.Sprite):
    WIDTH = 48
    HEIGHT = 48
    LOCAL_FPS = 6

    def __init__(self, x: int, y: int, *args, **kwargs):
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
            # im = pygame.transform.scale(im, (48 * 5, 48 * 5))
            self.images.append(im)
        self.images_flip = [pygame.transform.flip(image, True, False) for image in self.images]
        self.current_cadr = 0
        self.image = self.images[self.current_cadr]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.frame = 0
        self.direction = LEFT_DIRECTION
        self.observers = []

    def _set_direction(self, direction):
        if self.direction != direction:
            self.direction = direction
            self.images, self.images_flip = self.images_flip, self.images

    def _move(self, dx, dy, is_notify=True):
        self.rect.move_ip(dx, dy)
        if is_notify:
            self.notify('move_ip', dx, dy)

    def move_ip(self, dx, dy):
        self._move(dx, dy, is_notify=False)

    def move(self, dx, dy):
        if dx > 0:
            self._set_direction(RIGHT_DIRECTION)
        elif dx < 0:
            self._set_direction(LEFT_DIRECTION)
        self._move(dx * Settings.STEP_SIZE, dy * Settings.STEP_SIZE)

    def update(self, *args, **kwargs):
        self.frame += 1
        self.frame %= Settings.FPS // self.LOCAL_FPS
        if self.frame == 0:
            self.current_cadr += 1
            self.current_cadr %= 2
            self.image = self.images[self.current_cadr]

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify(self, method, *args, **kwargs):
        for observer in self.observers:
            try:
                getattr(observer, method)(self, *args, **kwargs)
            except BaseException as e:
                print(e)
import pygame

class GameMap:
    def __init__(self, level: list[str], cell_size: int):
        self.level = level
        self.cell_size = cell_size
        self.x = 0
        self.y = 0
        self.height = len(level)
        self.width = len(level[0])

    def draw(self, screen: pygame.Surface) -> None:
        rect = pygame.Rect(0, 0, self.cell_size, self.cell_size)
        for row in range(self.height):
            for col in range(self.width):
                new_rect = rect.move(
                    self.x + col * self.cell_size,
                    self.y + row * self.cell_size
                )
                pygame.draw.rect(screen, 'black', new_rect, 1)

    def move_ip(self, sender, dx, dy):
        self.x -= dx
        self.y -= dy
        sender.move_ip(-dx, -dy)

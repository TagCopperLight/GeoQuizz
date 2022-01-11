import pygame

from data.enums.enums import Colors


class Button:
    def __init__(self, width, height, corner, color, alpha, hovered_color, hovered_alpha, text, font_size, clickable=True, events=[], mouse_pos=(0, 0)):
        self.width = width
        self.height = height
        self.corner = corner
        self.color = color
        self.alpha = alpha
        self.hovered_color = hovered_color
        self.hovered_alpha = hovered_alpha
        self.text = text
        self.font_size = font_size
        self.clickable = clickable
        self.events = events
        self.mouse_pos = mouse_pos

        self.clicked = False

        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

    def update(self, events, mouse_pos, x, y):
        self.events = events
        self.mouse_pos = mouse_pos
        self.clicked = False

        self.surface.fill((0, 0, 0, 0))

        if self.alpha != 255:
            self.color[-1] = self.alpha
            self.color = tuple(self.color)
        if self.hovered_alpha != 255:
            self.hovered_color[-1] = self.hovered_alpha
            self.hovered_color = tuple(self.hovered_color)

        hitbox = self.surface.get_rect()
        hitbox.topleft = (x, y)

        if hitbox.collidepoint(self.mouse_pos) and self.clickable:
            pygame.draw.rect(self.surface, self.hovered_color, pygame.Rect(0, 0, self.width, self.height), 0, self.corner)

            for event in self.events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicked = True
        else:
            pygame.draw.rect(self.surface, self.color, pygame.Rect(0, 0, self.width, self.height), 0, self.corner)

        font = pygame.font.Font('data/font/myriad-pro.otf', 24)
        text_surface = font.render(self.text, True, Colors.WHITE.value)

        self.surface.blit(text_surface, ((self.width - text_surface.get_width()) / 2, (self.height - text_surface.get_height()) / 2 + 2))

        return self.clicked

    def get_surface(self):
        return self.surface
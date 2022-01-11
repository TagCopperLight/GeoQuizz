import pygame

from data.enums.enums import Colors


class Interface:
    def __init__(self, width, height, has_return, has_logo, events=[], mouse_pos=(0, 0)):
        self.width = width
        self.height = height
        self.events = events
        self.mouse_pos = mouse_pos
        self.has_return = has_return
        self.has_logo = has_logo

        self.clicked = False

        self.surface = pygame.Surface((self.width, self.height))

        self.surface.fill(Colors.DARK_BLUE1.value)
        self.top_bar = pygame.Surface((self.width, 20))
        self.top_bar.fill(Colors.BLUE1.value)
        self.surface.blit(self.top_bar, (0, 0))

        if self.has_return:
            try:
                self.return_button = pygame.image.load("data/imgs/return.png").convert_alpha()
            except FileNotFoundError:
                print('Return button not found')
                self.return_button = pygame.Rect(0, 0, 35, 37)
            self.return_button = pygame.transform.scale(self.return_button, (35, 37))
            self.surface.blit(self.return_button, (14, 34))

        if self.has_logo:
            try:
                self.logo = pygame.image.load("data/imgs/logo.png").convert_alpha()
            except FileNotFoundError:
                print('Logo image not found')
                self.logo = pygame.Rect(0, 0, 246, 246)
            self.logo = pygame.transform.scale(self.logo, (246, 246))
            self.surface.blit(self.logo, (837, 70))

    def get_surface(self):
        return self.surface

    def update(self, events, mouse_pos, *args):
        self.events = events
        self.mouse_pos = mouse_pos
        self.clicked = False
        collection = None
        if len(args) > 0:
            collection = args[0]

        self.surface.fill(Colors.DARK_BLUE1.value)
        self.surface.blit(self.top_bar, (0, 0))

        if self.has_return:
            self.return_button = pygame.transform.scale(self.return_button, (35, 37))
            self.surface.blit(self.return_button, (14, 34))
        if self.has_logo:
            self.logo = pygame.transform.scale(self.logo, (246, 246))
            self.surface.blit(self.logo, (837, 70))

        result = self.sub_update(self.events, self.mouse_pos, collection)

        if self.has_return:
            hitbox = self.return_button.get_rect()
            hitbox.topleft = (14, 34)

            if hitbox.collidepoint(self.mouse_pos):
                for event in self.events:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.clicked = True
            result['return'] = self.clicked

        return result
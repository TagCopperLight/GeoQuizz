import pygame
import random

from data.interface.interface import Interface
from data.enums.enums import Colors, Interfaces
from data.interface.widgets.button import Button


class Collections(Interface):
    def __init__(self, width, height, collections):
        super().__init__(width, height, True, True)

        self.collections = collections.get_collections()
        self.actions = []

        self.page_showed = 0
        self.collection_clicked = None
        self.coords = [387, 510, 633]

        for index, collection in enumerate(self.collections):
            if 3 * self.page_showed <= index < 3 * (self.page_showed + 1):
                exec(f"""self.collection_{str(index)}_button = Button(581, 95, 16, Colors.DARK_BLUE2.value, 255, Colors.BLUE1.value, 255, "{collection.get_name()}", 24)""")
                exec(f"self.collection_{str(index)}_button_action = False")
                exec(f"self.actions.append(self.collection_{str(index)}_button_action)")

        self.random_collection_button = Button(581, 95, 16, Colors.DARK_BLUE2.value, 255, Colors.BLUE1.value, 255, 'Random Collection', 24)
        self.random_collection_button_action = False

        self.select_line = Button(194, 5, 16, Colors.LIGHT_BLUE.value, 255, Colors.LIGHT_BLUE.value, 255, '', 4, clickable=False)
        self.select_right_arrow = pygame.transform.scale(pygame.image.load("data/imgs/select_right_arrow.png").convert_alpha(), (26, 30))
        self.select_left_arrow = pygame.transform.scale(pygame.image.load("data/imgs/select_left_arrow.png").convert_alpha(), (26, 30))

        self.font = pygame.font.Font('data/font/myriad-pro.otf', 32)
        self.page_text_surface = self.font.render(str(self.page_showed + 1), True, Colors.LIGHT_BLUE.value)

        self.account_button = Button(143, 42, 16, Colors.DARK_BLUE2.value, 255, Colors.BLUE1.value, 255, 'Account', 20)
        self.account_button_action = False

    def sub_update(self, events, mouse_pos, *args):
        self.events = events
        self.mouse_pos = mouse_pos
        self.coords = self.coords
        self.actions.clear()

        for index, collection in enumerate(self.collections):
            if 3 * self.page_showed <= index < 3 * (self.page_showed + 1):
                exec(f"""self.collection_{str(index)}_button = Button(581, 95, 16, Colors.DARK_BLUE2.value, 255, Colors.BLUE1.value, 255, "{collection.get_name()}", 24)""")
                exec(f"self.collection_{str(index)}_button_action = self.collection_{str(index)}_button.update(self.events, self.mouse_pos, 670, {self.coords[index - self.page_showed * 3]})")
                exec(f"self.actions.append(self.collection_{str(index)}_button_action)")
                exec(f"self.surface.blit(self.collection_{str(index)}_button.get_surface(), (670, {self.coords[index - self.page_showed * 3]}))")

        self.random_collection_button = Button(581, 95, 16, Colors.DARK_BLUE2.value, 255, Colors.BLUE1.value, 255, 'Random Collection', 24)
        self.random_collection_button_action = self.random_collection_button.update(self.events, self.mouse_pos, 670, 798)
        self.select_line = Button(194, 5, 16, Colors.LIGHT_BLUE.value, 255, Colors.LIGHT_BLUE.value, 255, '', 4, clickable=False)
        self.account_button = Button(143, 42, 16, Colors.DARK_BLUE2.value, 255, Colors.BLUE1.value, 255, 'Account', 20)
        self.account_button_action = self.account_button.update(self.events, self.mouse_pos, 1763, 34)
        self.select_line.update(self.events, self.mouse_pos, 725, 757)

        self.font = pygame.font.Font('data/font/myriad-pro.otf', 32)
        self.page_text_surface = self.font.render(str(self.page_showed + 1), True, Colors.LIGHT_BLUE.value)

        self.surface.blit(self.random_collection_button.get_surface(), (670, 798))

        self.surface.blit(self.select_line.get_surface(), (728, 760))
        self.surface.blit(self.select_line.get_surface(), (1000, 760))
        self.surface.blit(self.page_text_surface, (964 - self.page_text_surface.get_width() // 2, 764 - self.page_text_surface.get_height() // 2))
        self.surface.blit(self.account_button.get_surface(), (1763, 34))

        if self.page_showed < len(self.collections) // 3:
            self.surface.blit(self.select_right_arrow, (1212, 748))

            hitbox = self.select_right_arrow.get_rect()
            hitbox.topleft = (1212, 748)

            if hitbox.collidepoint(self.mouse_pos):
                for event in self.events:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.page_showed += 1

        if self.page_showed > 0:
            self.surface.blit(self.select_left_arrow, (682, 748))

            hitbox = self.select_left_arrow.get_rect()
            hitbox.topleft = (682, 748)

            if hitbox.collidepoint(self.mouse_pos):
                for event in self.events:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.page_showed -= 1

        clicked = False
        if self.random_collection_button_action:
            self.collection_clicked = random.choice(self.collections)
            clicked = True
        for index, action in enumerate(self.actions):
            if action:
                self.collection_clicked = self.collections[index + (self.page_showed * 3)]
                clicked = True

        return {Interfaces.INTER_COLLECTION: clicked, Interfaces.ACCOUNT: self.account_button_action}

    def get_collection_clicked(self):
        return self.collection_clicked
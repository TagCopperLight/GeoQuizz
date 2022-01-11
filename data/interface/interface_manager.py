import pygame

from data.enums.enums import Interfaces
from data.interface.interfaces_class.main_menu import MainMenu
from data.interface.interfaces_class.settings import Settings
from data.interface.interfaces_class.collections import Collections
from data.interface.interfaces_class.inter_collection import InterCollection


class InterfaceManager:
    def __init__(self, width, height, scripts_manager, events=[], mouse_pos=(0, 0)):
        self.width = width
        self.height = height
        self.scripts_manager = scripts_manager
        self.events = events
        self.mouse_pos = mouse_pos
        self.collection_clicked = self.scripts_manager.get_collections().get_collections()[0]

        self.lasts_interfaces = []
        self.current_interface = Interfaces.MAIN_MENU

        self.main_menu_interface = MainMenu(self.width, self.height)
        self.settings_interface = Settings(self.width, self.height)
        self.collections_interface = Collections(self.width, self.height, self.scripts_manager.get_collections())
        self.inter_collection_interface = InterCollection(self.width, self.height, self.collection_clicked)

        self.interfaces = [self.main_menu_interface, self.main_menu_interface, self.main_menu_interface, self.settings_interface, self.collections_interface, self.inter_collection_interface, self.main_menu_interface]

        self.surface = pygame.Surface((self.width, self.height))

    def update(self, events, mouse_pos):
        self.events = events
        self.mouse_pos = mouse_pos

        if self.current_interface.value[1] == 5:
            self.collection_clicked = self.collections_interface.get_collection_clicked()
            actions = self.interfaces[self.current_interface.value[1]].update(self.events, self.mouse_pos, self.collection_clicked)
        else:
            actions = self.interfaces[self.current_interface.value[1]].update(self.events, self.mouse_pos)

        self.surface.blit(self.interfaces[self.current_interface.value[1]].get_surface(), (0, 0))

        if 'return' in actions.keys():
            if actions['return']:
                self.current_interface = self.lasts_interfaces[-1]
                del self.lasts_interfaces[-1]

        for action in actions:
            if actions[action] and action != 'return':
                self.lasts_interfaces.append(self.current_interface)
                self.current_interface = action

    def get_surface(self):
        return self.surface

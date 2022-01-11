from data.interface.interface import Interface
from data.enums.enums import Colors, Interfaces
from data.interface.widgets.button import Button


class MainMenu(Interface):
    def __init__(self, width, height):
        super().__init__(width, height, False, True)

        self.singleplayer_button = Button(581, 95, 16, Colors.DARK_BLUE2.value, 255, Colors.BLUE1.value, 255, 'Singleplayer', 24)
        self.singleplayer_button_action = False
        self.multiplayer_button = Button(581, 95, 16, Colors.DARK_BLUE2.value, 255, Colors.BLUE1.value, 255, 'Multiplayer', 24)
        self.multiplayer_button_action = False
        self.settings_button = Button(581, 95, 16, Colors.DARK_BLUE2.value, 255, Colors.BLUE1.value, 255, 'Settings', 24)
        self.settings_button_action = False
        self.account_button = Button(143, 42, 16, Colors.DARK_BLUE2.value, 255, Colors.BLUE1.value, 255, 'Account', 20)
        self.account_button_action = False

    def sub_update(self, events, mouse_pos, *args):
        self.events = events
        self.mouse_pos = mouse_pos

        self.singleplayer_button = Button(581, 95, 16, Colors.DARK_BLUE2.value, 255, Colors.BLUE1.value, 255, 'Singleplayer', 24)
        self.multiplayer_button = Button(581, 95, 16, Colors.DARK_BLUE2.value, 255, Colors.BLUE1.value, 255, 'Multiplayer', 24)
        self.settings_button = Button(581, 95, 16, Colors.DARK_BLUE2.value, 255, Colors.BLUE1.value, 255, 'Settings', 24)
        self.account_button = Button(143, 42, 16, Colors.DARK_BLUE2.value, 255, Colors.BLUE1.value, 255, 'Account', 20)

        self.singleplayer_button_action = self.singleplayer_button.update(self.events, self.mouse_pos, 670, 387)
        self.multiplayer_button_action = self.multiplayer_button.update(self.events, self.mouse_pos, 670, 510)
        self.settings_button_action = self.settings_button.update(self.events, self.mouse_pos, 670, 675)
        self.account_button_action = self.account_button.update(self.events, self.mouse_pos, 1763, 34)

        self.surface.blit(self.singleplayer_button.get_surface(), (670, 387))
        self.surface.blit(self.multiplayer_button.get_surface(), (670, 510))
        self.surface.blit(self.settings_button.get_surface(), (670, 675))
        self.surface.blit(self.account_button.get_surface(), (1763, 34))

        return {Interfaces.COLLECTIONS: self.singleplayer_button_action, Interfaces.MAIN_MENU: self.multiplayer_button_action, Interfaces.SETTINGS: self.settings_button_action, Interfaces.ACCOUNT: self.account_button_action}

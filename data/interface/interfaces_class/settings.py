from data.interface.interface import Interface
from data.enums.enums import Colors, Interfaces
from data.interface.widgets.button import Button


class Settings(Interface):
    def __init__(self, width, height):
        super().__init__(width, height, True, True)

        self.change_number_questions_text = Button(581, 95, 16, Colors.DARK_BLUE2.value, 255, Colors.BLUE1.value, 255, 'Change number of questions :', 24)
        self.change_number_questions_text_action = False

        self.change_time_respond_text = Button(581, 95, 16, Colors.DARK_BLUE2.value, 255, Colors.BLUE1.value, 255, 'Change time to respond :', 24)
        self.change_time_respond_text_action = False

        self.change_number_questions = Button(132, 95, 16, Colors.DARK_BLUE2.value, 255, Colors.BLUE1.value, 255, '10', 24)
        self.change_number_questions_action = False

        self.time_respond_button = Button(132, 95, 16, Colors.DARK_BLUE2.value, 255, Colors.BLUE1.value, 255, '10', 24)
        self.time_respond_button_action = False

        self.account_button = Button(143, 42, 16, Colors.DARK_BLUE2.value, 255, Colors.BLUE1.value, 255, 'Account', 20)
        self.account_button_action = False

    def sub_update(self, events, mouse_pos, *args):
        self.events = events
        self.mouse_pos = mouse_pos

        self.change_number_questions_text = Button(581, 95, 16, Colors.DARK_BLUE2.value, 255, Colors.BLUE1.value, 255, 'Change number of questions :', 24, clickable=False)
        self.change_time_respond_text = Button(581, 95, 16, Colors.DARK_BLUE2.value, 255, Colors.BLUE1.value, 255, 'Change time to respond :', 24, clickable=False)
        self.change_number_questions = Button(132, 95, 16, Colors.DARK_BLUE2.value, 255, Colors.BLUE1.value, 255, '10', 24)
        self.time_respond_button = Button(132, 95, 16, Colors.DARK_BLUE2.value, 255, Colors.BLUE1.value, 255, '10', 24)
        self.account_button = Button(143, 42, 16, Colors.DARK_BLUE2.value, 255, Colors.BLUE1.value, 255, 'Account', 20)

        self.change_number_questions_text_action = self.change_number_questions_text.update(self.events, self.mouse_pos, 590, 387)
        self.change_time_respond_text_action = self.change_time_respond_text.update(self.events, self.mouse_pos, 590, 510)
        self.change_number_questions_action = self.change_number_questions.update(self.events, self.mouse_pos, 1199, 387)
        self.time_respond_button_action = self.time_respond_button.update(self.events, self.mouse_pos, 1199, 510)
        self.account_button_action = self.account_button.update(self.events, self.mouse_pos, 1763, 34)

        self.surface.blit(self.change_number_questions_text.get_surface(), (590, 387))
        self.surface.blit(self.change_time_respond_text.get_surface(), (590, 510))
        self.surface.blit(self.change_number_questions.get_surface(), (1199, 387))
        self.surface.blit(self.time_respond_button.get_surface(), (1199, 510))
        self.surface.blit(self.account_button.get_surface(), (1763, 34))

        return {Interfaces.ACCOUNT: self.account_button_action}

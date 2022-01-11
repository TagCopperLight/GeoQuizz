from enum import Enum


class Interfaces(Enum):
    MAIN_MENU = ['main_menu', 0]
    LOGIN = ['login', 1]
    ACCOUNT = ['account', 2]
    SETTINGS = ['settings', 3]
    COLLECTIONS = ['collections', 4]
    INTER_COLLECTION = ['inter_collection', 5]
    QUESTION = ['question', 6]


class Emojis(Enum):
    HOURGLASS = '⌛'
    CROSS = '❌'
    GRAPH = '📊'


class Colors(Enum):
    DARK_BLUE1 = (4, 41, 64)
    DARK_BLUE2 = (16, 77, 115)
    BLUE1 = (50, 121, 166)
    BLUE2 = (72, 149, 217)
    LIGHT_BLUE = (154, 193, 217)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (119, 255, 0)
    YELLOW = (255, 230, 0)
    RED = (255, 0, 0)

    ALPHA_DARK_BLUE1 = [4, 41, 64, 0]
    ALPHA_DARK_BLUE2 = [16, 77, 115, 0]
    ALPHA_BLUE1 = [50, 121, 166, 0]
    ALPHA_BLUE2 = [72, 149, 217, 0]
    ALPHA_LIGHT_BLUE = [154, 193, 217, 0]
    ALPHA_WHITE = [255, 255, 255, 0]
    ALPHA_BLACK = [0, 0, 0, 0]
    ALPHA_GREEN = [119, 255, 0, 0]
    ALPHA_YELLOW = [255, 230, 0, 0]
    ALPHA_RED = [255, 0, 0, 0]
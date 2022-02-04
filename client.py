import pygame

from data.utility.utility import maximize_window, exit_window, check_minimizing
from data.interface.interface_manager import InterfaceManager
from data.scripts.scripts_manager import ScriptsManager

pygame.init()
clock = pygame.time.Clock()
START = True

print('aled')

screen = pygame.display.set_mode((1920, 1057), pygame.RESIZABLE)
maximize_window()

scripts_manager = ScriptsManager()
interface_manager = InterfaceManager(screen.get_width(), screen.get_height(), scripts_manager)

while START:
    clock.tick(60)

    events = pygame.event.get()
    mouse_pos = pygame.mouse.get_pos()

    START = exit_window(events)
    check_minimizing(events)

    interface_manager.update(events, mouse_pos, )

    screen.blit(interface_manager.get_surface(), (0, 0))
    pygame.display.update()

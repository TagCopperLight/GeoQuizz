import ctypes
import pygame


def maximize_window():
    user32 = ctypes.WinDLL('user32')
    hwnd = user32.GetForegroundWindow()
    user32.ShowWindow(hwnd, 3)


def exit_window(events):
    for event in events:
        if event.type == pygame.QUIT:
            return False
    return True


def check_minimizing(events):
    for event in events:
        if event.type == pygame.WINDOWRESTORED:
            maximize_window()
import time, keyboard, win32api, win32con, win32gui
import minilib as mouse

width, height = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
print(width, height)

keyboard.press_and_release("left windows+r")
keyboard.write(iexplore -k)

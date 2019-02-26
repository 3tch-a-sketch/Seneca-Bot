import time, keyboard, win32api, win32con, win32gui
import minilib as mouse

width, height = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
print(width, height)

keyboard.press_and_release("left windows+r")
time.sleep(0.2)
keyboard.write("iexplore -k https://app.senecalearning.com/login")
keyboard.press_and_release("enter")
time.sleep(0.2)
keyboard.press_and_release("f11")

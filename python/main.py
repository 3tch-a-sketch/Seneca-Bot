import time, keyboard, win32api, win32con, time
import minilib as mouse

width, height = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
print(width, height)

mouse.moveClick(0, width -10, 0.1)
time.sleep(0.5)
keyboard.write('Internet Explorer')
keyboard.press('enter')
